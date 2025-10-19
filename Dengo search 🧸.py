#__استدعاء المكتبات__
import tkinter as tk
import webbrowser
import random as r
#__استدعاء ملفات المشروع__
import check_internet as check
import news_file 
import voice_search as voice
import errors_file as errors
import web_sites_dict as sites_dict
import web_sites_funcs as funcs




stop_words = ["chat", "gpt", "tik", "tok", "wiki", "wikipedia", "youtube", 
            "يوتيوب", "تيك", "توك", "شات", "جي", "بي", "تي", "ويكيبيديا", "video", "فيديو", "yalla", "kora", "يلا", "كورة", "كوره", "كورا"]
root = tk.Tk()

def clear_search(event=None):
    search_input.delete(0, tk.END)


#__البحث الصوتي__
def voice_search():
    # استدعاء دالة التعرف على الصوت
    user_query = voice.get_voice_input()

    if user_query:
        # لو تم التعرف على الكلام، ابدأ عملية البحث
        search_input.delete(0, tk.END) # امسح أي كلام قديم
        search_input.insert(0, user_query) # ضيف الكلام الجديد في مربع البحث
        Main()  
        
#__الداله الاساسيه للبرنامج__
def Main():
    
    user_query = search_input.get().strip().lower()
    if not check.is_connected(): #اذا لم يتحقق شرط اتصال الانترنت
        errors.internet_error_message() #عرض نافذه الخطا
        return #لكي لا يتم فتح الصفحه
        
    filtered_words = [word for word in user_query.split() if word.lower() not in stop_words] #لتصفية البحث من الكلمات الغير مرغوب فيها
    final_query = " ".join(filtered_words)
    if user_query == "":
        
        errors.get_empty_input()
    
    else:

        try:

            for key, func in sites_dict.sites.items():
                if key in user_query:
                    func(final_query)
                    return

                elif user_query in ["x", "اكس"]:
                    funcs.open_X(final_query)
                    return

            webbrowser.open("https://www.google.com/search?q=" + user_query)
            
        except webbrowser.Error:

            errors.web_browser_error()

        except Exception as e:
        
            errors.get_error(e)


title = tk.Label(root, text="Dengo search | دينجو سيرش 🧸\n", font=("Arial", 19, "bold"),fg="#FDFEFE", bg="#020632", wraplength=350, justify="center")
title.pack(side="top")


search_input = tk.Entry(root, font=("Arial", 20, "bold"), justify="center", bg="#EFF7FF")
search_input.pack()

btn = tk.Button(root, text="بحث", command=Main, width=10, height=1, bg="#3A74D9", fg="#FAF9F8") 
btn.pack(pady=5)

search_input.bind("<Return>", lambda event: Main())


root.bind("<Escape>", clear_search)

root.bind("<Control-space>", lambda event: voice_search())
def update_them(event=None):
    root.is_dark = not root.is_dark
    if root.is_dark:
        root.configure(bg="#FDFDFF")
        title.config(bg="#FDFDFF", fg="#070024")
        news_show.config(bg="#FDFDFF", fg="#070024")
        search_input.config(bg="#CED1EE")
    else:
        root.configure(bg="#020632")
        title.config(fg="#FDFEFE", bg="#020632")
        news_show.config(fg="#678AB0", bg="#020632")
        search_input.config(bg="#eeeeee")

root.bind("<Control-u>", update_them)
root.bind("<Control-U>", update_them)
root.bind("<Control-F7>", update_them)
news_choose = r.choice(news_file.news)
news_show = tk.Label(root, text=news_choose, font=("Arial", 20, "bold"),fg="#678AB0", bg="#020632", justify="center", wraplength=350, anchor="e")
news_show.pack(pady=90, anchor="center")
root.is_dark = True 

def update_news():
    new_text = r.choice(news_file.news)
    news_show.config(text=new_text)
    root.after(30000, update_news)  

update_news()

root.iconbitmap("pngtree-teddy-bear-brown-sitting-with-yellow-scarf-png-image_4538773.ico")
root.configure(bg="#020632")


root.geometry("700x600")
root.title("Dengo search")

root.mainloop()