import mysql.connector

mydb=mysql.connector.connect(
     host="localhost",
     user="root",
     password="123456",
     database="prodevops"
     
 )
mycursor=  mydb.cursor()


  
  
def showAllDB():
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)
    
def CreateTabale():
    mycursor.execute("CREATE TABLE log (host VARCHAR(255), status VARCHAR(255))")
    
def showTables():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)  

def alterTable():
       mycursor.execute("ALTER TABLE log ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")   
       
def insertData(arr):
    sql="INSERT INTO log (host, status) VALUES (%s, %s)"
    val=arr
    
    mycursor.executemany(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "was inserted.") 
    print("1 record inserted, ID:", mycursor.lastrowid)        
    
def selectAll(tabalename,state,limit): #(tabale name, fetch node) 
    
    sql="SELECT * FROM "+tabalename+"  LIMIT "+limit 
    mycursor.execute(sql)
     
    if state=="all":
      myresult = mycursor.fetchall() #all record
      for x in myresult:
            print(x)
            
    else:    
        myresult=mycursor.fetchone() #one record
        print(myresult)
        
def seletcWhere(tableName,condition):
    sql="SELECT * FROM "+tableName+" WHERE host= %s ORDER BY id DESC" #Prevent SQL Injection
    host=(condition,)
    
    mycursor.execute(sql,host) 
    myresult = mycursor.fetchall() 
    
    for x in myresult:
        print(x)
        
def deleteRecord(tableName,condition):
    sql="DELETE FROM "+tableName+" WHERE host= %s" #Prevent SQL Injection
    host=(condition,)
    
    mycursor.execute(sql,host)
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) deleted") #Prevent SQL Injection
     
def updateTable(tabalename,condition):
    sql="UPDATE log SET status=%s WHERE host=%s"
    val=(condition[0],condition[1])
    
    
    mycursor.execute(sql,val)
    mydb.commit()
    
    print(mycursor.rowcount, "record(s) deleted")              
   
       
        
        
              
   
    
#showAllDB()    
#CreateTabale()    #If the above code was executed with no errors, you have now successfully created a table.
#showTables()
#alterTable()

value = [
  ('arifa.ir', 'false'),
  ('prodevops.ir', 'false'),
  ('jabj.ir', 'true'),
  ('bojd.ir', 'true')
]
#insertData(value)
#selectAll("log","all","1000") # "all"-> fetchall record and  "one"-> fetch one record and 5 -> limit
#seletcWhere("log","arifa.ir")
#deleteRecord("log","arifa.ir")

val=["unknown","arifa.ir"]
updateTable("log",val)