do_uong = ["sting", "coca-cola", "pepsi", "red-bull"]
gia_tien = [10000, 15000, 17000, 18000]
count = 0

print("---Danh sách đồ uống và giá tiền---")
for i in range(len(do_uong)):
    print(i+1, do_uong[i], "có giá", gia_tien[i])

choose = input("Hãy chọn đồ uống bạn muốn: ")
so_luong = int(input("Nhập vào số lượng bạn muốn mua: "))

for i in range(len(do_uong)):
    if choose == do_uong[i]:
        print(f"Bạn đã mua {choose} số lượng {so_luong}, tổng cộng {gia_tien[i] * so_luong} VNĐ.")
        break
    else:
        count += 1

if count == len(do_uong):
    print("Xin lỗi chúng tôi không có !!!")