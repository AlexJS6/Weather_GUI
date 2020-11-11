import tkinter as tk #tkinter doc: https://www.tutorialspoint.com/python/python_gui_programming.htm
from tkinter import font
import requests

#pack() -> keywords: expand, fill, side
#place() -> Best -> 
#grid()


WIDTH = 675
HEIGHT = 550

def test_function(entry):
    print('Button clicked!:' + entry)


def format_response(weather):
    try:  #use try and except for if name is invalid! 
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']

        final_str = 'City: {} \nConditions: {} \nTemperature (Celsius): {}'.format(name, description, temperature)
    except:
        final_str = 'There was a problem retrieving that info'
    return final_str

def get_weather(city):
    weather_key = ''
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params = params)
    weather = response.json()
    
    label['text'] = format_response(weather)


root = tk.Tk() #tkinter needs a root window

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = './pictures/traunstein.png')
background_label = tk.Label(root, image = background_image)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

frame = tk.Frame(root, bg = '#7ad', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n') #anchor is north (default north west) so 0.5 will be middle -> middle with relx 0.5

entry = tk.Entry(frame, font = ('Constantia', 16))
entry.place(relwidth = 0.65, relheight = 1)

button = tk.Button(frame, text="Get Weather", font = ('Constantia', 14), command = lambda:  get_weather(entry.get())) #its defined at the time it is run
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)


lower_frame = tk.Frame(root, bg = '#7ad', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font = ('Constantia', 20))
label.place(relwidth = 1, relheight = 1)

print(tk.font.families())

root.mainloop() # everything runs betwwen root = tk.Tk() and root.mainloop()