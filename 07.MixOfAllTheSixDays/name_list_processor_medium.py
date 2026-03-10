def process_names(names):
    processed = []

    for name in names:
        name = name.strip().title()

        if len(name) > 3:
            short = name[:3]      # slicing
        else:
            short = name

        processed.append(short)

    return processed


user_input = input("Enter names separated by comma: ")

names = user_input.split(",")

result = process_names(names)

print("Processed names:", result)