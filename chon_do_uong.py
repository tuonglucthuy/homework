# Danh sách các đồ uống
do_uong = ["sting", "coca-cola", "pepsi", "red-bull"]
# Danh sách giá tiền tương ứng với các đồ uống
gia_tien = [10000, 15000, 17000, 18000]

print("---Danh sách đồ uống và giá tiền---")
# Sử dụng vòng lặp for để in từng đồ uống và giá tiền tương ứng
for i in range(0, 4):
    print(do_uong[i], ":", gia_tien[i])

chon = int(input("Vui lòng chọn loại đồ uống (1-4): "))

if 1 <= chon <= 4:
    # In ra đồ uống mà người dùng đã chọn (do chỉ số trong danh sách bắt đầu từ 0, nên cần -1)
    print("Bạn đã chọn", do_uong[chon - 1])
    # Yêu cầu người dùng nhập số lượng muốn mua
    so_luong = int(input("Vui lòng nhập số lượng bạn muốn mua: "))
    # Tính tổng tiền bằng cách nhân số lượng với giá của đồ uống đã chọn
    tong_tien = so_luong * gia_tien[chon - 1]
    # In ra hóa đơn tổng tiền
    print("Hóa đơn của bạn là:", tong_tien)
else:
    # Nếu người dùng nhập sai lựa chọn, in thông báo lỗi
    print("Bạn đã nhập sai")
