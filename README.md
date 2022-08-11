![title](https://user-images.githubusercontent.com/105242871/184060106-abb6bfbf-eada-49ca-9f89-12ec3ffd2657.jpg)

# 🔆 🄲🄻🄰🅂🅂 🄳🄴🄼🄾🅂 & 🅁🄴🅂🄾🅄🅁🄲🄴🅂

## ◽ Data Acquisition
[Acquire Lesson](acquire_lesson.ipynb)

## ◽ Working with Time Series Data
[Working with Time Series Data in Pandas](working_with_time_series_in_pandas.ipynb)

## ◽ Data Preparation
### Prepare
- The most common activity in preparing time series data is setting dates to datetime types using `pd.to_datetime`.

- Another common activity is looking at the frequency of the data and gaps in time or null values.

### Data Splitting
Splitting time series data into train, test, and validate sets is a little trickier than with previous data we have looked at. Because the data points have an order to them, we **cannot** simply assign each point randomly to train, validate, or test.

Ideally all splits should contain one season's worth of data. There are several methods we can use to split our time series data:

- **Human-based**: use, for example, the last year in the dataset as test split

- **Percentage based**: use the last 20% as test

- **Cross Validate**: break data up into slices and use successive slices as train and test repeatedly (`sklearn.model_selection.TimeSeriesSplit`)

## ◽ Exploratory Analysis
The primary use case for Time Series EDA techniques is when we have a single continuous variable sampled over time and we want to identify **trend** and **seasonality**.


# 🔆 🄴🅇🄴🅁🄲🄸🅂🄴🅂

## ◽ Data Acquisition
[Acquire](acquire.ipynb)

## ◽ Working with Time Series Data
[Working with Times Series Data in Pandas](time_series_data_exercises.ipynb)

## ◽ Data Preparation
[Prepare](prepare.ipynb)

[Prepare Functions](prepare.py)

## ◽ Exploratory Analysis