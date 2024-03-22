#2자리 숫자를 입력받아 앞자리와 뒷자리 값을 더하세요.abs

number = input("2자리 숫자를 입력하세요 : ")
print(type(number))

if len(number) != 2:
    print("2자리 숫자를 입력하세요.")
else:
    first_num = int(number[0]) + int(number[1])
    print(first_num)