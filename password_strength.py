import re

from getpass import getpass

BLACKLIST = (
        'y7u8i9o0', 'warcraft', 'testtest', 'terminal', 'dotadota', 'telegram',
        'sysadmin', 'startrek', 'software', 'security', 'qwertyui', 'qwerasdf',
        'qawsedrf', 'q1w2e3r4', 'password', 'passport', 'operator', 'joystick',
        'internet', 'iloveyou', 'football', 'computer', 'azsxdcfv', 'asdfqwer',
        'alphabet', 'academic', 'academia', 'abcdefgh', 'abcd1234', 'a1b2c3d4',
        '7y8u9i0o', '7890yuio', '1234qwer', '0p9o8i7u', '0987poiu', '!@#$%^&*',
        'sherlock', 'telegraph', 'superuser', 'professor', 'password1',
        'qwerty123', 'abcabcabc', 'qwertyuiop', '1q2w3e4r5t', 'qwerty1234',
        'qwerasdfzxcv', 'q1w2e3r4t5y6', '1q2w3e4r5t6y'
    )


def in_blacklist(password):
    return password.lower() in BLACKLIST


def get_password_strength(password):
    strength = 1
    min_len = 6
    password_len = len(password)
    if password_len >= min_len and not in_blacklist(password):
        digits = re.search("[0-9]", password)
        letters = re.search("[A-Za-z]", password)
        lower_case = re.search("[a-z]", password)
        upper_case = re.search("[A-Z]", password)
        special_chars = re.search("[\W_]", password)
        if digits and letters:
            strength += 1
        if upper_case and lower_case:
            strength += 1
        if special_chars:
            strength += 1
        strength_increase = password_len - min_len
        strength += strength_increase
    return min(10, strength)


if __name__ == '__main__':
    password = getpass("Input the password for estimation --- ")
    password_strength = get_password_strength(password)
    print("Password complexity --- %d/10" % password_strength)
