# Various exercises to practice loops, conditionals, functions, and classes
# @author Nishank Kuppa

word = "nishank"
vowels = ["a", "e", "i", "o", "u"]

vowelCount = 0
for character in word:
    if character in vowels:
        vowelCount += 1

print(vowelCount)
print(type(character))

for i in range(2, 100, 14):
    print(i)

for v in vowels:
    print (v)

length = len(vowels)
print((length))

w=0
while w < len(vowels):
    print(vowels[w])
    w += 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))


def Fibonacci (n):
    if n==1:
        return  0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(5))

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark (self):
        print("woof")

fido = Dog("Fido", 2)
fido.bark()
print(fido.name)
print(fido.age)
fido.age +=1
print(fido.age)
