so_gio_lam = float(input("Nhap so gio lam moi tuan "))
luong_gio = float (input("Nhap thu lao tren moi gio lam tieu chuan "))
giotc = 44
giovc = max(0,so_gio_lam - giotc)
thuclinh = giotc * luong_gio+ giovc *luong_gio * 1.5
print(f"so tien thuc linh cua nhan vien  {thuclinh}")