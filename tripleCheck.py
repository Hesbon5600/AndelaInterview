# finding the single element in a list where 
# every element appears three times except for one

# Accept as a parameter a list where every element appears three times except for one
def tripple_check(lst):

    for i in lst:
        # count the number of occurance of a number
        ls = lst.count(i)
        if ls < 3:
            print(i)

            return i

