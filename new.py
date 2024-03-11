words="Where are you? Meet me near the clock tower"
w=words.split(" ")
vowel="aeiou"
l=[]
for i in w:
    if i in vowel:
        i="%"
        l.append(i)
    else:
        l.append(i)
print(l)