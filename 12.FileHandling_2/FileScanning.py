# Search for a word in a file

file = open("data.txt", "r")

search_word = input("Enter word to search: ")

found = False

for line in file:
    if search_word in line:
        found = True
        print("Found in line:", line.strip())

file.close()

if not found:
    print("Word not found in file.")
