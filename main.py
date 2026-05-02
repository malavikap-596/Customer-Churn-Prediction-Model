from src.data_preprocessing import load_data, clean_data, feature_engineering
from src.encoding import encode_data
from src.train_model import split_data, train_model
from src.evaluate_model import evaluate
from src.visualize import plot_confusion_matrix, plot_roc_curve


def main():
    # Load
    df = load_data('data/raw/telco_churn.csv')

    # Process
    df = clean_data(df)
    df = feature_engineering(df)
    df = encode_data(df)

    # Train-test split
    X_train, X_test, y_train, y_test = split_data(df)

    # Train model
    model = train_model(X_train, y_train)

    # Evaluate
    acc, report, cm = evaluate(model, X_test, y_test)

    print("Accuracy:", acc)
    print("\nClassification Report:\n", report)
    print("\nConfusion Matrix:\n", cm)

    # Visualize
    plot_confusion_matrix(model, X_test, y_test)
    plot_roc_curve(model, X_test, y_test)


if __name__ == "__main__":
    main()