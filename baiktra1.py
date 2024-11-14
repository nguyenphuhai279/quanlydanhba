"""
Xây dựng chương trình tính toán chỉ số BMI (Body Mass Index) và phân loại tình trạng cân nặng.
Viết hàm tinh_bmi(can_nang, chieu_cao) để tính toán chỉ số BMI với can_nang (kg) và chieu_cao (m) là tham số đầu vào.
Viết hàm phan_loai_bmi(bmi) để phân loại tình trạng cân nặng dựa trên chỉ số BMI, trả về kết quả là một chuỗi:
"Gầy" nếu BMI < 18.5
"Bình thường" nếu 18.5 <= BMI < 25
"Thừa cân" nếu 25 <= BMI < 30
"Béo phì" nếu BMI >= 30
Viết chương trình chính yêu cầu người dùng nhập cân nặng và chiều cao,
sau đó gọi hai hàm trên để tính toán và in ra chỉ số BMI cùng với phân loại tình trạng cân nặng.
"""
def tinh_bmi(can_nang, chieu_cao):  
    bmi = can_nang / chieu_cao**2
    return bmi

def phan_loai_bmi(bmi):
    if bmi < 18.5:  
        print("Gầy")
    elif 18.5 <= bmi < 25:  
        print("Bình thường")
    elif 25 <= bmi < 30:  
        print("Thừa cân")
    else:  
        print("Bép phì")

can_nang = float(input("Nhập vào cân nặng(kg):"))
chieu_cao = float(input("Nhập vào chiều cao(m):"))
bmi = tinh_bmi(can_nang, chieu_cao)
phan_loai_bmi(bmi)
