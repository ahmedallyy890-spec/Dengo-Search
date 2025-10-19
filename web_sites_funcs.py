import webbrowser
import urllib.parse

def open_youtube(query):
    if query == "":
        webbrowser.open("https://www.youtube.com")

    else:
        webbrowser.open(f"https://www.youtube.com/results/search?q={urllib.parse.quote_plus(query)}")

    
    
def open_tiktok(query):
    if query == "":
        webbrowser.open("https://www.tiktok.com")

    else:
        webbrowser.open(f"https://www.tiktok.com/search?q={urllib.parse.quote_plus(query)}")



def open_chatgpt(query):
        if query == "":
            webbrowser.open("https://chat.openai.com")

        else:
            webbrowser.open(f"https://chat.openai.com/?q={urllib.parse.quote_plus(query)}")


def open_wiki_ar(query):
        if query == "":
            webbrowser.open("https://ar.wikipedia.org/wiki")

        else:
            webbrowser.open(f"https://ar.wikipedia.org/wiki/Special:Search?search={urllib.parse.quote_plus(query)}")


def open_wiki_en(query):
        if query == "":
            webbrowser.open("https://en.wikipedia.org/wiki")

        else:
            webbrowser.open(f"https://en.wikipedia.org/wiki/Special:Search?search={urllib.parse.quote_plus(query)}")


def open_claude(query):
    webbrowser.open("https://claude.ai/")  


def open_copilot(query):
    webbrowser.open("https://copilot.microsoft.com/")    


def open_gemini(query):
    webbrowser.open("https://gemini.google.com/app")


def open_replit(query):
    webbrowser.open("https://replit.com/~")


def open_programiz(query):
    webbrowser.open("https://www.programiz.com/python-programming/online-compiler/")


def open_github(query):
    webbrowser.open("https://github.com/")


def open_facebook(query):
    webbrowser.open("https://www.facebook.com/")


def open_discord(query):
    webbrowser.open("https://discord.com/")


def open_X(query):
    webbrowser.open("https://x.com/")


def open_instagram(query):
    webbrowser.open("https://www.instagram.com/")


def open_snapchat(query):
    webbrowser.open("https://www.snapchat.com/")


def open_reddit(query):
    webbrowser.open("https://www.reddit.com")


def open_translate(query):
    webbrowser.open("https://translate.google.com")


def open_weather_App(query):
    webbrowser.open("https://weather.com")

def open_classroom(query):
    webbrowser.open("https://classroom.google.com/")


def open_roblox_ar(query):
    webbrowser.open("https://www.roblox.com/ar/home")

def open_roblox_en(query):
    webbrowser.open("https://www.roblox.com/en/home")

def open_Yallakora(query):
    webbrowser.open("https://www.yallakora.com/")
        
def open_kick(query):
    webbrowser.open("https://kick.com/")

def open_manus(query):
    webbrowser.open("https://manus.im/")

def open_twitch(query):
    webbrowser.open("https://www.twitch.tv/")

def open_iSchool(query):
    webbrowser.open("https://www.ischooltech.com/eg/home-ar")

def open_islam_web(query):
    webbrowser.open("https://islamweb.net/ar/")