
# Island Archipelago Graph Analysis

This repository demonstrates the creation and analysis of a graph representing an island archipelago. The graph consists of cities and highways connecting them. The project includes tasks such as counting connected components (islands), calculating island populations, and finding the shortest path between cities.

---

## Features

### **Task 1: City Class**
- A class `City` is implemented to represent each city.
- **Fields**:
  - `name`: Name of the city.
  - `population`: Population of the city.
  - `connected_cities`: List of cities directly connected to this city via highways.
- **Methods**:
  - `link_city(destination)`: Adds a bi-directional connection to another city.

---

### **Task 2: Construct Graph**
- **Input**: 
  - `city_population.txt`: Contains city names and populations in the format `<city>: <population>`.
  - `road_network.txt`: Contains highways connecting cities in the format `<city 1>: <city 2>`.
- **Output**: Constructs a graph using the `City` class (similar to an adjacency list).

---

### **Task 3: Count Islands**
- **Description**: Counts the number of disconnected components (islands) in the graph.
- **Methodology**: Uses depth-first search (DFS) to explore connected components.

---

### **Task 4: Calculate Island Population**
- **Description**: Calculates the total population of each island in the archipelago.
- **Methodology**: Performs DFS to sum the populations of connected components.

---

### **Task 5: Find Shortest Path**
- **Description**: Finds the minimum number of highways required to travel between two specified cities.
- **Methodology**: Uses breadth-first search (BFS) to find the shortest path.

---

## Example

### Input:
#### `city_population.txt`
```
City A: 1000
City B: 2000
City C: 1500
City D: 1200
```

#### `road_network.txt`
```
City A: City B
City B: City C
City D: City C
```

### Output:
- **Number of Islands**: `1`
- **Island Populations**: `[5700]`
- **Shortest Path**: 
  - From `City A` to `City D`: 
    - Highways: `2`
    - Path: `City A -> City B -> City C -> City D`

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/Graphs_ImplementationPython.git
   ```
2. Navigate to the folder:
   ```bash
   cd Graphs
   ```
3. Place the input files (`city_population.txt` and `road_network.txt`) in the same directory.
4. Run the Python script:
   ```bash
   python graphs.py
   ```

---

## Learning Outcomes

- Understand graph representations and traversal algorithms.
- Calculate connected components and perform operations on graph data.
- Implement shortest path algorithms (BFS) for real-world use cases.

---

This project provides a hands-on understanding of graph analysis and its applications in modeling real-world scenarios.
