import random

def bottles():
    number = int(input("How many bottles are on the wall"))

    for i in range(number):
        quant = number - i
        print(quant, "green bottles sitting on the wall")

def fibonacci(num):
    num_a = 0
    num_b = 1
    print("1")
    for i in range(num-1):
        buffer = num_a+num_b
        num_a = num_b
        num_b = buffer
        print(buffer)
        
def maths_test():
    score = 0
    for i in range(10):
        a = random.randint(1,10)
        b = random.randint(1, 10)
        ans = a+b
        string = str((str(a))+"+"+(str(b)))
        stu = int(input(string))
        if stu == ans:
            print("Correct")
            score += 1
            print(score)
        else:
            print("Incorrect")
    print("You got", score,"/10")
