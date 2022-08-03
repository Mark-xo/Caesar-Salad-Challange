import random

a=random.randint(1,308)
print (a)
with open('salad.txt', 'r',encoding='utf-8') as f:
    line=f.readlines()[a]
    f.close()
    w=line.split()[0]
    print (w)
    line=line.replace(w,'',1)
    print (line)
    # encrypt the line in caesar cipher
    key = 3
    cipher = ''
    for char in line:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + key - 97) % 26 + 97)
    print (cipher)
    ans=input('Enter the answer: ')
    if ans==w:
        print ('Correct!')
    else:
        print('Wrong!')

