def add(firstName: str | None, lastName: str = None):
    return firstName.capitalize() + " " + lastName


fName= "Bill"
lName= "Gates"

name = add(fName.capitalize(),lName)
print(name)