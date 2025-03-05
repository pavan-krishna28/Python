# The number of lines in the triangle
size = 10

# Loop through each line
for i in range(size):
    # Calculate the number of spaces needed to center the line
    spaces = (size - i - 1)  
    
    # Print the spaces
    print(' ' * spaces, end='')  
    
    # Print the stars
    print('*' * (2 * i))
    
    # Calculate the number of spaces needed to center the line
    spaces = (size - i - 1)
