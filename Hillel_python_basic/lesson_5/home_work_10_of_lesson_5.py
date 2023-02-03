import string
import keyword

my_string = input()
result = True
if my_string[0].isdigit() or any(el.isupper() for el in my_string) or ' ' in my_string or keyword.iskeyword(my_string):
    result = False
elif any(el in string.punctuation for el in my_string):
    if '_' in my_string:
        result = True
    else:
        result = False

print(result)
