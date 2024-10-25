# Câu 3:
thong_tin = {
    'ten' : ['Đỗ Mạnh Tường','Nguyễn Văn Bình','Trần Văn Bình'],
    'que_quan': ['Nam Định','Nam Định','Việt Nam']
}
count = 0
print("---Thông tin quê quán trong lớp là---")
for key,names in thong_tin.items():
    print(f'{key}')
    for name in names:
        print(f'-{name}')
for que_quan in thong_tin['que_quan']:
    if(que_quan == 'Nam Định'):
        count += 1
print("Số người sống ở Nam Định là :",count)