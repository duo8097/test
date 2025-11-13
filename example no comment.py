import math
from collections import Counter

chuoi = input()
so_nguyen = int(input())
so1, so2 = map(int, input().split())
print("------------------------------")
if chuoi == "may gay":  
    print("t bi gay")
elif chuoi == "t thu dam":  
    print("t les")
else:  
    print("t la lgbt")

is_lon = so_nguyen > 10
is_bang = so1 == so2
co_chu_so = any(char.isdigit() for char in chuoi)  
tat_ca_in_hoa = all(char.isupper() for char in chuoi)  

print("so_nguyen > 10?", is_lon)
print("so1 == so2?", is_bang)
print("chuoi có ký tự số không?", co_chu_so)
print("chuoi có toàn chữ in hoa không?", tat_ca_in_hoa)

if so1 == so2 and so_nguyen == 10:  
    print("so1 = so2 và so_nguyen = 10")
elif so1 != so2 and so_nguyen == 0: 
    print("so1 khác so2 và so_nguyen = 0")
elif so1 > so2 or so_nguyen > 100: 
    print("so1 > so2 hoặc so_nguyen > 100")
else:  
    print("Nothing =)))")

i = 0
print("Vòng lặp vô tận với break:")
while True:        
    if i == so_nguyen:     
        break
    i += 1         
    print(i, end=" ")  
print()

i = 0
print("Vòng lặp while với điều kiện:")
while i != so_nguyen:      
    i += 1
    print(i, end=" ")
print()

print("Vòng lặp for cơ bản:")
for i in range(1, so_nguyen + 1):  
    print(i, end=" ")
print()

ds = [chuoi, so_nguyen, so1, so2]      
for x in ds:            
    print(x, end=" ")           

print("GCD của so1 và so2:", math.gcd(so1, so2)) 
print("LCM của so1 và so2:", math.lcm(so1, so2))       
print("Căn bậc 2 của so_nguyen (int):", math.isqrt(so_nguyen)) 
print("Căn bậc 2 của so_nguyen (float):", math.sqrt(so_nguyen)) 

dem_ky_tu = Counter(chuoi)                 
print("Counter của chuoi:", dem_ky_tu)

dem_so = Counter([so_nguyen, so1, so2, so_nguyen, so1])   
print("Counter của ds số:", dem_so)

tat_ca_duong = all(x > 0 for x in [so_nguyen, so1, so2])   
co_so_lon = any(x > 100 for x in [so_nguyen, so1, so2])    
print("Tất cả số > 0?", tat_ca_duong)
print("Có số nào > 100 không?", co_so_lon)