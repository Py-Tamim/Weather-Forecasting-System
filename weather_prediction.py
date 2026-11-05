import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

df = pd.read_csv("weather_forcast.csv", skiprows=3)             # Load Datas/CSV Files
df = df.dropna(axis=1, how="all")
df.columns = ["time", "temperature", "humidity", "rain", "wind"]
df = df.dropna()
df["time"] = pd.to_datetime(df["time"])
cols = ["temperature", "humidity", "rain", "wind"]
print("Data loaded:", df.shape[0], "hours")
print("From", df["time"].min(), "to", df["time"].max())

feature_cols = ["hour"] + [c + "_1h" for c in cols] + [c + "_24h" for c in cols] # Define User Input
def make_features(data):
    data = data.copy()
    data["hour"] = data["time"].dt.hour
    for c in cols:
        data[c + "_1h"] = data[c].shift(1)
        data[c + "_24h"] = data[c].shift(24)
    data = data.dropna()
    return data

def train_model(data):              # Train the model
    data = make_features(data)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(data[feature_cols].values, data[cols].values)
    return model 

def make_forecast(model, data, end_time):
    history = data[cols].values.tolist()
    time = data["time"].iloc[-1]
    new_rows = []

    while time < end_time:
        time = time + pd.Timedelta(hours=1)
        last_1h = history[-1]
        last_24h = history[-24]
        features = [time.hour] + last_1h + last_24h
        guess = model.predict([features])[0]
        history.append(list(guess))
        new_rows.append([time] + list(guess))
    return pd.DataFrame(new_rows, columns=["time"] + cols)

# Check that how good the model is {Optionalm, If you want you can comment out this whole part}
old_part = df.iloc[:-48]
real_part = df.iloc[-48:].reset_index(drop=True)
test_model = train_model(old_part)
test_forecast = make_forecast(test_model, old_part, real_part["time"].iloc[-1])
print("\nModel check - average difference between predicted and real values:")
for c in cols:
    error = (test_forecast[c] - real_part[c]).abs().mean()
    print(" ", c, ":", round(error, 2))        # End of this part.

model = train_model(df)
print("\n----- Weather Forecast -----")  # print a heading
date_text = input("Enter date or date range (e.g. 12-10-2026  or  12-10-2026 to 15-10-2026): ")
time_text = input("Enter time or time range (e.g. 1 pm  or  2 to 5 am). Press Enter for the full day: ")
date_parts = date_text.lower().replace("from", "").split(" to ")
start_date = pd.to_datetime(date_parts[0].strip(), dayfirst=True).normalize()
end_date = pd.to_datetime(date_parts[-1].strip(), dayfirst=True).normalize()

def read_hour(text, am_pm):
    text = text.strip()
    if "am" in text:
        am_pm = "am"
    if "pm" in text:
        am_pm = "pm"
    number = int(text.replace("am", "").replace("pm", "").strip())
    if am_pm == "pm" and number != 12:
        number = number + 12
    if am_pm == "am" and number == 12:
        number = 0
    return number

if time_text.strip() == "":
    start_hour = 0
    end_hour = 23
else:
    time_text = time_text.lower()
    if "pm" in time_text:
        am_pm = "pm"  # use pm
    elif "am" in time_text:
        am_pm = "am"
    else:
        am_pm = ""
    time_parts = time_text.split(" to ")
    start_hour = read_hour(time_parts[0], am_pm)
    end_hour = read_hour(time_parts[-1], am_pm)


last_time = df["time"].iloc[-1]
end_time = end_date + pd.Timedelta(hours=23)
df["source"] = "Real data"

if end_time > last_time:
    future = make_forecast(model, df, end_time)
    future["source"] = "Predicted"
    all_weather = pd.concat([df, future])
else:
    all_weather = df

all_weather["date"] = all_weather["time"].dt.normalize()
all_weather["hour"] = all_weather["time"].dt.hour
result = all_weather[
    (all_weather["date"] >= start_date)
    & (all_weather["date"] <= end_date)
    & (all_weather["hour"] >= start_hour)
    & (all_weather["hour"] <= end_hour)
]

if result.shape[0] == 0:
    print("\nNo data found for that date/time. Please try again.")
else:  # if rows were found
    for i in range(len(result)):
        row = result.iloc[i]
        day_text = row["time"].strftime("%A, %d %b %Y")
        time_text = row["time"].strftime("%I:%M %p").lstrip("0")
        wind_mph = row["wind"] * 0.621371

        print("\nDhaka, Bangladesh")
        print(day_text + ", " + time_text + "  (" + row["source"] + ")")
        print(str(round(row["temperature"])) + " °C")
        print("Rain:     " + str(round(row["rain"], 1)) + " mm")
        print("Humidity: " + str(round(row["humidity"])) + "%")
        print("Wind:     " + str(round(wind_mph)) + " mph")

    if (end_date - last_time.normalize()).days > 7:
        print("\nNote: forecasts more than 7 days ahead are less accurate.")
    else:
        print("-------------------------Thank you for using our service-------------------------")
        
if result.shape[0] > 0:                  #Graph Ploting
    wind_mph = result["wind"] * 0.621371
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.plot(result["time"], result["temperature"], color="orange", marker="o")
    plt.title("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.subplot(2, 2, 2)
    plt.plot(result["time"], result["humidity"], color="skyblue", marker="o")
    plt.title("Humidity (%)")
    plt.xticks(rotation=45)
    plt.subplot(2, 2, 3)
    plt.plot(result["time"], result["rain"], color="blue", marker="o")
    plt.title("Rain (mm)")
    plt.xticks(rotation=45)
    plt.subplot(2, 2, 4)
    plt.plot(result["time"], wind_mph, color="green", marker="o")
    plt.title("Wind (mph)")
    plt.xticks(rotation=45)
    plt.tight_layout()  # fix spacing between graphs
    plt.show()