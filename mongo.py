import pymongo


myClient=pymongo.MongoClient("mongodb://localhost:27017/")

myDict={"ip":"192.168.1.2","host":"prdevops.ir","status":"false"}
multi_dict=[
    {"ip":"192.168.1.3","host":"prdevops.ir","status":"false"},
    {"ip":"192.168.1.4","host":"arifa.ir","status":"true"},
    {"ip":"192.168.1.5","host":"bojd.ir","status":"true"},
    {"ip":"192.168.1.6","host":"jabj.ir","status":"unknown"}
]


############################################################################


def insert_document(data,myCol):
    result=myCol.insert_many(data)
    return result.inserted_ids

############################################################################


def create_collection(colName,myDB):
    coList=myDB.list_collection_names()
    print(coList) #ouput=['log']
    
    if colName in coList:
        return False
    else:
        myColl=myDB[colName]
        return myColl   
#############################################################################    

def create_databaase(dbName):
    dbList=myClient.list_database_names()
    print(dbList) #output=['admin', 'config', 'local']
    
    if dbName  not in dbList:
        myDB=myClient[dbName]
        return myDB    
    
##############################################################################

def finddoc(colName):
    return colName.find_one()
    
##############################################################################

def findAllDoc(colName):
    return colName.find().sort("ip",-1).limit(5) #To limit the result 

#sort("name", 1) #ascending
#sort("name", -1) #descending

##############################################################################

def findSomefiled(colName,ip,status):
    return colName.find({},{"ip":ip,"status":status}) #one method like select * and two method like just show ip and status filed -SELECT ip,status
   
    
##############################################################################

def findSomeDoc(colName,ip,status):
    return colName.find({"ip":ip,"status":status}) # like where in sql -select * where ip=ip and status= ...

##############################################################################

def uptadeDoc(colName,host,status):
    myquery={"host":host}
    newvalue={ "$set": { "status": status } }
    
   # return colName.update_one(myquery,newvalue)
    return colName.update_many(myquery,newvalue)
   


dbResult=create_databaase("prodevops") 
if dbResult:
    print("Database create")
    myDB=(dbResult)
else:
    print("The database exist!")
    myDB=myClient["prodevops"]
  
 
collResult=create_collection("log",myDB)
if collResult:
    print("Collection create")
    myColl=collResult
else:
    print("The collection exist!")
    myColl=myDB["log"]


docResult=insert_document(multi_dict,myColl)
if docResult:
    print("Document insert",docResult),
    for objID in docResult:
        print(objID)
else:
    print("Oops!")    


findResult=finddoc(myColl)
if findResult:
    print(findResult)
    for key,value in findResult.items():
        #print(key,value)
        pass
    
findAllResult=findAllDoc(myColl)
if findAllResult:
    for i in findAllResult:
        #print(i)
        pass
 
findSomeResult=findSomefiled(myColl,"192.168.1.3","false")
if findSomeResult:
    for i in findSomeResult:
       #print(i)
        pass
    
findSomeDocResult=findSomeDoc(myColl,"192.168.1.4","false")
if findSomeDocResult:
    for i in findSomeDocResult:
       #print(i)
        pass

updateDocResult=uptadeDoc(myColl,"arifa.ir","true")                                