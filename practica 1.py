#Practica 1

#1
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)
# resultado de linea anterior: ['trek', 'cannondale', 'redline', 'specialized']

#1.1
print(bicycles[1])
#resultado: cannondale
print (bicycles[0].title())
#resultado: Trek

#1.2 
#Lista Names
names=['Carlos','Karla','Rafael','Gabriela','Ernesto']

#mensaje personalizado
print("Hola",names[0],"¿como te va?")#('Hola', 'Carlos', '\xc2\xbfcomo te va?')
print("Hola",names[1],"¿como te va?")#('Hola', 'Karla', '\xc2\xbfcomo te va?')
print("Hola",names[2],"¿como te va?")#('Hola', 'Rafael', '\xc2\xbfcomo te va?')
print("Hola",names[3],"¿como te va?")#('Hola', 'Gabriela', '\xc2\xbfcomo te va?')
print("Hola",names[4],"¿como te va?")#('Hola', 'Ernesto', '\xc2\xbfcomo te va?')

#Mi propia lista
list_wishes=['tener una casa','viajar','tener coche','tener una empresa','aprender a bailar','escribir un libro','aprender a cocinar','aprender a hacer tragos','aprender a programar muy bien','conocer lugares increibles','ver las maravilas del mundo','viajar con mi familia','investigar algo que revolucione al pais o mundo','crecer mas','tener dos carreras']
##print(len(list_wishes)#15
print("me gustaria",list_wishes[1])#('me gustaria', 'viajar')
print("me gustaria",list_wishes[5])#('me gustaria', 'escribir un libro')
print("me gustaria",list_wishes[4])#('me gustaria', 'aprender a bailar')
print("me gustaria",list_wishes[10])#('me gustaria', 'ver las maravilas del mundo')

#2
#2.1
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)#['honda', 'yamaha', 'suzuki']
motorcycles[0] = ('ducati')
print(motorcycles)#['ducati', 'yamaha', 'suzuki']

#2.2
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)#['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)#['honda', 'yamaha', 'suzuki', 'ducati']

#2.3
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)#['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)#['ducati', 'honda', 'yamaha', 'suzuki']

#2.4 pop y del
#2.4.1
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)#['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print (motorcycles)#['yamaha', 'suzuki']

#3 funciones 
def greet_user():
    #"""dipaly a simple greeting""""
    print("hello!")
greet_user() #hello!

#3.1
def greet_user(username):
    #imprime saludo 
    print("Hello "+username.title()+"!")
greet_user('jessie') #Hello Jessie!

#3.2.1
def describe_pet(anymal_type, pet_name):
    print("\nI have a "+anymal_type+".")
    print("My "+anymal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')
describe_pet('dog','willie')#I have a hamster.
                           #My hamster's name is Harry.
                           #I have a dog.
                           #My dog's name is Willie.
#comparacion
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "’s name is " + pet_name.title() + ".")
describe_pet('harry', 'hamster')#I have a harry.
                               #My harry’s name is Hamster.


#3.2.2
def describe_pet(anymal_type, pet_name):
    print("\nI have a "+anymal_type+".")
    print("My "+anymal_type+"'s name is "+pet_name.title()+".")
describe_pet(anymal_type='hamster',pet_name='harry')#I have a hamster.
                                                    #My hamster's name is Harry.

#3.3
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "’s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')#I have a dog.
                              #My dog’s name is Willie

#3.4
def make_shirt(tamano, texto):
    print("Se ha imprimido playera "+tamano+" con texto "+ texto.title())
make_shirt('grande','hola mundo:)')#Se ha imprimido playera grande con texto Hola Mundo:)
    
def make_shirt(tamano='grande', texto='I <3 Python'):
    print("Se ha imprimido playera "+tamano+" con texto "+ texto.title())
make_shirt()#Se ha imprimido playera grande con texto I <3 Python
make_shirt('mediana')#Se ha imprimido playera mediana con texto I <3 Python
make_shirt('pequeña','Hola Programacion')#Se ha imprimido playera pequeña con texto Hola Programacion

def describe_city(ciudad,pais='mexico'):
    print(ciudad.title()+" esta en "+pais.title())
describe_city('CDMX')#Cdmx esta en Mexico
describe_city('paris','francia')#Paris esta en Francia
describe_city('guadalajara')#Guadalajara esta en Mexico

#4
class Dog():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is now sitting")
    def roll_over(self):
        print(self.name.title()+" ha dado una vuelta.")
my_dog = Dog('willie',6)
print("My dog’s name is " + my_dog.name.title() + ".")#My dog’s name is Willie.
print("My dog is " + str(my_dog.age) + " years old.")#My dog is 6 years old.
my_dog.sit()#Willie is now sitting
my_dog.roll_over()#Willie ha dado una vuelta.

#4.2
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("El restaurante "+self.restaurant_name.title()+" es de cocina "+self.cuisine_type)
    def open_restaurant(self):
        print("El restaurante "+self.restaurant_name.title()+" esta abierto")
#Restaurant
restaurante=Restaurant('busines', 'fria')
restaurante.describe_restaurant()#El restaurante Busines es de cocina fria
restaurante.open_restaurant()#El restaurante Busines esta abierto
#Tres Resrtaurantes
restaurante1=Restaurant('kalifa', 'china')
restaurante1.describe_restaurant()#El restaurante Kalifa es de cocina china
restaurante1.open_restaurant()#El restaurante Kalifa esta abierto

restaurante2=Restaurant('maravilla','japonesa')
restaurante2.describe_restaurant()
restaurante2.open_restaurant()

restaurante3=Restaurant('slip','italiana')
restaurante3.describe_restaurant()
restaurante3.open_restaurant()

#Usuarios
class User():
    def __init__(self,first_name, last_name, mobile, age, country):
        self.first_name=first_name
        self.last_name=last_name
        self.mobile=mobile
        self.age=age
        self.country=country
    def describe_user(self):
        print("Usuario: "+self.first_name.title()+" "+self.last_name.title()+ " Celular: "+self.mobile+" Edad: "+self.age+" Pais: "+self.country.title())
    def greet_user(self):
        print("Hola "+self.first_name.title()+" "+self.last_name.title()+" bienvenido!")
us1=User('carlos','coutinho','5565342354','20','mexico')
us1.describe_user()
us1.greet_user()

us2=User('carmen','gonzales','5582390565','23','peru')
us2.describe_user()
us2.greet_user()

us3=User('litzy','otanez','5581204820','19','mexico')
us3.describe_user()
us3.greet_user()

us4=User('hernesto','rojas','5500223388','18','mexico')
us4.describe_user()
us4.greet_user()

us5=User('lalo','nuno','6878458988','19','mexico')
us5.describe_user()
us5.greet_user()

us6=User('laura','mancera','5592304866','19','mexico')
us6.describe_user()
us6.greet_user()

us7=User('ximena','quintanar','5582934056','18','mexico')
us7.describe_user()
us7.greet_user()

us8=User('lizbeth','hernandez','7782034056','20','mexico')
us8.describe_user()
us8.greet_user()

us9=User('miguel','arizmendi','8822308450','20','mexico')
us9.describe_user()
us9.greet_user()

us10=User('karen','servin','6678239455','18','mexico')
us10.describe_user()
us10.greet_user()