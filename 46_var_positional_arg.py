#variable length arguments
#3.1]variable positional arguments:-
#note1:packing

def dreambig(*args):#packing into tuple
    print(args)

dreambig("cricketer","doctor","police","pilot","avenger","athlete","officer","astronut","writer")

#note2:unpacking
def remove(a,b,c):
    print(a,b,c,sep='\n')

l=[11,22,33]#iterable
remove(*l)#when we use *iterable unpacking into positional arguments
          #no of values unpacked=no of parameters

#using both packing&unpacking
def remove(*args):#packing
    print(args)

l=[11,22,33]#iterable
remove(*l)#unpacking
