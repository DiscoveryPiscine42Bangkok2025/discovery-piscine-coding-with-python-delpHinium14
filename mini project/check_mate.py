def checkmate(board):
    n = len(board)

    #  เช็คคิงก่อน
    king_pos = None   # ตำแหน่งคิง
    king_count = 0    # นับจำนวนคิง ตอนแรกมี 0
    for i in range(n):               # วนหาแต่ละแถว
        for j in range(n):           # จากนั้นหาแต่ละคอลัมน์
            if board[i][j] == 'K':   # ถ้าเจอคิง
                king_pos = (i, j)    # เก็บตำแหน่งคิงไว้ (row=i, col=j)
                king_count += 1      # เพิ่มจำนวนคิง ตอนนี้มี 1

    # ถ้าไม่เจอคิงหรือเจอมากกว่า 1 ตัว ป้องกัน error
    if king_count != 1:
        print("Error")
        return

    # แยกตำแหน่งคิงออกมา r=row c=column
    kr, kc = king_pos   

    # เบี้ย
    for pr, pc in [(kr + 1, kc - 1), (kr + 1, kc + 1)]:            # ล่างซ้าย ล่างขวา
        if 0 <= pr < n and 0 <= pc < n and board[pr][pc] == 'P':   # ต้องอยู่ในขอบเขตบอร์ด และเจอ P
            print("Success")   # รุกฆาต!!!
            return

    # เรือ และ ควีน ในแนวตรง ขึ้น ลง ซ้าย ขวา
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]: # พิกัด ขึ้น ลง ซ้าย ขวา
        r, c = kr+dr, kc+dc                    # เริ่มจากตำแหน่งถัดไป
        while 0 <= r < n and 0 <= c < n:       # วนไปจนสุดกระดาน
            piece = board[r][c]
            if piece == '.':                   # ช่องว่าง >>> ไปต่อ
                r += dr; c += dc 
                continue
            if piece in ['R','Q']:             # เจอ เรือ หรือ ควีน >>> โจมตีได้
                print("Success")
                return
            break                              # เจอชิ้นอื่นที่ไม่ใช่เป้าหมาย >>> หยุด

    # บิชอป และ ควีน แนวทแยง
    for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
        r, c = kr+dr, kc+dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]
            if piece == '.':                   # ช่องว่าง >>> ไปต่อ
                r += dr; c += dc
                continue
            if piece in ['B','Q']:             # เจอ Bishop หรือ Queen >>> โจมตีได้
                print("Success")
                return
            break                              # เจอชิ้นอื่น >>> หยุด
    print("Fail")

# บอร์ด 4x4
board4 = [
    "R...",   
    ".K..",   
    "..P.",   
    "...."
]

print("Board 4x4:")
checkmate(board4)  


# บอร์ด 8x8 
board8 = [
    "........",   
    "........",
    "........",   
    "........",
    "....K...",   
    "....P...",
    "...Q....",   
    "........"
]

print("Board 8x8:")
checkmate(board8)   

# success รุกฆาต
# fail คิงรอดจ้า
# วนตำแหน่งคิงว่าจะเจอตัวรุกฆา