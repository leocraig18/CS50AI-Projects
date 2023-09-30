# Shopping Predictor

An AI-powered tool that predicts whether online shopping customers will complete a purchase based on their online behavior.

## Usage

To predict the customer's shopping behavior:
``` bash
python shopping.py shopping.csv
```

## Output

The program outputs:

- Number of correct predictions
- Number of incorrect predictions
- True Positive Rate
- True Negative Rate

## Background

Online shopping websites often face a challenge: not all visitors end up making a purchase. To optimize user experience, it would be beneficial to predict a user's purchasing intent. Based on this prediction, the website could, for instance, display targeted content or offers. This tool uses machine learning to make such predictions.

Given information about a user, such as the number of pages they've visited, whether they're shopping on a weekend, the web browser they're using, and more, this AI predicts whether the user will complete a purchase. The data used to train the AI comes from about 12,000 user sessions from a shopping website.

## How It Works

1. **Data Interpretation**: The tool reads data from a CSV file, `shopping.csv`, which provides user session data from a shopping website.
   
2. **Model Training**: Using the `train_model` function, the tool trains a nearest-neighbor classifier based on the provided training data.
   
3. **Evaluation**: The tool predicts the purchasing behavior of users in the testing set and then evaluates the sensitivity and specificity of its predictions. Sensitivity represents the proportion of users who made a purchase and were correctly identified, while specificity represents the proportion of users who didn't make a purchase and were correctly identified.

## Features

- **Numeric Data Handling**: All data is numeric, ensuring compatibility with the nearest-neighbor classifier. For instance, months are represented numerically (0 for January, 1 for February, etc.), and user types are categorized as returning (1) or non-returning (0).

- **k-Nearest-Neighbor Classifier**: Uses a k-nearest-neighbor classifier where \( k = 1 \) from the `scikit-learn` library.

- **Performance Metrics**: Measures both sensitivity (true positive rate) and specificity (true negative rate) for a comprehensive understanding of the model's accuracy.

## Dependencies

- Python 3.10
- scikit-learn
- (Optional) numpy, pandas


