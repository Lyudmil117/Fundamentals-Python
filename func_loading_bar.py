def loading_bar(num):

    if num == 100:
        print("100% Complete!")
        print("%%%%%%%%%%")
    else:
        percent = (num//10) * '%'
        dots = (num//10) * "."

        loading_status = f'{percent}{dots}'
        print(f'{num}% {loading_status}')
        print('Still loading...')


num = int(input())
loading_bar(num)
