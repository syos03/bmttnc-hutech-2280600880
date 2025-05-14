def ktsnt (n):
    if n <= 1 :
        return False
    for i in range(2,int (n ** 0.5) + 1):
        if n %i == 0:
            return False
    return True
number =  int (input("Nhap so can tim kiem "))
if ktsnt(number):
    print(number,"la so nguyen to ")
else:
    print(number,"khong phia la so nguyen to ")