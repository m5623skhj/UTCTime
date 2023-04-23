from datetime import datetime, timedelta
import msvcrt

UTC_Minus5 = datetime.now()
UTC_0 = datetime.now()
UTC_Plus1 = datetime.now()
UTC_Plus8 = datetime.now()
UTC_Plus9 = datetime.now()

def CalcTime(delta : timedelta):
    global UTC_Minus5, UTC_0, UTC_Plus1, UTC_Plus8, UTC_Plus9
    UTC_Minus5 += delta
    UTC_0 += delta
    UTC_Plus1 += delta
    UTC_Plus8 += delta
    UTC_Plus9 += delta
    
def main():
    print("UTC-5 : 1 / UTC+0 : 2 / UTC+1 : 3 / UTC+8 : 4 / UTC+9 : 5")
    timezoneString = input()
    timezone = int(timezoneString);
    
    if timezone > 5 or timezone < 1:
        print("사용자 입력 오류")
        return
    
    print("시간 입력")
    print("ex : 2023-01-01 00:00:00")
    inputTimeString = input()
    inputTime = datetime.strptime(inputTimeString, '%Y-%m-%d %H:%M:%S')
    
    global UTC_Minus5, UTC_0, UTC_Plus1, UTC_Plus8, UTC_Plus9
    UTC_Minus5 = inputTime + timedelta(hours=-5)
    UTC_0 = inputTime
    UTC_Plus1 = inputTime + timedelta(hours=1)
    UTC_Plus8 = inputTime + timedelta(hours=8)
    UTC_Plus9 = inputTime + timedelta(hours=9)
    
    # UTC - 5
    if timezone == 1:
        CalcTime(timedelta(hours=+5))
    # UTC + 0
    elif timezone == 2:
        CalcTime(timedelta(hours=0))
    # UTC + 1
    elif timezone == 3:
        CalcTime(timedelta(hours=-1))
    # UTC + 8
    elif timezone == 4:
        CalcTime(timedelta(hours=-8))
    # UTC + 9
    elif timezone == 5:
        CalcTime(timedelta(hours=-9))
        
    print("\n-------------------------------")
    print("UTC-5 :", UTC_Minus5)
    print("UTC+0 :", UTC_0)
    print("UTC+1 :", UTC_Plus1)
    print("UTC+8 :", UTC_Plus8)
    print("UTC+9 :", UTC_Plus9)
    print("-------------------------------")
    
    print("\n\n아무 키나 입력하면 종료됩니다.")
    msvcrt.getch()
    
    
if __name__ == '__main__':
    main()