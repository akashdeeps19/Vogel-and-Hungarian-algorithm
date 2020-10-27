import math
import numpy as np

class Hungarian:
    def __init__(self, matrix):
        self.cost_matrix = matrix
        self.pad_matrix(0)
        self.size = len(self.cost_matrix)

    def pad_matrix(self, x):
        r = len(self.cost_matrix)
        c = max([len(self.cost_matrix[i]) for i in range(r)])

        for i in range(r):
            for j in range(c - len(self.cost_matrix[i])):
                self.cost_matrix[i].append(x)

    def sub_min_from_row(self):
        for i in range(self.size):
            m = min(self.cost_matrix[i])
            for j in range(self.size):
                self.cost_matrix[i][j] -= m
    
    def sub_min_from_col(self):
        for i in range(self.size):
            m = math.inf
            for j in range(self.size):
                m = min(m,self.cost_matrix[j][i])

            for j in range(self.size):
                self.cost_matrix[j][i] -= m

    def solve(self):
        self.sub_min_from_row()
        self.sub_min_from_col()

class CoverZeros:

    def __init__(self, matrix):
        """
        Input a matrix and save it as a boolean matrix to designate zero locations.
        Run calculation procedure to generate results.
        """
        matrix = np.array(matrix)
        # Find zeros in matrix
        self._zero_locations = (matrix == 0)
        self._shape = matrix.shape

        # Choices starts without any choices made.
        self._choices = np.zeros(self._shape, dtype=bool)

        self._marked_rows = []
        self._marked_columns = []

        # marks rows and columns
        self.__calculate()

        # Draw lines through all unmarked rows and all marked columns.
        self._covered_rows = list(set(range(self._shape[0])) - set(self._marked_rows))
        self._covered_columns = self._marked_columns

    def get_covered_rows(self):
        return self._covered_rows

    def get_covered_columns(self):
        return self._covered_columns

    def __calculate(self):

        while True:
            # Erase all marks.
            self._marked_rows = []
            self._marked_columns = []

            # Mark all rows in which no choice has been made.
            for index, row in enumerate(self._choices):
                if not row.any():
                    self._marked_rows.append(index)

            # If no marked rows then finish.
            if not self._marked_rows:
                return True

            # Mark all columns not already marked which have zeros in marked rows.
            num_marked_columns = self.__mark_new_columns_with_zeros_in_marked_rows()

            # If no new marked columns then finish.
            if num_marked_columns == 0:
                return True

            # While there is some choice in every marked column.
            while self.__choice_in_all_marked_columns():
                # Some Choice in every marked column.

                # Mark all rows not already marked which have choices in marked columns.
                num_marked_rows = self.__mark_new_rows_with_choices_in_marked_columns()

                # If no new marks then Finish.
                if num_marked_rows == 0:
                    return True

                # Mark all columns not already marked which have zeros in marked rows.
                num_marked_columns = self.__mark_new_columns_with_zeros_in_marked_rows()

                # If no new marked columns then finish.
                if num_marked_columns == 0:
                    return True

            # No choice in one or more marked columns.
            # Find a marked column that does not have a choice.
            choice_column_index = self.__find_marked_column_without_choice()

            while choice_column_index is not None:
                # Find a zero in the column indexed that does not have a row with a choice.
                choice_row_index = self.__find_row_without_choice(choice_column_index)

                # Check if an available row was found.
                new_choice_column_index = None
                if choice_row_index is None:
                    # Find a good row to accomodate swap. Find its column pair.
                    choice_row_index, new_choice_column_index = \
                        self.__find_best_choice_row_and_new_column(choice_column_index)

                    # Delete old choice.
                    self._choices[choice_row_index, new_choice_column_index] = False

                # Set zero to choice.
                self._choices[choice_row_index, choice_column_index] = True

                # Loop again if choice is added to a row with a choice already in it.
                choice_column_index = new_choice_column_index

    def __mark_new_columns_with_zeros_in_marked_rows(self):
        num_marked_columns = 0
        for index, column in enumerate(self._zero_locations.T):
            if index not in self._marked_columns:
                if column.any():
                    row_indices, = np.where(column)
                    zeros_in_marked_rows = (set(self._marked_rows) & set(row_indices)) != set([])
                    if zeros_in_marked_rows:
                        self._marked_columns.append(index)
                        num_marked_columns += 1
        return num_marked_columns

    def __mark_new_rows_with_choices_in_marked_columns(self):
        num_marked_rows = 0
        for index, row in enumerate(self._choices):
            if index not in self._marked_rows:
                if row.any():
                    column_index, = np.where(row)
                    if column_index in self._marked_columns:
                        self._marked_rows.append(index)
                        num_marked_rows += 1
        return num_marked_rows

    def __choice_in_all_marked_columns(self):
        for column_index in self._marked_columns:
            if not self._choices[:, column_index].any():
                return False
        return True

    def __find_marked_column_without_choice(self):
        for column_index in self._marked_columns:
            if not self._choices[:, column_index].any():
                return column_index

        print("Could not find a column without a choice. Failed to cover matrix zeros. Algorithm has failed.")
        exit()

    def __find_row_without_choice(self, choice_column_index):
        row_indices, = np.where(self._zero_locations[:, choice_column_index])
        for row_index in row_indices:
            if not self._choices[row_index].any():
                return row_index

        # All rows have choices. Return None.
        return None

    def __find_best_choice_row_and_new_column(self, choice_column_index):
        """
        Find a row index to use for the choice so that the column that needs to be changed is optimal.
        Return a random row and column if unable to find an optimal selection.
        """
        row_indices, = np.where(self._zero_locations[:, choice_column_index])
        for row_index in row_indices:
            column_indices, = np.where(self._choices[row_index])
            column_index = column_indices[0]
            if self.__find_row_without_choice(column_index) is not None:
                return row_index, column_index

        # Cannot find optimal row and column. Return a random row and column.
        from random import shuffle

        shuffle(row_indices)
        column_index, = np.where(self._choices[row_indices[0]])
        return row_indices[0], column_index[0]




# mat = [[250, 400, 350],
#        [400, 600, 350],
#        [200, 400, 250]]

mat = [[90, 75, 75, 80],
       [35, 85, 55, 65],
       [125, 95, 90, 105],
       [45, 110, 95, 115]]

print(mat)
h = Hungarian(mat)
h.solve()
print(h.cost_matrix)
cz = CoverZeros(h.cost_matrix)
print(len(cz.get_covered_columns()) + len(cz.get_covered_rows()))