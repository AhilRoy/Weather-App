import tkinter as tk
from weather import get_weather


def search():

    city = city_entry.get()

    if city == "":
        result.delete("1.0", tk.END)
        result.insert(tk.END, "⚠ Please enter city name")
        return


    weather = get_weather(city)


    if weather:

        report = f"""

📍 City: {weather['city']}
🌍 Country: {weather['country']}


🌡 Temperature: {weather['temperature']} °C

🥵 Feels Like: {weather['feels_like']} °C

🔺 Maximum: {weather['max_temp']} °C

🔻 Minimum: {weather['min_temp']} °C


💧 Humidity: {weather['humidity']} %

📈 Pressure: {weather['pressure']} hPa


{weather['emoji']} Weather: {weather['weather']}

📝 Description: {weather['description']}


💨 Wind Speed: {weather['wind_speed']} m/s

🧭 Wind Direction: {weather['wind_direction']}°


👀 Visibility: {weather['visibility']} km


📍 Latitude: {weather['latitude']}

📍 Longitude: {weather['longitude']}


☁️ Cloudiness: {weather['cloudiness']} %


🌅 Sunrise: {weather['sunrise']}

🌇 Sunset: {weather['sunset']}

"""


        # Clear old result
        result.delete("1.0", tk.END)

        # Insert new weather report
        result.insert(tk.END, report)


    else:

        result.delete("1.0", tk.END)
        result.insert(tk.END, "❌ City not found")



# ---------------- Window ----------------

root = tk.Tk()

root.title("Weather Forecast App")

root.geometry("500x750")

root.configure(bg="#87CEEB")



heading = tk.Label(
    root,
    text="🌤 Weather Forecast App",
    font=("Arial",22,"bold"),
    bg="#87CEEB",
    fg="white"
)

heading.pack(pady=20)



city_label = tk.Label(
    root,
    text="Enter City",
    font=("Arial",14),
    bg="#87CEEB"
)

city_label.pack()



city_entry = tk.Entry(
    root,
    font=("Arial",16),
    width=25
)

city_entry.pack(pady=10)



search_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial",14),
    bg="blue",
    fg="white",
    width=15,
    command=search
)

search_button.pack(pady=20)



# ---------------- Scrollable Result Box ----------------

result_frame = tk.Frame(root)

result_frame.pack(pady=10)



scrollbar = tk.Scrollbar(result_frame)

scrollbar.pack(
    side="right",
    fill="y"
)



result = tk.Text(
    result_frame,
    height=22,
    width=45,
    font=("Arial",12),
    bg="white",
    wrap="word",
    yscrollcommand=scrollbar.set
)

result.pack(
    side="left"
)



scrollbar.config(
    command=result.yview
)



root.mainloop()