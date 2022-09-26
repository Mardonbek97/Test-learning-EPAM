# This script was written by me for understanding basic code in python

import math
x = int(input("Istalgan sonni kiriting: "))
if x > 0:
    print("X musbat son")
elif x < 0:
        print("X manfiy son")
else:
        print("X = 0")

print(math.pow(3, 2))

x ='ISm';
y = 4;

print(type(x));
print(type(y))

ism = 'Abdulloh';
print("Mening ismim " + ism)

name = "mardonbek";
last_name = "sobirov";

print( f"{name} \n{last_name}".title());


x = 1_325_654_478;
print(x) 

name = 'Mardonbek';
sname = 'Sobirov';
age = 23;

full_inf = str(name) + ' ' + str(sname) +' ' + str(age);
print(full_inf)


x = input("Please input your birth year: ");
print(2022 - int(x));

names = [];
names.append('Mardonbek');
names.append('Shoxruh');
names.append('Abdukarim');
names.append('Abdulvosid');

names.insert(2, 'Mirzakarim');

my_friend = [names.pop(1), names.pop(3) ];


print(my_friend);
print(names);


ismlar = ['Mardonbek', 'Abdurauf', 'Boymirzo', 'Celtic']


ismlar.reverse()
print(ismlar)


numbers = (1, 3, 5, 8, 9, 7)
numbers=list(numbers)
numbers.append(10)
print(numbers)

import math
x = input("Istalgan sonni kiriting!!!: ")
x=int(x)
if x>=0:
    print(math.sqrt(x))
else:
    print("iltmos musbat son kiritng")

login = input("Istalgan loginni kiriting: ")
login = login.capitalize()

if login == 'Mardonbek':
    print("Siz togri loginni kiritdiz")
else:
    print("Siz notogri login kiritidiz")
    
mevalar = ['apple', 'grape', 'pear', 'mandarin']
for meva in mevalar:
    print(meva)

 
phones = {
      'name':'Iphone',
      'OZU':'8GB',
      'made':'2022',
      'RAM':'256GB'
      }

for key, value in phones.items():
    print(f"KEY: {key}")
    print(f"VALUE: {value}\n")

x = input("Istalgan davlat nomini kiritng: ")
country = {
    'USA':'Washington D.C',
    'Uzbekistan':'Tashkent',
    'Kirgizia':'Bishkek',
    'Russia':'Moscow'
    }

for key in country.keys():
    if key == x:
        for value in country.values():
            print(value)
    else: print("Siz notogri davlat tanladiz")
   
        
car1 = {
        'name':'Malibu',
        'made':'2022',
        'probeg':'20100',
        'rangi':'qora'
        }
car2 = {
        'name':'Tahoe',
        'made':'2022',
        'probeg':'200',
        'rangi':'qizil'
        }
cars = [car1, car2]
for key in cars:
    print(f"name: {key['name']}, \nmade: {key['made']},"
          f"\nprobeg: {key['probeg']}")

    
print('Salom dunyo', end=' ');
print('hello world');



orders = []
print("Buyurtmalar ro'yxati")
n=1
while True:
    savol=f"{n} buyurtmangiz nomini kiriting: "
    name = input(savol)
    orders.append(savol)
    javob = input("Yana buyurtma berasizmi(Ha/Yo'q'): ")
    if javob == 'Ha':
        n += 1
        continue
    else:
        break
    

def take_hello(name):
    "Salom beruvhi faunksiya"
    print(f"Salom, {name}")

take_hello("Mardonbek")


def cheque_even(son1, son2):
    """Sonlarni katta kichikligini aniqlovchi funksiya"""
    if son1>son2:
        print(f"birinchi son katta: {son1}")
    elif son1<son2:
        print(f"Ikkinchi son katta: {son2}")
    else:
        print("Ikkala son teng")

cheque_even(12.5, 13.5)


x = range(2, 10)
count=0
def cheque_mod(y):
    for x in range(2, 9):
        if y%x == 0:
            print(f"{y} soni {x} ga bo'linadi")
         
y=int(input("Istalgan sonni kiriting: "))
cheque_mod(24)
        

def user_info(name, sname, birth_date, address):
    user = {
        'name':name,
        'sname':sname,
        'birht_date':birth_date,
        'address':address
        }
    return user

odam = user_info('Mardonbek', 'Sobirov', '03.10.1997', 'Andijon')
print(odam)

x=[]
def max_number(son1, son2, son3):
    x.append(son1)
    x.append(son2)
    x.append(son3)
    x.sort()
    return x[2]

max_number(12, 13, 14)
print(x[2])



def self_divide(son):
    x=son%10
    y=son/10
    if son%x == 0 and son%y == 0:
        print(f"Bu son self_divide: {son}")
    else:
        print("Bu son unaqabas")
self_divide(20)
        


def self_divide(son1, son2):
    # odd_number = []
    for son in range(son1, son2+1):
        for y in str(son):
            if int(y) == 0 or son%int(y) != 0:
                break
            else:
                odd_number.append(son)
    return odd_number

a = self_divide(1, 20)
print(a) 
                
def summ_num(*sonlar):
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
            
print(summ_num(1, 1, 2, 3))


def multiple_summ(*numbers):
    multi = 1
    for number in numbers:
        multi *= number
    return multi

print(multiple_summ(1, 4, 5, 6))


def student_info(name, sname, **add_info):
    """Studentlar haqidagi ma`lumotlar"""
    add_info['name'] = name
    add_info['sname'] = sname
    return add_info

student1 = student_info("Mardonbek", 'Sobirov', birth_date='03.10.1997')
print(student1)


import math
print(math.fabs(-45))

import random as ran
son = ran.randint(0, 100)
print(son)

import math
son = math.sqrt(25)+math.pow(5, 2)
print(str(son))


def lambda_test(son):
    return lambda x : x**son
a = lambda_test(3)
print(a(10))


x = 'fruits'
for y in x:
    if y == 'b':
        continue
    print(y)
else:
    print(y)
    

for x in [0, 1, 2]:
  pass
  
print(x)


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()        
            
    
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


cars = ["Ford", "Volvo", "BMW"]
a=len(cars)
print(a)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

    
    class Programm:
          def __init__(self, name, sname):
            self.name = name
            self.sname = sname
                
          def my_name(self):
            print("My full name is: "+self.name+' '+self.sname)
            
    a = Programm("Mardonbek", "Sobirov")
    a.my_name()


class Checking_info:
    def __init__(self, name, sname, birth_date, mail):
        self.name=name
        self.sname=sname
        self.birth_date=birth_date
        self.mail=mail
    def get_sname(self, sname):
        self.sname=sname
    def get_birthdate(self, birth_date):
        self.birth_date=birth_date
    def get_mail(self, mail):
        self.mail=mail
    def all_info(self):
        
        print(f"To'liq ismingiz: {self.name} {self.sname}"
              f"\nTugulgan kuninghiz: {self.birth_date}"
              f"\nelektron pochtangiz: {self.mail}")
 
student = Checking_info("Mardonbek", "Sobirov", "03.10.1997", "Smardonbek9797@gmail.com")
student.all_info()
 
    
import pandas as pd

ds = pd.Series([2, 4, 6, 8, 10])

print(ds)


class Checking_info:
    def __init__(self, name, sname, birth_date, mail):
        self.name=name
        self.sname=sname
        self.birth_date=birth_date
        self.mail=mail
    def get_sname(self, sname):
        self.sname=sname
    def get_birthdate(self, birth_date):
        self.birth_date=birth_date
    def get_mail(self, mail):
        self.mail=mail
    def all_info(self):
        
        print(f"To'liq ismingiz: {self.name} {self.sname}"
              f"\nTugulgan kuninghiz: {self.birth_date}"
              f"\nelektron pochtangiz: {self.mail}")
 
student = Checking_info("Mardonbek", "Sobirov", "03.10.1997", "Smardonbek9797@gmail.com")
student.all_info()

class Checking_info2:
    def __init__(self, region, birth_country, email):
        self.region=region
        self.birth_country=birth_country
        self.email=email
    def get_sname(self, region):
        self.region=region
    def get_birthdate(self, birth_country):
        self.birth_country=birth_country
    def get_mail(self, email):
        self.email=email
    def all_info(self):
        
        print(f"To'liq ismingiz: {self.region} {self.birth_country}"
              f"\nelektron pochtangiz: {self.mail}")
 
student = Checking_info2("Sultonbek", "Sobirov", "Smardonbek9799@gmail.com")
student.all_info()





































 



































