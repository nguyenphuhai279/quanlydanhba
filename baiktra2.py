"""
Viết chương trình quản lý danh sách học viên của một lớp học.
Xây dựng hàm them_hoc_vien(danh_sach, ho_ten, diem) để thêm một học viên mới vào danh_sach. danh_sach là một list chứa các dictionary,
 mỗi dictionary lưu thông tin của một học viên bao gồm ho_ten và diem.
Xây dựng hàm tim_hoc_vien(danh_sach, ho_ten) để tìm kiếm học viên theo tên. 
Hàm trả về dictionary chứa thông tin của học viên nếu tìm thấy, ngược lại trả về None.
Xây dựng hàm cap_nhat_diem(danh_sach, ho_ten, diem_moi) để cập nhật điểm cho học viên.
Viết chương trình chính cho phép người dùng thực hiện các chức năng sau:
- Thêm học viên mới
- Tìm kiếm học viên
- Cập nhật điểm học viên
- Hiển thị danh sách học viên
"""
danh_sach = {}
diem = globals 
diem_moi = globals
ho_ten = globals
def them_hoc_vien(danh_sach, ho_ten, diem):
    them_hoc_vien = {"ho_ten": ho_ten, "diem": diem}
    danh_sach[ho_ten] = them_hoc_vien
def tim_hoc_vien(danh_sach, ho_ten):   
    if ho_ten in danh_sach:
        print(f"họ tên '{ho_ten}' điểm '{danh_sach[ho_ten]['diem']}'") 
    else:
        return None
def cap_nhat_diem(danh_sach, ho_ten, diem_moi):
    if ho_ten in danh_sach:
        danh_sach[ho_ten]["diem"] = diem_moi
def hien_thi_danh_sach_hoc_vien():
    for i in danh_sach:
        print(f"họ tên '{i}' điểm '{danh_sach[i]['diem']}'")
while True:
    print("1. Thêm học viên mới")
    print("2. Tìm kiếm học viên")
    print("3. Cập nhật điểm học viên")
    print("4. Hiển thị danh sách học viên")
    print("5. Thoát chương trình")
    chon = int(input("lựa chọn của bạn: "))
    if chon == 1:
        ho_ten = input("Ho ten hoc vien can them: ")
        diem = float(input("Diem hoc vien can them: "))
        them_hoc_vien(danh_sach, ho_ten, diem)
    elif chon == 2:
        ho_ten = input("Ho ten hoc vien can tim: ")
        hoc_vien = tim_hoc_vien(danh_sach, ho_ten)
    elif chon == 3:
        ho_ten = input("Ho ten hoc vien can cap nhat diem: ")
        diem_moi = float(input("Diem moi: "))
        cap_nhat_diem(danh_sach, ho_ten, diem_moi)
    elif chon == 4:
        hien_thi_danh_sach_hoc_vien()
    elif chon == 5:
        break
    else:
        print("Bạn chọn sai chức năng.")
        chon = int(input("Nhập lại lựa chọn của bạn"))
        