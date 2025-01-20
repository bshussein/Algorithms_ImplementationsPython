# Assignment 4: Graphs

# Task 1: Implement a class for a city that has the name of the city, population, and list of cities connected
class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.connected_cities = []

    # Add the destination (other city) if it is not in the connected cities list
    def link_city(self, destination):
        if destination not in self.connected_cities:
            self.connected_cities.append(destination)

    # A string representation of city object (name, population, and connection routes)
    def __repr__(self):
        return f"City: {self.name}, Population: {self.population}, Connection Routes: {[city.name for city in self.connected_cities]}"


# Helper function to remove whitespace in the road and city files
def remove_whitespace(text):
    return text.strip()


# Task 2: Read the city and road data files to create City objects and establish bidirectional connections between them.
def read_city_data(file_name):
    cities = {}
    with open(file_name, 'r') as file:
        for data_line in file:  # Iterate through every row in the file
            name, population = data_line.strip().split(": ")  # splitting the row into name and population
            name = remove_whitespace(name)  # Remove whitespace in the file
            # If a city with this name is not already in the dictionary, add it (duplicate cities will be ignored).
            if name not in cities:
                cities[name] = City(name, int(population))

    return cities


def read_road_data(file_path, cities):
    with open(file_path, 'r') as file:  # Open the road network file in read mode
        for data_line in file:  # Iterate through each row
            departure_city_name, arrival_city_name = data_line.strip().split(": ")  # Split the row into two city names
            departure_city_name = remove_whitespace(departure_city_name)
            arrival_city_name = remove_whitespace(arrival_city_name)

            # Retrieve the City objects
            departure_city = cities.get(departure_city_name)
            arrival_city = cities.get(arrival_city_name)

            # Ensure that both cities are found in the cities dict
            if departure_city and arrival_city:
                departure_city.link_city(arrival_city)  # Add a road from departure to arrival
                arrival_city.link_city(departure_city)  # Add a road from arrival to departure

def task_2_results (file_path, cities):
    with open(file_path, 'w') as f:
        for city in cities.values():
            f.write(f"{city}\n")

# Task 3: Count the number of islands (connected components) in the graph
def count_islands(cities):
    explored_cities = set()  # Keep track of explored cities

    # Function using depth-first search to mark all connected cities as explored
    def dfs(city):
        explored_cities.add(city)  # characterize the current city as explored
        for neighboring_city in city.connected_cities:
            if neighboring_city not in explored_cities:  # If not explored
                dfs(neighboring_city)  # Recursively visit the connected city

    islands_count = 0  # Count the number of islands
    for city in cities.values():  # Go through each city in the dictionary
        if city not in explored_cities:  # If the city hasn't been explored yet
            dfs(city)  # Start a depth-first search from this city
            islands_count += 1  # Increment the island count

    return islands_count


# Task 4: Calculate the population of each island
def island_population(cities):
    explored = set()
    populations = []  # Store population for each island

    # Function to perform Depth-First Search (DFS)
    def dfs(city):
        explored.add(city)
        total_population = city.population  # Current city's population

        for neighboring_city in city.connected_cities:  # Go through connected cities
            if neighboring_city not in explored:  # If neighboring city hasn't been explored
                total_population += dfs(neighboring_city)  # Recursively add population
        return total_population

    for city in cities.values():  # Go through all city objects in the dictionary
        if city not in explored:
            island_pop = dfs(city)  # Use DFS
            populations.append(island_pop)  # Add population of the island to the list

    return populations


# Task 5: Write a function that returns the minimum number of unique highways required to travel between two specified cities in the archipelago
def find_min_highways(start_city, end_city):
    # Base case
    if start_city == end_city:
        return 0, [start_city]

    queue = [(start_city, 0)]  # (city, distance)
    explored = set() # Track explored cities
    paths = {start_city: [start_city]}

    # Use BFS to get the shortest route
    while queue:
        current_city, distance = queue.pop(0)  # Dequeue the first element

        if current_city == end_city:
            return distance, paths[current_city]

        # Iterate through connected cities of the current city
        for neighboring_city in current_city.connected_cities:
            if neighboring_city not in explored:
                explored.add(neighboring_city)  # Mark as explored
                queue.append((neighboring_city, distance + 1)) # Append with incremented distance

                # Record the path to this neighboring city
                paths[neighboring_city] = paths[current_city] + [neighboring_city]

    return -1, [] # No route is found


if __name__ == "__main__":
    # Task 2: Read the text file and construct a graph of cities
    cities = read_city_data('./city_population.txt')  
    read_road_data('./road_network.txt', cities)  

    # Write task 2 results to a relative path
    task_2_results('./Task_2_Results.txt', cities)  


    # Task 3: Count the number of islands
    print("------- Task 3 --------")
    num_islands = count_islands(cities)
    print(f"Number of islands: {num_islands}")

    # Task 4: Get populations of each island
    print("------- Task 4 --------")
    populations = island_population(cities)
    print(f"Total Population of island: {populations}")

    # Task 5: Test the find_min_highways function
    print("------- Task 5 --------")

    start_city_name = 'Pensacola'
    end_city_name = 'Los Angeles'

    # Retrieve the City objects
    start_city = cities.get(remove_whitespace(start_city_name))
    end_city = cities.get(remove_whitespace(end_city_name))

    if start_city and end_city:
        min_highways, path = find_min_highways(start_city, end_city)
        if min_highways != -1:
            print(
                f"The minimum number of unique highways required to travel from {start_city_name} to {end_city_name} is: {min_highways}")
            print("The path is:", " -> ".join(city.name for city in path))
        else:
            print(f"There is no route between {start_city_name} and {end_city_name}.")
    else:
        print("One or both city names are invalid.")
