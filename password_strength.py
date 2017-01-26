import re
from getpass import getpass


def get_password_strength(password):
    strength = 1
    blacklist = (
        'y7u8i9o0', 'warcraft', 'transfer', 'testtest', 'terminal', 'dotadota',
        'telegram', 'sysadmin', 'startrek', 'somebody', 'software', 'simpsons',
        'security', 'qwertyui', 'qwerasdf', 'qawsedrf', 'q1w2e3r4', 'password',
        'passport', 'operator', 'napoleon', 'joystick', 'internet', 'iloveyou',
        'geometry', 'football', 'december', 'computer', 'azsxdcfv', 'asdfqwer',
        'alphabet', 'academic', 'academia', 'abcdefgh', 'abcd1234', 'a1b2c3d4',
        '7y8u9i0o', '7890yuio', '1234qwer', '0p9o8i7u', '0987poiu', '!@#$%^&*',
        'sherlock', 'telephone', 'telegraph', 'superuser', 'professor',
        'password1', 'microsoft', 'hollywood', 'qwerty123', 'abcabcabc',
        'qwertyuiop', '1q2w3e4r5t', 'qwerty1234', 'qwerasdfzxcv',
        'q1w2e3r4t5y6', '1q2w3e4r5t6y'
    )
    password_len = len(password)
    if password_len >= 6 and password.lower() not in blacklist:
        strength += 1
        special_chars = 0
        digits = 0
        letters = 0
        upper_case = 0
        lower_case = 0
        for symbol in password:
            if symbol.isdigit():
                digits += 1
            elif symbol.isalpha():
                letters += 1
                if symbol.islower():
                    lower_case += 1
                else:
                    upper_case += 1
            else:
                special_chars += 1

        if digits and letters:
            strength += 1
        if upper_case and lower_case:
            strength += 1
        if special_chars:
            strength += 1
        if password_len >= 8:
            strength += 1
        if password_len >= 10:
            if password_len == 10:
                pattern = """
                (0[1-9]|[12][0-9]|3[01])[- /.]
                (0[1-9]|1[012])[- /.](19|20)\d\d
                """
                date_re = re.compile(pattern)
                match = date_re.match(password)
                if match:
                    return 1
            strength += 1
        if password_len >= 12:
            strength += 1
        if password_len >= 14:
            strength += 1
        if password_len >= 16:
            strength += 1
    return strength

if __name__ == '__main__':
    password = getpass("Input the password for estimation --- ")
    password_strength = get_password_strength(password)
    print("Password complexity --- %d/10" % password_strength)
    
