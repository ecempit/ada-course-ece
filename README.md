# ADA Course Project :computer: :books:

A simple project, consisting of distinquished and independent small .py files, each one of them providing a solution to algorithm analysis tasks.

This project is primarily developed for personal presentation purposes, showcasing various algorithms and techniques implemented in Python. However, anyone who finds the code useful and wishes to utilize it for their own projects or learning purposes is welcome to do so. Feel free to explore the code, modify it according to your needs, and use it in accordance with the license provided in the repository. If you have any questions or feedback, please don't hesitate to reach out. Happy coding! :muscle:

## Contents <!-- omit in toc -->

- [Structure](#structure)
  - [network_route.py](#network_route.py)
  - [sjn_algorithm.py](#sjn_algorithm.py)
  - [dp_string_split.py](#dp_string_split.py)
- [Installation](#installation)
  - [Using pip](#using-pip)
  - [Using conda](#using-conda)


## Structure

The project consists of three distinquished and independent small .py files:

### network_route.py

This Python script defines a GraphClass that creates a random graph, computes the shortest path between two nodes with Dijkstra's algorithm considering a maximum distance limit, and visualizes the graph and the shortest path using NetworkX and Matplotlib.

To run the script:

1. Ensure you have the required libraries installed (networkx, matplotlib).

2. Copy the script into a Python file (e.g., graph_algorithm.py).

3. Open a terminal or command prompt.

4. Navigate to the directory containing the Python file.

5. Run the script using Python:
   ```cmd
   python graph_algorithm.py
   
The script will generate a random graph, find the shortest path between two random nodes with a maximum distance limit, and display the graph and the shortest path using Matplotlib.

### sjn_algorithm.py

This Python script defines an OptimalServiceClass that simulates scheduling tasks using the Shortest Job Next (SJN) algorithm and visualizes the tasks with a Gantt chart using Matplotlib.

To run the script:

1. Ensure you have the required library installed (matplotlib).

2. Copy the script into a Python file (e.g., optimal_service.py).

3. Open a terminal or command prompt.

4. Navigate to the directory containing the Python file.

5. Run the script using Python:
   ```cmd
   python optimal_service.py

The script will generate a random number of citizens to be served, simulate scheduling their tasks with the SJN algorithm, and display the tasks as a Gantt chart using Matplotlib.

### dp_string_split.py

This Python script defines a StringSplittingClass that implements dynamic programming to find the minimum computational cost of splitting a string at specified positions. The script also demonstrates how to use this class to split a randomly generated English word.

To run the script:

1. Ensure you have the required libraries installed (random, random-word).

2. Copy the script into a Python file (e.g., string_splitting.py).

3. Open a terminal or command prompt.

4. Navigate to the directory containing the Python file.

5. Run the script using Python:
   ```cmd
   python string_splitting.py

The script will generate a random English word, randomly select positions for cuts, split the word using dynamic programming, and print the resulting split parts along with the minimum computational cost.


## Installation

The below are clear instructions for both `pip` and `conda` users on how to install necessary Python packages for the project.

### Using pip

1. Clone the GitHub repository:
   ```sh
   git clone https://github.com/username/repository.git

2. Navigate to the repository directory:
   ```sh
   cd repository
  
3. Install the packages using pip:
   ```sh
   pip install -r requirements.txt
   
### Using conda

1. Clone the GitHub repository:
   ```sh
   git clone https://github.com/username/repository.git
   
2. Navigate to the repository directory:
   ```sh
   cd repository
   
3. Create a conda environment (optional but recommended):
   ```sh
   conda create --name myenv python
   conda activate myenv
   
4. Install the packages via conda environment.yml
   ```sh
   conda env create -f environment.yml
   conda activate myenv
