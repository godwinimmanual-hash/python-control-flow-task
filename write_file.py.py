# write_file.py

with open("quotes.txt", "a") as file:
    print("Enter your three favorite quotes:")

    for i in range(1, 4):
        quote = input(f"Quote {i}: ")
        file.write(quote + "\n")

print("Quotes have been saved successfully!")