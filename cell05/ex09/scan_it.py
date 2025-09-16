import sys  
import re   # สำหรับใช้งานการค้นหาข้อความแบบ pattern

def main():
    if len(sys.argv) < 3:
        print("none")  
        return  # ออกจากฟังก์ชัน

    keyword = sys.argv[1]  # คำที่จะหา
    text = sys.argv[2]     # ข้อความที่ใช้หา

    # ใช้ re.findall() เพื่อค้นหาคำ 
    # re.escape() ใช้ป้องกันอักขระพิเศษในข้อความ
    matches = re.findall(re.escape(keyword), text)

    if matches:              # ถ้ามี match อย่างน้อย 1 ตัว
        print(len(matches))  # พิมพ์จำนวนครั้งที่พบ keyword
    else:
        print("none")        # ถ้าไม่พบ keyword เลย ให้พิมพ์ "none"

if __name__ == "__main__":
    main()
