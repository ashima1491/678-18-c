

#import logger

import aggiestack_project.utility.database_crud as db_crud

def loadFlavorList(flavorListPath):
    db_crud.loadList(flavorListPath,["flavor_name","RAM","numDisks","numVcpus"],'flavor_collection','flavor_name',0)

def getFlavorList():
    print ("These are the flavors configured on the server")
    db_crud.getList('flavor_collection',["flavor_name","RAM","numDisks","numVcpus"])  
def getFlavor(flavor):
    return db_crud.getItem('flavor_name',flavor,'flavor_collection')
