# Task 1: Phone Number Validator
- [ ] Complete the function in the file `src/validate_phone_num.py` so that it checks if the string provided `phone_num_input` respects the correct format:
* Starts with a '+' symbol.
* Then Country code (range = 1-999).
* Then space.
* Then comes the area code inside parenthesis () (area code should be in range 1-999).
* Then 3 digits after a space.
* Then again 4 digits after a space.
* Example: `+358 (468) 342 0010`.
* The function returns `True` if the pattern is respected. Otherwise, it returns `False`.

To test your code, run the command:
```
python tests/check_1_validate_phone_num.py
```


# Task 2: Get Username
- [ ] Complete the function in the file `src/get_username_from_email.py` so that it extracts
It takes the username from the `email` input i.e. the part before @. The function returns the username. If it doesn't find an email, it returns `None`.

To test your code, run the command:
```
python tests/check_2_get_username.py
```
