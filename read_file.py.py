# read_file.py

try:
    with open("input.txt", "r") as file:
        content = file.read()

    words = content.split()
    word_count = len(words)

    print(f"Total number of words: {word_count}")

except FileNotFoundError:
    print("Error: 'input.txt' file not found.")

except Exception as e:
    print(f"An error occurred: {e}")