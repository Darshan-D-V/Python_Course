#variable keywords arguments:-

#note1:-packing
def display(**kwargs):#FD when we use **kwargs packing(dict) can seen
    
    print(kwargs)#{'soc': 95, 'kan': 93, 'eng': 85, 'maths': 100, 'bio': 100, 'phy': 96}

display(soc=95,kan=93,eng=85,maths=100,bio=100,phy=96)

def display(kan,soc,bio,**kwargs):#FD when we use **kwargs packing(dict) can seen
    
    print(kwargs)#{'eng': 85, 'maths': 100, 'phy': 96}

display(soc=95,kan=93,eng=85,maths=100,bio=100,phy=96)


#note2:-unpacking
def extract(maths,phy,eng):
    print(eng,maths,phy,sep='\n')

d={'eng': 85, 'maths': 100, 'phy': 96}#when used in FC,IT UNPACKS into kwargs ,
                                      #but keyword name shud match the parameters
extract(**d)

#both unpacking and packing
def extract(**kwargs):#FD when we use **kwargs packing(dict) can seen
    print(kwargs)

d={'eng': 85, 'maths': 100, 'phy': 96}#when used in FC,IT UNPACKS into kwargs ,
                                      #but keyword name shud match the parameters
extract(**d)
