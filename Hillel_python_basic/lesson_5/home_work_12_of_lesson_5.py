import string

# Python Community -> #PythonCommunity
#
# i like python community! -> #ILikePythonCommunity
#
# Should, I. subscribe? Yes! -> #ShouldISubscribeYes

user_input = list(input())
for el in range(len(user_input)):
    if user_input[el] in string.punctuation:
        user_input[el] = ''

result = ''.join(user_input)
print("#" + result[:140].title().replace(' ',
      '').replace(string.punctuation, ''))
