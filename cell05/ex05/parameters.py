import sys   # ใช้ sys.argv เพื่ออ่าน arguments ที่ส่งมาตอนรันโปรแกรม

def main():
    # ถ้ามี argument ที่ส่งเข้ามามากกว่า 1 ตัว เพราะ sys.argv[0] คือชื่อไฟล์ ตัวนี้ไม่เอานะจ๊ะ
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

# ถ้าไฟล์นี้ถูกรันโดยตรง → เรียก main()
if __name__ == "__main__":
    main()
