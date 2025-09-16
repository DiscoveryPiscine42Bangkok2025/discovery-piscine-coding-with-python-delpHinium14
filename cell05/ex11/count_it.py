import sys  

def main():
    params = sys.argv[1:]  # เก็บทุก argument แต่ไม่เอาชื่อไฟล์!!!!!!

    if not params:  # ถ้าไม่มี argument ถูกส่งมา
        print("none")  
        return  # ออกจากฟังก์ชัน

    # ถ้ามี argument อย่างน้อย 1 ตัว ให้พิมพ์จำนวน argument
    print(f"parameters: {len(params)}")

    # วนลูปพิมพ์แต่ละ argument พร้อมกับความยาวของมัน
    for p in params:
        print(f"{p}: {len(p)}") 

if __name__ == "__main__":
    main()
