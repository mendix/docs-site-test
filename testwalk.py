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
rootdirectory = os.getcwd()
print("Working directory is " + rootdirectory)

for dirpath, dirnames, allfiles in os.walk(topdir):
   for filename in allfiles:
        altpath = dirpath.replace(os.sep, os.altsep)
        print ("dirpath, and filename are: " + altpath +  ", and " + filename)
