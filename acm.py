def p1():
    print('hello world')
    print(10+5)
#we can add more than 1 datatype in list 
#reversestring print(text[::1])
#index right from 0 left from-1
def p2():
    l=['cat','krishna','meow',49]
    print(l[1],'\n' ,l[2],'\n',l[-1],'\n',l[-4])
    l1=[1,2,3,5]
    l1.sort(reverse=True)
    print(l1)
def p3():
    r=[]
    r.append(3)
    r.append(5)
    r.append(6)
    r.append(7)
    r.append(8)
    r.append(9)
    r.remove(9)
    r.sort()
    index6=r.index(6)
    r.reverse()
    print(r)
    print(index6)

def p4():
    t=[]
    t.append(10)
    t.append(20)
    t.append(30)
    t.append(20)
    t.append(20)
    t.append(40)
    t.append(50)
    print(t)
    t.insert(2,25)
    print(t)
    c20=t.count(20)
    print(c20)
    t.remove(40)
    print(t)

def p5():
    text='HelloWorld'
    print(text[::3])
def p6():
    t=input('whats your name')
    print('hi ' +t+" welcome")
def p7():
    age=int(input('your age'))
    print(age+10)
def p8():
    print(10==10)
    print(10%5)
    print(3+4*2)
    print((3+4)*2, 10/2-3,(10/2)-3,2**3+1,2+3*(4-1))
def p9():
    weather=input('hows the weather')
    if(weather=='rainy'):
        print('take the umbrella')
    elif(weather=='sunny'):
        print('take glasses')
    else:
        print('just do whatever you like buddy')
            
    '''else:
     print('dont take umbrella') '''
def p10():
    w=int(input('enter number'))
    if(w%2==0):
        print('its even')
    else:
        print('its odd')
def p11():
    #match case
    day=input()
    match day:
        case 'monday':
            print('new week')
        case 'tuesday'|'wednesday'| 'thursday'|"friday":
            print('boring')
        
        case 'saturday':
            print('weekend')
        case 'sunday':
            print('weekend')
def p12():
    month=input()
    match month:
        case 'jan'|'mar'|'may'|'july'|'aug'|'oct'|'dec':
            print(31)
        case 'feb':
            print(28)
        case 'apr'|'june'|"sep"|'nov':
            print(30)

def p13():
    a=int(input('enter 1st number'))
    b=int(input('enter second number'))
    f=input('function')  
    if(f=='add'):
        print(a+b)  
    elif(f=='mul'):
        print(a*b)
    elif(f=='sub'):
        print(a-b)
    elif(f=='div'):
        print(a/b)
    elif(f=='rem'):
        print(a%b)
def p14():
    b=int(input('grade'))
      
    if(0<b<30):
        print('f')  
    elif(30<b<45):
        print(b)
    elif(45<b<50):
        print('b+')
    elif(50<b<75):
        print('a')
    elif(70<b<80):
        print('a+') 
    elif(80<b<100):
        print('o')   
    else:
        print('not valid') 

def p15():
    for i in range(1,11):
        print(i)
def p16():
    for i in range(1,21):
        if(i%2==00):
            print(i)
def p17():
    i=1
    while i<21:
        print(i)
        i+=1
def p18():
    i=1
    while i<=10:
        print(i)
        i+=1            
           
def p19():
    i=2
    while i<=20:
        print(i)
        i+=2
def p20():
    for i in range (1,21):
        if i==12:
            break
        print(i)
def p21():
    for i in range(1,11):
        if i==4:
         continue
        print(i)
def p22():
    n=int(input(''))
    total=1
    print('factorial of 0',1)
    i=1
    while i <=n:
        total*=i
        print('factorial of',i,total)
        i+=1
def p23():
    for i in range(1,11):
        
        print('2 x',i,'=',i*2)

        
def p24():
    num=int(input(''))
    count=0
    while(num!=0):
        count+=1
        num//=10
    print(count) 

def p25():
    def p1():
      x=[]
      pass

    p1()


p25()
