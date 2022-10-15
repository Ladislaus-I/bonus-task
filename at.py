def help_message():
    print("placeholder")
    return()

def delete_string(i = 0):
    if (not i):
        print("Enter the number of string to delete or 0 to exit to menu")
        i = int(input())
    if (i < 0):
        print("Error. The number of the string is too low.")
        return()
    if i:
        #print(str(i))
        file_text.pop(i - 1)
    return()

def add_string(i = 0, string = ""):
    if (not i):
        print("Enter the number of string to insert or 0 to exit to menu")
        i = int(input())
    if (i < 0):
        print("Error. The number of the string is too low.")
        return()
    if i:
        if (not string):
            print("Enter the string")
            string = input()
        file_text.insert(i - 1, string + "\n")
    return()

def append(string):
    if (not string):
        print("Enter the string")
        string = input()
    file_text.append(string + "\n")

def show_from_to(a, b):
    if (not a):
        print("Enter the number of the first string or 0 to exit")
        a = int(input())
    if (not a):
        return()
    if (a < 1):
        print("Error. The number of the first string is too low.")
        return()
    if (not b):
        print("Enter the number of the last string")
        b = int(input())
    if (b < a):
        print("Error. The number of the last string shoudn't be lower than the number of the first one.")
        return()
    if (b > len(file_text)):
        print("Error. The number of a second string is too big.")
        return()
    while (a <= b):
        print(file_text[a - 1])
        a += 1
    return()

def remove_from_to(a, b):
    #print(str(a) + " " + str(b))
    if (not a):
        print("Enter the number of the first string")
        a = int(input())
    if (b > len(file_text)):
        print("Error. The number of the first string is too low.")
        return()
    if (not b):
        print("Enter the number of the last string")
        b = int(input())
    if (b < a):
        print("Error. The number of the last string shoudn't be lower than the number of the first one.")
        return()
    if (b > len(file_text)):
        print("Error. The number of a second string is too big.")
        return()
    i = a
    while (i <= b):
        #print(str(a) + " " + str(b))
        delete_string(a)
        i += 1
    return()

def assign(i, string):
    if (not i):
        print("Enter the number of string to insert or 0 to exit to menu")
        i = int(input())
    if (i < 0):
        print("Error. The number of the string is too low.")
        return()
    if i:
        if (not string):
            print("Enter the string")
            string = input()
        file_text.pop(i - 1)
        file_text.insert(i - 1, string + "\n")
    return()    

def save():
    file = open(file_name, "w")
    file.writelines(file_text)
    file.close()

def saveas(new_file_name):
    if (not new_file_name):
        print("Enter the file name")
        new_file_name = input()
    file = open(new_file_name, "w")
    file.writelines(file_text)
    file.close()

def menu():
    print("Enter your command: \n (Type help to dispay all commands)")
    cmd = input().rsplit(" ")
    cmd.append(0)
    cmd.append(0)
    
    if (cmd[0] == "help"):
        help_message()
    elif (cmd[0] == "append"):
        append(cmd[1])
    elif (cmd[0] == "show"):
        show_from_to(int(cmd[1]), int(cmd[2]))
    elif (cmd[0] == "remove"):
        remove_from_to(int(cmd[1]), int(cmd[2]))
    elif (cmd[0] == "delstr"):
        delete_string(int(cmd[1]))
    elif (cmd[0] == "addstr"):
        add_string(int(cmd[1]), cmd[2])
    elif (cmd[0] == "assign"):
        assign(int(cmd[1]), cmd[2])
    elif (cmd[0] == "save"):
        save()
    elif (cmd[0] == "saveas"):
        saveas(cmd[1])    
    elif (cmd[0] == "exit"):
        return()
    else:
        print("Incorrect command")
    
    menu()
    return()



file_name = input("Enter file name: ")
#file = open(file_name, "w")
#file.close()
try:
    file = open(file_name, "r")
    file_text = file.readlines()
    file.close()
except FileNotFoundError:
    file = open(file_name, "w+")
    file_text = file.readlines()
    file.close()

menu()

i = 0
while(i < len(file_text)):
    print(file_text[i])
    i += 1
