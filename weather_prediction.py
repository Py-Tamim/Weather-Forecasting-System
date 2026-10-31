import pandas as pd
from sklearn.ensemble import RandomForestRegressor


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