# Append data to an existing file

file = open("data.txt", "a")

new_text = input("Enter text to append: ")

file.write("\n" + new_text)

file.close()

print("Data appended successfully.")
