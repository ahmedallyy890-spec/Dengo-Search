import speech_recognition as sr
from tkinter import messagebox

def get_voice_input():
    # إنشاء كائن للتعرف على الصوت
    voice = sr.Recognizer()
    
    # استخدام الميكروفون كمصدر للصوت
    with sr.Microphone() as source:
    
        messagebox.showinfo("info", "تكلم الآن...")

        try:
            # ضبط حساسية الضوضاء المحيطة
            voice.adjust_for_ambient_noise(source, duration=1)
            # الاستماع للصوت
            audio = voice.listen(source)
            messagebox.showinfo("info", "جاري التعرف على الصوت...")
            
            # استخدام محرك جوجل للتعرف على الصوت (ممكن تغيره لو محتاج)
            query = voice.recognize_google(audio, language="ar-EG") # ar-EG للغة العربية
            messagebox.showinfo("info", f"أنت قلت: {query}")

            return query
        
        except sr.UnknownValueError:
            try: 
                voice.adjust_for_ambient_noise(source, duration=1)
            # الاستماع للصوت
                audio = voice.listen(source)
                messagebox.showinfo("info", "جاري التعرف على الصوت...")


                query = voice.recognize_google(audio, language="en-USA") # للغة الانجليزية en-USA
                messagebox.showinfo("info", f"أنت قلت: {query}")

                return query
            
            except sr.UnknownValueError:
                messagebox.showerror("Error", "عذراً، لم أستطع فهم ما قلته.")
                return ""
        
        except sr.RequestError:
            messagebox.showerror("Error", "عذراً، الخدمة غير متاحة الآن.")
            return ""
            