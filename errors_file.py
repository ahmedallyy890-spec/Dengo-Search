from tkinter import messagebox
def internet_error_message():
    messagebox.showerror("Error", "انت غير متصل, تحقق من اتصالك بالانترنت وسرعة شبكتك")

def get_empty_input():
    messagebox.showinfo("info", "البحث فارغ تماما, اكتب شيء للبحث عنه")

def web_browser_error():
    messagebox.showerror("Error", "تعذر فتح الصفحة, حاول مرة اخرى او ابحث بصيغة مختلفة")

def get_error(error):
    messagebox.showerror("Error", f"خطا: {error}")