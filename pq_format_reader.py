import os
import sys
import simplejson as json
import traceback

import graphviz as gv
import pylab
import random


def append_to_report(workdir, str_to_write, to_print=True):
    work_report = os.path.join(workdir, "report.txt")
    if not os.path.isfile(work_report):
        with open(work_report, "w+") as wr:
            wr.write(str_to_write)
            wr.write("\n")
    else:
        with open(work_report, "ab") as wr:
            wr.write(str_to_write.encode("utf-8"))
            wr.write("\n".encode("utf-8"))

    if to_print:
        print(str_to_write)


def split_reference_section_into_references(all_content, to_print=True):
    '''
    Takes a raw string that resembles references and returns a python
    list where each element is composed of a tuple of four elements:
        - The number of the reference
        - The data of the reference
        - The offset where the reference begins in the raw data
        - The offset where the reference ends in the raw data
            (This end offset is not entirely workign and will often
             be 0)
    Each tuple is arranged in the order of the elements listed above.
    '''

    collect_num = False
    curr_num = ""
    curr_content = ""
    idx_offset = 0
    begin_offset = 0
    end_offset = 0

    references = list()

    for c in all_content:
        if collect_num == True:
            try:
                n = int(c)
                curr_num = "%s%s" % (curr_num, c)
            except:
                None

        if c == "[":
            # Make sure the next character is a number
            try:
                tmpi = int(all_content[idx_offset + 1])
            except:
                curr_content += c
                continue

            if curr_content != "":
                references.append({
                    "number": curr_num,
                    "raw_content": curr_content,
                    "offset": begin_offset
                })
                #references.append((curr_num, curr_content, begin_offset, end_offset))
            curr_num = ""
            collect_num = True
            begin_offset = idx_offset
        elif c == "]":
            collect_num = False
            #print("Got a number: %d"%(int(curr_num)))
            #curr_num = ""
            curr_content = ""
        elif collect_num == False:
            curr_content += c

        idx_offset += 1

    # Add the final reference
    #references.append((curr_num, curr_content, begin_offset, end_offset))
    references.append({
        "number": curr_num,
        "raw_content": curr_content,
        "offset": begin_offset
    })
    print("Size of references: %d" % (len(references)))

    if to_print == True:
        for ref in references:
            print("Ref: %s" % (str((ref))))

    return references


####################################################################
# Reference author routines
#
#
# These routines are used to take raw reference data
# and split it up between authors and title of reference.
#
# We need multiple routines for this since there are multiple
# ways of writing references.
####################################################################
def read_single_letter_references(r_num, r_con, r_beg, r_end):
    '''
    Parse a raw reference string and extract authors as well as title.
    This parsing routine is concerned with references where there is only a single
    name spelled out entirely per author, and the rest are delivered as single letters
    followed by periods. 

    Examples of strings it parses:
        - T. Ball, R. Majumdar, T. Millstein, and S. K. Rajamani. Automatic predicate abstraction of C programs.
        - A. Bartel, J. Klein, M. Monperrus, and Y. Le Traon. Automatically securing permission-based software by reducing the attack
        - A. Bose, X. Hu, K. G. Shin, and T. Park. Behavioral detection of malware on mobile handsets.

    Inputs: 
        - An element from a list as parsed by read_harvard_references

    Outputs:
        - On failure: None
        - On success:
    '''
    # Now find the period that divides the authors from the title
    authors = None
    rest = None
    space_split = r_con.split(" ")
    for idx2 in range(len(space_split) - 4):
        try:
            # This will capture when there are multiple authors
            if (space_split[idx2].lower() == "and"
                    and space_split[idx2 + 1][-1] == "."
                    and space_split[1][-1] == "."):
                # If we have a double single-letter name

                # Example: T. Ball, R. Majumdar, T. Millstein, and S. K. Rajamani. Automatic predicate abstraction of C programs.
                if space_split[idx2 + 2][-1] == "." and len(
                        space_split[idx2 + 2]) == 2:
                    print("Potentially last1: %s" % (space_split[idx2 + 4]))
                    authors = " ".join(space_split[0:idx2 + 4])
                    rest = " ".join(space_split[idx2 + 4:])
                # Example:  A. Bartel, J. Klein, M. Monperrus, and Y. Le Traon. Automatically securing permission-based software by reducing the attack
                elif space_split[idx2 + 2][-1] != "." and space_split[
                        idx2 + 3][-1] == ".":
                    print("Potentially last2: %s" % (space_split[idx2 + 4]))
                    authors = " ".join(space_split[0:idx2 + 4])
                    rest = " ".join(space_split[idx2 + 4:])
                # Example:A. Bose, X. Hu, K. G. Shin, and T. Park. Behavioral detection of malware on mobile handsets.
                else:
                    print("Potentially last3: %s" % (space_split[idx2 + 3]))
                    authors = " ".join(space_split[0:idx2 + 3])
                    rest = " ".join(space_split[idx2 + 3:])
                break
        except:
            None

    if authors == None:
        for idx2 in range(len(space_split) - 4):
            try:
                # This will capture when there is only a single author
                if (len(space_split[idx2]) == 2
                        and space_split[idx2][-1] == "."
                        and len(space_split[idx2 + 2]) > 2):
                    # If we have double single-letter naming
                    if space_split[idx2 + 1][-1] == "." and len(
                            space_split[idx2 + 1]) == 2:
                        print("Potentially last single 1: %s" %
                              (space_split[idx2 + 3]))
                        authors = " ".join(space_split[0:idx2 + 3])
                        rest = " ".join(space_split[idx2 + 3:])
                        break
                    else:
                        print("Potentially last single 2: %s" %
                              (space_split[idx2 + 2]))
                        authors = " ".join(space_split[0:idx2 + 2])
                        rest = " ".join(space_split[idx2 + 2:])
                        break
            except:
                None

    # Do some post processing to ensure we got the right stuff.
    # First ensure we at least have two words in authors:
    if authors != None and len(authors.split(" ")) < 2:
        print("Breaking 1")
        return None

    # Now ensure that the title is not just a name:
    if authors != None:
        try:
            title = int(rest.split(".")[0])
            # If the above is successful, then the title is just a number, which cannot be true
            print("Breaking 2")
            return None
        except:
            print("Could not break 2")
            None

    if authors != None:
        r_title = rest.split(".")[0]

        # with the special '' symbols (0x201c and 0x201d, respectively).
        #if chr(0x201d) in r_title:
        #    r_title = rest.split(chr(0x201d))[0]
        #    r_title = r_title[1:-1]
        #    rest = ".".join(rest.split(chr(0x201d))[1:])

        print("Authors: %s" % (authors))
        print("Title: %s" % (r_title))
        print("rest: %s" % (rest))

        # Create a directory
        ref_dict = dict()
        ref_dict['Authors'] = authors
        ref_dict['Title'] = r_title
        ref_dict['rest'] = rest
        ref_dict['num'] = r_num
        return ref_dict
    else:
        return None
    print("----------------")


def read_full_author_references(r_num, r_con, r_beg, r_end):
    '''
        This routine is focused on parsing references where the authors names are
        spelled out fully, including all names of each author.

        Examples: Sang Kil Cha, Thanassis Avgerinos, Alexandre Rebert, and David Brumley. 2012. Unleashing Mayhem on Binary Code. In IEEE Symposium on Security and Privacy (S&P).
    '''
    # Now find the period that divides the authors from the title
    authors = None
    rest = None
    space_split = r_con.split(".")
    print("Space split: %s" % (str(space_split)))

    # Merge all of the elements of the list that are of less than 2 in length:
    new_space_split = list()
    curr_elem = ""
    for elem in space_split:
        if len(elem) <= 2:
            curr_elem += "%s." % (elem)
        elif len(elem) > 2 and elem[-2] == ' ' and elem[-1] != ' ':
            curr_elem += "%s." % (elem)
        else:
            new_elem = "%s%s" % (curr_elem, elem)
            print("New elem: %s" % (new_elem))
            new_space_split.append(new_elem)
            curr_elem = ""
    space_split = new_space_split

    print("Refined space split: %s" % (str(space_split)))

    # See if it is clean
    if len(space_split) == 4:
        try:
            year = int(space_split[1])
            print("Gotten the reference")

            ref_dict = dict()
            ref_dict['Authors'] = space_split[0]
            ref_dict['Title'] = space_split[2]
            ref_dict['Venue'] = space_split[3]
            ref_dict['Year'] = space_split[1]
            ref_dict['rest'] = space_split[3]
            ref_dict['num'] = r_num
            return ref_dict
        except:
            None
    # Let's try a bit vaguer for the sake of it
    try:
        year = int(space_split[1])
        print("Gotten the reference")

        ref_dict = dict()
        ref_dict['Authors'] = space_split[0]
        ref_dict['Year'] = space_split[1]
        ref_dict['Title'] = space_split[2]
        ref_dict['rest'] = ".".join(space_split[3:])
        ref_dict['num'] = r_num
        return ref_dict
    except:
        None

    return None


def normalise_title(title):
    return title.lower().replace(",", "").replace(" ", "").replace("-", "")


##########################################
# End of citation parsing routines
##########################################


def parse_raw_reference_list(refs):
    '''
    The goal of this function is to convert the raw references
    into more normalized references, and in particular split
    the raw reference into authors and title of reference.

    An important aspect of this function is that it tries to pass
    the reference in multiple ways, based on how the citations
    are written.

    As such, this routine is somewhat implemented with a 
    test-and-check aproach in mind.
    '''
    parse_funcs = [read_single_letter_references, read_full_author_references]
    parse_success = []
    for parse_func in parse_funcs:
        missing_refs = []
        refined = []
        for ref in refs:
            res = parse_func(ref['number'], ref['raw_content'], ref['offset'],
                             0)
            if res == None:
                missing_refs.append(ref)
            else:
                refined.append(res)
        parse_success.append({
            'missing_refs': missing_refs,
            'refined': refined
        })

    # Now pick the index with highest number of successful parses
    if len(parse_success[0]['refined']) > len(parse_success[1]['refined']):
        parse_func = parse_funcs[0]
    else:
        parse_func = parse_funcs[1]

    # Now parse a last time and insert the parsed data into
    # the references dictionary.
    # This loop will modify the content of the dictionary.
    for ref in refs:
        res = parse_func(ref['number'], ref['raw_content'], ref['offset'], 0)
        ref['parsed'] = res
        if res != None:
            ref['normalised-title'] = normalise_title(res['Title'])
        else:
            ref['normalised-title'] = None


########################################
# Utility functions
########################################


def print_refined(refined):
    print("Refined lists:")
    #for rd in refined:
    #    try:
    #        print("\t%d"%(int(rd['num'])))
    #    except:
    #        None
    #    print("\tTitle: %s"%(rd['Title']))
    #    print("\tAuthors: %s"%(rd['Authors']))
    #    print("\tRest: %s"%(rd['rest']))
    #    print("#"*90)


def print_missing(missings):
    print("Missing refs:")
    #for ms in missings:
    #    print("\t%s"%(str(ms)))
    #    print("<"*90)


def read_decoded(file_path):
    '''
    Reads a file an encodes each data as an ASCII string. We do
    the ASCII encoding because many of the papers have some form
    of weird UTF-coding and we do not handle those at the moment.
    '''
    with open(file_path, "r") as f:
        json_content = json.loads(str(f.read().replace('\r\n', '')),
                                  strict=False)
        dec_content = dict()
        for elem in json_content:
            #dec_content[elem] = json_content[elem].encode('utf-8')
            dec_content[elem] = json_content[elem].encode('ascii', 'ignore')
            #asciidata= dec.encode("ascii","ignore")
        return dec_content


def parse_file(file_path):
    '''
    Parses a json file with the raw data of title and references
    and returns a list of citations made by this paper.
    '''
    # Read the json file with our raw data.
    dec_json = read_decoded(file_path)

    # Merge all lines in the file by converting newlines to spaces
    dec_json['References'] = dec_json['References'].decode("utf-8")
    print("Type: %s" % (str(type(dec_json['References']))))
    print(dec_json['References'])
    print(dec_json['References'].encode('ascii', 'ignore'))
    all_refs = dec_json['References'].replace(
        "\n", " ")  #decode("utf-8").replace("\n", " ")

    # Extract the references in a raw format. This is just splitting
    #
    references = split_reference_section_into_references(all_refs)

    # Decipher the references
    print("References")
    print(references)
    #refined, missing_sigs = parse_raw_reference_list(references)
    parse_raw_reference_list(references)
    print("Refined refs:")
    print(references)

    #print_refined(refined)
    #print_missing(missing_sigs)
    #print("Refined sigs: %d"%(len(refined)))

    # Now create our dictionary where we will wrap all data in
    paper_dict = {}
    paper_dict['paper-title'] = dec_json['Title']
    paper_dict['paper-title-normalised'] = normalise_title(
        dec_json['Title'].decode("utf-8"))
    paper_dict['references'] = references
    #paper_dict['success-sigs'] = refined
    #paper_dict['missing-sigs'] = missing_sigs

    return paper_dict
    #return refined, missing_sigs, dec_json['Title']


def read_json_file(filename):
    print("[+] Parsing file: %s" % (filename))
    ret = None
    try:
        ret = parse_file(filename)
    except:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_tb(exc_traceback, limit=10, file=sys.stdout)
        traceback.print_exception(exc_type,
                                  exc_value,
                                  exc_traceback,
                                  limit=20,
                                  file=sys.stdout)
        traceback.print_exc()
        formatted_lines = traceback.format_exc().splitlines()
    print("[+] Completed parsing of %s" % (filename))
    return ret


def identify_group_dependencies(workdir, parsed_papers):
    """ identifies who cites who in a group of papers """
    append_to_report(workdir, "######################################")
    append_to_report(workdir, "Dependency graph based on citations")
    #append_to_report(workdir, "######################################")
    g1 = gv.Digraph(format='png')

    MAX_STR_SIZE = 15
    idx = 0
    paper_dict = {}
    normalised_to_id = {}

    for src_paper in parsed_papers:
        #paper_dict[src_paper['result']['paper-title-normalised']] = idx
        if len(src_paper['result']['paper-title-normalised']) > MAX_STR_SIZE:

            target_d = src_paper['result']['paper-title-normalised'][
                0:MAX_STR_SIZE]
        else:
            target_d = src_paper['result']['paper-title-normalised']

        #paper_dict[src_paper['result']['paper-title-normalised']] = src_paper['result']['paper-title-normalised']
        paper_dict[src_paper['result']['paper-title-normalised']] = target_d
        #g1.node(str(idx))
        g1.node(target_d)
        idx += 1

    #print("Paper dict")
    #print(paper_dict)
    #print("-"*50)
    #raw_dependency_graph_path = os.path.join(workdir, "raw_dependency_graph.json")
    #with open(raw_dependency_graph_path, "w+") as dependency_graph_json:
    #    json.dump(paper_dict, dependency_graph_json)

    dependency_graph = []
    for src_paper in parsed_papers:

        cited_by = []
        for tmp_paper in parsed_papers:
            if tmp_paper == src_paper:
                continue
            # Now go through references of tmp_paper and
            # see if it cites the src paper
            cites = False
            for ref in tmp_paper['result']['references']:
                if ref['parsed'] != None:
                    if ref['normalised-title'] == src_paper['result'][
                            'paper-title-normalised']:
                        if len(tmp_paper['result']
                               ['paper-title-normalised']) > MAX_STR_SIZE:
                            src_d = tmp_paper['result'][
                                'paper-title-normalised'][0:MAX_STR_SIZE]
                        else:
                            src_d = tmp_paper['result'][
                                'paper-title-normalised']

                        if len(src_paper['result']
                               ['paper-title-normalised']) > MAX_STR_SIZE:
                            dst_d = src_paper['result'][
                                'paper-title-normalised'][0:MAX_STR_SIZE]
                        else:
                            dst_d = src_paper['result'][
                                'paper-title-normalised']
                        g1.edge(src_d, dst_d)

                        #src_idx = paper_dict[tmp_paper['result']['paper-title-normalised']]
                        #dst_idx = paper_dict[src_paper['result']['paper-title-normalised']]
                        #g1.edge(str(src_idx), str(dst_idx))
                        cites = True
            if cites == True:
                cited_by.append(tmp_paper)
        src_paper['cited_by'] = cited_by
        append_to_report(workdir, "Paper:")
        append_to_report(workdir, "\t%s" % (src_paper['filename']))
        append_to_report(workdir, "\t%s" % (src_paper['result']['paper-title']))
        append_to_report(workdir, "\tNormalised title: %s" %
              (src_paper['result']['paper-title-normalised']))
        append_to_report(workdir, "\tCited by: ")
        for cited_by_paper in cited_by:
            append_to_report(workdir, "\t\t%s" % (cited_by_paper['result']['paper-title']))
        append_to_report(workdir, "---------------------------------")

        paper_info = {}
        paper_info['name'] = src_paper['result']['paper-title'].decode("utf-8")
        paper_info['minimized-name'] = src_paper['result'][
            'paper-title-normalised']
        paper_info['imports'] = []
        for cited_by_paper in cited_by:
            paper_info['imports'].append({
                "name":
                cited_by_paper['result']['paper-title'].decode("utf-8"),
                "minimized-name":
                cited_by_paper['result']['paper-title-normalised']
            })
        dependency_graph.append(paper_info)

    #append_to_report(workdir, "Done identifying references within the group")
    #g1.view()

    filename = g1.render(
        filename=os.path.join(workdir, "img", "citation_graph"))
    print("idx: %d" % (idx))
    #print(parsed_papers)

    dependency_graph_path = os.path.join(workdir,
                                         "normalised_dependency_graph.json")
    with open(dependency_graph_path, "w+") as dependency_graph_json:
        json.dump(dependency_graph, dependency_graph_json)


def display_summary(workdir, parsed_papers_raw):
    succ = []
    fail = []
    succ_sigs = []
    miss_sigs = []
    all_titles = []
    append_to_report(workdir, "######################################")
    append_to_report(workdir, " Parsed papers summary        ")
    #append_to_report(workdir, "######################################")
    all_normalised_citations = set()
    for paper in parsed_papers_raw:
        append_to_report(workdir, "paper:")
        append_to_report(workdir, "\t%s" % (paper['filename']))
        append_to_report(workdir, "\t%s" % (paper['result']['paper-title']))
        append_to_report(workdir, "\tNormalised title: %s" %
              (paper['result']['paper-title-normalised']))
        append_to_report(workdir, "\tReferences:")
        for ref in paper['result']['references']:
            if ref['parsed'] != None:
                append_to_report(workdir, "\t\tAuthors: %s" % (ref['parsed']['Authors']))
                append_to_report(workdir, "\t\tTitle: %s" % (ref['parsed']['Title']))
                append_to_report(workdir, "\t\tNormalised: %s" % (ref['normalised-title']))
                all_normalised_citations.add(ref['normalised-title'])
            else:
                append_to_report(workdir, "\t\tCould not parse")
            append_to_report(workdir, "\t\t-------------------")
            #print("\t\t%s"%(str(ref['parsed'])))

        #print("[+] %s"%(paper['title']))
        if paper['result'] == None:
            fail.append(paper['filename'])
        else:
            succ.append(paper['filename'])

            for ref in paper['result']['references']:
                if ref['parsed'] != None:
                    succ_sigs.append(ref['parsed'])
                else:
                    miss_sigs.append(ref['raw_content'])

            #succ_sigs.append(paper['result']['success-sigs'])
            #miss_sigs.append(paper['result']['missing-sigs'])
            all_titles.append(paper['result']['paper-title'])

    # Check which papers are in our set:
    append_to_report(workdir, "######################################")
    append_to_report(workdir, "Papers in the data set :")
    #append_to_report(workdir, "######################################")
    cited_papers = list()
    noncited_papers = list()
    for paper in parsed_papers_raw:
        print(paper['result']['paper-title'])
        cited_by_group = False
        for s in all_normalised_citations:
            if s == paper['result']['paper-title-normalised']:
                cited_by_group = True
        if cited_by_group:
            cited_papers.append(paper)
        else:
            noncited_papers.append(paper)
    #append_to_report(workdir, "######################################")
    append_to_report(workdir, "Cited papers:")
    #append_to_report(workdir, "######################################")
    for p in cited_papers:
        append_to_report(workdir, "\t%s" % (p['result']['paper-title']))


    #append_to_report(workdir, "######################################")    
    append_to_report(workdir, "Noncited papers:")
    #append_to_report(workdir, "######################################")
    for p in noncited_papers:
        append_to_report(workdir, "\t%s" % (p['result']['paper-title']))

    #exit(0)

    # Now display the content.
    append_to_report(workdir, "Succ: %d" % (len(succ)))
    append_to_report(workdir, "Fail: %d" % (len(fail)))
    append_to_report(workdir, "Succ sigs: %d" % (len(succ_sigs)))
    append_to_report(workdir, "Failed sigs: %d" % (len(miss_sigs)))

    #append_to_report(workdir, "Summary of references:")
    # Now do some status on how many references we have in total
    all_refs = dict()
    #for siglist in succ_sigs:
    for sig in succ_sigs:
        # Normalise
        #append_to_report(workdir, "Normalising: %s" % (sig['Title']))
        tmp_sig = sig['Title'].lower().replace(",", "").replace(" ",
                                                                "").replace(
                                                                    "-", "")
        #append_to_report(workdir, "\tNormalised: %s" % (tmp_sig))

        #if "\xe2\x80\x9c" in tmp_sig:
        #    s1_split = tmp_sig.split("\xe2\x80\x9c")
        #    if "\xe2\x80\x9d" in s1_split[1]:
        #        tmp_sig = s1_split[1].split("\xe2\x80\x9d")[0]
        #    else:
        #        tmp_sig=s1_split[1]

        if tmp_sig not in all_refs:
            all_refs[tmp_sig] = 0
        all_refs[tmp_sig] += 1

        #if sig['Title'].lower() not in all_refs:
        #    all_refs[sig['Title'].lower().strip()] = 0
        #all_refs[sig['Title'].lower().strip()] += 1

    append_to_report(workdir, "######################################")
    append_to_report(workdir, "All Titles (normalised) of the papers in the data set:")
    #append_to_report(workdir, "######################################")
    for t in all_titles:
        append_to_report(workdir, "\t%s" % (t))
    append_to_report(workdir, "######################################")        

    append_to_report(workdir, "######################################")
    append_to_report(workdir, "All references/citations (normalised) issued by these papers")
    #append_to_report(workdir, "######################################")
    append_to_report(workdir, "\tName : Count")
    sorted_list = list()
    for title in all_refs:
        sorted_list.append((title, all_refs[title]))
    sorted_list = sorted(sorted_list, key=lambda x: x[1])
    for title, counts in sorted_list:
        append_to_report(workdir, "\t%s :  %d" % (title, counts))

    append_to_report(workdir, "######################################")
    append_to_report(workdir, "The total number of unique citations: %d" % (len(sorted_list)))
    #append_to_report(workdir, "######################################")
    return
    #exit(0)

    #all_missing_sigs = []
    #for missig in miss_sigs:
    #    all_missing_sigs += missig

        #for miss in missig:
        #    print("###\t%s"%(str(miss)))

    #print(
    #    "[+] The references that we were unable to fully parse, but yet are cited by the papers:"
    #)
    #print(
    #    "Total amount of references not parsed and thus not included in analysis: %d"
    #    % (len(all_missing_sigs)))
    #print("All of these references:")
    #for missig in all_missing_sigs:
    #    print("###\t%s" % (str(missig)))


def parse_first_stage(workdir, target_dir):
    parsed_papers = []
    for json_f in os.listdir(target_dir):
        if ".json" in json_f:
            complete_filename = os.path.join(target_dir, json_f)
            print("Checking: %s" % (complete_filename))
            res = read_json_file(complete_filename)
            parsed_papers.append({
                "filename": complete_filename,
                "result": res
            })
    #display_summary(parsed_papers)

    parsed_papers_json = os.path.join(workdir, "parsed_paper_data.json")
    with open(parsed_papers_json, "w+", encoding='utf-8') as ppj:
        json.dump(parsed_papers, ppj)

    return parsed_papers


if __name__ == "__main__":
    succ = []
    fail = []
    succ_sigs = []
    miss_sigs = []
    all_titles = []
    for json_f in os.listdir("."):
        if ".json" in json_f:
            if len(sys.argv) == 2:
                if sys.argv[1] not in json_f:
                    continue
            print("Checking: %s" % (json_f))

            res = read_json_file(json_f)
            if res == None:
                fail.append(json_f)
                sys.stdout.flush()
                continue
            succ.append(json_f)
            succ_sigs.append(res['success-sigs'])
            miss_sigs.append(res['missing-sigs'])
            all_titles.append(res['paper-title'])

    print("Succ: %d" % (len(succ)))
    print("Fail: %d" % (len(fail)))
    print("Succ sigs: %d" % (len(succ_sigs)))
    print("Failed sigs: %d" % (len(miss_sigs)))
    display_summary(succ, fail, succ_sigs, miss_sigs, all_titles)
