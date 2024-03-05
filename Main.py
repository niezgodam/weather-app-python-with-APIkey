from requests import get
from pprint import PrettyPrinter
from tkinter import *
from tkinter import messagebox
import os
from dotenv import load_dotenv
load_dotenv()


BASE_LINK = "https://api.openweathermap.org/data/2.5"
API_KEY = os.getenv('API_KEY')
printer = PrettyPrinter()
#city = input("Enter a city: ")


def weather(city):
    endpoint = f"/weather?q={city}&appid={API_KEY}"
    
    try:
        data = get(BASE_LINK+endpoint).json()
        temperature = round(float(data['main']['temp']) - 273.15, 1)
        weather_desc = data['weather'][0]['description']
        return temperature, weather_desc
    except Exception as e:
        messagebox.showerror("Data Error","Failed to fetch weather data.")
        return None, None

def search():
    city = entry_city.get()
    temperature, weather_desc = weather(city)

    imageweather=None
    if "drizzle" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('DRIZZLE_PATH')}", height=500)
    elif "few clouds" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('FEW_CLOUDS_PATH')}", height=500)
    elif "mist" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('MIST_PATH')}", height=500)
    elif "clouds" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('CLOUDS_PATH')}", height=500)
    elif "rain"in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('RAIN_PATH')}", height=500)
    elif "snow" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('SNOW_PATH')}", height=500)
    elif "clear" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('CLEAR_SNOW')}", height=500)
    elif "thunderstorm" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('THUNDERSTORM_PATH')}", height=500)
    elif "fog" in weather_desc:
        imageweather = PhotoImage(file=f"{os.getenv('MIST_PATH')}", height=500)

    new_label = Label(window, image=imageweather, width=600, height=500,compound="top")
    new_label.image = imageweather  
    new_label.place(x=320, y=350)

    label_background = Label(window,text=f"{temperature}",font=("Consolas",25,"bold"),width=10,height=5,background="#2b2b2b",fg="white")
    label_background.place(x=530,y=630)
    return city 


window = Tk()

window_width = 1280
window_height = 1080
screen_width = 1920
screen_height = 1080
x = int((screen_width/2)-(window_width/2))
y = int((screen_height/2)-(window_height/2))
window.resizable(False, False)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.title("WeatherAPP")

backgroundImage = PhotoImage(file=f"{os.getenv('BACKGROUND_PATH')}")
background = Label(window, image=backgroundImage)
background.place(x=0, y=0)


entry_city = Entry(window,width=25,font=("Consolas",25,'bold'))
entry_city.place(x=390,y=200)

buttonImage = PhotoImage(file=f"{os.getenv('BUTTON_PATH')}",width=570)
city_button = Button(window,text="SEARCH",image=buttonImage,width=170,height=30,relief="raised",bd=4,command=search)
city_button.place(x=530,y=250)



window.mainloop()