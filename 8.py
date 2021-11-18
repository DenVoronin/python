s="0123456789"

f = open ('123.txt','w')
f.write(s);
f.close
f = open ('123.txt','r')
s1 = f.read()
print(s1)
f.close



f1 = open ('1234.txt','w')
f1.write(s1[::-1])
f1.close
f1 = open ('1234.txt','r')
print(f1.read())
f1.close
