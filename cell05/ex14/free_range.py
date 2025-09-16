import sys 

def main():

    if len(sys.argv) != 3:
        print("none")  
        return  

    try:
        start = int(sys.argv[1])  # แปลง argument ตัวแรกเป็นจำนวนเต็ม
        end = int(sys.argv[2])    # แปลง argument ตัวที่สองเป็นจำนวนเต็ม 

        numbers = list(range(start, end + 1))  # สร้าง list ตั้งแต่ start ถึง end รวม end ด้วย เลยต้องบวก 1

        print(numbers)  

    except ValueError:  
        print("none")  

if __name__ == "__main__":
    main()
