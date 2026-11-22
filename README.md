# Weather Forecasting System – Dhaka, Bangladesh

A Python-based weather forecasting project that uses **Machine Learning (Random Forest Regression)** to predict weather conditions in Dhaka, Bangladesh.

The system analyzes historical weather data and generates weather predictions based on user-selected dates and hours. It predicts temperature, humidity, rainfall, and wind speed, with an additional version that also predicts atmospheric pressure.

The project includes two different forecasting approaches, allowing me to explore how different input features and historical weather patterns affect prediction results.

## Project Overview

This project contains two approaches to weather forecasting.

### Version 1: Date and Time-Based Forecasting

The first version uses the hour of the day and day of the year as input features to predict weather conditions.

**Key features:**
- Uses Random Forest Regression with 100 trees.
- Predicts temperature, humidity, rainfall, atmospheric pressure, and wind speed.
- Uses the last 30 days of available data for model evaluation.
- Supports individual dates and date ranges.
- Supports individual hours, time ranges, and full-day forecasts.
- Displays historical and predicted weather separately.
- Generates bar charts to visualize weather conditions.

**Dataset:** `weather_forcast_1.csv`

### Version 2: Historical Weather-Based Forecasting

The second version uses previous weather observations to predict future weather conditions.

The model uses three types of input features:

- Current hour.
- Weather values from 1 hour earlier.
- Weather values from 24 hours earlier.

It learns the relationship between previous weather conditions and the next hour's weather. After predicting the next hour, it uses that prediction as part of the input for subsequent forecasts.

**Key features:**
- Uses Random Forest Regression with 100 trees.
- Predicts temperature, humidity, rainfall, and wind speed.
- Evaluates the model using the last 48 hours of available data.
- Supports individual dates and date ranges.
- Supports individual hours, time ranges, and full-day forecasts.
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
| Scikit-learn | Machine learning implementation |
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

*Note: Update the filenames above if your actual Python scripts or dataset files have different names.*

## Installation and Setup

**1. Clone the repository**

```bash
git clone https://github.com/Py-Tamim/Weather-Forecasting-System.git
```

**2. Navigate to the project directory**

```bash
cd Weather-Forecasting-System
```

**3. Install the required libraries**

```bash
pip install pandas scikit-learn matplotlib numpy
```

Alternatively, install the dependencies using:

```bash
pip install -r requirements.txt
```

## Dataset Requirements

Both versions use historical hourly weather data in CSV format.

### Version 1 Dataset

The `weather_forcast_1.csv` file should contain seven columns in the following order:

```text
date, clock, temperature, humidity, rain, pressure, wind
```

The script assigns these column names automatically, so the CSV column order must match.

### Version 2 Dataset

The `weather_forcast.csv` file should contain hourly weather observations.

The script skips the first three metadata rows and expects the remaining data to have these five columns:

```text
time, temperature, humidity, rain, wind
```

Completely empty columns and rows containing missing values are removed during data preprocessing.

## How to Run

There are two separate Python scripts for the two forecasting approaches.

**Run Version 1:**

```bash
python weather_forecasting.py
```

**Run Version 2:**

```bash
python weather_forecasting_v2.py
```

After running either script, the program asks the user to enter a date or date range and a time or time range.

### Example Inputs

**Single date:**

```text
12-12-2026
```

**Date range:**

```text
12-12-2026 to 15-12-2026
```

**Specific time:**

```text
1 pm
```

**Time range:**

```text
2 am to 6 am
```

**Full-day forecast:**

Press Enter without entering a time.

The system then displays the weather information for the requested dates and hours.

## Model Evaluation

Both versions evaluate their forecasting performance using historical data that is excluded from the training process.

### Version 2 – Sample Evaluation Results

The second version was tested using the last 48 hours of available historical weather data.

| Weather Parameter | Average Absolute Error |
|---|---:|
| Temperature | 2.38 °C |
| Humidity | 5.37 % |
| Rainfall | 0.09 mm |
| Wind Speed | 1.52 km/h |

The evaluation uses Mean Absolute Error (MAE), which measures the average absolute difference between predicted and actual values.

A lower MAE indicates that the predictions are closer to the actual observations.

*These are sample results from one dataset and may change when the dataset or training period changes.*

## Sample Forecast Output

The following table shows selected predictions generated by Version 2 for Dhaka, Bangladesh, on 12 December 2026.

| Time | Temperature | Rainfall | Humidity | Wind |
|---|---:|---:|---:|---:|
| 12:00 AM | 29 °C | 0.1 mm | 73% | 3 mph |
| 6:00 AM | 28 °C | 0.1 mm | 79% | 3 mph |
| 12:00 PM | 33 °C | 0.1 mm | 57% | 3 mph |
| 3:00 PM | 34 °C | 0.1 mm | 53% | 4 mph |
| 6:00 PM | 32 °C | 0.1 mm | 60% | 4 mph |
| 11:00 PM | 30 °C | 0.0 mm | 71% | 3 mph |

*These values are example predictions from a program run, not live weather observations.*

## Data Visualization

Version 1 generates four bar charts using Matplotlib to visualize the predicted weather conditions:

- Temperature (°C)
- Humidity (%)
- Rainfall (mm)
- Wind Speed (mph)

These visualizations make it easier to compare weather conditions across the selected dates and hours.

## AI Assistance and Acknowledgement

During the development of this project, I used AI tools as a learning and development assistant.

I took assistance from AI for:

- Exploring and refining the initial project idea.
- Finding suitable CSV weather datasets for the project.
- Understanding different machine learning approaches for weather forecasting.
- Comparing possible models and selecting Random Forest Regression as the model used in this project.
- Understanding model evaluation, feature selection, and forecasting methods.
- Troubleshooting coding issues and improving my understanding of the implementation.

The project implementation, testing, code modifications, and evaluation were carried out as part of my own learning and development process. I used AI assistance to support my research and understanding rather than treating it as a replacement for learning and experimentation.

## Limitations

- The project uses historical weather data and does not connect to a live weather API.
- Predictions are estimates based on patterns learned from the available dataset.
- Version 1 uses hour and day-of-year features and does not directly consider previous weather measurements.
- Version 2 uses previous weather observations and recursive forecasting, so prediction errors may accumulate over longer forecast periods.
- Forecasts more than 7 days ahead may be less accurate.
- Model performance depends on the quality, quantity, and coverage of the historical dataset.

## Future Improvements

- Integrate a live weather API for real-time weather information.
- Collect and use more historical weather data.
- Experiment with other machine learning models, such as XGBoost.
- Explore deep learning approaches such as LSTM.
- Improve forecasting accuracy, especially for longer prediction periods.
- Develop an interactive weather dashboard.
- Include additional weather parameters.

## Author

**Fuad Tamim**

GitHub: [Py-Tamim](https://github.com/Py-Tamim)

---

*This project was developed as a practical machine learning project to explore weather forecasting, historical data analysis, model evaluation, and data visualization using Python.*
