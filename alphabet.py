a = input("enter a word : ")

alpha = False
for char in a:
    if('a' <= char <= 'z')or ('A' <= char <= 'Z'):
        alpha = True
        break

if alpha:
    print("The word has atlease one letter")
else:
    print("It dose not have an letter")