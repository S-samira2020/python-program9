Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> age_1 = 22
>>> age_2 = 18
>>> age_1 >= 21 and age_2 >= 21
False
>>> age_1 <= 21 and age_2 >= 21
False
>>> age_1 <= 21 and age_2 <= 21
False
>>> age_1 >= 21 and age_2 <= 21
True
>>> age_1 >= 21 or age_2 >= 21
True
>>> age_1 >= or age_2 <= 21
SyntaxError: invalid syntax
>>> age_1 >= 21 or age_2 <= 21
True
>>> age_1 <= 21 or age_2 >= 21
False
>>> 