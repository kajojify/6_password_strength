6_password_strength
===================

The script is a password complexity estimator. 

It takes arbitrary string as input and estimates this string from a password complexity point of view. 

This estimation is based on several criteria: password presence in the black list, password length, inclusion of special characters etc. 

How to run
---------- 

Clone this repository. Then go to the repository directory.

Run the script:
```
python3 password_strength.py 
```

Usage
-----

```
~$ python3 password_strength.py
Input the password for estimation --- Utka4%3i
Password complexity --- 6/10

~$ python3 password_strength.py
Input the password for estimation --- Password1
Password complexity --- 1/10
```
