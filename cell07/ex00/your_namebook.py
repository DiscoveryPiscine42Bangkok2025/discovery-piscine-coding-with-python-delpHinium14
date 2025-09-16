def array_of_names(persons):
    full_names = [] # สร้างลิสต์

    for first, last in persons.items():
        full_name = f"{first.capitalize()} {last.capitalize()}" # ชื่อ-นาทสกุล ขึ้นต้นตัวใหญ่
        full_names.append(full_name) # เพิ่มลงลิสต์
    return full_names


if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }

    print(array_of_names(persons))