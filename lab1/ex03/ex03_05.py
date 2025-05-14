def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

input_srting = input("Nhap danh sach cac so, cach nhau boi dau cach: ")
word_list = input_srting.split()

so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("so lan xuat hien cua cac phan tu: ", so_lan_xuat_hien)
    