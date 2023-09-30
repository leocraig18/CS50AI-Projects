# Heredity

An AI model designed to harness the power of Bayesian Networks to assess the likelihood of an individual inheriting a specific genetic trait. Genetic trait prediction plays a pivotal role in understanding potential health risks, aiding preventive care, and advancing personalized medicine.

## Overview

- **Objective:** Predict the probability of an individual inheriting a specific genetic trait.
- **Input:** Data about family members, their genetic composition, and any observed traits.
- **Output:** Probability distribution for each individual's genes and the likelihood of them exhibiting the trait in question.

## Usage

Run the program using:

```bash
python heredity.py data/family0.csv
```
Sample output:
Harry:
  Gene:
    2: 0.0092
    1: 0.4557
    0: 0.5351
  Trait:
    True: 0.2665
    False: 0.7335

## Background
This AI model is based on the Bayesian Network concept, considering relationships between family members and how genes might be passed down or mutate. It's particularly focused on the GJB2 gene, a leading cause of hearing impairment in newborns.

## Data 
The program expects CSV files with columns for a person's name, their mother, their father, and a trait indicating whether they exhibit a particular genetic characteristic.





