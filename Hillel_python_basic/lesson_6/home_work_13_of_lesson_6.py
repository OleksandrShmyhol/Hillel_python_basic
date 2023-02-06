import string
# PS. я був в екстазі коли додумався до такого рішення однією стрічкою))))
inp = list(input())
print(string.ascii_letters[string.ascii_letters.index(inp[0]):string.ascii_letters.index(inp[-1]) + 1])

