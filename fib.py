
def r_fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    return r_fibonacci(n-1) + r_fibonacci(n-2)

def i_fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    nminus2 = 0
    nminus1 = 1
    fibonacci_number = 0
    for i in range(2, n+1):
        fibonacci_number = nminus2 + nminus1
        nminus2 = nminus1
        nminus1 = fibonacci_number
    return fibonacci_number

"""
randlist = generate_random_numbers(30)

@timer
def main():
    print(selection_sort(randlist))

if __name__ == '__main__':
    main()
"""