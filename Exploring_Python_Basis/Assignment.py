#Task 1: Variable Manipulation
def task1():
    name = "Sadia Tabassum"
    age = "23"
    print("My name is " + name + " and I am " + str(age) + " years old.")

#Task 2: Data Types and Type Conversion#
def task2():
    num1 = 10
    num2 = 10.5
    num1_float = float(num1)
    num2_int = int(num2)
    print("num1:", num1, "Type:", type(num1))
    print("num2:", num2, "Type:", type(num2))
    print("num1_float:", num1_float, "Type:", type(num1_float))
    print("num2_int:", num2_int, "Type:", type(num2_int))

#Task 3:String Manipulation
def task3():
    sentence = "Python programming is fun!"
    print("Length of the string:", len(sentence))
    print("8th character:", sentence[7])
    substring = sentence[1:7]
    result = substring + " I enjoy it!"
    print(result)

#Task 4: Lists and List Manipulation
def task4():
    fruits = ["apple", "banana", "cherry", "date"]
    fruits.append("grape")
    fruits.remove("banana")
    print("Length of the list:", len(fruits))
    sliced_fruits = fruits[1:3]
    extra_fruits = ["kiwi", "lemon"]
    combined_list = sliced_fruits + extra_fruits
    print("Combined list:", combined_list)

#Task 5: Conditional Statements
def task5():
    num = 7
    if num % 2 == 0:
        print(num, "is even.")
    else:
        print(num, "is odd.")

#Task 6: Loops
def task6():
    print("Numbers from 1 to 10:")
    for i in range(1, 11):
        print(i)
    sum_of_numbers = 0
    for i in range(1, 101):
        sum_of_numbers += i
    print("Sum of numbers from 1 to 100:", sum_of_numbers)


#Task 7: Functions
def task7():
    def calculate_square(num):
        return num ** 2
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    number_to_square = 7
    square_of_7 = calculate_square(number_to_square)
    print("Square of", number_to_square, "is:", square_of_7)
    number_to_check = 29
    if is_prime(number_to_check):
        print(number_to_check, "is a prime number.")
    else:
        print(number_to_check, "is not a prime number.")


#Task 8: Dictionaries
def task8():
    student = {
        "name": "Sadia Tabassum",
        "age": 23,
        "grade": "A"
    }
    student["course"] = "Computer Science"
    print("Keys in the dictionary:", student.keys())
    print("Key-value pairs in the dictionary:")
    for key, value in student.items():
        print(key, ":", value)
task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()