import pandas as pd 
from sklearn.ensemble import RandomForestRegressor 
import matplotlib.pyplot as plt
 

df = pd.read_csv("weather_forcast_1.csv")                           # Data Load and Preprocessing
df = df.fillna(0)
df.columns = ["date", "clock", "temperature", "humidity", "rain", "pressure", "wind"]
df["time"] = pd.to_datetime(df["date"] + " " + df["clock"])
cols = ["temperature", "humidity", "rain", "pressure", "wind"]
print("Data loaded:", df.shape[0], "hours")
print("From", df["time"].min(), "to", df["time"].max())
df["hour"] = df["time"].dt.hour                                    # Input For the Model
df["day"] = df["time"].dt.dayofyear


train_part = df.iloc[:-720]                                        # Check How Good the Model Is (Can be skipped if you want to directly train the model on all data)
test_part = df.iloc[-720:]
test_model = RandomForestRegressor(n_estimators=100, random_state=42)
test_model.fit(train_part[["hour", "day"]], train_part[cols])
test_guess = test_model.predict(test_part[["hour", "day"]])
print("\nModel check - average difference between predicted and real values:")
for i in range(len(cols)):  # repeat for each weather value
    error = abs(test_guess[:, i] - test_part[cols[i]].values).mean()
    print(" ", cols[i], ":", round(error, 2))                    # Model check Part End



model = RandomForestRegressor(n_estimators=100, random_state=42)                  # Train the model on all data
model.fit(df[["hour", "day"]], df[cols])

 
print("\n----- Weather Forecast -----")                                           # User Input for Date and Time
date_text = input("Enter date or date range (e.g. 12-12-2026  or  11-11-2026 to 11-01-2027): ")
time_text = input("Enter time or time range (e.g. 1 pm  or  1 am to 6 am). Press Enter for 24 hours: ")
date_parts = date_text.lower().replace("from", "").split(" to ")
start_date = pd.to_datetime(date_parts[0].strip(), dayfirst=True)
end_date = pd.to_datetime(date_parts[-1].strip(), dayfirst=True)
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
    time_text = time_text.lower().replace("from", "")
    if "pm" in time_text:
        am_pm = "pm"
    elif "am" in time_text:
        am_pm = "am"
    else:
        am_pm = ""
    time_parts = time_text.split(" to ")
    start_hour = read_hour(time_parts[0], am_pm)
    end_hour = read_hour(time_parts[-1], am_pm)