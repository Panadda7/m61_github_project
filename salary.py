# รับเงินเดือนจากผู้ใช้
salary = float(input("กรอกเงินเดือน: "))

# คำนวณภาษี 3%
tax = salary * 0.03

# คำนวณเงินคงเหลือ
remaining = salary - tax

# แสดงผล
print("ภาษี 3% =", tax, "บาท")
print("เงินคงเหลือ =", remaining, "บาท")

