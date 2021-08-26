#Functions with Outputs

def format_name(fName, lName):
    """Take first and last name as input and return the title case version of the name """
    if fName == "" or lName == "":
        return
    name = (fName + " " +lName).title()
    return name


firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
fullName = format_name(fName=firstName, lName=lastName)

print(fullName)