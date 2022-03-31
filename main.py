# a= 2, b=5
# a=2, b=-3
# a= -3, b=-3
# a=0.3 b=0.7
# a=1.2 b=-0.2
# a=0, b=0

# a=3, b
# a='3' b='3'
#

# cart = [55.55, 60.37, 100.01]
# cart = [0, 0, 0]
# cart = ['33.05', 12, 500, 50.05]

# cart = [] => 0
# cart = [20]

# ===================================
# cart = []
#
#
# if not cart:
#     print('Final sum = 0')
#     exit()
#
#
# if len(cart) == 1:
#     print('Final sum =', cart[0])
#     exit()
#
#
# def min_func(array):
#     my_min = array[0]
#
#     for i in array:
#         if i < my_min:
#             my_min = i
#     return my_min
#
#
# def make_sale(num, percent):
#     return (num * percent) / 100
#
#
# def cart_sum(cart):
#     total_sum = 0
#
#     for i in cart:
#         total_sum = total_sum + i
#
#     return total_sum
#
#
# min_cost = min_func(cart)
# sale = make_sale(min_cost, 20)
# simple_user = min_cost - sale
# total_amount = cart_sum(cart)
# final_sum = total_amount - sale
#
# print("Final sum:", final_sum)
# print("Discounter price of the most cheapest item:", simple_user)
# ===================================
from enum import Enum


class User(Enum):
    SILVER = 5
    GOLD = 10
    PLATINUM = 20

    @classmethod
    def _missing_(cls, value):
        return 0


cart = [
    ([20, 30], 46.0),
    ([], 0.0),
    ([20], 20.1),
    ([100, 100, 100], 280.0)
]


def calcValueWithPercent(value, percent=0):
    return value - ((value * percent) / 100) # 100 (20%) = 80


def bubbleSort(arr): #[20, 5, 10] => [5, 10, 20]
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr


def total(arr, user_type='DEFAULT'):
    length = len(arr)

    if length == 0:
        return 0

    if user_type == 'DEFAULT':
        if length == 1:
            return arr[0]
        else:
            sorted_arr = bubbleSort(arr)
            min_value = sorted_arr[0]

            return calcValueWithPercent(min_value, 20) + sum(sorted_arr[1:]) #[100, 200, 200] => (100 20%) + [200, 200]
    else:
        percent = User[user_type].value
        return calcValueWithPercent(sum(arr), percent)


if __name__ == '__main__':
    print(total([100, 100, 100], 'PLATINUM'))

    for case in cart:
        assert total(case[0]) == case[1]

        # try:
        #     assert total(case[0]) == case[1]
        # except AssertionError:
        #     print(f'ERROR: Total {total(case[0])} is not equal {case[1]}')
