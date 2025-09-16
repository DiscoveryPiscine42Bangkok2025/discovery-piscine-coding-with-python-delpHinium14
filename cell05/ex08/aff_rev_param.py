import sys  

def main():
    # ตรวจสอบว่าจำนวน arguments ที่ส่งมาน้อยกว่า 3 ตัวหรือไม่
    if len(sys.argv) < 3:
        print("none")
    else:
        # ถ้า arguments มีอย่างน้อย 2 ตัว ให้วนลูปพิมพ์แต่ละ argument แบบย้อนกลับ
        for param in reversed(sys.argv[1:]):  
            print(param)  

if __name__ == "__main__":
    main()
