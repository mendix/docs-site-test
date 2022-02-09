# -*- coding: UTF-8 -*-
"""
Usage:

python souptest <directory>

<directory> is the root directory for the site

Input a directory to work from, specify which filetype to search through,
type in the regex expression to match.
The script walks through all files within the top directory. 
Each line in each file is searched for the regex query. 
The url parameter gets grabbed from the directory path, reformatted and 
inserted in a new line after the matched query.
I still have to figure out what to do with files named 'index',
as the url is in part made up of the file name.
"""

import os    # Using os.chdir(), os.listdir(), os.path.isfile(), os.rename()
import sys   # sys.argv are the arguments to the python program

# Import BeautifulSoup to help with HTML parsing
from bs4 import BeautifulSoup

# Define variables

topdir = '.' # start in current directory - once we have changed directory to first argument
exten = '.html' # Only html files
os.altsep = '/' # to ensure links have correct separators

link_list = []
id_list = []

# Helper functions for find_all
# Return true if tag has an href attribute
def has_href(tag):
    return tag.has_attr('href')

# Return true if tag has an id or name attribute
def has_name_or_id(tag):
    return tag.has_attr('name') or tag.has_attr('id')


# Need to loop through all files here!
# ====================================

# First change to selected directory
os.chdir (str(sys.argv[1]))
print("Working directory is " + os.getcwd())

# for dirpath, dirnames, allfiles in os.walk(topdir):
#    for filename in allfiles:
#        if filename.lower().endswith(exten):
# hardcode for now
dirpath = ".\\"
filename = "souptest.html"

#remove leading "." and put in correct separators
altpath = str(dirpath.replace(os.sep, os.altsep))[1:]

# Open the file
with open(filename, encoding="utf-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Find all the tags within <main></main> with href and add them to 
# We haven't recorded the file where the error is going to be found. We need to sort it as well :-( need to append the information  to link_list, but ignore when comparing the lists) perhaps look at this: https://www.pythonpool.com/python-sort-list-of-lists/
for link_tag in soup.main.find_all(has_href):
    this_href = link_tag['href']
    if this_href.startswith("https://"):
        pass # external link
    elif this_href.startswith("http://"):
        pass # external link
    elif this_href.startswith("#"):
        # add current path and file to anchor
        link_list.append (altpath + ("" if altpath.endswith("/") else os.altsep) + os.path.splitext(filename)[0] + this_href)
    else:
        # add filename "index"
        link_list.append (this_href.replace("#", "index#"))

# Add this path and file (without extension) to id_list 
id_list.append (altpath + ("" if altpath.endswith("/") else os.altsep) + os.path.splitext(filename)[0])
# Add all id tags to id_list in the format
# path/file#tag (where file has no extension)
for id_tag in soup.main.find_all(has_name_or_id):
    id_list.append (altpath + ("" if altpath.endswith("/") else os.altsep) + os.path.splitext(filename)[0] + "#" + id_tag ['id'])

link_list.sort()
print ("All the HREF tags")
print (*link_list, sep="\n")
id_list.sort()
print ("All the ID tags")
print (*id_list, sep="\n")

# Now we need to go through these lists and compare
# something like: https://stackoverflow.com/questions/50224772/python-algorithm-to-compare-two-sorted-lists-and-count-how-many-elements-are-the
# We haven't recorded the file where the error is going to be found. A third list original_file_list[]?
