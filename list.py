n = int(input())  # Read number of commands
lst = []  # Initialize an empty list
    
for _ in range(n):
    command = input().split()  # Read command and split into parts
        
    if command[0] == "insert":
        lst.insert(int(command[1]), int(command[2]))
    elif command[0] == "print":
            print(lst)
    elif command[0] == "remove":
        lst.remove(int(command[1]))
    elif command[0] == "append":
        lst.append(int(command[1]))
    elif command[0] == "sort":
        lst.sort()
    elif command[0] == "pop":
        lst.pop()
    elif command[0] == "reverse":
        lst.reverse()