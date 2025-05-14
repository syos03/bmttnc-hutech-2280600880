def chiahetcho5 (sonhiphan):
    sothapphan = int (sonhiphan, 2 )
    if(sothapphan % 5 ==0 ):
        return True
    else:
        return False
chuoisonhinphan =  input("Nhap chuoi so nhi phan: ")
sonhiphan_list = chuoisonhinphan.split(',')
sochiahetcho5 = [so for so in sonhiphan_list if chiahetcho5(so)]
if len(sochiahetcho5) >0:
    ketqua = ','.join(sochiahetcho5)
    print("cac so nhi phan chia het cho 5 ",ketqua)
else:
    print("Khong co so nhi phan chia het cho 5")