
from pymongo import MongoClient



class Pymongo_:
    def __init__(self):
        pass
        
    def connect(self):
        try: 
            conn = MongoClient() 
            print("Connected successfully to MongoDB!!!")
            print("##########################################") 
        except:   
            print("Could not connect to MongoDB") 
        dbase=input("Please enter the database name:")    
        db=conn.dbase
        collectn=input("Please enter the collection name:")
        self.collection=db.collectn   
        
    def current_docs(self):
        print("Current documents in the collection") 
        cursor = self.collection.find()
        for record in cursor: 
            print(record)
        
    def user_interests(self):
        print("#####################################")
        print("Enter 1 for inserting a new document")
        print("Enter 2 for updating existing document")
        print("Enter 3 for deleting document")
        Choice=int(input("Please enter your choice:"))
        return Choice
    
    def execution(self,Choice):        
        if Choice==1:
            Obj.current_docs()
            n=int(input("how many columns you want in your collection:"))
            a={}
            i=1
            while i<=n:
                key=input("Enter column %s name:" %i)
                value=input("Enter its value:")
                a[key]=value
                i+=1
            records = Obj.collection.insert_one(a)
            Obj.current_docs()
        
        elif Choice==2:
            Obj.current_docs()
            updtkey=int(input("Please enter the id of the employee who needs updation:"))
            updcol=str(input("Please enter the update column:"))
            newval=input("Please enter new value:")
            result = self.collection.update_many({"_id":updtkey},{"$set":{updcol:newval}})
            Obj.current_docs()   


        elif Choice==3:
            Obj.current_docs()
            delkey=int(input("Please enter the id of the employee who needs to be deleted:"))
            result=self.collection.delete_one({"_id":delkey})
            Obj.current_docs()
        else:
            print("Please verify your choice. Its incorrect!")    

Obj=Pymongo_()
Obj.connect()
Obj.current_docs()
Choice=Obj.user_interests()
Obj.execution(Choice)

    