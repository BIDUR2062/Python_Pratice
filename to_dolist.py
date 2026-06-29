to_do=[]

while True:
    print('Menu:\n1.Enter the task to the list\n2.Display the task to be done\n3.Delete the task from the list\n4.Exit')
    user_input=input("Enter what you want to perform:(1,2,3 or 4): ")
    if user_input=='1':
        task=input("Enter the task that you want to do: ")
        to_do.append(task)
    elif user_input=='2':
        if not to_do:
            print("No task to show")
        else:
            print("Task to be done: ")
            for i,task in enumerate(to_do,start=1):
                print(f'{i}.{task}')
    elif user_input=='3':
        if not to_do:
            print('No task to delete!')
        else:
            print('\tTask: ')
            for i,task in enumerate(to_do,start=1):
                print(f'{i}.{task}')
            user_choice=int(input("Which task do you want to delete: "))
            if 1<=user_choice<=len(to_do):
                removed=to_do.pop(user_choice-1)
                print(f'Tasked removed: {removed}')
            else:
                print("Invalid Choice!")    
    elif user_input=='4':
        print("Goodbye!")
        break
    else:
        print("Invalid!")
