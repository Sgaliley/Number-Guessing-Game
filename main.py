import random
from colorama import init
from colorama import Fore, Back, Style

init()

n = random.randrange(1, 10)
guess = int(input('Введите число от 1 до 10: '))
while n != guess:
    if n > guess:
        print(Fore.RED + 'Неправильное число. Введите больше число.')
        guess = int(input('Введите число от 1 до 10: ' + Style.RESET_ALL))
    elif n < guess:
        print(Fore.BLUE + 'Неправильное число. Введите меньше число.')
        guess = int(input('Введите число от 1 до 10: ' + Style.RESET_ALL))
    else:
        break
print(Fore.GREEN + 'Вы угадали. Поздравляю!!!')
