do_uong = ["sting", "coca-cola", "pepsi", "red-bull"]
gia_tien = [10000, 15000, 17000, 18000]

print("---Danh sách đồ uống và giá tiền---")
for i in range(len(do_uong)):
    print(i+1, do_uong[i], "có giá :", gia_tien[i],"VNĐ")

print("Bạn có muốn thêm muốn mới vào menu? ")
new_do_uong = int(input("Vui lòng chọn số lượng bạn muốn thêm vào menu :"))

for i in range(new_do_uong):
    do_uong.append(input("Vui lòng nhập tên đồ uống bạn muốn thêm : "))
    gia_tien.append(input("Vui lòng nhập giá tiền của đồ uống bạn muốn thêm :"))

print("---Menu hiện tại của quán là---")
for i in range(len(do_uong)):
    print(i+1,do_uong[i], "có giá", gia_tien[i],"VNĐ")