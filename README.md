# Weather Forecasting System – Dhaka, Bangladesh

A Python-based weather forecasting project that uses **Machine Learning (Random Forest Regression)** to predict weather conditions in Dhaka, Bangladesh.

The system can display historical weather data and generate future weather predictions based on user-selected dates and hours. It predicts temperature, humidity, rainfall, and wind speed, with an additional version that also predicts atmospheric pressure.

## Project Overview

This project contains two approaches to weather forecasting:

### Version 1: Date and Time-Based Forecasting

The first version uses the hour of the day and day of the year as input features.

- Uses Random Forest Regression.
- Predicts temperature, humidity, rainfall, atmospheric pressure, and wind speed.
- Uses the last 30 days of available data to evaluate the model.
- Supports individual dates and date ranges.
- Supports individual hours, time ranges, and full-day forecasts.
- Displays real and predicted weather separately.
- Generates bar charts for weather conditions.

**Dataset:** `weather_forcast_1.csv`

### Version 2: Historical Weather-Based Forecasting

The second version uses previous weather observations to predict future conditions.

It uses:
- Current hour.
- Weather values from 1 hour earlier.
- Weather values from 24 hours earlier.

The model uses these historical values to predict the next hour's weather. It then uses its own predictions to forecast subsequent hours.

- Uses Random Forest Regression with 100 trees.
- Predicts temperature, humidity, rainfall, and wind speed.
- Evaluates the model using the last 48 hours of available data.
- Supports date and time selection.
- Displays historical and predicted weather separately.
- Provides a warning when forecasting more than 7 days ahead.

**Dataset:** `weather_forcast.csv`

## Features

- Weather forecasting for Dhaka, Bangladesh.
- Temperature prediction (°C).
- Humidity prediction (%).
- Rainfall prediction (mm).
- Wind speed prediction (mph).
- Atmospheric pressure prediction (hPa) in Version 1.
- Historical and future weather data identification.
- Custom date and date-range selection.
- Custom time and time-range selection.
- Model evaluation using Mean Absolute Error (MAE).
- Weather visualization using Matplotlib.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading and processing |
| Scikit-learn | Machine learning model |
| Random Forest Regressor | Weather prediction |
| Matplotlib | Data visualization |
| NumPy | Numerical operations |

## Project Structure

```text
Weather-Forecasting-System/
│
├── weather_forecasting.py
├── weather_forecasting_v2.py
│
├── weather_forcast_1.csv
├── weather_forcast.csv
│
├── README.md
└── requirements.txt
```

*The filenames above are suggested. Update them to match your actual GitHub repository.*

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/your-username/Weather-Forecasting-System.git
```

**2. Open the project folder**

```bash
cd Weather-Forecasting-System
```

**3. Install the required libraries**

```bash
pip install pandas scikit-learn matplotlib numpy
```

Or install using the requirements file:

```bash
pip install -r requirements.txt
```

## Dataset Requirements

Both versions require hourly weather data in CSV format.

**Version 1**

The CSV file should contain seven columns representing:

```text
date, clock, temperature, humidity, rain, pressure, wind
```

The script renames the columns automatically, so the CSV column order must match.

**Version 2**

The CSV file should contain hourly weather observations with these five columns after skipping the first three metadata rows:

```text
time, temperature, humidity, rain, wind
```

The second version removes completely empty columns and rows containing missing values.

## How to Run

Run the first version:

```bash
python weather_forecasting.py
```

Run the second version:

```bash
python weather_forecasting_v2.py
```

The program will ask for a date or date range and a time or time range.

**Example input:**

```text
Enter date or date range:
12-12-2026

Enter time or time range:
Press Enter for the full day
```

You can also enter:

```text
12-12-2026 to 15-12-2026
```

Or specify a time:

```text
1 pm
```

Or a time range:

```text
2 am to 6 am
```

## Model Evaluation

The second version was evaluated using the last 48 hours of available historical data.

**Sample evaluation results:**

| Weather Parameter | Average Absolute Error |
|---|---:|
| Temperature | 2.38 °C |
| Humidity | 5.37 % |
| Rainfall | 0.09 mm |
| Wind Speed | 1.52 km/h |

These values represent the average absolute difference between predicted and actual observations in the test period. Lower values indicate smaller prediction errors.

## Sample Forecast Output

Example forecast for Dhaka, Bangladesh, on 12 December 2026:

| Time | Temperature | Rain | Humidity | Wind |
|---|---:|---:|---:|---:|
| 12:00 AM | 29 °C | 0.1 mm | 73% | 3 mph |
| 6:00 AM | 28 °C | 0.1 mm | 79% | 3 mph |
| 12:00 PM | 33 °C | 0.1 mm | 57% | 3 mph |
| 3:00 PM | 34 °C | 0.1 mm | 53% | 4 mph |
| 6:00 PM | 32 °C | 0.1 mm | 60% | 4 mph |
| 11:00 PM | 30 °C | 0.0 mm | 71% | 3 mph |

<sub>Example values from a sample program run, not live weather observations.</sub>

## Data Visualization

Version 1 generates four bar charts to visualize:

- Temperature
- Humidity
- Rainfall
- Wind Speed

These charts help compare the predicted weather conditions across the selected hours.

## Important Notes and Limitations

- This project uses historical weather data and does not connect to a live weather API.
- Predictions are estimates based on patterns learned from the available dataset.
- Version 1 uses hour and day-of-year features, so it does not directly learn from previous weather measurements.
- Version 2 uses previous weather observations and recursive predictions. Prediction errors can accumulate over longer forecast periods.
- Forecasts more than 7 days ahead may be less accurate.
- Model performance depends on the quality, quantity, and coverage of the training data.
- The sample evaluation results may change when the dataset changes.

## Future Improvements

- Integrate a live weather API.
- Add more historical weather data.
- Experiment with XGBoost, LSTM, and other forecasting models.
- Improve long-term forecasting accuracy.
- Add interactive weather dashboards.
- Include additional weather parameters.

* ## This project was developed as a practical machine learning project to explore weather forecasting, historical data analysis, model evaluation, and data visualization using Python.*
