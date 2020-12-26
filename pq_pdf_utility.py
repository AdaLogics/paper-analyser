import xml.etree.ElementTree as ET
import subprocess
import shutil
import sys
import os
import simplejson as json


def print_recursively(elem, depth):
    # The below is only for debugging
    #print("\t"*depth + "%s - %s"%(elem.tag, elem.attrib))
    #if "size" in elem.attrib:
    #sz = float(elem.attrib['size'])
    #print("We got a size: %f"%(sz))
    #if sz > 20.0:
    #    print("Text: %s"%(elem.text))
    for child in elem:
        print_recursively(child, depth + 1)


def get_all_texts_rec(elem):
    '''
    Extracts all <text> elements from an xml
    file generatex by pdf2txt. As such, this function
    is simply a partial XML parser.
    This is a recursive function where the recursion
    is used to capture recursive XML elements.
    '''
    global saw_page2
    all_texts = []

    # If we hit page 2, then we return empty list
    if saw_page2 == True:
        return []

    # We don't want to move beyond page 2, as the
    # we assume the title must have been given here.
    if elem.tag == "page":
        if int(elem.attrib['id']) > 3:
            saw_page2 = True
            return []

    # Extract all XML elements recursively
    for c in elem:
        tmp_txts = get_all_texts_rec(c)
        for t2 in tmp_txts:
            all_texts.append(t2)

    # If the current elem is a text element,
    # add this to our list of all texts.
    if elem.tag == "text":
        all_texts.append(elem)
    return all_texts


def get_all_texts(elem):
    global saw_page2
    saw_page2 = False
    return get_all_texts_rec(elem)


def get_title(the_file):
    '''
    Gets the title of the paper by:
        1) Reading an xml representation of the PDF converted by pdf2txt
        2) Searching for the top font size of page 1
        3) Exiting if we reach page 2 of the paper.

    returns 
        @max_string which is the string with the max font in a paper
        @second_max_string which is the string with the second max font
            in a paper.
    '''
    print("[+] Getting title")
    print("Extracting content from %s" % (the_file))
    #print("current working directory: %s"%(os.getcwd()))
    try:
        tree = ET.parse(the_file)
    except:
        print("[+] Error when ET.parse of the file %s" % (the_file))
        return None

    root = tree.getroot()
    #print_recursively(root, 0)
    all_texts = get_all_texts(root)
    sizes = dict()
    latest_size = None
    for te in all_texts:
        #print("%s-%s"%(te.attrib, te.text))
        if 'size' not in te.attrib:
            if latest_size != None:
                sizes[latest_size].append(" ")
            continue
        sz = float(te.attrib['size'])
        latest_size = sz
        if sz not in sizes:
            sizes[sz] = list()
        sizes[sz].append(te.text)

    # We now have all the text elements and we can proceed
    # to extract the elements with the highest and second-highest
    # font sizes.
    sorted_sizes = sorted(sizes.keys())

    # Highest font size
    max_string = ""
    for c in sizes[sorted_sizes[-1]]:
        max_string += c

    # Second highest font size
    second_max_string = ""
    for c in sizes[sorted_sizes[-2]]:
        second_max_string += c

    # Log them
    #print("max %s"%(max_string))
    #print("second max %s"%(second_max_string))

    # Print the bytes: only used for debugging
    ords = list()
    for c in max_string:
        ords.append(hex(ord(c)))
    s1 = " ".join(ords)
    #print("\t\t%s"%(s1))
    #print("\tCompleted getting title")
    return max_string, second_max_string


def get_references(text_file):
    '''
    Reads a txt file converted by pdf2txt and extracts
    the "references" section of the paper.

    This function assumes the references are at the end
    of a paper and that there might be an appendix after.
    As such, we read the text from "References" until end
    of the file, and only stop in case we hit an 
    "appendix" keyword.
    '''
    references = ""
    reading_references = False
    with open(text_file, "r") as tf:
        for l in tf:
            if reading_references == True and "appendix" in l.lower():
                reading_references = False

            if reading_references:
                references += l

            if "references" in l.lower():
                #print("We have a line with references: %s"%(l))
                if len(l.split(" ")) < 3:
                    reading_references = True
    #print("References: %s"%(references))
    return references


def convert_folder(workdir, folder_name):
    '''
    Converts an entire folder of PDFs into representations
    where we have the:
        title
        references
    for each paper. 


    returns a list of dictionaries, where each element
    in the dictionary holds data about a given paper.
    '''
    all_titles = list()
    all_seconds = list()
    title_pairs = list()

    paper_list = []
    data_out_dir = os.path.join(workdir, "data_out")
    if not os.path.isdir(data_out_dir):
        os.mkdir(data_out_dir)
    for l in os.listdir(folder_name):
        if ".pdf" not in l:
            continue

        print("======================================")
        print("[+] working on %s" % (l))
        paper_dict = {
            "file": l,
            "title": None,
            "second_title": None,
            "references": None,
            "success": False
        }

        # First step.
        # Convert the pdf to xml format. This is for getting
        # the title of the paper.
        target_xml = os.path.join(data_out_dir, "%s_analysed.xml" % (l))
        cmd = ["pdf2txt.py", "-t", "xml", "-o", target_xml]
        cmd.append(os.path.join(folder_name, l))
        try:
            subprocess.check_call(" ".join(cmd), shell=True)
        except:
            paper_list.append(paper_dict)
            print("Could not execute the call")
            continue

        try:
            res = get_title(target_xml)
            if res == None:
                paper_list.append(paper_dict)
                continue
            the_title, second = res
        except:
            #    print("Exception in get_title")
            paper_list.append(paper_dict)
            continue
        all_titles.append(the_title)
        all_seconds.append(second)

        # Second step.
        # Convert the pdf to txt format. This step if for getting
        # the references of the paper.
        target_txt = os.path.join(data_out_dir, "%s_analysed.txt" % (l))
        cmd = ["pdf2txt.py", "-t", "text", "-o", target_txt]
        cmd.append(os.path.join(folder_name, l))
        try:
            subprocess.check_call(" ".join(cmd), shell=True)
        except:
            print("Could not execute the call")
            paper_list.append(paper_dict)
            continue

        references = get_references(target_txt)
        paper_dict = {
            "file": l,
            "title": the_title,
            "second_title": second,
            "references": references,
            "success": True
        }
        paper_list.append(paper_dict)
        #print("Adding: %s ----- %s"%(the_title, second))

    return paper_list


def should_select_title(title):
    # Check if there is any characters with value greater than 0xff in first
    # If this is the case then we use the second highest font for title.
    total_above = 0
    for c in title:
        if ord(c) > 0xff:
            total_above += 1
    if total_above > 3:
        return False

    # Now check if "(cid:" is in the name:. If it is,
    # then we will use the second highest font for title.
    if "(cid:" in str(title):
        return False

    return True


def write_to_json(results, target_directory=None):
    counter = 0
    for paper_dict in results:
        if paper_dict['success'] == False:
            print("####### %s" % (paper_dict['file']))
            print("Unsuccessful")
            print("-" * 60)
            continue

        first = paper_dict['title']
        second = paper_dict['second_title']
        use_second = not should_select_title(first)

        # Create a json dictionary and write it to the file system
        json_dict = {
            "Title": first if use_second == False else second,
            "References": paper_dict['references'],
            "Year": "1999",
            "Authors": "David",
            "ReferenceType": "Automatically"
        }
        filepath = "json_dump_%d.json" % (counter)
        if target_directory != None:
            filepath = os.path.join(target_directory, filepath)
        with open(filepath, "w+") as jf:
            json.dump(json_dict, jf)
        counter += 1

        # Now print the content for convenience
        print("########## %s" % (paper_dict['file']))
        print("[+] Title: %s" % (json_dict['Title']))
        #print("[+] References: ")
        #print("%s"%(paper_dict['references']))
        print("-" * 60)


if __name__ == "__main__":
    results = convert_folder("papers")
    target_dir = "json_data"
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    os.chdir(target_dir)
    write_to_json(results)
