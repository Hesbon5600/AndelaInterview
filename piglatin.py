def pig_latin(string):
    num_of_qmarks = 0
    current_num = 0
    sum_is_10 = False

    # Loop through the string to check every element
    for ch in string:
        # If character is a digit
        if ch.isdigit():
            # if sum of the digit and the current_num is 10 and 3 question marks have been found,
            # set sum_is_10 to true
            if int(ch) + current_num == 10 and num_of_qmarks == 3:
                sum_is_10 = True 
            # If a digit is found and the sum of digit and current_num is not equal to 10,
            # Even if 3 question marks have been found
            # initialize the current_num as the found digit
            current_num = int(ch)
            # Reset the num_of_qmarks to zero
            num_of_qmarks = 0

        # If character is a question mark
        elif ch == '?':
            # Increment the number of question marks by one
            num_of_qmarks += 1
    # Return True or False based on the value of "sum_is_10"
    return sum_is_10
    
   