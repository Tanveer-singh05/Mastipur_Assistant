import datetime
import speak
import webbrowser
import weather
import os

def Action(send):
    data_btn = send.lower()

    if "what is your name" in data_btn or "who are you" in data_btn or "tell me about yourself" in data_btn:
        speak.speak("I am your mastipur assistant, I can help you with many things")
        return "I am your mastipur assistant, I can help you with many things"

    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn:
        speak.speak("Hello ji, ki haal chaal ji")  
        return "Hello ji,  ki haal chaal ji"

        

    elif "how are you" in data_btn or "how r u" in data_btn :
            speak.speak("mai Good aa ji, aap kaise ho ji") 
            return "mai changa ji, aap kaise ho ji" 

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("koi chakker nai mittar")
           return "koi chakker nai mittar"      

    elif "good morning" in data_btn:
           speak.speak("good morning pinapple, looking very good very niceeee")
           return "good morning pinapple, looking very good very niceeee"   
    
    elif "good afternoon" in data_btn:
        speak.speak("Good afternoon sir, I think you might need some help")
        return "Good afternoon sir, I think you might need some help"
    
    elif "good evening" in data_btn:
        speak.speak("Good evening sir, I think you might need some help")
        return "Good evening sir, I think you might need some help" 
    
    elif "good night" in data_btn:  
        speak.speak("Good night sir, I think you might need some help")
        return "Good night sir, I think you might need some help"
    
    elif "what is the date" in data_btn or "today's date" in data_btn:
        current_date = datetime.datetime.now()
        Date = f"{current_date.day} {current_date.strftime('%B')} {current_date.year}"
        speak.speak(Date)
        return Date
    


    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        speak.speak(Time)
        return Time

    elif "shutdown" in data_btn or "quit" in data_btn:
        speak.speak("ok sir")
        return "ok sir"

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        speak.speak("gaana.com is now ready for you, enjoy your music")
        return "gaana.com is now ready for you, enjoy your music"

    elif 'open google' in data_btn or 'google' in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open")
        return "YouTube open"

    elif 'weather' in data_btn or "open weather" in data_btn:
        ans = weather.Weather()
        speak.speak(ans)
        return ans

    elif 'music from my laptop' in data_btn or "open song" in data_btn:
        url = 'D:\\music'
        try:
            songs = os.listdir(url)
            if songs:
                os.startfile(os.path.join(url, songs[0]))
                speak.speak("songs playing...")
                return "songs playing..."
            else:
                speak.speak("No songs found in the folder.")
                return "No songs found in the folder."
        except Exception as e:
            speak.speak("Unable to play music from your laptop.")
            return "Unable to play music from your laptop."

    elif 'open steam' in data_btn or 'steam' in data_btn or 'start steam' in data_btn :
        steam_path = r"C:\Program Files (x86)\Steam\Steam.exe"  
        try:
            os.startfile(steam_path)
            speak.speak("Steam app is opening")
            return "Steam app is opening"
        except Exception as e:
            speak.speak("Unable to open Steam app. Please check the installation path.")
            return "Unable to open Steam app. Please check the installation path."

    elif 'open chrome' in data_btn or 'chrome' in data_btn or 'start chrome' in data_btn :
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  
        try:
            os.startfile(chrome_path)
            speak.speak("Chrome browser is opening")
            return "Chrome browser is opening"
        except Exception as e:
            speak.speak("Unable to open Chrome browser. Please check the installation path.")
            return "Unable to open Chrome browser. Please check the installation path."
    


    elif 'open whatsapp' in data_btn or 'whatsapp' in data_btn or 'start whatsapp' in data_btn:
        url = 'https://web.whatsapp.com/'
        webbrowser.get().open(url)
        speak.speak("whatsapp open")
        return "whatsapp open"

    elif 'open facebook' in data_btn or 'facebook' in data_btn or 'start facebook' in data_btn:
        url = 'https://www.facebook.com/'
        webbrowser.get().open(url)
        speak.speak("facebook open")
        return "facebook open"

    elif 'open instagram' in data_btn or 'instagram' in data_btn or 'start instagram' in data_btn:
        url = 'https://www.instagram.com/'
        webbrowser.get().open(url)
        speak.speak("instagram open")
        return "instagram open"

    elif 'open twitter' in data_btn or 'twitter' in data_btn or 'start twitter' in data_btn:
        url = 'https://twitter.com/'
        webbrowser.get().open(url)
        speak.speak("twitter open")
        return "twitter open"

    elif 'open linkedin' in data_btn or 'linkedin' in data_btn or 'start linkedin' in data_btn:
        url = 'https://www.linkedin.com/'
        webbrowser.get().open(url)
        speak.speak("linkedin open")
        return "linkedin open"

    elif 'open github' in data_btn or 'github' in data_btn or 'start github' in data_btn:
        url = 'https://github.com/'
        webbrowser.get().open(url)
        speak.speak("github open")
        return "github open"
    
    elif 'open photos' in data_btn or 'photos' in data_btn or 'start photos' in data_btn or 'open pictures' in data_btn or 'pictures' in data_btn:
        photos_path = r"C:\Users\MSI\Pictures"
        try:
            os.startfile(photos_path)
            speak.speak("Photos or pictures folder is opening")
            return "Photos or pictures folder is opening"
        except Exception as e:
            speak.speak("Unable to open Photos or pictures folder. Please check the installation path.")
            return "Unable to open Photos or pictures folder. Please check the installation path."
        
    elif 'open videos' in data_btn or 'videos' in data_btn or 'start videos' in data_btn or 'open movies' in data_btn or 'movies' in data_btn:
        videos_path = r"C:\Users\MSI\Videos"
        try:
            os.startfile(videos_path)
            speak.speak("Videos or movies folder is opening. videos ka folder open ho gya hai ! aage khud dekh lo")
            return "Videos or movies folder is opening"
        except Exception as e:
            speak.speak("Unable to open Videos or movies folder. Please check the installation path. ")
            return "Unable to open Videos or movies folder. Please check the installation path."

    elif 'open notepad' in data_btn or 'notepad' in data_btn or 'start notepad' in data_btn:
        notepad_path = r"C:\Windows\System32\notepad.exe"
        try:
            os.startfile(notepad_path)
            speak.speak("Notepad app is opening")
            return "Notepad app is opening"
        except Exception as e:
            speak.speak("Unable to open Notepad app. Please check the installation path.")
            return "Unable to open Notepad app. Please check the installation path."
    
    elif 'open calculator' in data_btn or 'calculator' in data_btn or 'start calculator' in data_btn:
        calculator_path = r"C:\Windows\System32\calc.exe"
        try:
            os.startfile(calculator_path)
            speak.speak("Calculator app is opening")
            return "Calculator app is opening"
        except Exception as e:
            speak.speak("Unable to open Calculator app. Please check the installation path.")
            return "Unable to open Calculator app. Please check the installation path."
    
    elif 'open file explorer' in data_btn or 'file explorer' in data_btn or 'start file explorer' in data_btn:
        try:
            os.startfile(os.path.expanduser("~"))  # Opens the user's home directory
            speak.speak("File Explorer is opening")
            return "File Explorer is opening"
        except Exception as e:
            speak.speak("Unable to open File Explorer. Please check the installation path.")
            return "Unable to open File Explorer. Please check the installation path."
        
    elif 'open settings' in data_btn or 'settings' in data_btn or 'start settings' in data_btn:
        settings_path = r"C:\Windows\System32\control.exe"
        try:
            os.startfile(settings_path)
            speak.speak("Settings app is opening")
            return "Settings app is opening"
        except Exception as e:
            speak.speak("Unable to open Settings app. Please check the installation path.")
            return "Unable to open Settings app. Please check the installation path."
    
    elif 'mastipur' in data_btn or 'masti pur'  in data_btn:
        url = 'https://www.google.com/maps/place/Masti+Pur,+Uttar+Pradesh+226302/@26.5944848,81.0109895,1583m/data=!3m2!1e3!4b1!4m6!3m5!1s0x399bedc4c82469e3:0xec8c1bb88b9bac15!8m2!3d26.5944069!4d81.0168013!16s%2Fg%2F1tdncnq1?entry=ttu&g_ep=EgoyMDI1MDgwNC4wIKXMDSoASAFQAw%3D%3D'
        webbrowser.get().open(url)
        speak.speak("mastipur is now open in your browser")  
        return "mastipur is now open in your browser"

    elif 'open command prompt' in data_btn or 'command prompt' in data_btn or 'start command prompt' in data_btn:
        cmd_path = r"C:\Windows\System32\cmd.exe"
        try:
            os.startfile(cmd_path)
            speak.speak("Command Prompt is opening")
            return "Command Prompt is opening"
        except Exception as e:
            speak.speak("Unable to open Command Prompt. Please check the installation path.")
            return "Unable to open Command Prompt. Please check the installation path."


    else:
        speak.speak("I'm unable to understand, will you please elaborate more!")
        return "I'm unable to understand, will you please elaborate more!"