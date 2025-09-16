
def find_the_redheads(family):
    redheads = filter(lambda name: family[name] == "red", family) # กรองหาคนผมแดง
    return list(redheads)                                         # แปลงผลลัพธ์เป็น list 

if __name__ == "__main__":
    # กำหนด dictionary ของสมาชิกในครอบครัวและสีผม
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_redheads(dupont_family))  
