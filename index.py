# ### Problem 1:
# Create a function with the variable below. After you create the variable do the instructions below that.
# ```
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# ```
# a) Print the 3rd element of the numberList.
# 
#     b) Print the size of the array
# 
# c) Delete the second element.
# 
#     d) Print the 3rd element.

# def main():
#     problem1()
# def problem1():
#     myArray = ["Kenn", "Kevin", "Erin", "Meka"]
#     # print(myArray[3])
#     # myArray.remove(myArray[2])
#     # print(myArray[3])


#     ### Problem 2:
#     ##### We will keep having this problem until EVERYONE gets it right without help
#     Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.


#
# user = input("")
# while user != "q":
#    user = input("Try Again- ")


# ### Problem 4:
# Create an array of 5 numbers. <strong>Using a loop</strong>, print the elements in the array reverse order. <strong>Do not use a function</strong>

# myArray = 


# ### Problem 5:
# Create a function that will have a hard coded array then ask the user for a number. Use the userInput to state how many numbers in an array are higher, lower, or equal to it.

def main():
    myArray = [1, 2, 3, 4, 4, 2, 4, 2, 2, 1, 4, 2]
    userInput = int(input("Pick a number 1-4: "))
    for eachNum in myArray:
        one = 0
        two = 0
        three = 0
        four = 0

        if userInput == 1:
            one = one + 1
        elif userInput == 2:
            two = two + 1
        elif userInput == 3:
            three = three + 1
        elif userInput == 4:
            four = four + 1
    print(f"1= {one}")
    print(f"2= {two}")
    print(f"3= {three}")
    print(f"4= {four}")

main()
