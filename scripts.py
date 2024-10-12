# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

# Python If-Else
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if  (n%2)==0 and 2<=n<=5:
     print('Not Weird')
if (n%2)==0 and 6<=n<=20:
    print('Weird')
if (n%2)==0 and n>20:
    print('Not Weird')
if n%2!=0:
    print('Weird')

# What's Your Name?
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(f'Hello {first_name} {last_name}! You just delved into python.')


# sWAP cASE
def swap_case(s):
    return s.swapcase()

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
coordinate=[[i,j,k] for i in range(0,x+1,1)
                    for j in range(0,y+1,1)
                    for k in range(0,z+1,1)
                    if i+j+k!=n
                    ]
print(coordinate)

# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    massimo=max(arr)
    arr=[(i) for i in arr if i!=massimo]
    print(max(arr))
    

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        dati = input().split()  
        name = dati[0]
        voti = dati[1:]  
        scores = list(map(float, voti))
        student_marks[name] = scores
    query_name = input()
    media = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{media:.2f}")

# Lists
if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        comando = input().split()
        if comando[0] == "insert":
            intero=int(comando[1])
            posizione=int(comando[2])
            arr.insert(intero, posizione)
        elif comando[0] == "print":
            print(arr)
        elif comando[0] == "remove":
            arr.remove(int(comando[1]))
        elif comando[0] == "append":
            intero=int(comando[1])
            arr.append(intero)
        elif comando[0] == "sort":
            arr.sort()
        elif comando[0] == "pop":
            arr.pop()
        elif comando[0] == "reverse":
            arr.reverse()
 

# Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash(t))

# Mutations
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]

# Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count = count + 1
    return count

# String Validators
if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))

# Text Alignment
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
spessore = int(sys.stdin.readline().strip())
H = 'H'
sys.stdout.write((H).center(spessore * 2) + '\n')
sys.stdout.write((H*3).center(spessore * 2) + '\n')
sys.stdout.write((H*5).center(spessore * 2) + '\n')
sys.stdout.write((H*7).center(spessore * 2) + '\n')
sys.stdout.write((H*9).center(spessore * 2) + '\n')
for i in range(spessore + 1):
    sys.stdout.write((H * spessore).center(spessore * 2) + (H * spessore).center(spessore * 6) + '\n')
i = 0
while i <= 3:
    sys.stdout.write((H*25).center(spessore * 6) + '\n')
    i = i + 1
for i in range(spessore + 1):
    sys.stdout.write((H * spessore).center(spessore * 2) + (H * spessore).center(spessore * 6) + '\n')
sys.stdout.write(((H*9).center(spessore * 2)).rjust(spessore * 6) + '\n')  
sys.stdout.write(((H*7).center(spessore * 2)).rjust(spessore * 6) + '\n')
sys.stdout.write(((H*5).center(spessore * 2)).rjust(spessore * 6) + '\n')
sys.stdout.write(((H*3).center(spessore * 2)).rjust(spessore * 6) + '\n')
sys.stdout.write(((H).center(spessore * 2)).rjust(spessore * 6) + '\n')

# Text Wrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

# String Formatting
def print_formatted(number):
    # your code goes here
    lunghezza = len(bin(number)) - 2
    for i in range(1, number + 1):
        decim = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        print(decim.rjust(lunghezza), octal.rjust(lunghezza), hexa.rjust(lunghezza), binary.rjust(lunghezza))

# Capitalize!

# Complete the solve function below.
def solve(s):
    propcase = []
    sottostringhe = s.split(' ')
    
    for i in sottostringhe:
        if len(i) > 0:
            maiuscola = i[0].upper() + i[1:]
        else:
            maiuscola = i
        
        propcase.append(maiuscola)
    
    return ' '.join(propcase)

# String Split and Join

def split_and_join(line):
    # write your code here
    sottostringhe=line.split(' ')
    stringa = '-'.join(sottostringhe)
    return stringa
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# Introduction to Sets
def average(array):
    # your code goes here
    elementi=set(array)
    result=sum(elementi)/len(elementi)
    return result

# Symmetric Difference
M = int(input())  
a = set(map(int, input().split()))
N = int(input())  
b = set(map(int, input().split()))  
diff_simmetrica = sorted(a^b)
for num in diff_simmetrica:
    print(num)

# No Idea!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split()) 
arr = list(map(int,input().split() ))  
A = set(map(int, input().split()))  
B = set(map(int, input().split()))  
felicita = 0

for num in arr:
    if num in A:
        felicita =felicita+ 1
    elif num in B:
        felicita =felicita- 1
print(felicita)

# Set .discard(), .remove() & .pop()
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
numero_comandi = int(input())
for i in range(numero_comandi):
    comandi = input().split()
    if comandi[0] == "remove":
        numero = int(comandi[1])
        if numero in s:
            s.remove(numero)
    elif comandi[0] == "discard":
        s.discard(int(comandi[1]))
    elif comandi[0] == "pop":
        s.pop()
print(sum(s))

# Set .union() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inglesi = set(map(int, input().split()))
b = int(input())
francesi = set(map(int, input().split()))
unione = inglesi.union(francesi)
print(len(unione))

# Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inglesi = set(map(int, input().split()))
b = int(input())
francesi = set(map(int, input().split()))
intersezione = inglesi.intersection(francesi)
print(len(intersezione))

# Set .difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inglesi = set(map(int, input().split()))
b= int(input())
francesi = set(map(int, input().split()))
differenza = inglesi.difference(francesi)
print(len(differenza))

# Set .symmetric_difference() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
inglesi = set(map(int, input().split()))
b = int(input())
francesi = set(map(int, input().split()))
diff_simmetrica = inglesi.symmetric_difference(francesi)
print(len(diff_simmetrica))

# Calendar Module
# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
month, day, year = map(int, input().split())
giorno = calendar.weekday(year, month, day)
settimana = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
print(settimana[giorno])

# Time Delta
#!/bin/python3
import math
import os
import random
import re
import sys
from datetime import datetime  
# Complete the time_delta function below.
def time_delta(t1, t2):
    formato = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, formato)
    t2 = datetime.strptime(t2, formato)
    diff=t1-t2
    diff = abs(int((diff).total_seconds()))
    return str(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

# Exceptions
# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    try:
        a, b = input().split()
        divisione_intera = int(a) // int(b)
        print(divisione_intera)
    except ZeroDivisionError as q:
        print("Error Code:", q)
    except ValueError as p:
        print("Error Code:", p)

# Birthday Cake Candles
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
def birthdayCakeCandles(candles):
    massimo=max(candles)
    print(massimo)
    print(candles)
    count=0
    for i in candles:
        if i==massimo:
            count=count+1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    candles_count = int(input().strip())
    candles = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(candles)
    fptr.write(str(result) + '\n')
    fptr.close()

# Number Line Jumps
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#
def kangaroo(x1, v1, x2, v2):
    for y in range(10000):
        if x1 + v1 * y == x2 + v2 * y:
            return "YES"
    return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

# Viral Advertising
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def viralAdvertising(n):
    x = 5  
    mipiace = math.floor(x / 2) 
    condivisioni = mipiace * 3  
    totale_mipiace = mipiace  
    for i in range(n - 1):  
        mipiace = math.floor(condivisioni / 2)  
        totale_mipiace =totale_mipiace+ mipiace  
        condivisioni = mipiace * 3
    return totale_mipiace
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    result = viralAdvertising(n)
    fptr.write(str(result) + '\n')
    fptr.close()

# Recursive Digit Sum
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def superDigit(n, k):
    # Write your code here
    def app(p):
        if len(p) == 1:
            return int(p)
        else:
            somma=0
            for i in str(p):
                somma=somma+int(i)
            return app(str(somma))
    somma=0
    for i in str(n):
        somma=somma+int(i)
    somma=somma*k
    return app(str(somma))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()

# Insertion Sort - Part 1
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort1(n, arr):
    # Write your code here
    elemento=arr[n-1]
    i=n-1
    while(i>0) and elemento<arr[i-1]:
        arr[i]=arr[i-1]
        print(' '.join(str(i) for i in arr))
        i=i-1
    arr[i]=elemento
    print(' '.join(str(i) for i in arr))
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

# Insertion Sort - Part 2
#!/bin/python3
import math
import os
import random
import re
import sys
#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def insertionSort2(n, arr):
    # Write your code here
    for i in range(1,n):
        app=arr[i]
        j=i-1
        while j>= 0 and arr[j]>app:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1] = app
        print(' '.join(str(k) for k in arr))
             
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)

# collections.Counter()
from collections import Counter
numero_scarpe=int(input())
lista_taglie_disponibili=list(map(int,input().split()))
contatore_taglie_disponibili=Counter(lista_taglie_disponibili)
numero_clienti=int(input())
guadagno=0
for i in range(numero_clienti):
  taglia,prezzo=map(int,input().split())
  if contatore_taglie_disponibili[taglia]>0:
    guadagno=guadagno+prezzo
    contatore_taglie_disponibili[taglia]=contatore_taglie_disponibili[taglia]-1
print(guadagno)

# DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
gruppoa = []
gruppob = []
for i in range(n):
    gruppoa.append(str(input().strip()))
for i in range(m):
    gruppob.append(str(input().strip()))
for i in range(m):
    posizioni = []
    for j in range(n):
        if gruppob[i] == gruppoa[j]:
            posizioni.append(str(j + 1))
    if len(posizioni) == 0:
        print(-1)
    else:
        print(" ".join(posizioni))

# Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N=int(input())
name_columns = list(map(str, input().strip().split()))
Student = namedtuple('Student',name_columns)
totale_mark=0
for i in range(N):
    dati_studente=input().split()
    student=Student(*dati_studente)
    totale_mark=totale_mark+int(student.MARKS)
media=totale_mark/N
print(media)

# Collections.OrderedDict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
acquisti = {}
for i in range(N):
    dati = input().split()
    prodotto = ' '.join(dati[:-1])
    prezzo = int(dati[-1])
    if prodotto in acquisti:
        acquisti[prodotto] += prezzo
    else:
        acquisti[prodotto] = prezzo
for prodotto, prezzo in acquisti.items():
    print(prodotto, prezzo)

# Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
elenco=[]
for i in range(n):
    word=str(input())
    elenco.append(word)
parole_distinte=set(elenco)
print(len(parole_distinte))
frequenza=[]
frequenze = Counter(elenco)
frequenza = ' '.join(map(str, frequenze.values()))
print(frequenza)    
       


# Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
n = int(input())
d = deque()
for i in range(n):
    operazione = input().split()
    if operazione[0] == "append":
        d.append(int(operazione[1]))  
    elif operazione[0] == "appendleft":
        d.appendleft(int(operazione[1]))
    elif operazione[0] == "pop":
        d.pop()
    elif operazione[0] == "popleft":
        d.popleft()
print(" ".join(map(str, d)))

# Company Logo
#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    s = input()
    frequenza = Counter(s)
    frequenza_ordinata = sorted(frequenza.items(), key=lambda x: (-x[1], x[0]))
    for i in range(min(3, len(frequenza_ordinata))):
        print(frequenza_ordinata[i][0], frequenza_ordinata[i][1])
        

# Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
elenco=[]
for i in range(N):
    paesi=str(input())
    elenco.append(paesi)
elenco=set(elenco)
print(len(elenco))

# Nested Lists
if __name__ == '__main__':
    N = int(input())
    students = []
    voti = []
    for _ in range(N):
        name = input()
        grade = float(input())
        voti.append(grade)
        students.append([name, grade])
    voti_unici = sorted(set(voti))
    penultimo = voti_unici[1]
    nome_penultimo = [name for name, grade in students if grade == penultimo]
    nome_penultimo.sort()
    for name in nome_penultimo:
        print(name)
  

# Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, x = map(int, input().split()) 
matrice=[]
for i in range(x):
  voti=list(map(float,input().split()))
  matrice.append(voti)
for i in range(n):
    somma_voti = 0
    for j in range(x):
        somma_voti =somma_voti+ matrice[j][i]
    media = somma_voti / x
    print(round(media, 1))

# Athlete Sort
#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    def riga(i):
        return i[k]
        
    k = int(input().strip())
    arr.sort(key=riga)
    for i in arr:
        print(" ".join(map(str, i)))

# ginortS
# Enter your code here. Read input from STDIN. Print output to STDOUT
s=list(input())
minuscole=[]
maiuscole=[]
dispari=[]
pari=[]
for i in s:
    if i.islower():
        minuscole.append(i)
    elif i.isupper():
        maiuscole.append(i)
    elif i.isdigit() and int(i) % 2 != 0:
        dispari.append(i)
    elif i.isdigit() and int(i) % 2 == 0:
        pari.append(i)
minuscole.sort()
maiuscole.sort()
dispari.sort()
pari.sort()
print(''.join(minuscole+maiuscole+dispari+pari))
        

# Map and Lambda Function
cube = lambda x: x**3# complete the lambda function 
def fibonacci(n):
    # return a list of fibonacci numbers
    if n>1:
        i=2
        n1=0
        n2=1
        lista=[n1,n2]
        while(i<n):
            app=n2
            n2=n1+n2
            n1=app
            lista.append(n2)
            i=i+1
        return lista
    elif n==0:
        return []
    elif n==1:
        return [0]

# XML 1 - Find the Score

def get_attr_number(node):
    # your code goes here
    attributes = len(node.attrib)
    for i in node:
        attributes =attributes+get_attr_number(i)
    return attributes

# XML2 - Find the Maximum Depth

maxdepth=0
def depth(elem, level):
    global maxdepth
    if level+1 > maxdepth:
        maxdepth = level+1
    for i in elem:
        depth(i, level + 1)
    # your code goes here

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        # complete the function
        new_numero = []
        for i in l:
            numero = '+91 ' + i[-10:-5] + ' ' + i[-5:]
            new_numero.append(numero)
        return f(new_numero)
    return fun

# Decorators 2 - Name Directory

def eta(x):
    return int(x[2])
def person_lister(f):
    def inner(people):
        # complete the function
        people_ord=sorted(people,key=eta)
        app=[]
        for i in people_ord:
            app.append(f(i))
        return app 
    return inner

# Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b);
print(a-b);
print(a*b);

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i**2)

# Write a function
def is_leap(year):
    leap =False
    
    # Write your logic here
    if year%4==0:
        if year%100==0:
            if year%400==0:
                leap=True
            else:
                leap=False
        else:
            leap=True
    else:
        leap=False
    return leap

# Print Function
if __name__ == '__main__':
    n = int(input())
    stringa=''
    for i in range(1,n+1,1):
        stringa=stringa+str(i)
    print(stringa)

# Eye and Identity
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
N,M=map(int,input().split())
print(numpy.eye(N,M))

# Detect Floating Point Number
# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())
for i in range(T):
    N=input()
    if N.count('.')==1:
        try:
            float(N)
            print(True)
        except ValueError:
            print(False)
    else:
        print(False)

# Re.split()
regex_pattern = r"[.,]"	# Do not delete 'r'.

# Group(), Groups() & Groupdict()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
check = False
for i in range(len(s)):
    p = re.match(r'([a-zA-Z0-9])\1', s[i:])
    if p:
        print(p.group(1))
        check = True
        break
if check==False:
    print(-1)

# Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
k=input()
check=False
for i in range(len(s)):
    m=re.search(k,s[i:])
    if m!=None and m.start()==0:
        print((m.start()+i,m.end()+i-1))
        check=True
if check==False:
    print((-1,-1))

# Regex Substitution
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
p=[]
for i in range(N):
    p.append(input())
text='\n'.join(p)
text = re.sub(r'(?<= )&&(?= )', 'and', text)
text = re.sub(r'(?<= )\|\|(?= )', 'or', text)
print(text)

# Re.findall() & Re.finditer()
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
p=re.findall(r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])',s)
if p:
    for i in p:
        print(i)
else:
    print(-1)

# Validating Roman Numerals
regex_pattern = r"^(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

# Validating phone numbers
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N=int(input())
for i in range(N):
    stringa=input()
    if re.match(r"^[789]\d{9}$", stringa):
        print("YES")
    else:
        print("NO")

# Validating and Parsing Email Addresses
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
N = int(input())
for i in range(N):
    name,email=email.utils.parseaddr(input())
    if re.match(r'^[a-zA-Z][\w.-]*@[a-zA-Z]+\.[a-zA-Z]{2,3}$',email):
        print(email.utils.formataddr((name,email)))

# Arrays

def arrays(arr):
    # complete this function
    # use numpy.array
    p=numpy.array(arr,float)
    return p[::-1]

# Shape and Reshape
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
p = list(map(int, input().split()))
print(numpy.reshape(p,(3,3)))

# Transpose and Flatten
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N,M=map(int, input().split())
p=[]
for i in range(N):
    p.append(list(map(int,input().split())))
my_array=numpy.array(p)
print(numpy.transpose(my_array))
print(my_array.flatten())

# Concatenate
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N,M,P=map(int,input().split())
colonna=[]
righe=[]
for i in range(N):
    colonna.append(list(map(int,input().split())))
array_1=numpy.array(colonna)
for j in range(M):
    righe.append(list(map(int,input().split())))
array_2=numpy.array(righe)
print(numpy.concatenate((array_1,array_2),axis=0))

# Zeros and Ones
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
p = list(map(int, input().split()))
print(numpy.zeros(p, dtype=int))
print(numpy.ones(p, dtype=int))

# Array Mathematics
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N, M = map(int, input().split())
A=[]
B=[]
for i in range(N):
    A.append(list(map(int,input().split())))
A=numpy.array(A)
for i in range(N):
    B.append(list(map(int,input().split())))
B=numpy.array(B)
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))

# Floor, Ceil and Rint
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
p = numpy.array(list(map(float, input().split())))
print(numpy.floor(p))
print(numpy.ceil(p))
print(numpy.rint(p))

# Sum and Prod
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N,M=map(int,input().split())
a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
A=numpy.array(a)
print(numpy.prod(numpy.sum(A,axis=0)))

# Min and Max
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
A=numpy.array(a)
print(numpy.max(numpy.min(A,axis=1))) 

# Mean, Var, and Std
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m=map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
A=numpy.array(a)
print(numpy.mean(A,axis=1))
print(numpy.var(A,axis=0))
print(round(numpy.std(A),11))

# Dot and Cross
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N=int(input())
a=[]
b=[]
for i in range(N):
    a.append(list(map(int,input().split())))
A=numpy.array(a)
for i in range(N):
    b.append(list(map(int,input().split())))
B=numpy.array(b)
print(numpy.dot(A,B))

# Inner and Outer
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A=numpy.array(A)
B=numpy.array(B)
print(numpy.inner(A,B))
print(numpy.outer(A,B))

# Polynomials
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
P=list(map(float,input().split()))
x=float(input())
print(numpy.polyval(P, x))

# Linear Algebra
# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
N=int(input())
a=[]
for i in range(N):
    a.append(list(map(float,input().split())))
A=numpy.array(a)
print(round(numpy.linalg.det(A),2))

