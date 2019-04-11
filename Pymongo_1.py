
from pymongo import MongoClient

try: 
    conn = MongoClient() 
    print("Connected successfully to MongoDB!!!") 
    print("###########################")
except:   
    print("Could not connect to MongoDB") 

db=conn.Employee
collection=db.Empl_details

class Pymongo_:
    def __init__(self):
        pass
        
    def current_docs(selfJ):
        print("Current documents in the collection") 
        cursor = collection.find()
        for record in cursor: 
            print(record)
        
    def user_interests(self):
        print("Enter 1 for inserting a new document")
        print("Enter 2 for updating existing document")
        print("Enter 3 for deleting document")
        Choice=int(input("Please enter your choice:"))
        return Choice

Obj=Pymongo_()

Choice=Obj.user_interests()

        
if Choice==1:
    Obj.current_docs()
    id=int(input("Please enter employee id:"))
    name=input("Please enter employee name:")
    Ph=int(input("Please enter employee's phone number:"))
    Addr=input("Please enter employee's address:")

    employee={"_id":id,"name":name,"Phone":Ph,"Address":Addr}
    records = collection.insert_one(employee)
    Obj.current_docs()
    
elif Choice==2:
    Obj.current_docs()
    updtkey=int(input("Please enter the id of the employee who needs updation:"))
    new_addr=input("Please enter the new address of the employee:")
    result = collection.update_one({"_id":updtkey},{"$set":{"Address":new_addr}})
    Obj.current_docs()   


elif Choice==3:
    Obj.current_docs()
    delkey=int(input("Please enter the id of the employee who needs to be deleted:"))
    result=collection.delete_one({"_id":delkey})
    Obj.current_docs()
else:
    print("Please verify your choice. Its incorrect!")    