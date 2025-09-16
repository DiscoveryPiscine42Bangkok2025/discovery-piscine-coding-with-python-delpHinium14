import sys   # ใช้ sys.argv เพื่อดึง arguments ที่ส่งมาตอนรันโปรแกรม

def main():
    # เช็คว่ามี argument ถูกส่งมา "แค่ 1 ตัว" เท่านั้น (ไม่รวมชื่อไฟล์)
    if len(sys.argv) == 2:
        # แสดง argument ตัวนั้น โดยแปลงเป็น "ตัวพิมพ์ใหญ่ทั้งหมด"
        print(sys.argv[1].upper())
    else:
        # ถ้าไม่มี argument หรือมีมากกว่า 1 ตัว >>> แสดง "none"
        print("none")

# ถ้าไฟล์นี้ถูกรันโดยตรง → เรียก main()
if __name__ == "__main__":
    main()
