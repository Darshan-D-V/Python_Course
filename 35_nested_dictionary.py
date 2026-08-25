company={'emp1':{'name':'Amy',
                 'salary':94000,
                 'dept':'HR'
                 },
         'emp2':{'name':'Ben',
                 'salary':75000,
                 'dept':'Research'
                 },
         'emp3':{'name':'Chad',
                 'salary':80000,
                 'dept':'Sales'
                 }
         }
print(company)
for i in company:
    print(i)

print("==========================================================")
for i in company:
    print(company[i])
    #print(company.get(i))

print("==========================================================")
    
for i  in company.values():
    print(i)

print("==========================================================")

for i in company.values():
    print(i['name'])#or i.get('name')
#or
for i in company:
    print(company[i]['name'])
#or
for i in company:
    print(company.get(i).get('name'))#or .get(i)['name']

print("==========================================================")

for i in company.values():
    print(i['salary'])

print("==========================================================")

for i in company.values():
    if i['salary']>78000:
        print(i['name'])

print("==========================================================")

for i in company.values():
    if i['dept'].lower()=='hr':
        print(i['name'])

print("==========================================================")

for i in company.values():
    for j in i.values():
        print(j)
#or
for i in company.values():
    print(i['name'],i['salary'],i['dept'],sep='\n')    

