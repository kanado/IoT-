import LINE
import serial
# シリアルポートへの接続
ser = serial.Serial('/dev/ttyACM0', 115200)

old = None

while True:
    # シリアル通信で1行読み込む
    line = ser.readline()
    # 余分な空白や改行を除き、バイト列を文字列に変換する
    temp = line.strip().decode()
    if temp != old:
        # if temp == "KAN":
        #    print("缶を検知しました")
        #    LINE.line("缶を検知しました")

        # elif temp == "PET":
        #    print("ペットボトルを検知しました")
        #    LINE.line("ペットボトルを検知しました")

        if temp == "KANFull":
            print("缶がいっぱいになります")
            LINE.line("缶がいっぱいになりそうです")

        elif temp == "PETFull":
            print("ペットボトルがいっぱいになります")
            LINE.line("ペットボトルがいっぱいになりそうです")

        elif temp == "KANReset":
            print("缶が清掃されました")
            LINE.line("缶が清掃されました")

        elif temp == "PETReset":
            print("ペットボトルが清掃されました")
            LINE.line("ペットボトルが清掃されました")

        else:
            print("不明")
    temp = None
