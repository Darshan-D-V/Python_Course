'''
JSON STANDS FOR JAVASCRIPT OBJECT NOTATION
It's basically a format to store and share structured data-
especially b/w client and server in web apps,API's,etc.

'''
company=[{'name':'Amy',
          'salary':94000,
          'dept':'HR'
         },
         {'name':'Ben',
          'salary':75000,
          'dept':'Research'
         },
         {'name':'Chad',
          'salary':80000,
          'dept':'Sales'
         }
         ]

for i in company:
    print(i['name'])

for i in company:
    if i['salary']>78000:
        print(i['name'])

