import re  #importing re library

def main():
    print("Hello, world!")

    # Read a regular expression from the user
    regex_pattern = input("Enter a regular expression: ")


    text = "This is a sample text containing some numbers like 12345 and 67890."

    # Search for matches using the regular expression
    matches = re.findall(regex_pattern, text)

    # Print the matched results
    if matches:
        print("Matches found:")
        for match in matches:
            print(match)
    else:
        print("No matches found.")

if __name__ == "__main__":
    main()
