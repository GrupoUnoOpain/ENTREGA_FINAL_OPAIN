# How to launch docker
https://dev.to/rajeshj3/dockerize-fastapi-project-like-a-pro-step-by-step-tutorial-7i8

Just execute: docker compose up --build

In the terminal, you have to cd to the repo folder first.

# Example data
Feel free to test it with example_data.json

# GET methods

## GET /predict
Returns valor venta for each marca and all in one (muelle), with a column for each marca.

## GET /analyze_sala
Returns valor venta for each marca and all in one (muelle), with a column for each marca, testing different sala configurations.

## GET /analyze_hour
Returns valor venta for each marca and all in one (muelle), with a column for each marca, testing different hour configurations.

## GET /analyze_week_day
Returns valor venta for each marca and all in one (muelle), with a column for each marca, testing different week day (7 days) configurations.

## GET /analyze_week
Returns valor venta for each marca and all in one (muelle), with a column for each marca, testing different number of week in year configurations.

## GET /analyze_month
Returns valor venta for each marca and all in one (muelle), with a column for each marca, testing different number of month in year configurations.

## GET /analyze_month_day
Returns valor venta for each marca and all in one (muelle), with a column for each marca, testing different number of day in a month configurations.

## GET /model_metrics
Returns model metrics found in training and test. This for each marca model.

## GET /feature_importances
Returns the feature importances. This for each marca model.



