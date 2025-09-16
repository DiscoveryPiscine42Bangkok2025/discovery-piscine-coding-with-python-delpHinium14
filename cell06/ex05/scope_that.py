
def add_one(n):
    n = n + 1  
    return n   

if __name__ == "__main__":
    x = 5                                # กำหนด x = 5
    print("Before calling add_one:", x)  # แสดงค่า x 

    x = add_one(x)                       # เรียก add_one และผลกลับไปที่ x
    print("After calling add_one:", x)   # แสดงค่า x หลังเรียกฟังก์ชัน


