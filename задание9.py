spisok = ['student1, student2, student3']
spisok = ''.join(spisok)
print(spisok+",")
spisok= spisok.split(', ')
print(spisok)
s = []
for i in spisok:
    s.append(i+"_good")
print(s)
