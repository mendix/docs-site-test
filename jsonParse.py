import json
import os
import fileinput
import copy

jsonToParse = input('Please specify JSON file: ')

# grab working directory
startDir = input('Please specify directory: ')
# change current working directory
os.chdir(startDir)
# print new working directory
print('\nCurrent working directory: ', os.getcwd(), end='\n')

# The top argument for walk
topdir = '.'
# The extension to search through
exten = '.md'
# What will be logged
logname = 'json-log.log'
catName = 'json-cat.log'
results = str()
categories = str()
myList = []
baseParent = []
childrenOfCategories = []
childrenOfParents = []
childrenOfParentsCopy = []
parents = []
catList = []

# returns dictionary item from a list of dictionaries
def nextItem(key, value, list_dicts):
    for item in list_dicts:
        if item[key] == value:
            return item

# JSON parsing
print("Started Reading JSON file")
with open(jsonToParse, "r") as read_file:
    #initial list of menu items, kept so we can debug 
    menuItems = json.load(read_file)
    #completely detatched copy of menuItems
    myList = copy.deepcopy(menuItems)

    #first loop to grab all items and create separate lists
    for item in myList:
        # grabs item that has a category tag as parent and adds to childrenOfCategories list
        if "c" in item:
            childrenOfCategories.append(item)
        # grabs item that has a parent tag, puts into parent list and adds to childrenOfParents list
        elif "p" in item:
            childrenOfParents.append(item)
            parents.append(item["p"])
        # grabs baseparent of all entries in json
        elif "m" in item:
            baseParent = item
        # grabs all categories and adds to catList and parents list
        else:
            categories += '%s\n' % item["i"]
            catList.append(item)
            parents.append(item["i"])

        #hardcopy of childrenOfParents list, original gets changed with every item update
        childrenOfParentsCopy = copy.deepcopy(childrenOfParents)

    #loop again to sort directory of each item
    for item in myList:
        #if item is not a parent to any page, it won't be _index, won't get a directory named after it
        if item["i"] not in parents:
            item["d"] = "/"
        #if it is a parent, it will be _index and get a directory named after it
        else:
            item["d"] = "/" + item["i"] + "/"
            item["indexFlag"] = "true"
        #checks if item has a parent
        if "p" in item:
            parentChecker = nextItem("i", item["p"], childrenOfParentsCopy)
            #as long as item has a parent
            while parentChecker != None:
                if parentChecker["i"] not in parents:
                    item["d"] = "/" + parentChecker["p"] + item["d"]
                else:
                #add parent name to dir path
                    item["d"] = "/" + parentChecker["i"] + item["d"]
                #set parent
                item["p"] = parentChecker["p"]
                #grabs next parent, if there is one
                parentChecker = nextItem("i", item["p"], childrenOfParentsCopy)
            #checks if the next parent is a child of a category
            childOfCategoryChecker = nextItem("i", item["p"], childrenOfCategories)
            #if next parent is a child of a category
            if childOfCategoryChecker != None:
                #set parent to child of category
                item["p"] = childOfCategoryChecker["i"]
                #add child category name to dir path
                item["d"] = "/" + childOfCategoryChecker["i"] + item["d"]
            #checks if the next parent is a category
            categoryChecker = nextItem("t", childOfCategoryChecker["c"], catList)
            #if next parent is a category
            if categoryChecker != None:
                #set parent to category
                item["p"] = categoryChecker["i"]
                #add base directory and category to dir path
                item["d"] = baseParent["u"] + categoryChecker["i"] + item["d"]
        #checks if item has a category as parent (for items with only category parents)
        elif "c" in item:
            categoryChecker = nextItem("t", item["c"], catList)
            #if next parent is a category
            if categoryChecker != None:
                #set parent to category
                item["p"] = categoryChecker["i"]
                #add base directory and category to dir path
                item["d"] = baseParent["u"] + categoryChecker["i"] + item["d"]
        #checks if item is baseParent
        elif "m" in item:
            #set dir path
            item["d"] = baseParent["u"]
            #add indexFlag
            item["indexFlag"] = "true"
        #for categories
        else:
            #set dir path
            item["d"] = baseParent["u"] + item["i"] + "/"

        #save items to results
        results += '%s\n' % item

#for all files in dir path
for dirpath, dirnames, allfiles in os.walk(topdir):
    for name in allfiles:
        #if name is lowecase with extension .md
        if name.lower().endswith(exten):
            #matches next item by name
            itemGrab = nextItem("i", name[:-(len(exten))], myList)
            #if the name exists in myList
            if itemGrab != None:
                #reverse / to \ in path
                altPath = itemGrab["d"].replace('/', os.sep)
                #make all levels of directories between supplied path of itemGrab and starting directory
                os.makedirs((startDir + altPath), exist_ok=True)
                #if file has indexFlag
                if "indexFlag" in itemGrab:
                    #move file and rename to _index.md
                    os.replace(startDir + dirpath + '\\' + name, startDir + altPath + '\\' + '_index.md')
                else:
                    #move file
                    os.replace(startDir + dirpath + '\\' + name, startDir + altPath + '\\' + name)

# Write results to logfile
with open(logname, 'w') as logfile:
    logfile.write(results)
with open(catName, 'w') as catfile:
    catfile.write(categories)