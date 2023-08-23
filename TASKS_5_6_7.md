# User Accounts
The goal is to create a program that allows user to register their accounts by:
* Providing their email addresses.
* Setting up a password.
* Writing a bio. The program takes care of formatting it.

The program must also show a list of all the registered accounts when asked.

We will create the functionalities of the program.

**Notes:** 
* The main function of the program is provided in the file `src/main.py`. You can run the script at any time to check the behavior of your program: `python src/main.py`
* In this project, it is ok to show the password in the console for learning purpose. That's not the case in a professional environment.

## Task 5: Email Address Validator
When the user inputs an email address, the program must check if the string provided respect the correct format:
* Case-insensitive.
* Starts with a letter.
* At least **two characters** *before the @*.
* The accepted characters *before the @* are **letters**, **digits**, **underscore '_'**, **dash '-'**, and **dot '.'**.
* *After the @*, the characters accepted are **letters**, **digits**, **underscore '_'**, **dash '-'**, and **dot '.'**.
* After the @, there can't be 2 dots in a row '..'.
* The email address end with a **dot '.' followed by 2 to 5 letters**. Example: ".me", ".com", ".euro" ".rugby".

- [ ] In the file ``src/validate_email.py``, Complete the function ``validate_email(email_input)`` so that the above conditions are respected.

To test your code, run the command:
```
python tests/check_5.py
```

## Task 6: Password Validator
When the user inputs a password, the program must check if the string provided respect the correct format:
* At least 8 characters
* At most 30 characters
* At least one Uppercase letter
* At least one lowercase letter
* At least one digit
* At least one special character from this set: `*!-_.`.
* Only accept the characters mentioned above

- [ ] In the file `src/validate_password.py`, Complete the function `validate_password(pwd_input)` so that the above conditions are respected.

To test your code, run the command:
```
python tests/check_6.py
```
*Extra challenge: Can you improve your code so that the password validator shows a message describing the issue with the password provided by the user?*

## Task 7: Format Bio
*This part is relatively challenging. If you don't manage to do it, don't hesitate to look at the solution*

We want to format the bio provided by the user. After formatting, the bio must respect these conditions:
* If it starts with a letter, it must be an uppercase.
* If there are consecutive multiple spaces, they must be reduced to one space.
* Each sentence must start with a capital letter, but the case of the rest of the sentence mustn't be modified. Therefore, you can't use the method `capitalize()`.
* After the dot '.'  marking the end of a sentence, there must be a space before the following sentence.
* If there are multiple dots '.' in a row, they mustn't be changed.
* Remove the trailing spaces in the beginning and the end of the file.

- [ ] In the file `src/format_bio.py`, Complete the function `format_bio(bio_input)` so that the above conditions are respected.

To test your code, run the command:
```
python tests/check_7.py
```
