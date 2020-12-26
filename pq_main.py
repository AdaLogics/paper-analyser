import os
import sys
import simplejson as json
import argparse
import shutil

import pq_format_reader
import pq_pdf_utility


### Utilities
def create_working_dir(target_dir):
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)


def create_workdir():
    MDIR = "pq-out"
    if not os.path.isdir(MDIR):
        os.mkdir(MDIR)

    FNAME = "out-"
    max_idx = -1
    for l in os.listdir(MDIR):
        if FNAME in l:
            try:
                val = int(l.replace(FNAME, ""))
                if val > max_idx:
                    max_idx = val
            except:
                None
    max_idx += 1
    new_workdir = os.path.join(MDIR, "%s%d" % (FNAME, max_idx))
    print("Making the work directory: %s" % (new_workdir))
    os.mkdir(new_workdir)
    return new_workdir


### Action functions
def convert_pdfs_to_data(paper_dir, workdir, target_dir):
    # First extract data from the pdf files, such as
    # title as well as the references cited by each paper.
    # This will produce json files with the data that we need.
    filtered_pdf_list = pq_pdf_utility.convert_folder(workdir, paper_dir)

    # Now write it out to a json folder
    create_working_dir(target_dir)
    pq_pdf_utility.write_to_json(filtered_pdf_list, target_dir)


def read_parsed_json_data(workdir, target_dir):
    # Reads the json files produced by "full-run", and extracts the
    # various forms of data.
    parsed_papers = pq_format_reader.parse_first_stage(workdir, target_dir)

    pq_format_reader.display_summary(workdir, parsed_papers)

    # Now extract the group dependencies
    pq_format_reader.identify_group_dependencies(workdir, parsed_papers)


### CLI
def parse_args():
    parser = argparse.ArgumentParser(
        "pq_main.py", description="Quantitative analysis of papers")

    parser.add_argument("-f", "--folder", help="Folder with PDFs")
    parser.add_argument("--task",
                        help="Specify a given task",
                        default="dependency-graph")
    parser.add_argument("--wd", help="Workdir")

    args = parser.parse_args()
    if args.folder != None:
        print("Analysing folder the pdfs in folder: %s" % (args.folder))

    return args


if __name__ == "__main__":
    args = parse_args()
    if args.task == "json-only":
        read_parsed_json_data(args.wd, os.path.join(args.wd, "json_data"))
    elif args.task == "dependency-graph":
        workdir = create_workdir()
        json_data_dir = os.path.join(workdir, "json_data")

        convert_pdfs_to_data(args.folder, workdir, json_data_dir)
        read_parsed_json_data(workdir, json_data_dir)
    else:
        print("Task not supported")
