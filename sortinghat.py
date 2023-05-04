#1~3までのQUESTIONとANSWERの繰り返しで表示
#リスト作成
import tkinter
QUES = [
    'Do you like Dawn or Dusk?',
    'When I\'m dead, I want people to rememver me as:',
    'Which kind of instrument most pleases your ear?'
]
ANS = [
    ['Dawn', 'Dusk'],
    ['The Good', 'The Great', 'The Wise', 'The Bold'],
    ['The violin', 'The trumpet', 'The piano', 'The drum']
]
txt = 'Enter your answer\'s number: '
res = []
#質問と答えをそれぞれ表示
for i in range(len(QUES)):
    print('Q'+str(i+1)+') '+QUES[i])
    print()
    lis = ANS[i]
    for j in range(len(lis)):
        print('    '+str(j+1)+') '+lis[j])
    print()
    res.append(input(txt)) #インプットエリア表示しただけだと保存されないからリストに格納
    print()
#No.スコア計算。判定。
#print(res)
house = {"g":0, "r":0, "h":0, "s":0}

if res[0] == "1" or res[0] == "１":
    house["g"] += 1
    house["r"] += 1
elif res[0] == "2" or res[0] == "２":
    house["h"] += 1
    house["s"] += 1
else:
    print("Q1 Please enter 1 or 2.")
    
if res[1] == "1" or res[1] == "１":
    house["h"] += 2
elif res[1] == "2" or res[1] == "２":
    house["s"] += 2
elif res[1] == "3" or res[1] =="３":
    house["r"] += 2
elif res[1] == "4" or res[1] =="４":
    house["g"] += 2
else:
    print("Q2 Please enter 1 〜 4.")

if res[2] == "1" or res[2] == "１":
    house["s"] += 2
elif res[2] == "2" or res[2] == "２":
    house["h"] += 2
elif res[2] == "3" or res[2] == "３":
    house["r"] += 2
elif res[2] == "4" or res[2] == "４":
    house["g"] += 2
else:
    print("Q3 Please enter 1 〜 4.")
#print(house)
# valueのマックスを取得
max_k = max(house, key=house.get)
#print(max_k)

#どの寮かウィンドウで表示される
root = tkinter.Tk()
root.title("Your HOUSE is ...")
canvas = tkinter.Canvas(width=1500, height=700, bg="white")

img = tkinter.PhotoImage(file=max_k + ".png")  #file = " ~ "でないのは文字列ではないため。

canvas.create_image(750, 350, image=img) #キャンバスの真ん中を指定
canvas.pack()
root.mainloop()