def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    new_array = [x + 2 for x in original_array if x > 5] # +2 ให้ตัวที่มากกว่า 5

    # ลบค่าที่ซ้ำกันออก โดยใช้ dict.fromkeys() (ลำดับเดิมด้วย)
    unique_new_array = list(dict.fromkeys(new_array))

    print(original_array)
    print(unique_new_array)


# ถ้าไฟล์นี้ถูกรันโดยตรง (ไม่ใช่ถูก import) → เรียก main()
if __name__ == "__main__":
    main()
