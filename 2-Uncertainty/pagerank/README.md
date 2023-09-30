# PageRank

An AI-powered tool designed to rank web pages by their importance, inspired by Google's PageRank algorithm.

## Table of Contents

- [PageRank](#pagerank)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Background](#background)
    - [Random Surfer Model](#random-surfer-model)
    - [Iterative Algorithm](#iterative-algorithm)
  - [Usage](#usage)
  - [Algorithm](#algorithm)
    - [Transition Model](#transition-model)
    - [Sample PageRank](#sample-pagerank)
    - [Iterate PageRank](#iterate-pagerank)
  - [Understanding](#understanding)
  - [Contributing](#contributing)

## Introduction

When search engines like Google display search results, they prioritize the "important" and higher-quality pages. But how does the search engine determine which pages are more significant than others?

The PageRank algorithm was created by Google’s co-founders to address this challenge. This project implements PageRank using two approaches: the Random Surfer Model and an Iterative Algorithm.

## Background

PageRank's algorithm considers a website more important if it is linked to by other significant websites. There are multiple strategies for calculating these rankings, two of which have been explored in this project.

### Random Surfer Model

The random surfer model is a hypothetical scenario where a user starts with a web page at random and chooses links to follow at random. This model handles weighting links by their importance.

### Iterative Algorithm

PageRank values for each page can be defined using a recursive mathematical expression. This approach involves repeatedly calculating new rank values based on the current rank values until the values converge.

## Usage
Run the program using:
``` bash
python pagerank.py corpus0
```
Expected Output:
PageRank Results from Sampling (n = 10000)
  1.html: 0.2223
  2.html: 0.4303
  3.html: 0.2145
  4.html: 0.1329
PageRank Results from Iteration
  1.html: 0.2202
  2.html: 0.4289
  3.html: 0.2202
  4.html: 0.1307

## Algorithm

### Transition Model
Given a corpus of web pages, a current page, and a damping factor, the transition model returns a probability distribution over which page a random surfer would visit next.

### Sample PageRank
Accepts a corpus of web pages, a damping factor, and a number of samples, and returns an estimated PageRank for each page.

### Iterate PageRank
Calculates PageRanks based on the iteration formula until the values converge.

## Understanding

The program expects a directory of a corpus of web pages to compute PageRanks for. The corpus is a dictionary where keys represent pages and values are sets of all the pages linked by the key.

## Contributing

Contributions are welcome! Enhance the algorithms, add features, or propose improvements.

