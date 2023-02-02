import string

my_string = input()
result = 1
if my_string[0].isdigit() or any(el.isupper() for el in my_string) or ' ' in my_string:
    result *= 0
elif any(el in string.punctuation for el in my_string):
    if '_' in my_string:
        result *= 1
    else:
        result *= 0

print(bool(result))
