
def perf_number():
    number = int(input())
    sum = 1
    for i in range(2, number):
        if number % i == 0:
            sum = sum + i

    if sum == number:
        print('We have a perfect number!')
    else:
        print("It's not so perfect.")


perf_number()
