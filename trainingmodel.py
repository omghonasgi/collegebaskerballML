import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def main():
    data = pd.read_csv('scraped_data.csv', index_col=0)

    # Define features and target
    target = 'Rk'
    features = data.drop(columns=['Rk', 'Team', 'Conf', 'G', 'Rec'], errors='ignore')  # Exclude target and non-numeric columns

# Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        features, data[target], test_size=0.2, random_state=42
)

    # Train a Random Forest Regressor
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

        # Predict on the test set
    predictions = model.predict(X_test)

    # Evaluate the model
    mae = mean_absolute_error(y_test, predictions)
    mae
    


main()