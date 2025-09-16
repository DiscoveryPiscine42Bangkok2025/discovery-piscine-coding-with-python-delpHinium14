import sys
def main():
    # เช็คว่ามี argument ที่ส่งมาตอนรันโปรแกรมหรือไม่ (ต้องมี 1 argument พอดี) ถ้าไม่ใช่ → จบการทำงาน
    if len(sys.argv) != 2:
        print("none")
        return   

    param = sys.argv[1] # เก็บค่าพารามิเตอร์

    user_input = input("What was the parameter? ")     # ขอให้ผู้ใช้พิมพ์สิ่งที่คิดว่าเป็น parameter

    if user_input == param:
        print("Good job!")          # ถ้าตรง
    else:
        print("Nope, sorry...")     # ถ้าไม่ตรง

if __name__ == "__main__":
    main()
