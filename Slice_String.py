def slice_and_rearrange(input_string, index):
    sliced_part = input_string[index:]
    rearranged_string = sliced_part + input_string[:index]
    return rearranged_string

# Taking input from the user
input_string = input("Enter a string: ")
index = int(input("Enter the index where the string is sliced: "))

# Calling the function and displaying the result
result = slice_and_rearrange(input_string, index)
print("Result:", result)
