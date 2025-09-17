from checkmate import checkmate

def main():
    # บอร์ดตัวอย่าง 4x4 
    board4 = """\
R...
.K..
....
...."""
    print("Board 4x4:")
    checkmate(board4.splitlines()) # แปลงเป็น list ของบรรทัด (list ของ string)

    # บอร์ด 8x8 
    board8 = """\
R.......
........
........
........
...K....
........
...Q....
........"""
    print("Board 8x8:")
    checkmate(board8.splitlines())

if __name__ == "__main__":
    main()

# success รุกฆาต
# fail คิงรอดจ้า