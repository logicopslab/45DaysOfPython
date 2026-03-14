# Count lines and words in a file

file = open("data.txt", "r")

lines = file.readlines()

line_count = len(lines)
word_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)

file.close()

print("Total lines:", line_count)
print("Total words:", word_count)
