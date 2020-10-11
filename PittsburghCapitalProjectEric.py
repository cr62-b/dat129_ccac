# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:33:05 2020

@author: Cliff
"""

"""
Dat-129  Python2 Programming
Assignment Pittsburgh Capital Project
Due 09-16-2020
Clifford B. Rohal

Session on JSON
Shows the basic usage of the json module and then inject data in JSON format
for processing and exporting transportable information.
"""
import json

# read in the contents of a file encoded in JSON and display
# in its native python object form
with open('pghprojserachcriteria.json') as proj_criteria:
    # give the file object to json.load, who will read its
    # contents and generate all native python objects 
    # which we can access through nativeCriteria
    native_criteria = json.load(proj_criteria)
    # manipulate the underlying python object in normal python
    native_criteria['fiscal_year'] = [2019, 2020]
    # see the result with a simple print
    print(native_criteria)
{'fiscal_year': [2019, 2020], 'start_date': [''], 'area': ['Facility Improvement'], 'asset_type': ['Park'], 'planning_status': ['Completed', 'Planned']}

'''
Generate objects in python and write them to a file in JSON format
using json.dumps

Chat processing specs:
0) Get file into PYTHON for text processing
1) Ingest native text file from Zoom, and at minimum,
aggregate each student's responses if issued over multiple 
chats
'''
import csv
# declare the Zoom-standard name prefix in its encoding of the chat history
STUD_NAME_PREFIX = ' From '

def build_dict_from_raw_name_content_list(f): 
    # we'll load this dictionary up as we read the chat CSV from the file
    responses = {}
    with open(f) as chats:
        chat_reader = csv.reader(chats, delimiter='\t')
        for line in chat_reader:
#             print(line)
            # the second item in the list is the name string (first is timestamp)
            name_cont = line[1]
            separated_name_cont = name_cont.split(sep=':',maxsplit=1)
            name = separated_name_cont[0][6:].rstrip()
            # extract second item from our list made from a chat line
            content = separated_name_cont[1]
            # check the dictionary for the presence of the name
            if name in responses:
                # if dict contains the key already, extract value, and append
                # the entire response string
                responses[name].append(content)
            else:
                # make a new dictionary entry keyed to the stripped student name
                responses[name] = [content,]
    print(responses)
    return responses

def write_chats_to_json(resdict):
    # Create a file into which we shall inject JSON
    with open('chat.json', 'w') as jsonfile:
        # give file and incoming content to json.dump
        json.dump(resdict, jsonfile)
        print("file written")

# run our dictionary assembly function that gives us a dictionary of
# responses given a text file name

response_dict = build_dict_from_raw_name_content_list('langs.txt')
write_chats_to_json(response_dict)