# Files can be opened in different modes in Python, as follows

# b 'stands' for binary

# w  / wb  -> Write Mode, Any existing data will be deleted with new one 
# r  / rb  -> Read Mode, Starts reading from the begining
# a  / ab  -> Append Mode, Add data to existing file, Pointer is placed at the EOF
# w+ / w+b -> Write & Read, Existing data will be deleted
# r+ / r+b -> Write & Read, Existing data is preserved, Pointer is placed at the start 
# a+ / a+b -> Append & Read, Pointer is placed at the end, If file does not exists new file will be created
#

# File operations Demo

# File create & write
file = open("test.txt","w")
user_input = input("Enter text:")
file.write(user_input+"\n")
file.close()

#File read

file = open("test.txt","r")
file_data = file.read()

print(file_data)
