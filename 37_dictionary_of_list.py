#Dictionary of Lists
company={'names':['Amy','Ben','Chad'],
         'depts':['HR','Sales','Marketing'],
         'salaries':[94000,78000,84000],
         'ids':[101,113,120]
         }
print(company)
for i in company:
    print(i)

print("==============================================")

for i in company.values():
    print(i)

print("==============================================")

for i in company.values():
    print(i[0])

print("==============================================")

for i in company:
    print(company[i][0])
    print(company[i][1])
    print(company[i][2])
    break
#or

for i in company['names']:
    print(i)
#or
for i in range(0,3):
    print(company['names'][i])

print("==============================================")

#if the sal>85000,print his name.
for i in range(0,3):
    j=company['salaries'][i]
    if j>85000:
        print(company['names'][i])
        
            
    
    
