def main():
    message = input("")

    for char in message:
        if char.islower():  
            # ถ้าเป็นตัวอักษรเล็ก >>> แปลงเป็นตัวอักษรใหญ่
            print(char.upper(), end="")
        elif char.isupper():
            # ถ้าเป็นตัวอักษรใหญ่ >>> แปลงเป็นตัวอักษรเล็ก
            print(char.lower(), end="")
        else:
            print(char, end="") # ไม่ใช่ตัวอักษร >>> ไม่เปลี่ยนนะจ๊ะ
    
    print("") # บบรทัดใหม่

main()
