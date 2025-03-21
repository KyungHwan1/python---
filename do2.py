src=int(input("입력진수 결정(16/10/8/2) : "))
tar=input("값 입력 : ")

num=int(tar,src)

print("변환 결과값")
print("2진수 :", bin(num))
print("8진수 :", oct(num))
print("10진수 :", num)
print("16진수 :", hex(num))