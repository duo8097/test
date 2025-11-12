# ===============================
# Import thư viện cần thiết
# math -> chứa các hàm toán học
# Counter -> đếm tần suất các phần tử trong list hoặc chuỗi
# ===============================
import math
from collections import Counter

# ===============================
# Nhập liệu
# ===============================
chuoi = input()                        # nhập chuỗi
so_nguyen = int(input())               # nhập số nguyên
so1, so2 = map(int, input().split())   # nhập hai số nguyên cùng lúc
print("------------------------------")
# ===============================
# If-Else cơ bản
# ===============================
# "==" = so sánh bằng nhau
# "!=" = so sánh khác nhau
# ">"  = lớn hơn
# "<"  = nhỏ hơn
# ">=" = lớn hơn hoặc bằng
# "<=" = nhỏ hơn hoặc bằng
if chuoi == "may gay":  
    print("t bi gay")
elif chuoi == "t thu dam":  
    print("t les")
else:  
    print("t la lgbt")

# ===============================
# Boolean cơ bản
# ===============================
# Kết quả của các biểu thức so sánh là True (đúng) hoặc False (sai)
is_lon = so_nguyen > 10
is_bang = so1 == so2
co_chu_so = any(char.isdigit() for char in chuoi)  
tat_ca_in_hoa = all(char.isupper() for char in chuoi)  

print("so_nguyen > 10?", is_lon)
print("so1 == so2?", is_bang)
print("chuoi có ký tự số không?", co_chu_so)
print("chuoi có toàn chữ in hoa không?", tat_ca_in_hoa)

# ===============================
# If-Else với logic nâng cao (AND / OR)
# ===============================
# "and" = và nghĩa là các điều kiện phải đúng hết
# "or"  = hoặc nghĩa là chỉ cần một điều kiện đúng
if so1 == so2 and so_nguyen == 10:  
    print("so1 = so2 và so_nguyen = 10")
elif so1 != so2 and so_nguyen == 0: 
    print("so1 khác so2 và so_nguyen = 0")
elif so1 > so2 or so_nguyen > 100: 
    print("so1 > so2 hoặc so_nguyen > 100")
else:  
    print("Nothing =)))")

# ===============================
# Vòng lặp vô tận với break
# ===============================
i = 0
print("Vòng lặp vô tận với break:")
while True:        
    if i == so_nguyen:     
        break
    i += 1         
    print(i, end=" ")  
print()

# ===============================
# Vòng lặp while với điều kiện
# ===============================
# sau while là điều kiện để vòng lặp tiếp tục chạy
i = 0
print("Vòng lặp while với điều kiện:")
while i != so_nguyen:      
    i += 1
    print(i, end=" ")
print()

# ===============================
# Vòng lặp for cơ bản
# ===============================
print("Vòng lặp for cơ bản:")
for i in range(1, so_nguyen + 1):  
    print(i, end=" ")
print()

# ===============================
# List và vòng lặp
# ===============================
ds = [chuoi, so_nguyen, so1, so2]      
for x in ds:            
    print(x, end=" ")           

# ===============================
# Dùng math
# ===============================
# Một số hàm phổ biến trong math:
# math.gcd(a, b)  -> ước chung lớn nhất của a và b
# math.lcm(a, b)  -> bội chung nhỏ nhất của a và b
# math.isqrt(n)   -> căn bậc 2 của n (trả về int)
# math.sqrt(n)    -> căn bậc 2 của n (trả về float)
print("GCD của so1 và so2:", math.gcd(so1, so2)) 
print("LCM của so1 và so2:", math.lcm(so1, so2))       
print("Căn bậc 2 của so_nguyen (int):", math.isqrt(so_nguyen)) 
print("Căn bậc 2 của so_nguyen (float):", math.sqrt(so_nguyen)) 

# ===============================
# Dùng Counter để đếm
# ===============================
# Counter từ collections giúp đếm tần suất xuất hiện của các phần tử trong chuỗi hoặc danh sách
dem_ky_tu = Counter(chuoi)                 
print("Counter của chuoi:", dem_ky_tu)

dem_so = Counter([so_nguyen, so1, so2, so_nguyen, so1])   
print("Counter của ds số:", dem_so)

# ===============================
# Boolean nâng cao + any/all
# ===============================
# any() -> trả về True nếu ít nhất một phần tử đúng
# all() -> trả về True nếu tất cả phần tử đúng
tat_ca_duong = all(x > 0 for x in [so_nguyen, so1, so2])   
co_so_lon = any(x > 100 for x in [so_nguyen, so1, so2])    
print("Tất cả số > 0?", tat_ca_duong)
print("Có số nào > 100 không?", co_so_lon)

# ====== END OF 4 DAYS OF CODE ====== 