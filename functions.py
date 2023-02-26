def hello_user():
    print("Hello")

hello_user()


def greet_user(username,roll_no):
    print(f"Hello {username} !! Your roll no is {roll_no}")

greet_user("Kamakshya",7)

greet_user(roll_no=8,username="kamakshya")


def musician(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title() 

name = musician("Jimmy","Page")
print(name)


def names(student):
    for student_name in student :
        print(student_name)

name_a = ["John","sarah"]
names(name_a[:])

def pizza_toppings(*toppings) :
    for topping in toppings:
        print(topping)

pizza_toppings("olive")
pizza_toppings("pepperoni","onion")


