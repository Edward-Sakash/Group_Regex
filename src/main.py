from format_bio import format_bio
from validate_email import validate_email
from validate_password import validate_password


def add_user():
    email = input("User's email: ")
    if not validate_email(email):
        print("Error: The email is not valid")
        return False
    psswd = input("Password: ")
    if not validate_password(psswd):
        print("Error: The password doesn't respect the required pattern")
        return False
    bio = input("Add bio:\n")
    bio = format_bio(bio)
    return email, psswd, bio


if __name__ == "__main__":
    records = []
    while True:
        print("\n\n-----------------")
        print(">>> Choose action")
        print("1 : Add user")
        print("2 : List users")
        print("0: Quit")
        ch = input("Your choice? ")

        if ch == "1":
            record = add_user()
            if record:
                records.append(record)

        elif ch == "2":
            print("List of users:")
            for record in records:
                print("Email:", record[0])
                print("Password:", record[1])
                print("Bio:\n" + record[2])
                print("---------------------")

        elif ch == "0":
            print("Good bye")
            break

        else:
            print("Wrong input")
