# a practice of mongodb crud operations 


import pymongo
from datetime import datetime


mongodbclient= pymongo.MongoClient('mongodb://127.0.0.1:27017/')
# mydb=mongodbclient['fyp-1']

dblist= mongodbclient.list_database_names();
if "fyp_1" in dblist:
    print('db-exist')
else:
    print('not exist')
print(mongodbclient.list_database_names())
mydb= mongodbclient['fyp_1']
mycol= mydb['p1']

dict_2={"_id": 16 , "name" : "alveena" , "timestamp" : True}
dict_3={"_id": 20 , "name" : "ahmer" , "CreatedAt" : datetime.utcnow(),"UpdatedAt": 'null'}

# z=mycol.insert_one(dict_3)

# first occurnance 
z=mycol.find_one()
print(z)


##find all occurnce 
#
# for x in mycol.find():
#   print(x)

t=mycol.find_one({"name": 'alveena'})
print(t)
# for x in mycol.find({} , {"name" : 0}):
#   print(x)
  
  
# sort method to ascending and descending order


query= {"address":"One way 98" }
a= mycol.delete_one(query)
# x=list(mycol.find().sort("name"))
# for i in x:
#   print(i)
  
#x= mycol.deletemany({}) delete all 

# x = mycol.delete_many(myquery)  delte specific object 


# to delete a collection we used method drop 

#mycol.drop()

# update values 

query_old ={"name" : 'alveena'}
query= {"$set" :{"name" : 'hammad '}}
mycol.update_one(query_old,query)
x=list(mycol.find().sort("name"))
for i in x:
  print(i)
# define how many documents we should return 
x= mycol.find().limit(3)
for i in x:
  print(i)
  
print("enter a name and descriptionm")
# name_1= input("enter a name\n")
# des= input("enter a description")

# mydict_4= {'_id':34 , 'name' : name_1 , 'description' : des  }

# g= mycol.insert_one(mydict_4)   

x= mycol.find()
for i in x:
  print(i)
  