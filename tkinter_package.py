from tkinter import *
import tkinter as tk


window=tk.Tk()
window.title("اتوماسیون ارسال پیامک نظرسنجی")


window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)

i = IntVar()
# .... for current date.....
entryCurrentDate = tk.Entry(window )
entryCurrentDate .grid(row=0, column=1)


label1 = tk.Label(window, text="تاریخ جاری")
label1.grid(row=0, column=2)
#... for choosing if granty is required or win ...
v = IntVar()
Radiobutton(window, text="اطلاعات مربوط به ارسال پیامک گارانتی", variable=v, value=1).grid(row=1, column=0)
Radiobutton(window, text="اطلاعات مربوط به ارسال پیامک نظر سنجی", variable=v, value=2).grid(row=1, column=1)

#...for having he choice of entering date manually...
i = IntVar()
checkBoxManualDate = Checkbutton(window, text="تاریخ به صورت دستی وارد شود", variable=i)
checkBoxManualDate.grid(row=2, column=1)

# ...for entering desired date by user .....

# entryManualDate = tk.Entry(window )
# entryManualDate .grid(row=3, column=0)

Manual_day = tk.Label(window, text="روز")
Manual_day.grid( row=3, column=2)
DayNum=Listbox(window, width=10, height=6)
DayNum.insert(1, "1")
DayNum.insert(2, "2")
DayNum.insert(3, "3")
DayNum.insert(4, "4")
DayNum.insert(5, "5")
DayNum.insert(6, "6")
DayNum.insert(7, "7")
DayNum.insert(8, "8")
DayNum.insert(9, "9")
DayNum.insert(10, "10")
DayNum.insert(11, "11")
DayNum.insert(12, "12")
DayNum.insert(13, "13")
DayNum.insert(14, "14")
DayNum.insert(15, "15")
DayNum.insert(16, "16")
DayNum.insert(17, "17")
DayNum.insert(18, "18")
DayNum.insert(19, "19")
DayNum.insert(20, "6")
DayNum.insert(21, "21")
DayNum.insert(22, "22")
DayNum.insert(23, "23")
DayNum.insert(24, "24")
DayNum.insert(25, "25")
DayNum.insert(26, "26")
DayNum.insert(27, "27")
DayNum.insert(28, "28")
DayNum.insert(29, "29")
DayNum.insert(30, "30")
DayNum.insert(31, "31")
DayNum.grid(row=4, column=2)

Manual_mounth = tk.Label(text="ماه")
Manual_mounth.grid(row=3, column=1)
mounthNum=Listbox()
mounthNum.insert(1, "فروردین")
mounthNum.insert(2, "اردیبهشت")
mounthNum.insert(3, "خرداد")
mounthNum.insert(4, "تیر")
mounthNum.insert(5, "مرداد")
mounthNum.insert(6, "شهریور")
mounthNum.insert(7, "مهر")
mounthNum.insert(8, "آبان")
mounthNum.insert(9, "آذر")
mounthNum.insert(10, "دی")
mounthNum.insert(11, "بهمن")
mounthNum.insert(12, "اسفند")
mounthNum.grid(row=4, column=1)

Manual_year = tk.Label(text="سال")
Manual_year.grid(row=3, column=0)
YearNum=Listbox()
YearNum.insert(1, "1399")
YearNum.insert(2, "1400")
YearNum.insert(3, "1401")
YearNum.insert(4, "1402")
YearNum.insert(5, "1403")
YearNum.grid(row=4, column=0)




b = Button(window, text="ایجاد فایل" )
b.grid(row=5, column=1)


window.mainloop()
