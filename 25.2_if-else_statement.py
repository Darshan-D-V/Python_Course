#accept any marks from the user,check if it is greater
#than or equal to 35 ,print "congratulations",otherwise "sorry about that"
marks=int(input("Enter your Marks:"))
if marks>=35:
    print("congratulations")
else:
    print("sorry about that")

#accept name from the user,check if it's length greater
#than 8 ,print "valid username",otherwise "invalid username"
name=input("Enter your name:")
if len(name)>8:
    print("valid username")
#print("good")#invalid syntax
#if will immeadiately followed by else,no other exectuble code will be introduced.
else:
    print("invalid username")

#accept a sentence from the user,if the sentence has more than 4 words print "valid sentence"
#else print "invalid sentence"
sentence=input("Enter your own sentence:")
wordslist=sentence.split()
print(wordslist)
if len(wordslist)>4:
    print("valid sentence")
else:
    print("invalid sentence")

##sentence=input("Enter your own sentence:")
##if len(sentences.split())>4:
##    print("valid sentence")
##else:
##    print("invalid sentence")
    
#when we have two possible choices, we go for if-else.
