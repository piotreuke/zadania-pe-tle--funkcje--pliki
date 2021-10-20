#Pętle

#Zadanie 1
'''
ile = int(input('Podaj koniec przedziału: '))
value = 0


while licznik < ile:
    print(value)
    value+=1


for number in range (ile):
    print(value)
    value+=1
'''

#Zadanie 2
'''

for number in range (100, 49, -1):
    print(number)
'''

#Zadanie 3
'''
value = 0

for number in range (21):
    print(value)
    value+=5
'''

#Zadanie 4
'''
ile = int(input('Podaj wartość potęgi: '))
number = 2

for numbers in range(ile):
    print(number)
    number*=2
'''

#Zadanie 5
'''
print('Przedział liczb to 50-100')
ile = int(input('Podaj liczbę k: '))

for numbers in range (50, 101):
    if numbers % ile == 0:
        print(numbers)
'''

#Zadanie 7
'''
#a
print('*'*10)

#d
m=4
n=1

for i in range(1,6):
    print( m* " " +"*"*n)
    m-=1
    n+=2

#c
width = 3

for j in range(3):
    print(width*'*')

#b
height = 1

for triangle in range(5):
    print(height*'*')
    height+=1
'''

#Zadanie 8
'''
sum = 0
for num in range(11):
    sum = sum+num
    wynik=sum/10
print(wynik)
'''

#Pętle rozszerzenie

#Zadanie 1
'''
star = '*'

m=5
n=1

for i in range(4):
    print(star*n)
    n+=1
while m>0:
    print(star*m)
    m-=1
'''

#Zadanie 2
'''
str = input('Podaj słowo')
l = len(str)
p = l-1
index = 0
while index < p:
    if str[index] == str[p]:
        index = index + 1
        p = p-1
        print('String jest palindromem')
        break
    else:
        print('Nie jest')
'''

#Zadanie 3
'''
family = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']
family1 = ['Adam', 'Stanisław', 'Joanna', 'Kornelia', 'Kacper']
import itertools


x = itertools.product(family, family1)

print(list(x))
'''

#Zadanie 4
'''
for i in range(1001, 10001):
    print(i)
'''

#Zadanie 5
'''
zamowienia={'Klient_1335' : {'nazwa_potrawy' : 'rosół', 'ocena' : 5,
'rachunek' : 20.0}, 'Klient_222' : {'nazwa_deseru' : 'lody waniliowe',
'rachunek' : 5.0}}

print(zamowienia['Klient_1335'])
print(zamowienia['Klient_222'])
'''

#Zadanie 6
'''
string = str(input('Podaj liczbę '))
print(string)
hash_table = {}

for char in string:
    if char in hash_table:
        hash_table[char]+=1
    else:
        hash_table[char]=1

print(hash_table)
'''

#Zadanie 7
'''
n = int(input('Podaj wartość n: '))

ciąg = [0,1,1,2,3,5,8,13,21,34,55,89]
print(ciąg[:n])
'''

#Funkcje

#Zadanie 1
'''
nums = [4, 6, 8, 24, 12, 2]

def numbers(nums):
    max_value = None
    for num in nums:
        if max_value is None or num > max_value:
            max_value=num
    print('Największa wartość to', max_value)

numbers(nums)
'''
#Zadanie 2

#Zadanie 3
'''
num=int(input('Wpisz liczbę '))
def fizz_buzz(num):
    if num%3==0 and num%5==0:
        print('FizzBuzz')
    elif num%5==0:
        print('Buzz')
    elif num%3==0:
        print('Fizz')
    else: print(num)

fizz_buzz(num)
'''

#Zadanie 4
'''
def obliczenie(*args):
    iloczyn=0
    for val in args:
        iloczyn = val*val
    return iloczyn
'''

#Zadanie 5
'''
def numbers(**kwargs):
    numbers_odd=[1,3,5,7,9]
    numbers_even=[0,2,4,6,8]
    value=0
    for key in range(len(numbers_odd)):
        print(f'{numbers_odd[value]} : {numbers_even[value]}')
        value+=1

numbers(number=[])
'''

#Zadanie 6
'''
nums = [1, 3, 8, 21, 34, 56, 78, 87, 89, 94]

def numbers(nums):
    for num in nums:
        if num >= 10:
            print(num)

numbers(nums)
'''

#Pliki

#Zadanie 3
'''
plik = open('przyklad.txt')

linia = plik.readlines()
print(linia[1])
plik.close()
'''

#Zadanie 6

'''
Tak samo jak wyżej tylko zmienić index
'''

#Zadanie 7
'''
plik = open('przyklad.txt', 'r+')

linia = plik.readline()
value = linia.split()
#print(value)
index = 0
for i in range(len(value)):
    if value[index-1] == value[index]:
        #print(value[index])
        how = (value[index].replace(value[index], ''))
        plik.write(how)
        
        
    else: print(value[index])
    index+=1


plik.close()
'''
