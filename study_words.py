import tkinter

FNT1 = ("Times New Roman", 12)
FNT2 = ("Times New Roman", 24)

WORDS = [
    "apple", "苹果",
    "book", "书",
    "cat", "猫",
    "dog", "狗",
    "egg", "鸡蛋",
    "fire", "火",
    "gold", "金",
    "head", "头",
    "ice", "冰",
    "juice", "果汁",
    "king", "王",
    "lemon", "柠檬",
    "mother", "妈妈",
    "notebook", "笔记本",
    "orange", "橘子",
    "pen", "笔",
    "queen", "女王",
    "room", "房间",
    "sport", "运动",
    "time", "时间",
    "user", "使用者",
    "vet", "兽医",
    "window", "窗户",
    "xanadu", "世外桃源",
    "yellow", "黄色",
    "zoo", "动物园"
]
MAX = int(len(WORDS) / 2)
score = 0
word_num = 0
yourword = ""
koff = False  # 1 문자씩 입력하기 위한 플래그

def key_down(e):
    global score, word_num, yourword, koff
    if koff == True:
        koff = False
        kcode = e.keycode
        ksym = e.keysym
        if 65 <= kcode and kcode <= 90:  # 영문자 대문자
            yourword = yourword + chr(kcode + 32)
        if 97 <= kcode and kcode <= 122:  # 영문자 소문자
            yourword = yourword[:-1]  # 맨 끝 1 문자 삭제
        if ksym == "Delete" or ksym == "BackSpace":
            yourword = yourword[:-1]  # 맨 끝 한 문자 삭제
        input_label["text"] = yourword
        if ksym == "Return":
            if input_label["text"] == english_label["text"]:
                score = score + 1
                set_label()

def key_up(e):
    global koff
    koff = True

def set_label():
    global word_num, yourword
    score_label["text"] = score
    english_label["text"] = WORDS[word_num * 2]
    korean_label["text"] = WORDS[word_num * 2 + 1]
    input_label["text"] = ""
    word_num = (word_num + 1) % MAX
    yourword = ""

root = tkinter.Tk()
root.title("영어 학습 애플리케이션")
root.geometry("400x200")
root.resizable(False, False)
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
root["bg"] = "#DEF"

score_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#4C0")
score_label.pack()
english_label = tkinter.Label(font=FNT2, bg="#DEF")
english_label.pack()
korean_label = tkinter.Label(font=FNT1, bg="#DEF", fg="#444")
korean_label.pack()
input_label = tkinter.Label(font=FNT2, bg="#DEF")
input_label.pack()
howto_label = tkinter.Label(text="영어 단어를 입력하고 [Enter] 키를 누릅니다.\n입력을 수정할 때는 [Delete] 혹은 [BackSpace]", font=FNT1, bg="#FFF", fg="#ABC")
howto_label.pack()

set_label()
root.mainloop()