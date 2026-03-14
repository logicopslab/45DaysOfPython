# Write text to a file

file = open("data.txt", "w")

text = input("Enter some text: ")

file.write(text)

file.close()

print("Data written to file.")
