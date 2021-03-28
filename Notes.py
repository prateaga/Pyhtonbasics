l = ['ABC19910010B', 'XYx2000100ba']
Counter = 0
for i in l:
    if len(i) == 12 and i[0:3].isalpha() and i[0:3].isupper() and 1990 <= int(i[3:7]) <= 2010 and i[7:11].isdigit()  and 10 <= int(i[7:11]) <= 1000:
        Counter = Counter + 1

print(Counter)
Counter = 0
s = " Learning Python is a fun"
for j in s:
    if j in 'aeiou':
        Counter+=1

print(s.casefold())


print(Counter)

# WAP to find if it has duplicate elements
m = [2,3,4,5,69,9,3,4]
v = set(m)
if len(v) == len(m):
    print (True)
else:
    print(False)

r1 = "king"
r2 = "sAGTREWDER"
print(r1 == r2)
























