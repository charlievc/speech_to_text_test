vowels = ('a','e','i','o','u')
var='a'
alphabets=[]
alphabets=[(chr(ord(var)+i)) for i in range(26)]
consonants = tuple([x for x in alphabets if x not in vowels])

def write_vc(text):
    if text.endswith(vowels) is True:
        return text+'-v'
    elif (text.endswith(consonants) is True):
        return text+'-c'
    else:
        return '' 