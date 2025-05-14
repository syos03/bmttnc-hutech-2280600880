def dao_nguoc_list(lst):
    return lst[::-1]

input_list = input("Nhap danh sach cac so, cach nhau boi phay: ")
numbers = list(map(int, input_list.split(',')))

list_dao_nguoc = dao_nguoc_list(numbers)
numbers = list(map(int, input_list.split(',')))
print("List sau khi dao nguoc:", list_dao_nguoc)