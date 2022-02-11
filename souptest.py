# -*- coding: UTF-8 -*-
"""
Usage:

python souptest <directory>

<directory> is the root directory for the site

The script walks through all files within the top directory. 

"""

import os    # Using os.chdir(), os.listdir(), os.path.isfile(), os.rename()
import sys   # sys.argv are the arguments to the python program, sys.exit allows exiting with an error message.

# Import SoupStrainer and BeautifulSoup to help with HTML parsing
from bs4 import SoupStrainer
from bs4 import BeautifulSoup

# Define variables

topdir = '.' # start in current directory - once we have changed directory to first argument
exten = '.html' # Only html files
os.altsep = '/' # to ensure links have correct separators

file_count = 0
link_list = []
id_list = []

# Helper functions for find_all
# Return true if tag has an href attribute
def has_href(tag):
    return tag.has_attr('href')

# Return true if tag has an id or name attribute
#######################################
# DO WE NEED TO LOOK AT NAME AS WELL? #
#######################################
def has_name_or_id(tag):
    return tag.has_attr('id') # or tag.has_attr('name')


# Need to loop through all files here!
# ====================================

# First change to selected directory
if len(sys.argv) < 2:
    sys.exit ("Program needs a directory as an argument")
os.chdir (str(sys.argv[1]))
print("Working directory is " + os.getcwd())

for dirpath, dirnames, allfiles in os.walk(topdir):
    for filename in allfiles:
        if filename.lower().endswith(exten):

            #remove leading "." and put in correct separators, including one at the end if necessary
            file_count += 1
            if file_count % 20 == 0:
                print ("Processed " + str(file_count) + " files")
            altpath = str(dirpath.replace(os.sep, os.altsep))[1:]
            altpath = altpath + ("" if altpath.endswith("/") else os.altsep)
            # and record this file name as this_file
            this_file = altpath + os.path.splitext(filename)[0]

            # Open the file
            with open(dirpath + os.sep + filename, encoding="utf-8") as fp:
                file_content = fp.read()

            main_tags = SoupStrainer("main")
            soup = BeautifulSoup(file_content, "lxml", parse_only=main_tags) # default parser is "html.parser"

            # break if there is no <main> section
            if soup.main is None:
                break
            
            # Find all the tags within <main></main> with href and add them to link_list
            # link_list is a list of lists: [[href, contained in file], [href, contained in file], ...]
            # If the target is wrong, we can then report which file contained the href

            for link_tag in soup.main.find_all(has_href):
                this_href = link_tag['href']
                if this_href.startswith("https://"):
                    pass # external link
                elif this_href.startswith("http://"):
                    pass # external link
                elif this_href.startswith("mailto:"):
                    pass # mailto link
                elif this_href.startswith("#"):
                    # add current path and file to anchor
                    link_list.append ([this_file + this_href, this_file])
                else:
                    # add filename "index"
                    if this_href.endswith("/"):
                        this_href = this_href + "index"
                    link_list.append ([this_href.replace("/#", "/index#"), this_file])

            # Add this path and file (without extension) to id_list 
            id_list.append (this_file)
            # Add all id tags to id_list in the format
            # path/file#tag (where file has no extension)
            for id_tag in soup.main.find_all(has_name_or_id):
                id_list.append (this_file + "#" + id_tag ['id'])

# Now we need to sort the lists and then go through them lists and compare
# For each non-matching item, add it to error_list
link_list.sort()
id_list.sort()

link_len = len(link_list)
id_len = len(id_list)
error_list = []
link_count = id_count = 0
while link_count< link_len and id_count< id_len:
    if link_list[link_count][0] > id_list[id_count] and id_count == id_len - 1 :
        # we've run out of ids to test against - this is the last one
        error_list.append (link_list[link_count])
        link_count += 1
    elif link_list[link_count][0] > id_list[id_count]:
        # haven't reached where the target would be
        id_count += 1
    elif link_list[link_count][0] == id_list[id_count]:
        # this one matches, go to next link to test
        link_count += 1
    else:
        # we've gone past without finding the match, so the match wasn't there
        error_list.append (link_list[link_count])
        link_count += 1

error_list.sort(key=lambda x:x[1]) # sort list on second item

with open("souptest-links.log", 'w') as logfile:
    for link_item in link_list:
        logfile.write (link_item[0] + " is a link in file " + link_item[1] + "\n")

with open("souptest-ids.log", 'w') as logfile:
    for id_item in id_list:
        logfile.write (id_item + " is a valid anchor id\n")

with open("souptest.log", 'w') as logfile:
    for error_item in error_list:
        logfile.write ("In " + error_item[1] + " link to " + error_item[0] + " is incorrect\n")

for error_item in error_list:
    print ("In " + error_item[1] + " link to " + error_item[0] + " is incorrect")

len_error_list = len(error_list)
if len_error_list == 0:
    print ("There were no bad links found")
elif len_error_list == 1:
    print ("There was " + str(len_error_list) + " bad link found")
else:    
    print ("There were " + str(len_error_list) + " bad links found")
