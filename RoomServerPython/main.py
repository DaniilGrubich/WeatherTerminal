import socket
import time
import requests
import json
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import threading
import pyautogui
import tkinter as tk
import os

clients = []
WebMessage = []

class Server(WebSocket):
    def handleMessage(self):
        print(self.data)
        if(self.data == "unlock"):
            password = "0804169"
            pyautogui.write(password, interval = 0.1)
            pyautogui.press('enter')
        else:
            esp = s.accept()[0]
            communicateWithESP(esp, bytearray(self.data.encode()))

    def handleConnected(self):
        print(self.address, 'connected')
        clients.append(self)
        sendTempToClients()

    def handleClose(self):
        print(self.address, 'closed')
        clients.remove(self)


def getWeatherAPIData():
    # api_key = "XXX"
    # lat = "XXX"
    # lon = "XXX"
    # url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    # response = requests.get(url)
    # data = json.loads(response.text)

    return {'lat': 42.6143, 'lon': -83.4251, 'timezone': 'America/Detroit', 'timezone_offset': -14400, 'current': {'dt': 1658343638, 'sunrise': 1658312020, 'sunset': 1658365565, 'temp': 29.85, 'feels_like': 34.44, 'pressure': 998, 'humidity': 69, 'dew_point': 23.55, 'uvi': 7.32, 'clouds': 6, 'visibility': 10000, 'wind_speed': 4.02, 'wind_deg': 219, 'wind_gust': 13.41, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}]}, 'minutely': [{'dt': 1658343660, 'precipitation': 0}, {'dt': 1658343720, 'precipitation': 0}, {'dt': 1658343780, 'precipitation': 0}, {'dt': 1658343840, 'precipitation': 0}, {'dt': 1658343900, 'precipitation': 0}, {'dt': 1658343960, 'precipitation': 0}, {'dt': 1658344020, 'precipitation': 0}, {'dt': 1658344080, 'precipitation': 0}, {'dt': 1658344140, 'precipitation': 0}, {'dt': 1658344200, 'precipitation': 0}, {'dt': 1658344260, 'precipitation': 0}, {'dt': 1658344320, 'precipitation': 0}, {'dt': 1658344380, 'precipitation': 0}, {'dt': 1658344440, 'precipitation': 0}, {'dt': 1658344500, 'precipitation': 0}, {'dt': 1658344560, 'precipitation': 0}, {'dt': 1658344620, 'precipitation': 0}, {'dt': 1658344680, 'precipitation': 0}, {'dt': 1658344740, 'precipitation': 0}, {'dt': 1658344800, 'precipitation': 0}, {'dt': 1658344860, 'precipitation': 0}, {'dt': 1658344920, 'precipitation': 0}, {'dt': 1658344980, 'precipitation': 0}, {'dt': 1658345040, 'precipitation': 0}, {'dt': 1658345100, 'precipitation': 0}, {'dt': 1658345160, 'precipitation': 0}, {'dt': 1658345220, 'precipitation': 0}, {'dt': 1658345280, 'precipitation': 0}, {'dt': 1658345340, 'precipitation': 0}, {'dt': 1658345400, 'precipitation': 0}, {'dt': 1658345460, 'precipitation': 0}, {'dt': 1658345520, 'precipitation': 0}, {'dt': 1658345580, 'precipitation': 0}, {'dt': 1658345640, 'precipitation': 0}, {'dt': 1658345700, 'precipitation': 0}, {'dt': 1658345760, 'precipitation': 0}, {'dt': 1658345820, 'precipitation': 0}, {'dt': 1658345880, 'precipitation': 0}, {'dt': 1658345940, 'precipitation': 0}, {'dt': 1658346000, 'precipitation': 0}, {'dt': 1658346060, 'precipitation': 0}, {'dt': 1658346120, 'precipitation': 0}, {'dt': 1658346180, 'precipitation': 0}, {'dt': 1658346240, 'precipitation': 0}, {'dt': 1658346300, 'precipitation': 0}, {'dt': 1658346360, 'precipitation': 0}, {'dt': 1658346420, 'precipitation': 0}, {'dt': 1658346480, 'precipitation': 0}, {'dt': 1658346540, 'precipitation': 0}, {'dt': 1658346600, 'precipitation': 0}, {'dt': 1658346660, 'precipitation': 0}, {'dt': 1658346720, 'precipitation': 0}, {'dt': 1658346780, 'precipitation': 0}, {'dt': 1658346840, 'precipitation': 0}, {'dt': 1658346900, 'precipitation': 0}, {'dt': 1658346960, 'precipitation': 0}, {'dt': 1658347020, 'precipitation': 0}, {'dt': 1658347080, 'precipitation': 0}, {'dt': 1658347140, 'precipitation': 0}, {'dt': 1658347200, 'precipitation': 0}, {'dt': 1658347260, 'precipitation': 0}], 'hourly': [{'dt': 1658343600, 'temp': 29.85, 'feels_like': 34.44, 'pressure': 998, 'humidity': 69, 'dew_point': 23.55, 'uvi': 7.32, 'clouds': 6, 'visibility': 10000, 'wind_speed': 7.79, 'wind_deg': 227, 'wind_gust': 13.55, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0.76}, {'dt': 1658347200, 'temp': 29.78, 'feels_like': 33.84, 'pressure': 998, 'humidity': 67, 'dew_point': 22.99, 'uvi': 5.63, 'clouds': 6, 'visibility': 10000, 'wind_speed': 8.09, 'wind_deg': 231, 'wind_gust': 13.7, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0.76}, {'dt': 1658350800, 'temp': 30.13, 'feels_like': 33.29, 'pressure': 998, 'humidity': 61, 'dew_point': 21.78, 'uvi': 3.66, 'clouds': 5, 'visibility': 10000, 'wind_speed': 8.57, 'wind_deg': 234, 'wind_gust': 14.15, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0.74}, {'dt': 1658354400, 'temp': 30.49, 'feels_like': 32.54, 'pressure': 999, 'humidity': 54, 'dew_point': 20.13, 'uvi': 2, 'clouds': 4, 'visibility': 10000, 'wind_speed': 8.18, 'wind_deg': 250, 'wind_gust': 14.76, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0.71}, {'dt': 1658358000, 'temp': 29.03, 'feels_like': 30.08, 'pressure': 999, 'humidity': 53, 'dew_point': 18.48, 'uvi': 0.79, 'clouds': 3, 'visibility': 10000, 'wind_speed': 7.73, 'wind_deg': 260, 'wind_gust': 14.57, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0.84}, {'dt': 1658361600, 'temp': 26.75, 'feels_like': 27.59, 'pressure': 1000, 'humidity': 57, 'dew_point': 17.46, 'uvi': 0.21, 'clouds': 2, 'visibility': 10000, 'wind_speed': 6.97, 'wind_deg': 261, 'wind_gust': 12.59, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0.84}, {'dt': 1658365200, 'temp': 25.13, 'feels_like': 25.34, 'pressure': 1000, 'humidity': 63, 'dew_point': 17.67, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 6.45, 'wind_deg': 262, 'wind_gust': 12.27, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658368800, 'temp': 24.03, 'feels_like': 24.29, 'pressure': 1001, 'humidity': 69, 'dew_point': 18.12, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.86, 'wind_deg': 265, 'wind_gust': 12.33, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0}, {'dt': 1658372400, 'temp': 23.31, 'feels_like': 23.58, 'pressure': 1001, 'humidity': 72, 'dew_point': 18.04, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 5.34, 'wind_deg': 269, 'wind_gust': 12.11, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0}, {'dt': 1658376000, 'temp': 22.56, 'feels_like': 22.83, 'pressure': 1001, 'humidity': 75, 'dew_point': 17.97, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 4.82, 'wind_deg': 261, 'wind_gust': 11.48, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0}, {'dt': 1658379600, 'temp': 22.28, 'feels_like': 22.55, 'pressure': 1001, 'humidity': 76, 'dew_point': 17.93, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 5.6, 'wind_deg': 266, 'wind_gust': 11.73, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0}, {'dt': 1658383200, 'temp': 21.69, 'feels_like': 22, 'pressure': 1001, 'humidity': 80, 'dew_point': 18.23, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 5.45, 'wind_deg': 269, 'wind_gust': 11.43, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0}, {'dt': 1658386800, 'temp': 21.08, 'feels_like': 21.46, 'pressure': 1001, 'humidity': 85, 'dew_point': 18.5, 'uvi': 0, 'clouds': 13, 'visibility': 10000, 'wind_speed': 5.14, 'wind_deg': 267, 'wind_gust': 11.31, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'pop': 0}, {'dt': 1658390400, 'temp': 20.62, 'feels_like': 21.01, 'pressure': 1002, 'humidity': 87, 'dew_point': 18.49, 'uvi': 0, 'clouds': 11, 'visibility': 10000, 'wind_speed': 5.38, 'wind_deg': 270, 'wind_gust': 11.64, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'pop': 0}, {'dt': 1658394000, 'temp': 20.21, 'feels_like': 20.61, 'pressure': 1002, 'humidity': 89, 'dew_point': 18.4, 'uvi': 0, 'clouds': 9, 'visibility': 10000, 'wind_speed': 5.49, 'wind_deg': 272, 'wind_gust': 12.09, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0}, {'dt': 1658397600, 'temp': 19.86, 'feels_like': 20.2, 'pressure': 1003, 'humidity': 88, 'dew_point': 17.87, 'uvi': 0, 'clouds': 14, 'visibility': 10000, 'wind_speed': 5.55, 'wind_deg': 280, 'wind_gust': 12.89, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'pop': 0}, {'dt': 1658401200, 'temp': 19.84, 'feels_like': 20.15, 'pressure': 1003, 'humidity': 87, 'dew_point': 17.59, 'uvi': 0.16, 'clouds': 13, 'visibility': 10000, 'wind_speed': 5.37, 'wind_deg': 282, 'wind_gust': 12.74, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0}, {'dt': 1658404800, 'temp': 21.13, 'feels_like': 21.39, 'pressure': 1004, 'humidity': 80, 'dew_point': 17.55, 'uvi': 0.67, 'clouds': 11, 'visibility': 10000, 'wind_speed': 5.41, 'wind_deg': 282, 'wind_gust': 12.63, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0}, {'dt': 1658408400, 'temp': 23.22, 'feels_like': 23.37, 'pressure': 1005, 'humidity': 68, 'dew_point': 16.97, 'uvi': 1.74, 'clouds': 0, 'visibility': 10000, 'wind_speed': 6.21, 'wind_deg': 286, 'wind_gust': 11.67, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658412000, 'temp': 25.64, 'feels_like': 25.7, 'pressure': 1005, 'humidity': 55, 'dew_point': 15.86, 'uvi': 3.4, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.96, 'wind_deg': 285, 'wind_gust': 9.69, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658415600, 'temp': 27.86, 'feels_like': 27.82, 'pressure': 1005, 'humidity': 44, 'dew_point': 14.53, 'uvi': 5.37, 'clouds': 0, 'visibility': 10000, 'wind_speed': 6.23, 'wind_deg': 282, 'wind_gust': 9.97, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658419200, 'temp': 29.65, 'feels_like': 28.9, 'pressure': 1005, 'humidity': 36, 'dew_point': 13.03, 'uvi': 7.05, 'clouds': 0, 'visibility': 10000, 'wind_speed': 7.09, 'wind_deg': 278, 'wind_gust': 10.29, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658422800, 'temp': 30.64, 'feels_like': 29.74, 'pressure': 1005, 'humidity': 34, 'dew_point': 13, 'uvi': 8.11, 'clouds': 0, 'visibility': 10000, 'wind_speed': 7.24, 'wind_deg': 276, 'wind_gust': 10.38, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658426400, 'temp': 31.66, 'feels_like': 30.55, 'pressure': 1005, 'humidity': 31, 'dew_point': 12.66, 'uvi': 8.18, 'clouds': 0, 'visibility': 10000, 'wind_speed': 7.33, 'wind_deg': 273, 'wind_gust': 10.72, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658430000, 'temp': 31.92, 'feels_like': 30.84, 'pressure': 1005, 'humidity': 31, 'dew_point': 12.95, 'uvi': 7.07, 'clouds': 1, 'visibility': 10000, 'wind_speed': 7.86, 'wind_deg': 275, 'wind_gust': 11.42, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658433600, 'temp': 32.05, 'feels_like': 30.99, 'pressure': 1005, 'humidity': 31, 'dew_point': 12.94, 'uvi': 5.42, 'clouds': 1, 'visibility': 10000, 'wind_speed': 7.78, 'wind_deg': 276, 'wind_gust': 12.84, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658437200, 'temp': 31.55, 'feels_like': 30.78, 'pressure': 1006, 'humidity': 34, 'dew_point': 13.85, 'uvi': 3.53, 'clouds': 7, 'visibility': 10000, 'wind_speed': 7.7, 'wind_deg': 276, 'wind_gust': 12.9, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658440800, 'temp': 30.76, 'feels_like': 30.22, 'pressure': 1006, 'humidity': 37, 'dew_point': 14.61, 'uvi': 1.88, 'clouds': 22, 'visibility': 10000, 'wind_speed': 7.14, 'wind_deg': 276, 'wind_gust': 12.44, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0}, {'dt': 1658444400, 'temp': 30.06, 'feels_like': 29.88, 'pressure': 1006, 'humidity': 41, 'dew_point': 15.54, 'uvi': 0.75, 'clouds': 22, 'visibility': 10000, 'wind_speed': 6.91, 'wind_deg': 274, 'wind_gust': 11.69, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0}, {'dt': 1658448000, 'temp': 28.07, 'feels_like': 28.35, 'pressure': 1007, 'humidity': 48, 'dew_point': 16.02, 'uvi': 0.19, 'clouds': 19, 'visibility': 10000, 'wind_speed': 6.51, 'wind_deg': 272, 'wind_gust': 10.07, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0}, {'dt': 1658451600, 'temp': 26.01, 'feels_like': 26.01, 'pressure': 1007, 'humidity': 54, 'dew_point': 16.06, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.98, 'wind_deg': 275, 'wind_gust': 9.99, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0.04}, {'dt': 1658455200, 'temp': 24.3, 'feels_like': 24.38, 'pressure': 1008, 'humidity': 61, 'dew_point': 16.23, 'uvi': 0, 'clouds': 0, 'visibility': 10000, 'wind_speed': 3.65, 'wind_deg': 269, 'wind_gust': 9.39, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0.16}, {'dt': 1658458800, 'temp': 23.02, 'feels_like': 23.13, 'pressure': 1008, 'humidity': 67, 'dew_point': 16.62, 'uvi': 0, 'clouds': 1, 'visibility': 10000, 'wind_speed': 2.93, 'wind_deg': 265, 'wind_gust': 7.55, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'pop': 0.16}, {'dt': 1658462400, 'temp': 22.46, 'feels_like': 22.64, 'pressure': 1008, 'humidity': 72, 'dew_point': 17.16, 'uvi': 0, 'clouds': 12, 'visibility': 10000, 'wind_speed': 2.61, 'wind_deg': 265, 'wind_gust': 6.74, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'pop': 0.12}, {'dt': 1658466000, 'temp': 22.23, 'feels_like': 22.52, 'pressure': 1008, 'humidity': 77, 'dew_point': 17.9, 'uvi': 0, 'clouds': 29, 'visibility': 10000, 'wind_speed': 2.18, 'wind_deg': 264, 'wind_gust': 5.21, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'pop': 0.4, 'rain': {'1h': 0.21}}, {'dt': 1658469600, 'temp': 21.79, 'feels_like': 22.09, 'pressure': 1009, 'humidity': 79, 'dew_point': 17.91, 'uvi': 0, 'clouds': 37, 'visibility': 10000, 'wind_speed': 2.42, 'wind_deg': 274, 'wind_gust': 5.42, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10n'}], 'pop': 0.24, 'rain': {'1h': 0.13}}, {'dt': 1658473200, 'temp': 21.56, 'feels_like': 21.86, 'pressure': 1009, 'humidity': 80, 'dew_point': 17.82, 'uvi': 0, 'clouds': 66, 'visibility': 10000, 'wind_speed': 2.2, 'wind_deg': 288, 'wind_gust': 4.83, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'pop': 0.19}, {'dt': 1658476800, 'temp': 20.89, 'feels_like': 21.18, 'pressure': 1009, 'humidity': 82, 'dew_point': 17.64, 'uvi': 0, 'clouds': 51, 'visibility': 10000, 'wind_speed': 2.5, 'wind_deg': 299, 'wind_gust': 5.71, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04n'}], 'pop': 0.12}, {'dt': 1658480400, 'temp': 20, 'feels_like': 20.3, 'pressure': 1010, 'humidity': 86, 'dew_point': 17.44, 'uvi': 0, 'clouds': 34, 'visibility': 10000, 'wind_speed': 2.65, 'wind_deg': 296, 'wind_gust': 6.17, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'pop': 0.07}, {'dt': 1658484000, 'temp': 19.32, 'feels_like': 19.58, 'pressure': 1010, 'humidity': 87, 'dew_point': 17.19, 'uvi': 0, 'clouds': 26, 'visibility': 10000, 'wind_speed': 2.44, 'wind_deg': 290, 'wind_gust': 4.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'pop': 0.03}, {'dt': 1658487600, 'temp': 19.12, 'feels_like': 19.31, 'pressure': 1011, 'humidity': 85, 'dew_point': 16.62, 'uvi': 0.16, 'clouds': 21, 'visibility': 10000, 'wind_speed': 2.78, 'wind_deg': 300, 'wind_gust': 6.49, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0.03}, {'dt': 1658491200, 'temp': 20.49, 'feels_like': 20.55, 'pressure': 1012, 'humidity': 75, 'dew_point': 15.9, 'uvi': 0.64, 'clouds': 17, 'visibility': 10000, 'wind_speed': 3.5, 'wind_deg': 285, 'wind_gust': 7.38, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}], 'pop': 0.01}, {'dt': 1658494800, 'temp': 22.59, 'feels_like': 22.52, 'pressure': 1012, 'humidity': 62, 'dew_point': 14.77, 'uvi': 1.63, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.12, 'wind_deg': 297, 'wind_gust': 7.1, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658498400, 'temp': 25.05, 'feels_like': 24.92, 'pressure': 1012, 'humidity': 50, 'dew_point': 14, 'uvi': 3.18, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.46, 'wind_deg': 308, 'wind_gust': 7.52, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658502000, 'temp': 28.04, 'feels_like': 27.27, 'pressure': 1012, 'humidity': 33, 'dew_point': 10.33, 'uvi': 5.03, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.43, 'wind_deg': 320, 'wind_gust': 7.96, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658505600, 'temp': 29.26, 'feels_like': 27.98, 'pressure': 1013, 'humidity': 28, 'dew_point': 9.16, 'uvi': 6.74, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.57, 'wind_deg': 311, 'wind_gust': 7.43, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658509200, 'temp': 30.29, 'feels_like': 28.75, 'pressure': 1013, 'humidity': 26, 'dew_point': 8.8, 'uvi': 7.76, 'clouds': 0, 'visibility': 10000, 'wind_speed': 5.05, 'wind_deg': 296, 'wind_gust': 7.63, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}, {'dt': 1658512800, 'temp': 31.27, 'feels_like': 29.53, 'pressure': 1013, 'humidity': 24, 'dew_point': 8.15, 'uvi': 7.83, 'clouds': 0, 'visibility': 10000, 'wind_speed': 4.83, 'wind_deg': 295, 'wind_gust': 7.6, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'pop': 0}], 'daily': [{'dt': 1658336400, 'sunrise': 1658312020, 'sunset': 1658365565, 'moonrise': 1658292300, 'moonset': 1658340540, 'moon_phase': 0.75, 'temp': {'day': 29.17, 'min': 22.65, 'max': 30.49, 'night': 23.31, 'eve': 29.03, 'morn': 22.68}, 'feels_like': {'day': 33.1, 'night': 23.58, 'eve': 30.08, 'morn': 23.09}, 'pressure': 999, 'humidity': 70, 'dew_point': 23.14, 'wind_speed': 8.57, 'wind_deg': 234, 'wind_gust': 14.76, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'clouds': 32, 'pop': 0.93, 'rain': 2.62, 'uvi': 7.92}, {'dt': 1658422800, 'sunrise': 1658398475, 'sunset': 1658451916, 'moonrise': 1658380080, 'moonset': 1658430900, 'moon_phase': 0.78, 'temp': {'day': 30.64, 'min': 19.84, 'max': 32.05, 'night': 23.02, 'eve': 30.06, 'morn': 19.84}, 'feels_like': {'day': 29.74, 'night': 23.13, 'eve': 29.88, 'morn': 20.15}, 'pressure': 1005, 'humidity': 34, 'dew_point': 13, 'wind_speed': 7.86, 'wind_deg': 275, 'wind_gust': 12.9, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'clouds': 0, 'pop': 0.16, 'uvi': 8.18}, {'dt': 1658509200, 'sunrise': 1658484932, 'sunset': 1658538265, 'moonrise': 1658467920, 'moonset': 1658521140, 'moon_phase': 0.82, 'temp': {'day': 30.29, 'min': 19.12, 'max': 32.21, 'night': 23.06, 'eve': 30.79, 'morn': 19.12}, 'feels_like': {'day': 28.75, 'night': 23.12, 'eve': 29.61, 'morn': 19.31}, 'pressure': 1013, 'humidity': 26, 'dew_point': 8.8, 'wind_speed': 5.05, 'wind_deg': 296, 'wind_gust': 10.17, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': 0, 'pop': 0.4, 'rain': 0.34, 'uvi': 7.83}, {'dt': 1658595600, 'sunrise': 1658571389, 'sunset': 1658624613, 'moonrise': 1658555940, 'moonset': 1658611440, 'moon_phase': 0.85, 'temp': {'day': 31.21, 'min': 19.54, 'max': 31.65, 'night': 25.58, 'eve': 28.94, 'morn': 19.62}, 'feels_like': {'day': 31.66, 'night': 26.28, 'eve': 32.06, 'morn': 19.83}, 'pressure': 1013, 'humidity': 43, 'dew_point': 17.18, 'wind_speed': 11.16, 'wind_deg': 275, 'wind_gust': 19.51, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'clouds': 60, 'pop': 0.99, 'rain': 6.82, 'uvi': 8.3}, {'dt': 1658682000, 'sunrise': 1658657847, 'sunset': 1658710959, 'moonrise': 1658644320, 'moonset': 1658701440, 'moon_phase': 0.88, 'temp': {'day': 28.84, 'min': 20.18, 'max': 30.92, 'night': 21.32, 'eve': 24.53, 'morn': 21.39}, 'feels_like': {'day': 30.2, 'night': 21.73, 'eve': 25.1, 'morn': 22.01}, 'pressure': 1010, 'humidity': 56, 'dew_point': 19.13, 'wind_speed': 5.2, 'wind_deg': 281, 'wind_gust': 11.07, 'weather': [{'id': 500, 'main': 'Rain', 'description': 'light rain', 'icon': '10d'}], 'clouds': 88, 'pop': 0.97, 'rain': 3.4, 'uvi': 7.61}, {'dt': 1658768400, 'sunrise': 1658744305, 'sunset': 1658797303, 'moonrise': 1658733060, 'moonset': 1658791260, 'moon_phase': 0.91, 'temp': {'day': 25.24, 'min': 16.47, 'max': 25.24, 'night': 18.89, 'eve': 22.54, 'morn': 18.14}, 'feels_like': {'day': 24.6, 'night': 18.19, 'eve': 21.95, 'morn': 17.84}, 'pressure': 1017, 'humidity': 30, 'dew_point': 6.74, 'wind_speed': 4.31, 'wind_deg': 354, 'wind_gust': 7.95, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': 72, 'pop': 0.14, 'uvi': 0.53}, {'dt': 1658854800, 'sunrise': 1658830764, 'sunset': 1658883645, 'moonrise': 1658822280, 'moonset': 1658880660, 'moon_phase': 0.94, 'temp': {'day': 27.61, 'min': 16.9, 'max': 28.13, 'night': 20.31, 'eve': 24.17, 'morn': 18.86}, 'feels_like': {'day': 26.91, 'night': 20.2, 'eve': 23.92, 'morn': 18.5}, 'pressure': 1017, 'humidity': 32, 'dew_point': 9.8, 'wind_speed': 2.45, 'wind_deg': 232, 'wind_gust': 3.86, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': 42, 'pop': 0, 'uvi': 1}, {'dt': 1658941200, 'sunrise': 1658917224, 'sunset': 1658969986, 'moonrise': 1658911920, 'moonset': 1658969640, 'moon_phase': 0.97, 'temp': {'day': 26.93, 'min': 18.52, 'max': 26.93, 'night': 21.17, 'eve': 23.12, 'morn': 20.25}, 'feels_like': {'day': 27.72, 'night': 21.82, 'eve': 23.76, 'morn': 20.5}, 'pressure': 1011, 'humidity': 56, 'dew_point': 17.31, 'wind_speed': 5.24, 'wind_deg': 191, 'wind_gust': 8.86, 'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10d'}], 'clouds': 91, 'pop': 0.97, 'rain': 7.35, 'uvi': 1}], 'alerts': [{'sender_name': 'NWS Storm Prediction Center (Storm Prediction Center - Norman, Oklahoma)', 'event': 'Severe Thunderstorm Watch', 'start': 1658336100, 'end': 1658361600, 'description': 'SEVERE THUNDERSTORM WATCH 477 IS IN EFFECT UNTIL 800 PM EDT\nFOR THE FOLLOWING LOCATIONS\nMI\n.    MICHIGAN COUNTIES INCLUDED ARE\nALCONA               ALPENA              ARENAC\nBAY                  CHEBOYGAN           CRAWFORD\nGENESEE              GLADWIN             HILLSDALE\nHURON                INGHAM              IOSCO\nJACKSON              LAPEER              LENAWEE\nLIVINGSTON           MACOMB              MIDLAND\nMONROE               MONTMORENCY         OAKLAND\nOGEMAW               OSCODA              OTSEGO\nPRESQUE ISLE         ROSCOMMON           SAGINAW\nSANILAC              SHIAWASSEE          ST. CLAIR\nTUSCOLA              WASHTENAW           WAYNE', 'tags': ['Thunderstorm']}]}



def communicateWithESP(esp, code):
    esp.send(code)
    content = str(esp.recv(1024), 'utf-8')

    return content


def sendTempToClients():
    global jsson, tempIn, humIn, tempOut, humOut, timeStamps
    tempInAvg = []
    tempOutAvg = []

    humInAvg = []
    humOutAvg = []

    timeStampsAvg = []

    if (len(tempIn) > 20):
        for i in range(0, len(tempIn), 2):
            n = 0
            sumTi = 0
            sumTo = 0

            sumHi = 0
            sumHo = 0

            sumMin = 0

            if len(tempIn) > (i + 10):
                for j in range(i, i + 10):
                    sumTi += float(tempIn[j])
                    sumTo += float(tempOut[j])
                    sumHi += float(humIn[j])
                    sumHo += float(humOut[j])
                    sumMin += timeStamps[j]
                    n += 1

                tempInAvg.append(sumTi / n)
                tempOutAvg.append(sumTo / n)
                humInAvg.append(sumHi / n)
                humOutAvg.append(sumHo / n)

                hour = int(sumMin / n / 60)
                minute = int(sumMin / n - hour * 60)
                timeStampsAvg.append(str(hour) + ":" + str(minute))
    else:
        tempInAvg = tempIn
        tempOutAvg = tempOut
        humInAvg = humIn
        humOutAvg = humOut

        # print("tempIn", tempInAvg)
        # print("tempOut", tempOutAvg)
        # print("humIn", humInAvg)
        # print("humOut", humOutAvg)

        for curMin in timeStamps:
            hour = int(curMin / 60)
            minute = int(curMin - hour * 60)
            timeStampsAvg.append(str(hour) + ":" + str(minute))

    messageForClients = str(tempInAvg) + "\n;"
    messageForClients += str(tempOutAvg) + "\n;"
    messageForClients += str(humInAvg) + "\n;"
    messageForClients += str(humOutAvg) + "\n;"
    messageForClients += str(timeStampsAvg) + "\n;"

    messageForClients += str(tempIn[len(tempIn) - 1]) + "\n;"
    messageForClients += str(humIn[len(humIn) - 1]) + "\n;"

    messageForClients = messageForClients.replace("[", "").replace("'", "").replace("", "").replace("]", "")
    messageForClients += str(jsson).replace("'", '"') + ";"


    for client in clients:
        client.sendMessage(messageForClients)


def temperatureThread():
    global stateFlag, jsson, tempIn, humIn, tempOut, humOut, timeStamps, txtConnected, txtIncommingMessage, txtLastUpdateTime, connectionState, s, espMessage
    while True:
        esp = s.accept()[0]

        try:
            print("message sent to esp")
            espMessage = communicateWithESP(esp, b'temp')
            print("message read from esp: ", espMessage)
        except:
            print("error communicating with esp")

        readingBits = espMessage.split(',')  # Ti, Hi
        print("message spliced: ", readingBits)



        localtimeObj = time.localtime(time.time())
        nowMin = localtimeObj[3] * 60 + localtimeObj[4]

        if (len(readingBits) == 2 and readingBits[0] != 'nan'):
            tempIn.append(readingBits[0])
            humIn.append(readingBits[1])

            if stateFlag:
                try:
                    jsson = getWeatherAPIData()
                    print("JSON Request: ", jsson)
                    humOut.append(jsson["current"]["humidity"])
                    tempOut.append(jsson["current"]["temp"])

                except:
                    print("JSON Request: ", "Error")
                    humOut.append(humOut[len(humOut) - 1])
                    tempOut.append(tempOut[len(tempOut) - 1])

                stateFlag = False
            else:
                print("JSON Request: ", "Skip")
                humOut.append(humOut[len(humOut) - 1])
                tempOut.append(tempOut[len(tempOut) - 1])
                stateFlag = True

            timeStamps.append(nowMin)

            if len(tempIn) > 180:
                tempIn.pop(0)
                humIn.pop(0)

                tempOut.pop(0)
                humOut.pop(0)

                timeStamps.pop(0)

        print()
        sendTempToClients()
        time.sleep(5)


def turn_red(event):
    os._exit(0)


def GUIThread():
    root = tk.Tk()
    lable = tk.Label(root, text="Room server")
    lable.pack()
    exitBtn = tk.Button(root, text="Exit")
    exitBtn.bind("<Button>", turn_red)
    exitBtn.pack()
    root.mainloop()


####################################################

stateFlag = True

espMessage = ""

tempIn = []
humIn = []
tempOut = []
humOut = []

timeStamps = []

####################################################
# sg.theme('DarkAmber')
#
# connectionState = "connected"
#
# txtConnected = sg.Text("Connection")
# txtIncommingMessage = sg.Text("Message")
# txtLastUpdateTime = sg.Text("XX:XX")

#####################################################




s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 8585))
s.listen(0)
print(s.getsockname())

server = SimpleWebSocketServer('', 4444, Server)
threading.Thread(target=temperatureThread).start()
threading.Thread(target=GUIThread).start()

server.serveforever()








