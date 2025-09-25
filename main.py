import tkinter
import tkinter.font
import random

def buttonClick():
    lotto_num = random.sample(range(1,46),6) # 1~45 사이의 랜덤 숫자 6개 
    lotto_num.sort() # 정렬
    print(lotto_num)

window = tkinter.Tk()  # 변수 지정(화면 설정)
window.title("lotto")  # 제목 설정 
window.geometry("400x200") # 크기 설정
window.resizable(False,False) # 크기 고정 

# 버튼 설정
button = tkinter.Button(window,overrelief="solid",text ="번호확인",width=15,command=buttonClick,repeatdelay=1000,repeatinterval=100)
button.pack() # 버튼 - 창에 포함하기

window.mainloop() # 실행상태 유지(무한)