from tkinter import *

def calculator():

    while True:
        try:
          result1 = int(my_entry.get())
          result2 = float(my_entry2.get())
          output=result1/(result2*result2)
          if output<18.5:
              my_label3.config(text=f"vücut kitle endeksiniz: {output} zayıfsınız")
          elif 18.5<output<24.5:
              my_label3.config(text=f"vücut kitle endeksiniz: {output} kilonuz normal")
          elif  output>24.5:
              my_label3.config(text=f"vücut kitle endeksiniz: {output} kilonuz yüksek")

          break
        except:
            my_label3.config(text="hatalı giriş yaptınız")
            break


window = Tk()
window.title("vücut kitle endeksi")
window.minsize(width=300,height=400)
window.config(padx=20,pady=40)

my_label=Label(text="Kilonuzu giriniz(kg) ")
my_label.config(width=14,height=2)
my_label.pack()

my_entry=Entry()
my_entry.pack()

my_label2=Label(text="Boyunuzu giriniz(m) ")
my_label2.config(width=15,height=2)
my_label2.pack()

my_entry2=Entry()
my_entry2.pack()

my_button=Button(text="Hesapla",command=calculator)
my_button.config(bg="black",fg="white")
my_button.pack()

my_label3=Label()
my_label3.pack()


mainloop()

