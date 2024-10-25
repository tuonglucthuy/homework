import turtle

# Thiết lập cửa sổ Turtle
screen = turtle.Screen()
screen.bgcolor('white')                 # Chỉnh sửa từ 'while' thành 'white'
start = turtle.Turtle()
start.speed(5)

# Hàm vẽ ngôi sao
def draw_start(size):
    start.color('yellow')               # Màu của ngôi sao là vàng
    start.begin_fill()                  # Bắt đầu quá trình tô màu
    for _ in range(5):
        start.forward(size)
        start.right(144)
        start.forward(size)             # Di chuyển về phía trước
        start.left(72)
    start.end_fill()                    # Kết thúc quá trình tô màu

# Hàm vẽ hình chữ nhật (lá cờ)

def draw_rectangle(width, height):
    start.color('red')                  # Màu của hình chữ nhật là đỏ
    start.penup()                       # Nhấc bút lên để di chuyển mà không vẽ
    start.goto(-width / 2, height / 2)  # Đưa bút đến góc trên trái của hình chữ nhật
    start.pendown()                     # Đặt bút xuống để bắt đầu vẽ
    start.begin_fill()                  # Bắt đầu tô màu cho hình chữ nhật
    for _ in range(2):
        start.forward(width)
        start.right(90)
        start.forward(height)
        start.right(90)
    start.end_fill()

# Kích thước lá cờ
rectangle_width = 600
rectangle_height = 400
                                        # Vẽ hình chữ nhật (lá cờ)

draw_rectangle(rectangle_width, rectangle_height)   

# Vẽ ngôi sao ở vị trí trung tâm
start.penup()                            # Nhấc bút lên để di chuyển mà không vẽ
start.goto(25, 20)                       # Đặt ngôi sao gần trung tâm
start.pendown()                          # Đặt bút xuống để bắt đầu vẽ
draw_start(100)                          # Vẽ ngôi sao vàng năm cánh với kích thước 100
start.hideturtle()                       # Ẩn turtle sau khi vẽ xong

turtle.done()