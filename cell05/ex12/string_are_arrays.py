import sys  

def main():
    # ตรวจสอบว่ามี arguments ที่ส่งเข้ามาไม่เท่ากับ 2 ตัวหรือไม่
    if len(sys.argv) != 2:
        print("none")  
        return  

    text = sys.argv[1]  # เก็บข้อความ

    # ใช้ list comprehension เพื่อกรองเฉพาะตัวอักษร 'z' จากข้อความ
    # ''.join(...) ใช้รวม list ของตัวอักษรกลับเป็น string
    result = ''.join([c for c in text if c == 'z'])

    if result:                 # ถ้ามีตัวอักษร 'z' อย่างน้อย 1 ตัว
        print(result.lower())  # พิมพ์ตัวอักษรทั้งหมดเป็นตัวพิมพ์เล็ก
    else:
        print("none")  

if __name__ == "__main__":
    main()
