f = open('GLL Comp.txt','r')
f2 = open('car-mpg (3).csv','r')
print(f.readline())

f1 = open('GLL Comp.txt','w')
f1.write("Something is better \n than nothing")

for data in f2:
    f1.write(data)

# Write a program to count the number of times a character appears in the File
import string

# Open the file in read mode
text = open("car-mpg (3).csv", "r")

# Create an empty dictionary
d = dict()

# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()

    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))

    # Split the line into words
    words = line.split(" ")

    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
for key in list(d.keys()):
    print(key, ":", d[key])
