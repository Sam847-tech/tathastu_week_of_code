def duplicate(string):
    duplicateString = ""
    for x in string:
        if x not in duplicateString:
            duplicateString += x
    return duplicateString

string = input("Enter string: ")
print("String after removing duplicates:", duplicate(string))
