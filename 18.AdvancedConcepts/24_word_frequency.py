# word_frequency.py

def clean_text(text):
    # Remove punctuation and make lowercase
    for char in ".,!?;:":
        text = text.replace(char, "")
    return text.lower()


def count_words(text):
    words = text.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def display_results(freq_dict):
    print("\nWord Frequency:")

    for word, count in freq_dict.items():
        print(f"{word}: {count}")


def main():
    text = input("Enter a paragraph:\n")

    cleaned = clean_text(text)
    freq = count_words(cleaned)

    display_results(freq)


main()
