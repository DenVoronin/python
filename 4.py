dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
dict1={}
d={}
for key in dict:
    if dict[key]>=3:
        d={key:dict[key]}
        dict1.update(d)
d.clear        
print(dict1)
