import string


def is_palindrome(res):
    word = ''
    for el in res.replace(' ', '').lower():
        if el not in string.punctuation:
            word += el
    return True * word == ''.join(reversed(word.replace(' ', ''))) or False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
print("ОК")
