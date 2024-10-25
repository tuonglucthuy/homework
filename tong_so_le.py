# Câu 2:

number = int(input("Nhập n số cần nhập :"))
tong = 0
for i in range(number):
    num = int(input(f"Nhập số thứ {i+1} : "))
    if num %2 != 0:
        tong += 0
if(tong == 0):
    print("Chương trình không có số lẻ")
else:
    print("Tổng số lẻ là :" )