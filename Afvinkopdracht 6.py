import time

def main():
    fib_test()

def fib_test():
    number = int(input('How many numbers do you want to produce?: '))
    
    s_time = time.time()
    for num in range(number):
        print(fib_recursive(num))

    print('Recursion took', time.time() - s_time, 'seconds.')

    s_time = time.time()
    for num in range(number):
        print(fib_iter(num))

    print('Iteration took', time.time() - s_time, 'seconds.')

def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

def fib_iter(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a

main()
