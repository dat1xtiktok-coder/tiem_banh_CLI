danh_sach_banh = {
    "bánh kem": 12000,
    "bánh trứng": 10000,
    "bánh phô mai": 20000
}


def danh_sach():
    print("danh sách bánh trong cửa hàng")
    for ten, gia in danh_sach_banh.items():
        print(f"loại bánh: {ten} - giá bán {gia:,} VNĐ")
        #hàm in danh sách

def khach_hang():
    khach = str(input("Mời bạn nhập tên:" )).strip().title()
    print(f"xin chào{khach}")
    #hàm nhập tên khách hàng
    return  khach

def tinh_tien(so_luong, gia):
    return so_luong *gia
def luu_hoa_don(ten_khach, ten_banh, tong_tien):
    with open("lich_su_tiem_banh.txt", "a", encoding = "utf-8") as f:
        f.write(f"\nKhách: {ten_khach} - Món: {ten_banh} - Tổng tiền: {tong_tien:,}")
        print("lưu hóa đơn thành công")


def chon_mon():
    danh_sach()
    khach = khach_hang()
    
    ten_banh = input("mời bạn nhập bánh muốn mua: ").strip().lower()
    if ten_banh in danh_sach_banh:
        try:
            so_luong = int(input("mời bạn nhập số lượng: "))
            if so_luong < 0:
                print("số lượng phải lớn hơn 0")
                return

            gia = danh_sach_banh[ten_banh]
            tong = tinh_tien(so_luong, gia)
            tong_dep = f"{tong:,}".replace(",", ".")
            print(f"\n => đặt hàng thành công ! tổng tiền của bạn là : {tong_dep} vnđ")
            
            luu_hoa_don(khach, ten_banh, tong)
           
        except ValueError:
            print("Lỗi nhập sai! Vui lòng chỉ nhập số nguyên cho số lượng")
    else:
        print("cửa hàng không có loại bánh này")




chon_mon()
