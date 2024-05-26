try:
    import networkx as nx
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import matplotlib as mpl
    import random
    import heapq

    from collections import deque
except ImportError as import_error:
    print(import_error)


class GraphClass:
    """
    Class for generating and analyzing random graphs with Dijkstra's algorithm.
    """

    def __init__(self):
        """
        Initialize the GraphClass with random parameters for nodes and edges.
        """
        self.nodes = random.randint(4, 15)  # Random number of nodes
        self.edges = random.randint(self.nodes, int(self.nodes * (self.nodes - 1) / 2))  # Random number of edges

        # Construct the graph G
        self.G = None  # Graph object
        self.pos = None  # Node positions
        self.shortest_paths = None  # Shortest paths dictionary

    @property
    def nodes(self):
        return self.__nodes

    @nodes.setter
    def nodes(self, value):
        # if not isinstance(value, int) or value < 0:
        #     raise ValueError("Nodes must be a non-negative integer.")
        self.__nodes = value

    @property
    def edges(self):
        return self.__edges

    @edges.setter
    def edges(self, value):
        # if not isinstance(value, int) or value < 0:
        #     raise ValueError("Edges must be a non-negative integer.")
        self.__edges = value

    @property
    def G(self):
        return self.__G

    @G.setter
    def G(self, value):
        self.__G = value

    def create_random_graph(self):
        """
        Generate a random graph with random nodes, edges, and edge weights.
        """
        try:
            # Create the figure
            fig, ax = plt.subplots()
            fig.patch.set_facecolor('black')  # Set background color
            ax.set_facecolor('black')  # Set axis background color
            ax.set_title("Shortest Path on a Graph with Dijkstra Algorithm", color='white',
                         bbox=dict(facecolor='blue', alpha=0.5, pad=5), fontweight='bold')  # Set title with style

            # Create a custom legend
            all_nodes_patch = mpatches.Patch(color='lightblue', label='All Nodes')
            path_nodes_patch = mpatches.Patch(color='red', label='Path Nodes')

            # Add the legend to the plot
            ax.legend(handles=[all_nodes_patch, path_nodes_patch], bbox_to_anchor=(0.8, 1), loc='upper left')

            # Information text
            info_text = "Details about Plot\n\n" \
                        "A random graph with a small number of nodes.\n\n" \
                        "Our goal is to find the shortest path between:\n" \
                        "   -- source node: the minimum value on the graph.\n" \
                        "   -- destination node: the one with the maximum value.\n\n" \
                        "Every edge is weighted with a distance.\n\n" \
                        "The only limitation for building the short path is that every \n" \
                        "distance must be smaller than a given distance L.\n\n" \
                        "Image in Full screen has better analysis."

            ax.text(0.7, -0.35, info_text, transform=ax.transAxes, wrap=True, horizontalalignment='left', fontsize=12,
                    color='white', bbox=dict(facecolor='blue', alpha=0.5, pad=5))  # Add information text

            # Adjust layout to make room for the text
            plt.subplots_adjust(bottom=0.3)

            # Generate a random graph with nodes and edges
            self.G = nx.gnm_random_graph(self.nodes, self.edges)

            # Assign random weights - lengths to the edges
            for (u, v) in self.G.edges():
                self.G.edges[u, v]['distance'] = random.randint(1, 12)

            # Draw the graph
            self.pos = nx.spring_layout(self.G, seed=42)  # positions for all nodes
            nx.draw(self.G, self.pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, ax=ax)
            labels = nx.get_edge_attributes(self.G, 'distance')
            nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=labels)

            return self.G
        except Exception as error:
            print(error)

    def reconstruct_path(self, predecessors, end):
        """
        Reconstruct the shortest path from predecessors and end node.

        Args:
            predecessors (dict): Predecessor dictionary.
            end (int): End node.

        Returns:
            list: Shortest path from start to end node.
        """
        try:
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = predecessors[current]
            path.reverse()
            return path
        except Exception as error:
            print(error)

    def draw_path(self, path):
        """
        Highlight the path nodes on the graph.

        Args:
            path (list): List of nodes in the shortest path.
        """
        try:
            path_edges = list(zip(path, path[1:]))  # Create a list of edges in the path

            nx.draw_networkx_nodes(self.G, self.pos, nodelist=path, node_color='red', node_size=500)
            nx.draw_networkx_edges(self.G, self.pos, edgelist=path_edges, edge_color='red', width=2, arrows=True,
                                   arrowstyle='-|>',
                                   arrowsize=20)
        except Exception as error:
            print(error)

    def check_journey(self, s, t, L):
        """
        Check if there exists a journey from node s to node t within a maximum distance L.

        Args:
            s (int): Source node.
            t (int): Destination node.
            L (int): Maximum distance limit.

        Returns:
            bool: True if journey exists, False otherwise.
        """
        try:
            # Initialize a double ended queue
            queue = deque([s])
            visited = set()

            while queue:
                current_city = queue.popleft()
                if current_city == t:
                    return True
                visited.add(current_city)
                for neighbor, distance in self.G[current_city].items():
                    if distance['distance'] <= L and neighbor not in visited:
                        queue.append(neighbor)
            return False
        except Exception as error:
            print(error)

    def dijkstra_shortest_path_with_limit(self, start_node, max_distance):
        """
        Implement Dijkstra's algorithm to find shortest paths within a maximum distance limit.

        Args:
            start_node (int): Start node.
            max_distance (int): Maximum distance limit.

        Returns:
            tuple: Tuple containing distances dictionary and shortest paths dictionary.
        """
        try:
            # Initialize distances dictionary with infinity and set the start node distance to 0
            distances = {node: float('inf') for node in self.G.nodes}
            distances[start_node] = 0

            # Initialize the predecessor dictionary
            predecessors = {node: None for node in self.G.nodes}

            # Priority queue to store (distance, node)
            priority_queue = [(0, start_node)]

            # While there are nodes to process
            while priority_queue:
                # Get the node with the smallest distance
                current_distance, current_node = heapq.heappop(priority_queue)

                # If the popped node distance is greater than the current known distance, skip processing
                if current_distance > distances[current_node]:
                    continue

                # Explode neighbors
                for neighbor in self.G.neighbors(current_node):
                    distance_weight = self.G[current_node][neighbor]['distance']

                    # Skip if the weight exceeds the maximum allowed distance
                    if distance_weight > max_distance:
                        continue

                    distance = current_distance + distance_weight

                    # If the calculated distance is less than the known distance, update and push to priority queue
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        predecessors[neighbor] = current_node
                        heapq.heappush(priority_queue, (distance, neighbor))

            self.shortest_paths = {node: self.reconstruct_path(predecessors, node) for node in self.G.nodes
                                   if distances[node] != float('inf')}
            return distance, distances, self.shortest_paths
        except Exception as error:
            print(error)


def main():
    """
    Main function for executing the program.
    """
    try:
        graph = GraphClass()
        graph.create_random_graph()

        s = min(graph.G.nodes())
        L = 10
        t = max(graph.G.nodes())

        print(f"Start node s: {s}")
        print(f"End node t: {t}")
        print(f"Maximum distance for full tank capacity L: {L} km", end="\n\n")

        if graph.check_journey(s, t, L):
            print(f"Journey from city s (node {s}) to city t (node {t}) is possible.", end="\n\n")
            max_distance, distances, shortest_paths = graph.dijkstra_shortest_path_with_limit(s, L)
            graph.draw_path(shortest_paths.get(t))
            print("----------")
            print(f"From s: node {s} to t: node {t} the shortest path is: {shortest_paths.get(t)}")
            print(f"Total distance from s to t: {distances.get(t)} km.")
            print(f"Maximum distance: {max_distance} km.")
        else:
            print(f"All distances connecting s to neighbors are greater than L minimum: {L} km.")

        plt.show()
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
