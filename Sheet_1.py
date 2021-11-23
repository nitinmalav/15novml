#Q2.___________________________________________________________

print(5**9)

print(3//2)
print(7//3)
print(7/3)

print(6==6)


a=20;
a+=30;
a%=3;
print(a)


print(True * False)
print(True & False)
print(True and False)

print(((6>3) and (7<4) or (18==3)) and (9>3))



print(True is False)
print(False in 'False')
print(((True == False) or (False > True)) and (False <= True))



#Q3.____________________________________________________________

s1="Nice to have it"
s2="here"
s3=s1+" "+ s2;
print(s3)

#Q4.____________________________________________________________


a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])


#Q5.____________________________________________________________

s1="Nice to have it"
s2="here"
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.insert(0,s1)
a.insert(len(a)+1,s2)
print(a)


#Q6.____________________________________________________________


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
for i in numbers:
    if(i%2==0):
        print(i)
    elif(i==237):
        break



#Q7.____________________________________________________________

    
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))


#Q8.____________________________________________________________

import string
  
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
  
    return True
      
# Driver code
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")


#Q9.____________________________________________________________


n=eval(input("enter number: "))
print(int(n)+int(str(n)+str(n))+int(str(n)+str(n)+str(n)))


#Q10.___________________________________________________________


s=input("Enter a string")
l=s.split("#")
x=l[0].split(' ')
for i in range(len(x)):
    x[i]=int(x[i])
y=l[1].split(' ')
for i in range(len(y)):
    y[i]=int(y[i])
print(x)
print(y)



#Q11.___________________________________________________________

print("Enter the string: ")
s4=input().split(',')
print(s4)
s4.sort()
print(s4)


#Q12.___________________________________________________________

d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
d1=d['Marks']
l=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==l):
        j=i

d2=d['Student']
print(d2[j])



#Q13.___________________________________________________________

s5=input("Enter a string:")
l=0
d=0
for i in s5:
    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("LETTERS ",l)
print("DIGITS ",d)


#Q14.___________________________________________________________

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject: ')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)




#Q16.___________________________________________________________

import math
x,y=0,0
while True:
    step = input('Type UP,DOWN,LEFT,RIGHT and corresponding Step number:')
    if step == '':
        break
    else:
        step = step.split(' ')
        if step[0]=='UP':
            y+=int(step[1])
        elif step[0]=='DOWN':
            y-=int(step[1])
        elif step[0]=='LEFT':
            x-=int(step[1])
        elif step[0]=='RIGHT':
            x+=int(step[1])
b= math.sqrt(x**2+y**2)
c=int(b)
print('Distance:',c)








