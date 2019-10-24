my_list = range(101)
#print(len(my_list))
#print(list(my_list[1::]))

my_ints = list(my_list[1::])
print(my_ints)

def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return 'FizzBuzz'
    elif num%5==0:
        return 'Buzz'
    elif num%3==0:
        return 'Fizz'
    else:
        return num

for num in my_ints:
    print(fizz_buzz(num))

