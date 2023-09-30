import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    # Read CSV into pandas dataframe.
    data = pd.read_csv('shopping.csv')

    # Convert month to integer, where Jan = 0, Feb = 1, ..., Dec = 11.
    data['Month'] = data['Month'].map(lambda x: 0 if x == 'Jan' else 1 if x == 'Feb' else 2 if x == 'Mar' else 3 if x == 'Apr' else 4 if x == 'May' else 5 if x == 'June' else 6 if x == 'Jul' else 7 if x == 'Aug' else 8 if x == 'Sep' else 9 if x == 'Oct' else 10 if x == 'Nov' else 11)

    # Visitor Type to binary dummy variable.
    data['VisitorType'] = data['VisitorType'].map(lambda x: 1 if x == 'Returning_Visitor' else 0)
    # Weekend and Revenue Booleans to binary dummy variable
    data['Weekend'] = data['Weekend'].map(lambda x: 1 if x is True else 0)
    data['Revenue'] = data['Revenue'].map(lambda x: 1 if x is True else 0)

    # Convert columns to integers.
    ints = ['Administrative', 'Informational', 'ProductRelated', 'OperatingSystems', 'Browser', 'Region', 'TrafficType']
    # Convert columns to floats.
    floats = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'BounceRates',
              'ExitRates', 'PageValues', 'SpecialDay']
    
    # Convert columns to integers.
    for i in ints:
        data[i] = data[i].astype('int')
    # Convert columns to floats.
    for i in floats:
        data[i] = data[i].astype('float')


    # Create a list called evidence and append each row of data to it apart from the last column.
    evidence = [data.iloc[i, :-1].tolist() for i in range(len(data))]
    # Create a list called labels and append each row of the last column to it.
    labels = [data.iloc[i, -1].tolist() for i in range(len(data))]

    # Return a tuple of evidence and labels.
    return evidence, labels



def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # Create a KNN model with k=1.
    model = KNeighborsClassifier(n_neighbors=1)
    # Fit the model to the data.
    model.fit(evidence, labels)
    # Return the model.
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # Create a list of true positives.
    tp = [1 for i in range(len(labels)) if labels[i] == 1 and predictions[i] == 1]
    # Create a list of true negatives.
    tn = [1 for i in range(len(labels)) if labels[i] == 0 and predictions[i] == 0]
    # Create a list of false positives.
    fp = [1 for i in range(len(labels)) if labels[i] == 0 and predictions[i] == 1]
    # Create a list of false negatives.
    fn = [1 for i in range(len(labels)) if labels[i] == 1 and predictions[i] == 0]
    # Calculate sensitivity.
    sensitivity = sum(tp) / (sum(tp) + sum(fn))
    # Calculate specificity.
    specificity = sum(tn) / (sum(tn) + sum(fp))
    # Return a tuple of sensitivity and specificity.
    return sensitivity, specificity


if __name__ == "__main__":
    main()
