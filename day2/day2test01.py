alpha=0
space=0
digit=0
other=0
input=input()
for char in input:
    if char.isalpha():
        alpha+=1
    elif char.isspace():
        space+=1
    elif char.isdigit():
        digit+=1
    else:
        other+=1
print("bumber of alpha:",alpha)
print("bumber of space:",space)
print("bumber of digit:",digit)
print("bumber of other:",other)