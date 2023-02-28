import string


def first_word(text):
    print(''.find(text[:text.index('e')]))


assert first_word("Hello world") == "Hello", 'Test1'
# assert first_word("greetings, friends") == "greetings", 'Test2'
# assert first_word("don't touch it") == "don't", 'Test3'
# assert first_word("... and so on ...") == "and", 'Test4'
# assert first_word("hi") == "hi", 'Test5'
# assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

# result = ''.join(el for el in text if el == "'" or el not in string.punctuation).split(' ')
# for el in result:
#     if el.isalpha() or "'" in el:
#         print(el)
#         return el

# result = ''.join(el for el in text if el == "'" or el not in string.punctuation).split(' ')
# print(result[0] if "'" in result[0] or result[0].isalpha() else result[1])
# return result[0] if "'" in result[0] or result[0].isalpha() else result[1]
