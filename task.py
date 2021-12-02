import sys        #to get command line arguments
import linecache as lc  #to read particular line by specifying line number
import re         #to match regular expression
from datetime import date  #for date 
import os.path    #to check whether file exists or not

usage  = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
"""

def add(priority, task):
    file = open('task.txt','a')
    file.write(priority + " " +task + "\n")
    file.close()
    print('Added task: "{}" with priority {}'.format(task,priority))

def ls():
    file = open("task.txt", "r")

    priority = [] # making list containing tuple like (priority, index of line) to display according to priority of task.  
    c= 1
    for each in file:
        priority.append( (int(each[0]), c) )
        c += 1
    priority = sorted(priority)
    
    
    for i in range(len(priority)):
        task = lc.getline('task.txt', priority[i][1])
        print("{}. {} [{}]".format(i+1, task[2:-1], task[0])) # index. "task" [priority]
    
    file.close()

def delete(index):    
   print("Deleted item with index {}".format(index))

def done(index):    
   print("Marked item as done.")
            
def report():
    
   file = open('task.txt', 'r')
   c = 0
   for each in file:
       c += 1
   file.close()   
   
   print("Pending: {}".format(c))
   ls()
   
   file = open('completed.txt', 'r')
   c = 0
   for each in file:
       c += 1
   file.close()   

   print("\nCompleted: {}".format(c))
   
   for index in range(c):
       line = lc.getline('completed.txt', (index + 1))
       print(line[:-1]) 

if __name__=="__main__":

    if len(sys.argv) < 2:
        print(usage)
    elif sys.argv[1] =="help":
        print(usage)     
    elif sys.argv[1] == "add":
        add(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "ls":
        ls()
    elif sys.argv[1] == "del":
        delete(sys.argv[2])
    elif sys.argv[1] == "done":
        done(sys.argv[2]) 
    elif sys.argv[1] == "report":
        report()
    else:
        print("Invalid argument provided\n",usage)
