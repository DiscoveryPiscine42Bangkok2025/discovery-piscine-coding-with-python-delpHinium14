import sys 

# ฟังก์ชันตัด string ให้เหลือ 8 ตัวอักษรแรก
def shrink(s):
    return s[:8]

# เติม Z ให้ string ยาว 8 ตัว
def enlarge(s):
    return s + "Z" * (8 - len(s))  

if __name__ == "__main__":
    # ตรวจสอบว่ามี arguments ที่ส่งมาหรือไม่
    if len(sys.argv) < 2:
        print("none")  # ไม่มี argument ให้พิมพ์ "none"
    else:
        for arg in sys.argv[1:]:
            if len(arg) > 8:         # ถ้ามากกว่า 8 ตัว
                print(shrink(arg))   # ตัดเหลือ 8 ตัว
            elif len(arg) < 8:       # ถ้าน้อยกว่า 8 ตัว
                print(enlarge(arg))  # เติม Z จนครบ 8 ตัว
            else:                    # ถ้าเท่ากับ 8 ตัว
                print(arg)           # ไม่ต้องเปลี่ยนอะไร
