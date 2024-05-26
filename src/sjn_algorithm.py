try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    import random
except ImportError as import_error:
    print(import_error)


class OptimalServiceClass:
    """
    Class for simulating optimal service scheduling and plotting using the Shortest Job Next (SJN) algorithm.
    """

    def __init__(self, citizens):
        """
        Initialize the OptimalServiceClass with the number of citizens to be served.

        Args:
            citizens (int): The number of citizens to be served.
        """
        self.citizens = citizens  # Total number of citizens to be served
        self.service_times = {}  # Dictionary to store service times for each citizen

    def create_citizens_dictionary(self):
        """
        Create a dictionary with citizens and their service time durations.
        """
        for citizen in range(self.citizens):
            # Generate a random service time for each citizen and round it to 2 decimal places
            self.service_times[f"Citizen {citizen}"] = round(random.uniform(1, 25), 2)

    def sjn_optimal_service_order(self):
        """
        Implement the Shortest Job Next (SJN) algorithm to schedule tasks optimally.

        Returns:
            tuple: A tuple containing a list of sorted tasks with their start times and durations,
            and the total waiting time.
        """
        try:
            # Sort the service times based on the time required
            sorted_citizens = sorted(self.service_times.items(), key=lambda x: x[1])

            # Initialize variables
            total_waiting_time = 0
            current_time = 0
            sorted_times = []

            # Calculate total waiting time and collect sorted times
            for citizen, time in sorted_citizens:
                sorted_times.append((citizen, current_time, time))
                total_waiting_time += current_time
                current_time += time

            return sorted_times, total_waiting_time
        except Exception as error:
            print(error)

    def gantt_plot_tasks(self):
        """
        Plot the tasks scheduled by the Shortest Job Next (SJN) algorithm using a Gantt chart.
        """
        try:
            sorted_times, total_waiting_time = self.sjn_optimal_service_order()

            # Create figure and axis
            fig, ax = plt.subplots()

            # Plot each task as a bar
            for citizen, start_time, duration in sorted_times:
                ax.barh(citizen, duration, left=start_time, color='skyblue')
                ax.text(start_time + duration / 2, citizen, str(duration), va='center', ha='center', color='black', fontsize=10)

            # Set labels and title
            ax.set_xlabel('Time in minutes')
            ax.set_ylabel('Citizens')
            ax.set_title('Tasks Scheduled by Shortest Job Next (SJN) Algorithm',
                         bbox=dict(facecolor='skyblue', alpha=0.5, pad=5), fontweight='bold')

            tasks_patch = mpatches.Patch(color='skyblue', label='Service Time (m)')

            # Add the legend to the plot
            ax.legend(handles=[tasks_patch], loc='upper left')

            # Add x, y gridlines
            ax.grid(True, which='both', color='grey', linestyle='-.', linewidth=0.5, alpha=0.2)

            # Show the plot
            plt.show()
        except Exception as error:
            print(error)


def main():
    try:
        # Create a random integer for the number of citizens to be served
        citizens_num = random.randint(1, 30)

        # Initialize class object
        service_obj = OptimalServiceClass(citizens_num)
        service_obj.create_citizens_dictionary()

        # Plot the tasks
        service_obj.gantt_plot_tasks()
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
