# -*- coding: UTF-8 -*-
"""
Pushes the JSON file created with the algolia index (public/mxdocsalgolia.json) to Algolia
1. Checks that this is a merge to master, otherwise ends
2. Checks that the file exists, otherwise errors
3. Uses algolia 

We don't need to check if this is a deployment merge as this will be called only in the deployment stage of Travis
"""

import os    # Using os.environ[], os.path.exists()
import sys   # Using sys.exit()
import json  # Using json.load
from algoliasearch.search_client import SearchClient # Using SearchClient.create client.init_index index.replace_all_objects

mxDocsAlgoliaFileName = "public/mxdocsalgolia.json" # the algolia index generated by HUGO
# Get Algolia credentials from environment variables - will error if variable doesn't exist.
algoliaApplicationID = os.environ['ALGOLIA_APPLICATION_ID']
algoliaAdminAPIKey = os.environ['ALGOLIA_ADMIN_API_KEY']
algoliaIndexName = os.environ['ALGOLIA_INDEX_NAME']
pushIfBranch = "master" # push to Algolia if we are merging to this branch
targetBranch = os.environ['TRAVIS_BRANCH'] # which branch are we merging to

if targetBranch == pushIfBranch: # Only process if this is the correct branch (e.g. master)
    print ("Pushing index to Algolia index", algoliaIndexName, ", target branch is", targetBranch)
    if os.path.exists (mxDocsAlgoliaFileName): # Only process if file exists
        print ("Found file", mxDocsAlgoliaFileName)
        if os.path.getsize(mxDocsAlgoliaFileName) != 0: # File must contain something
            mxDocsAlgoliaFile = open(mxDocsAlgoliaFileName, "r", encoding='utf-8')
            algoliaClient = SearchClient.create(algoliaApplicationID, algoliaAdminAPIKey)
            algoliaIndex = algoliaClient.init_index(algoliaIndexName)
            mxDocsAlgoliaJSON = json.load(mxDocsAlgoliaFile)     # Convert json file into a Python object.
            algoliaIndex.replace_all_objects(mxDocsAlgoliaJSON) # Zero downtime replacement of current index - needs this setting for some reason
            mxDocsAlgoliaFile.close()
        else:
            print ("File", mxDocsAlgoliaFileName, "is empty")
            sys.exit (-1)
    else:
        print ("File", mxDocsAlgoliaFileName, "not found")
        sys.exit (-1)
else:
    print ("Not pushing index to Algolia, target branch is", targetBranch)