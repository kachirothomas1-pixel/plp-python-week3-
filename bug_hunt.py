count = 1
total = 0

# BUG: Added a missing colon (:) at the end of the while loop statement to fix the syntax error.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Fixed the loop condition from '< 5' to '<= 5' so it includes the number 5, making the sum 15 instead of 10.
# BUG: Converted the integer 'total' to a string using str(total) to fix the TypeError when concatenating strings and numbers.
print("Sum of 1 to 5 is: " + str(total))
