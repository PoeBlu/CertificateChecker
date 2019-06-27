from tkinter import *

def submit():
    url = a.get()
    gtg = b.get()
    email = c.get()
    path = 'C:/Users/c5290346/Desktop/input.txt'
    file = open(path, 'a')
    url_file = url
    gtg_file = gtg
    email_file = email
    file.writelines(url + ',' + gtg + ',' + email + '\n')
    file.close()
    a.delete(0,30)
    b.delete(0,30)
    c.delete(0,30)

def exit():
    fenster.quit()

fenster = Tk()
fenster.title('Eingabe')
fenster.geometry('280x140')

url_label = Label(fenster, text='URL: ', width='10',height='1')
url_label.place(x=0, y=10)

gtg_label = Label(fenster, text='Tage: ', width='10', height='1')
gtg_label.place(x=0, y=30)

email_label = Label(fenster, text='E-Mail: ', width='10', height='1')
email_label.place(x=0, y=50)

a = Entry(fenster, width='30')
b = Entry(fenster, width='30')
c = Entry(fenster, width='30')

a.place(x=80, y=10)
b.place(x=80, y=30)
c.place(x=80, y=50)

button = Button(fenster,width=10, text='Bestätigen', command=submit)
exit_button = Button(fenster,width=10, text='Schließen', command=exit)
button.place(x=100, y=80)
exit_button.place(x=100, y=110)


fenster.mainloop()