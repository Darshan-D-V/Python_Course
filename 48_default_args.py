#default arguments
def display(age=0,height=0.0,ismarried=False):
    print(age,height,ismarried,sep='\n')

display()
display(43)
display(34,5.8)
display(88,8.8,True)

#order of passing all the args:-
def about(name,*friends,love='Mother',age,hobby,**bio):
    print(name)
    print(friends)
    print(love)
    print(age,hobby,sep='\n')
    print(bio)
about("Darshan","Chetan","Shrikanth",love="Father",age=21,hobby="Reading",hobby1="playing cricket",
      hobby2="Gym",hobby3="watching movies")
