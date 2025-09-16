def famous_births(figures):
    # sorted() เรียงค่าตามปีเกิดที่แปลงเป็น int
    sorted_people = sorted(figures.values(), key=lambda x: int(x["date_of_birth"])) 

    # วนลูปพิมพ์แต่ละคน
    for person in sorted_people:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

if __name__ == "__main__":
    women_scientists = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
        "cecilia": {"name": "Cecilia Payne", "date_of_birth": "1900"},
        "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
        "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
    }

    famous_births(women_scientists)
