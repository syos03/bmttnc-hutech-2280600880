from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSINHVIEN = []  # Biến thực thể - không dùng biến lớp

    def generateID(self):
        return max([sv._id for sv in self.listSINHVIEN], default=0) + 1

    def soLuongSinhVien(self):
        return len(self.listSINHVIEN)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành sinh viên: ")
        try:
            diemTB = float(input("Nhập điểm trung bình: "))
        except ValueError:
            print("Điểm không hợp lệ. Vui lòng nhập số.")
            return
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSINHVIEN.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            name = input("Nhập tên mới: ")
            sex = input("Nhập giới tính mới: ")
            major = input("Nhập chuyên ngành mới: ")
            try:
                diemTB = float(input("Nhập điểm mới: "))
            except ValueError:
                print("Điểm không hợp lệ.")
                return
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại.")

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSINHVIEN.remove(sv)
            return True
        return False

    def findByID(self, ID):
        return next((sv for sv in self.listSINHVIEN if sv._id == ID), None)

    def findByName(self, keyword):
        return [sv for sv in self.listSINHVIEN if keyword.lower() in sv._name.lower()]

    def sortByID(self):
        self.listSINHVIEN.sort(key=lambda sv: sv._id)

    def sortByName(self):
        self.listSINHVIEN.sort(key=lambda sv: sv._name.lower())

    def sortByDiemTB(self):
        self.listSINHVIEN.sort(key=lambda sv: sv._diemTB)

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV=None):
        if listSV is None:
            listSV = self.listSINHVIEN
        print("{:<8} {:<18} {:<8} {:<18} {:<8} {:<10}".format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<18} {:<8.2f} {:<10}".format(
                sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print()

    def getListSinhVien(self):
        return self.listSINHVIEN
