# Degrees of Separation in Hollywood

Determine the "degrees of separation" between two actors in the world of film.

## Background

The "Six Degrees of Kevin Bacon" game posits that anyone in Hollywood can be linked to Kevin Bacon within six steps, where each step involves identifying a film that two actors have both worked on.

In this project, the goal is to identify the shortest path between two actors by selecting a sequence of films that connects them. For instance, Jennifer Lawrence and Tom Hanks are separated by two degrees: Jennifer Lawrence co-starred with Kevin Bacon in "X-Men: First Class", and Kevin Bacon co-starred with Tom Hanks in "Apollo 13".

This can be visualized as a search problem where:
- **States** are actors.
- **Actions** are films, which transition from one actor to another.

Using breadth-first search, we can determine the shortest path between two actors.

## Dataset

There are two datasets provided:
- **Small**: Contains a subset of data for easy testing and experimentation.
- **Large**: Contains a comprehensive set of data.

Each dataset comprises three CSV files:
- `people.csv`: Contains a unique ID for each actor, along with their name and birth year.
- `movies.csv`: Contains a unique ID for each movie, along with its title and release year.
- `stars.csv`: Maps actor IDs to movie IDs, establishing which actors starred in which films.

## Implementation

The core of the project lies in the `shortest_path` function which is tasked with finding the shortest path (if it exists) between two actors. The path is represented as a list of tuples, where each tuple contains a movie ID and an actor ID.

For example, the list [(1, 2), (3, 4)] indicates:
1. The source actor co-starred in movie 1 with actor 2.
2. Actor 2 co-starred in movie 3 with actor 4 (the target).

## Usage

1. Ensure you have the data directories (`small` and `large`) in the same folder as the script.
2. Run the script using the command: ```python3 degrees.py [directory]``` where [directory] is an optional argument that can be either small or large to specify which dataset to use. If omitted, the program will default to the large dataset.
3. Follow the prompts to input two actor names.
4. The program will output the shortest path between the two actors or notify you if no connection exists.
