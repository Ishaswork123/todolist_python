# a simple to do list usin Cli and used a monodb local database to store task , update ,delee task 


import pymongo
from datetime import datetime




mongo_1 =pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb= mongo_1['fyp_1']
collect_todo = mydb['to_Do']

# Functions 

    
print(""" Welcome to  Organizer_Hub
      1. Press 1 to Add new task 
      2. Press 2 to List all task 
      3. Press 3 to list task status wise 
      4. Press 4 Mark a task as in progress or done
      5. Delete a task by name 
      6. Update the task 
      """)

press_key = input('Enter a key to start\n')

def addTask():
    print("""Enter name and description one by one """)
    name_1= input('Assign a unique name to user task\n')
    des_1 =input('Add task details\n')
    
    insert_Dict= {'name' : name_1 , 'description': des_1 , 'status': 'todo' , 
                  "CreatedAt" : datetime.now(), 'UpdatedAt' : 'none'}
    
    x = collect_todo.insert_one(insert_Dict)
    listAll()
   
def markTask(name_task):
    status_update= input(""" Marks a task status 
                         1. Press 1 for todo
                         2. Press 2 for in_progress
                         3. Press 3 for done
                         """)
    status_1=''
    if(status_update=='1'):
        status_1= 'todo' 
    elif(status_update == '2'):
        status_1= 'in_progress'
    elif(status_update == '3'):
        status_1 = 'done'
    else:
        print('user enter a wrong key')
    old_query={'name' : name_task}
    new_query= {'$set': { 'name' : name_task, 'status': status_1}}
    x= collect_todo.update_one(old_query,new_query)
    listAll()

def listAll():
    x= collect_todo.find()
    for i in x:
        print(i,'\n')





if (press_key == '1' ):
    addTask()
elif(press_key == '2'):
    listAll()
  
elif(press_key == '3'):
    print("""
          here show all the task by status as todo, in_progress , done 
          1. Press 1 for to show all to-do task
          2. Press 2 for the in_progress
          3. Press 3 for the done 
          """)
    press_key1=input("Enter a key\n")
    if(press_key1 == '1'):
        
        x=collect_todo.find({'status' : 'todo'})
        for i in x:
            print(i)

    elif(press_key1 == '2'):
        x=collect_todo.find({'status' : 'in_progress'})
        for i in x:
            print(i)
    
    elif(press_key1 == '3'):
        x=collect_todo.find({'status' : 'done'})
        for i in x:
            print(i)
    else:
        print('user enter a wrong key')
        
elif(press_key == '4'):
    x=collect_todo.find()
    for i in x:
        print(i)
    name_task= input('enter a name of task which can be marked')
    markTask(name_task)
elif(press_key == '5'):
     x=collect_todo.find()
     for i in x:
        print(i)
     name_1= input("name the task which you want to delete")
     x=collect_todo.delete_one({'name': name_1})
     print('delete successfully')
     listAll()
elif(press_key == '6'):
    
     x=collect_todo.find()
     for i in x:
        print(i)
     name_old=input('enter a name of task you want to update')

     des=input('enter updated descriptiom ')
     oldquery={'name' : name_old }
     newquery= {'$set': {'description': des , 'UpdatedAt': datetime.now()}}
     x=collect_todo.update_one(oldquery,newquery)
     print('updated Successfully')
     listAll()
    
else:
    print("user enter a wrong key")
    # start()


