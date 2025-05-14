def tinh_tong_so_chan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

intput_list = input("Nhap danh sach cac so, cach nhau boi phay: ")
numbers = list(map(int, intput_list.split(',')))
tong_chan = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong danh sach la:", tong_chan)