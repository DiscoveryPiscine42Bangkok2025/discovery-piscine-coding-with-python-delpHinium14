def average(class_scores):
    if not class_scores:  # ถ้า dictionary ว่าง
        return 0         
    
    total = sum(class_scores.values())   # ผลรวมคะแนนทั้งหมด
    count = len(class_scores)            # จำนวนสมาชิก
    return total / count                 # หาค่าเฉลี่ย

if __name__ == "__main__":
    # กำหนด dictionary คะแนนของนักเรียนแต่ละชั้น
    class_3B = {
        "marc": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }

    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephane": 13
    }

    print(f"Average for class 3B: {average(class_3B)}.")  
    print(f"Average for class 3C: {average(class_3C)}.")  
