
# Python program to check validation of password 
# Module of regular expression is used with search() 
import re 

valid = []   #Store the valid password(s)

#takes in a list of password(s) as a parameter
def password_validate(passwords):

    #flag is true if the conditions are met 
    #Otherwise, flag is set to false
    flag = True 
    
    i = 0 

    #Looping through the list to verify each password
    while i <  len(passwords):  

        #Length must be more than 6 chars but less than 12 chars
        if (len(passwords[i])<6 or len(passwords[i]) > 12): 
            flag = False
        
        #Password must have a lowercase letter
        elif not re.search("[a-z]", passwords[i]): 
            flag = False
        
        #Password must have an uppercase letter
        elif not re.search("[A-Z]", passwords[i]): 
            flag = False
        
        #Password must have a number
        elif not re.search("[0-9]", passwords[i]): 
            flag = False

        #Password must have one of the special characters [#@$]
        elif not re.search("[#@$]", passwords[i]): 
            flag = False

        #If a password meets all the above conditions,
        #It's appended to the list 'valid'
        else: 

            valid.append(passwords[i])

        #increment 'i' and go to the next item in the passwords list (if any)   
        i = i + 1
    if len(valid) > 0:
        print(", ".join(valid))   
        flag = True
        return flag
    
    else:
        flag = False
        return flag

password = input("Enter Password: \n")
passwords = password.split(',')
passwords = list(passwords)
password_validate(passwords)