while True:
    notes = []
    password = input("Enter password: ")
    if not any(i.isdigit() for i in password):
        notes.append("The password must contain at least one number")
    if not any(i.isupper() for i in password):
        notes.append("The password must contain at least one uppercase letter")
    if len(password) < 5:
        notes.append("The password must be at least 5 characters long")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)
