try:
    import random
    from random_word import RandomWords
except ImportError as import_error:
    print(import_error)


class StringSplittingClass:
    """
    Class for splitting strings with minimum cost.
    """

    def __init__(self, string, cuts):
        """
        Initialize StringSplittingClass with string and cuts.

        Args:
            string (str): The input string to be split.
            cuts (list): List of positions to make cuts in the string.
        """
        self.string = string  # Input string
        self.cuts = cuts  # Positions to make cuts

    def reconstruct_cuts(self, i, j, segments, split_point):
        """
        Reconstruct the cuts made in the string.

        Args:
            i (int): Start index.
            j (int): End index.
            segments (list): List to store segments.
            split_point (list): List of split points.
        """
        try:
            if i + 1 == j:
                return
            k = split_point[i][j]
            segments.append(self.cuts[k])
            self.reconstruct_cuts(i, k, segments, split_point)
            self.reconstruct_cuts(k, j, segments, split_point)
        except Exception as error:
            print(error)

    def cost(self, start, end):
        """
        Calculate the cost of splitting the substring from start to end.

        Args:
            start (int): Start index of substring.
            end (int): End index of substring.

        Returns:
            int: Cost of splitting.
        """
        return end - start

    def split_string_min_cost(self, string, cuts):
        """
        Split the string with minimum cost.

        Args:
            string (str): The input string to be split.
            cuts (list): List of positions to make cuts in the string.

        Returns:
            int: Minimum computational cost.
        """
        try:
            n = len(self.string)
            self.cuts = sorted(self.cuts)  # Sort the cuts array to ensure correct order
            self.cuts = [0] + self.cuts + [n]  # Add the start and end of the string to the cuts
            m = len(self.cuts) - 2

            # Initialize a table to store minimum costs
            dp = [[0] * (m + 2) for _ in range(m + 2)]
            split_point = [[-1] * (m + 2) for _ in range(m + 2)]

            # Calculate cost for substrings
            for length in range(2, m + 2):  # length is the distance between cuts
                for i in range(m + 2 - length):
                    j = i + length
                    dp[i][j] = float('inf')
                    for k in range(i + 1, j):
                        self.cost = dp[i][k] + dp[k][j] + (self.cuts[j] - self.cuts[i])
                        if self.cost < dp[i][j]:
                            dp[i][j] = self.cost
                            split_point[i][j] = k
                        # Detailed printing of the current state
                        print(f"Evaluating substring ({self.cuts[i]}, {self.cuts[j]}): "
                              f"cut at {self.cuts[k]} with cost = {dp[i][k]} + {dp[k][j]} + ({self.cuts[j]} - {self.cuts[i]}) = {self.cost}")
                        print(f"dp[{i}][{j}] = {dp[i][j]}")

            # Detailed printing of the dp table
            print("\nDynamic programming table (dp):")
            for row in dp:
                print(row)

            # Reconstruct the optimal cuts
            segments = []

            self.reconstruct_cuts(0, m + 1, segments, split_point)
            segments.sort()

            # Print the resulting segments
            split_parts = []
            prev_cut = 0
            for cut in segments:
                split_parts.append(string[prev_cut:cut])
                prev_cut = cut
            split_parts.append(string[prev_cut:n])

            print("\nSplit parts of the string:")
            for part in split_parts:
                print(part)

            return dp[0][m + 1]
        except Exception as error:
            print(error)


def main():
    """
    Main function for executing the program.
    """
    try:
        # Create a random english word from RandomWord package
        word = RandomWords()
        string_to_split = word.get_random_word()

        cuts_list = [2, 5]  # Positions of cuts

        # Initialize the class object
        dp_split_obj = StringSplittingClass(string_to_split, cuts_list)

        print(f"String to be split: {string_to_split}", end="\n\n")
        min_cost = dp_split_obj.split_string_min_cost(string_to_split, cuts_list)

        print(f"\nPosition of cuts: {cuts_list}")
        print("Minimum computational cost:", min_cost)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
