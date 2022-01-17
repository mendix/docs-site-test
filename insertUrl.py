# -*- coding: UTF-8 -*-
"""
Usage: 
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
import re    # Using re.sub()
import fileinput
import json

# grab working directory
startDir = input('Specify FULL PATH to local content directory: ')
# change current working directory
os.chdir(startDir)
# print new working directory
print('\nCurrent working directory: ', os.getcwd(), end='\n')

# The top argument for walk
topdir = '.'
# The extension to search through
#let's hardcode .md
exten = '.md'#input('\nPlease specify file extension to search: ')

# name of url log for later
logname = 'urlLog.json'
urlList = []
# What are we searching for
#let's hardcode
start = 'title: "?.*"?'#input('\nPlease type in Regex to match:\n(hint: to match an entire title type in title: ".*") ')

for dirpath, dirnames, allfiles in os.walk(topdir):
    for name in allfiles:
        if name.lower().endswith(exten):
            #print('File: ', os.path.join(dirpath, name))  # Print Filename
            os.altsep = '/'
            altPath = dirpath.replace(os.sep, os.altsep)
            # for toplevel directory
            with fileinput.input(os.path.join(dirpath, name), inplace=True, backup='', encoding="utf-8") as file:
                lineNum = 0
                for line in file:
                    lineNum += 1
                    searchTitle = re.search(start,line)
                    if lineNum < 5 and searchTitle != None:
                        matched = searchTitle
                        urlString = ''
                        # for toplevel directory
                        if dirpath == '.':
                            if name == 'index.md':
                                urlString = '/'
                            else:
                                urlString = '/' + name[:-(len(exten))] + '/'
                        # anything deeper
                        else:
                            if name == 'index.md':
                                urlString = '/' + altPath[2:] + '/'
                            else:
                                urlString = '/' + altPath[2:] + '/' + name[:-(len(exten))] + '/'
                        insert = matched.string + 'url: ' + urlString + '\n'
                        line = insert
                        # creates a dictionary for every entry, loggin the directory and url
                        itemDict = {"Dir": os.path.join(dirpath, name), "url": urlString}
                        # appends each dictionary to urlList
                        urlList.append(itemDict)
                    print(line, end='')


 
# Write grabbed urls to logfile
with open(logname, 'w') as logfile:
    # writes all of urlList as a json file (list of dicts)
    json.dump(urlList, logfile)