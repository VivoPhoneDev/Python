
amount = int(input("Введите кол-во чисел: "))
i = 0
nums = []
num = 0
total = 0 
try:

    for amount in range(amount):
        i += 1
        num = int(input(f"Число № {i}: "))
        nums.append(num)

    for num in nums:
        total = total + num  
    print(total)

except ValueError:
    print ("Ошибка! Вводите только целые числа!")
except Exception as e:
    print(f"Ошибка! {e} ")