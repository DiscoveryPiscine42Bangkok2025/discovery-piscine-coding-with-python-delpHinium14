import sys  

def main():
    # ตรวจสอบว่ามีการส่ง arguments มาทั้งหมด 2 ตัว
    if len(sys.argv) == 2:
        # แปลงเป็นตัวพิมพ์เล็ก
        print(sys.argv[1].lower())
    else:
        print("none")

# ส่วนนี้จะทำงานก็ต่อเมื่อรันไฟล์นี้โดยตรง (ไม่ใช่ import จากไฟล์อื่น)
if __name__ == "__main__":
    main()
