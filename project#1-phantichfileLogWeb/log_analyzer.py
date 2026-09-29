danh_sach_ip=[] #Tạo một danh sách rỗng để lưu trữ các địa chỉ IP
danh_sach_ip_loi=[] #Tạo một danh sách rỗng để lưu trữ các địa chỉ IP bị lỗi 403

with open ("access.log", "r") as f : #Lỗi thiếu dấu hai chấm ":"
    for dong in f : #Lỗi thiếu dấu hai chấm ":"
        cac_tu = dong.split() #Nó sẽ tự chia ra theo dấu cách, rồi gán vào mảng cac_tu
        ip = cac_tu[0] #Lấy ra địa chỉ IP từ mảng cac_tu đối với mỗi dòng
        ma_loi = cac_tu[7] #Lấy ra mã lỗi từ mảng cac_tu đối với mỗi dòng

        danh_sach_ip.append(ip) #Thêm địa chỉ IP vào danh sách
        if cac_tu[7] == "403" : #Nhớ bỏ thêm dấu "" vì cac_tu[7] là một chuỗi chứ kp số 
            danh_sach_ip_loi.append(ip)

thong_ke_ip = {} #Tạo một dictionary rỗng để lưu trữ thông tin thống kê IP

#Bây giờ ta dùng cái dict thong_ke_ip để thêm IP và Giá trị "số lần xuất hiện"
for ip in danh_sach_ip :
    if ip in thong_ke_ip :
        thong_ke_ip[ip] += 1 
    else :
        thong_ke_ip[ip] = 1
#Bây giờ trong dict đã có thông tin các IP khác nhau và số lần xuất hiện của IP đó

ma_loi_ip = {}

#Làm tương tự bước trên
for ip in danh_sach_ip_loi :
    if ip in ma_loi_ip :
        ma_loi_ip[ip] += 1 
    else :
        ma_loi_ip[ip] = 1
#Bây giờ ta đã có thông tin các IP lỗi 403 và số lần bị lỗi

print ("Thống kê truy cập theo IP :") #print trong Python đã tự động xuống dòng rồi
print (thong_ke_ip)
print ("\n")
print ("Danh sách IP bị lỗi 403 :")
for ip in ma_loi_ip :
    print(f" - IP {ip} : Bị lỗi 403 tổng cộng {ma_loi_ip[]} lần") 

#Cách dùng hàm items() cho dict, nó tự chia key và value ra, gán vào biến ta khai báo    
#for ip, so_lan in ma_loi_ip.items():
    #print(f" - IP {ip} : bị lỗi 403 tổng cộng {so_lan} lần")