'''
eval() is a built-in fun that evaluates(executes) a
str as a python expression and ret thr result.
-> it can auto-decide the type

expression:- is any valid combination of values, var,
operators, and fun, that produces a single value when
evaluated or calculated.

syntax:-
        result=eval("exp within a string")

Note: eval() executes arbitary code. if you're
      evaluating user input, it can be a huge security risk
'''

res1=eval("2+5")
print(res1)

a=100
b=25
res2=eval("a-b+50")
print(res2)

l=[10,20,30]
res3=eval("len(l)+24")
print(res3)

res4=eval("[]")
print(res4)
print(type(res4))
res5=eval("False")#Automatically performs typecasting and useful for accepting
                  #boolean value from user and evaluating expression.
print(res5)
print(type(res5))

is_citizen=eval(input("Are You Indian Citizen?"))
print(is_citizen)
print(type(is_citizen))



