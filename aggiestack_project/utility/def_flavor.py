'''
Created on Sep 23, 2018

@author: sharm
'''
import aggiestack_project.utility.database_connection
import os.path
#import logger

import aggiestack_project.utility.database_crud as db_crud

def loadFlavorList(flavorListPath):
    db_crud.loadList(flavorListPath,["flavor_name","RAM","numDisks","numVcpus"],'flavor_collection')

def getFlavorList():
    print ("These are the flavors configured on the server")
    db_crud.getList('flavor_collection')  

# def getFlavor(flavor):
#     return db_crud.getItem('flavor_name',flavor,'flavor_collection')
# 
# 
# def clearFlavorList():
#     db_crud.clearList('flavor_collection')
# 
# def isValidFlavor(flavor):
#     return db_crud.isAvailable('flavor_name',flavor,'flavor_collection')