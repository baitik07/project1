# a = 2**3
# b = 3**2
# if a < b:
#     print("a is smoller than b")
# else:
#     print("a is bigger than b")


a = int(input('First number: '))
b = int(input('Second number: '))
c = int(input('Third number: '))
if a < b < c:
    print('Самое большое С, самый маленький А')
elif c < b < a:
    print('Самое большое A, самый маленький C')
elif b < c < a:
    print('Самое большое A, самый маленький B')
elif a < c < b:
    print('Самое большое B, самый маленький А')
elif c < a < b:
    print('Самое большое B, самый маленький C')
elif b < a < c:
    print('Самое большое С, самый маленький B')
else:
    print('Сбой системы!!!')

