
for i in range(2,20):
    print(i)
    continue # all no will print from 2-19

for i in range(2,20):
    continue
    print(i) # no num will print

# when printing num from 43-63, skip any div by 3
#other num should be printed
for i in range(43,64):
    if i%3==0:
        continue # skips the if condition num
    print(i)
print("--------------")
# 2 and 5
for i in range(43,64):
    if i%2==0 and i%5==0:
        continue # skips the if condition num
    print(i)
print("--------------")
# print only the right marks skip the wrong marks
marks=[45,-74,62,74,52,-48,92,-35,27,93]
for i in marks:
    if i<0:
        continue
    print(i)
print("--------------")


names=["nandan","basu","raj","om","raghu","shravani","daniel"]
# when iterating to each names if num of char is <5
# skip that, if the num of char is>5 print them,
#if the num of char is =5 stop the loop come out
for i in names:
    if len(i)<5:
        continue
    elif len(i)>5:
        print(i)
    else:
        break













