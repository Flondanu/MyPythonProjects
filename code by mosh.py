first = 'john'
last = 'smith'
msg = f'{first} [{last}] is a coder'
print(msg)
course = 'python for beginners'
print(len(course))
print(course.upper())
print(course.find('r'))
print(course.replace('python', 'Python'))
print('for' in course)
x = 2.8
print(round(x))
print(abs(-2.8))
print(10//3)
#program that takes your weight and prints it in either kgs or lbs
weight = int(input('weight: '))
unit = input('lbs or kgs:')
if unit.lower == 'l':
    converted = weight*0.45
    print(f"you are{converted} kgs")
else:
    converted = weight/0.45
    print(f"you are {converted} lbs")

#this program is a guess game
secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('guess:'))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break
else : ('sorry you failed')






