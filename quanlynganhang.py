danh_ba_dien_thoai = {}
def them_lien_he():
    ten = input("Nhập tên liên hệ: ")
    while True:
        sdt = input("Nhập số điện thoại(phải đủ 10 số): ").replace(" ", "")
        if len(sdt) == 10:
             break
        print("Nhập lại số điện thoại: ")
   
    danh_ba_dien_thoai[ten] = sdt
    print("Đã thêm liên hệ ")

def xoa_lien_he():
    ten = input("Nhập tên liên hệ cần xóa: ")
    if ten in danh_ba_dien_thoai:
        del danh_ba_dien_thoai[ten]
        print("Đã xóa liên hệ")
    else:
        print("Không tìm thấy liên hệ ")

def tim_kiem_lien_he():
    if len(danh_ba_dien_thoai) == 0:
        print("Không có thông tin")
    else:
        ten = input("Nhập tên liên hệ cần tìm kiếm: ")
        if ten in danh_ba_dien_thoai:
            print(f"Thông tin liên hệ: {ten} có số là {danh_ba_dien_thoai[ten]}")
        else:
            print("Không tìm thấy liên hệ có tên ")

def xem_danh_ba():
    for i in danh_ba_dien_thoai:
        print(f"Thông tin liên hệ: {i} có số là {danh_ba_dien_thoai[i]}")
    
while True:
    print("\nMenu:")
    print("1. Thêm liên hệ")
    print("2. Xóa liên hệ")
    print("3. Tìm kiếm liên hệ")
    print("4. xem danh bạ ")
    print("5. Thoát")

    lua_chon = input("Chọn chức năng (1-5): ")

    if lua_chon == '1':
        them_lien_he()
    elif lua_chon == '2':
        xoa_lien_he()
    elif lua_chon == '3':
        tim_kiem_lien_he()
    elif lua_chon == '4':
        xem_danh_ba()
    elif lua_chon == '5':
        break
    else:
        print("Chức năng không hợp lệ. Vui lòng chọn lại.")