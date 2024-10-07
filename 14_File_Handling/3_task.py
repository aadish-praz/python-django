# Write a program that copies the content of one file (source.txt) to another file (destination.txt).
source=open(r"task\source.txt",'r')
lines=source.readlines()
source.close()

destination=open(r"task\destination.txt","w")
destination.writelines(lines)
destination.close()


# Create a program that reads a file and prints the following statistics:

# Number of characters
# Number of words
# Number of lines

with open(r"task\source.txt",'r') as file:
    print("Number of characters:",len(file.read()))
    file.seek(0)
    print("Number of words:",len(file.read().split()))
    file.seek(0)
    print("Number of lines:",len(file.read().strip().split("\n")))


# Write a program that reads a file and counts how many times a specific character (e.g., 'a') appears in the file.

with open(r"task\source.txt",'r') as file:
    print("Number of 'a':",file.read().count('a'))


# Write a program that reads a file and counts how many times a specific word (e.g., "Python") occurs in the file. Print the result.

with open(r"task\source.txt",'r') as file:
    print("Number of 'Python':",file.read().count('Python'))


# Write a program that reads a file and replaces all occurrences of a specific word (e.g., "Python") with another word (e.g., "Java") and writes the modified content to a new file.

with open(r"task\source.txt",'r+') as file:
    text=file.read()
    text=text.replace("Python","Java")

with open(r"task\newtext.txt",'w') as newfile:
    newfile.write(text)


# Write a program that reads a file and prints the line numbers where a specific word (e.g., "Python") appears.

with open(r"task\source.txt",'r+') as file:
    text=file.readlines()

    for i in range(len(text)):
        if "Python" in text[i]:
            print("'Python' found in line no.:",i+1)
