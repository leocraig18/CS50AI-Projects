# Nim AI

An AI model that teaches itself to play the game of Nim using reinforcement learning.

## Usage

To train the AI and let it play:
``` bash
python3 play.py
```

## Output

During training, you'll observe the AI playing against itself:

Playing training game 1
Playing training game 2
...
Playing training game 10000
Done training

Upon completion, the AI will play and make moves like:

Piles:
Pile 0: 1
Pile 1: 3
Pile 2: 5
Pile 3: 7

AI's Turn
AI chose to take 1 from pile 2.



## Background

Nim is a game that starts with several piles, each containing a number of objects. Players take turns removing any non-negative number of objects from any single non-empty pile. The player who removes the last object loses.

The strategy for this game can be simple when considering a single pile, but becomes more intricate as the number of piles increases. The AI in this project employs Q-learning to determine the best strategy by playing against itself and learning from its actions.

In Q-learning, the AI tries to learn a reward value for every (state, action) pair. An action that leads to a loss gets a reward of -1, an action that results in the other player losing gets a reward of 1, and an action that prolongs the game has an immediate reward of 0 but also future rewards.

## Key Features

- **State Representation**: Each state of the Nim game is defined by the current size of all piles.
  
- **Action Representation**: An action is denoted as a pair of integers `(i, j)`, signifying the removal of `j` objects from pile `i`.

- **Q-Learning**: The AI employs Q-learning to update its knowledge. Every time it's in a state `s` and takes an action `a`, it updates its Q-value based on the formula:

\[
Q(s, a) \leftarrow Q(s, a) + \alpha \times (\text{new value estimate} - \text{old value estimate})
\]

Where \( \alpha \) is the learning rate.

- **Epsilon-Greedy Algorithm**: For action selection, the AI utilizes the epsilon-greedy algorithm, opting for a random available action with a probability of `epsilon` and otherwise choosing the best available action.

## Dependencies

- Python 3.10
- (Optional) numpy, pandas

