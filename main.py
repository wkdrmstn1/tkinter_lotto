import tkinter
import tkinter.font
import random



def buttonClick():
    lotto_num = random.sample(range(1,46),6)
    lotto_num.sort()
    print(lotto_num)

window = tkinter.Tk()
window.title("lotto")
window.geometry("400x200")
window.resizable(False,False)

button = tkinter.Button(window,overrelief="solid",text ="번호확인",width=15,command=buttonClick,repeatdelay=1000,repeatinterval=100)
button.pack()

window.mainloop()