s1="python programming language"

#Methods of String:-
#1]ref.capitalize():-
#it returns the copy of the string with the only first letter will be capitalized.
print(s1.capitalize())#Python programming language
print(s1)#python programming language

#2]ref.title():-
#it returns a copy of a string where 1st letter of each word is capitalized.
print(s1.title())

#3]ref.upper():-
#it returns a copy of string which is in uppercase form.
print(s1.upper())

#4]ref.lower():-
#it returns a copy of string which is in lowercase form.
print(s1.lower())

#5]ref.isupper():-
#it returns True if string is already in uppercase,otherwise False.
print(s1.isupper())

#6]ref.islower():-
#it returns True if string is already in lowercase,otherwise False.
print(s1.islower())

#7]ref.startswith("substring"):-
#it returns True if the string starts with the given substring, otherwise False
s2="Govinda Gopala"
print(s2.startswith("Go"))

#8]ref.endswith("substring"):-
#it returns True if the string ends with the given substring, otherwise False
print(s2.endswith("pala"))

#9]ref.replace("old_substring","new_substring"):-
#it returns a copy of a string, where oldsubstring is replaced by the newstring.
print(s2.replace("Govi","Muku"))

#10]ref.isalpha():-
#it returns True if the string contains only alphabets(it can be upper or lower).
s3="Godzilla vs Kong"#it returns False,Bcz it contains spaces(it is also a character)
print(s3.isalpha())

#11]ref.isdigit():-
#it returns True if the string contains only digits.
s4="987456241"
print(s4.isdigit())

#12]ref.isalnum():-
#it returns True if string contains only alphabets,only numbers,or both.
s5="KGF2"
print(s5.isalnum())

#13]ref.swapcase():-
#it returns a copy of a string, where uppercase letters are swapped with lowercase
#and viseversa
s6="INVINcible"
print(s6.swapcase())

#14]ref.count("substring"):-
#it returns the number of occurences of the substring.
s7="Kannada"
print(s7.count("a"))

#15]ref.index("substring"):-
#it returns the index number of the first occuring substring.
s8="prestige" 
print(s8.index("e"))

#16]ref.lstrip()
#it returns a copy of a string with leading/lefthandside whitespaces removed.
s9="        Boom"
print(s9.lstrip())

#17]ref.rstrip():-
#it returns a copy of a string with trailing/righthandside whitespaces removed.
s10="OMG                      "
print(s10.rstrip())

#18]ref.strip():-
#it returns a copy of a string with both leading/lefthandside and
#trailing/righthandside whitespaces removed.
s11="                   Super Car                                   "
print(s11.strip())

#19]ref.split():-
#it splits a string based on string as a separator and
#returns list of substrings.
s12="dhee coding lab"
print(s12.split())

s13="7/8/2026"
print(s13.split("/"))

s="7jolly8jolly2026"
print(s.split("jolly"))

#20]"substring".join(list of strings)
#it returns a copy of a string with substring joined
#b/w those strings.
dates=["15","8","2026"]#list of strings
#15/8/2026
print("/".join(dates))

#example:-
string=" Today is Friday Good Afternoon "
l=string.split()
print(len(l))
print(l[2])












