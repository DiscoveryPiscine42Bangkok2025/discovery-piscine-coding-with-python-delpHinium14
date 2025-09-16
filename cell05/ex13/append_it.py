import sys

def main():
    params = sys.argv[1:]       # เก็บทุก argument ยกเว้นชื่อไฟล์ อย่า อย่า อย่า

    if not params:              # ถ้าไม่มี argument ถูกส่งมา
        print("none")  
        return  

    displayed = False           # ตัวแปรเพื่อตรวจสอบว่ามีการพิมพ์คำใด ๆ หรือไม่
    for word in params:
        if not word.endswith("ism"):  # ถ้าคำไม่ลงท้ายด้วย "ism"
            print(word + "ism")       # เติม "ism" ต่อท้ายและพิมพ์ออกมา
            displayed = True          # กำหนดว่าได้พิมพ์คำแล้ว

    if not displayed:                 # ถ้าไม่มีคำใดถูกพิมพ์ (ทุกคำลงท้ายด้วย "ism" หมด)
        print("none")  

if __name__ == "__main__":
    main()
