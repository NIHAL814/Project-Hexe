tasks=[]

while True:
    print("\nTO-DO List Manager")
    print("1.Add Task")
    print("2.Remove task")
    print("3.View task")
    print("4.Exit")
    
    c=input("Enter your choice:")

    if c=='1':
       task=input("Enter your task:")
       tasks.append(task)
       print("Task added")
    elif c=='2':
       task=input("Enter the task to remove:")
       if task in tasks:
            tasks.remove(task)
            print("Task removed")
       else:
            print("Task not found")
    elif c=='3':
        if len(tasks)==0:
           print("No task in the list")
        else:
             print("your tasks:")
             for t in tasks:
                 print( "-",t)
    elif c=='4':
        print("Exiting program")
        break
else:
    print("Invalid choice")