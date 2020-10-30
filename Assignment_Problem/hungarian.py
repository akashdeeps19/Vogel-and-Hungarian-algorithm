import math
import numpy as np

class Hungarian:
    def __init__(self, matrix):
        self.cost_matrix = matrix
        self.input_matrix = [[e for e in row] for row in matrix]
        self.pad_matrix(0)
        self.size = (len(self.cost_matrix), len(self.cost_matrix[0]))
        self.results = []
        self.totalPotential = 0

    def pad_matrix(self, x):
        r = len(self.cost_matrix)
        c = max([len(self.cost_matrix[i]) for i in range(r)])

        for i in range(r):
            for j in range(c - len(self.cost_matrix[i])):
                self.cost_matrix[i].append(x)

    def sub_min_from_row(self):
        for i in range(self.size[0]):
            m = min(self.cost_matrix[i])
            for j in range(self.size[1]):
                self.cost_matrix[i][j] -= m
    
    def sub_min_from_col(self):
        for i in range(self.size[1]):
            m = math.inf
            for j in range(self.size[0]):
                m = min(m,self.cost_matrix[j][i])

            for j in range(self.size[0]):
                self.cost_matrix[j][i] -= m

    def get_lines(self):

        total_covered = 0
        cover_zeros = CoverZeros(self.cost_matrix)
        covered_rows = cover_zeros.get_covered_rows()
        covered_columns = cover_zeros.get_covered_columns()
        total_covered = len(covered_rows) + len(covered_columns)

        return total_covered, covered_rows, covered_columns

    def sub_min_from_matrix(self, covered_rows, covered_columns):
        
        elements = []

        for row_index, row in enumerate(self.cost_matrix):
            if row_index not in covered_rows:
                for index, element in enumerate(row):
                    if index not in covered_columns:
                        elements.append(element)
                        
        min_uncovered_num = min(elements)

        uncovered_rows = []
        for index in range(self.size[0]):
            if index not in covered_rows:
                uncovered_rows.append(index)

        for row in uncovered_rows:
            for i in range(self.size[1]):
                self.cost_matrix[row][i] -= min_uncovered_num

        for column in covered_columns:
            for i in range(self.size[0]):
                self.cost_matrix[i][column] += min_uncovered_num

        

    def step5(self, total_lines, covered_rows, covered_columns):

        while total_lines < self.size[0]:
            self.sub_min_from_matrix(covered_rows, covered_columns)
            total_lines, covered_rows, covered_columns = self.get_lines()
            print(self.cost_matrix)

        return total_lines, covered_rows, covered_columns


    def solve(self):

        #Step - 1
        self.sub_min_from_row()

        #Step - 2
        self.sub_min_from_col()

        #Step - 3
        total_lines, covered_rows, covered_columns = self.get_lines()

        print(self.cost_matrix)
        print(covered_rows, covered_columns)
        #Step - 4
        if total_lines < self.size[0]:
            #Step - 5
            self.step5(total_lines, covered_rows, covered_columns)

        required = min(self.size[0], self.size[1])

        zeroes = [[False]*self.size[1] for i in range(self.size[0])]
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.cost_matrix[i][j] == 0:
                    zeroes[i][j] = True
        
        while len(self.results) != required:

            flag = True
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    if self.cost_matrix[i][j] == 0:
                        flag = False
                        break
            
            if flag:
                print("Algorithm couldn't find results for the given input")

            matched_rows, matched_columns = self.find_matches(zeroes)

            total_matched = len(matched_rows) + len(matched_columns)

            if total_matched == 0:
                matched_rows, matched_columns = self.select_arbitrary_match(zeroes)

            # Delete rows and columns
            for row in matched_rows:
                for i in range(len(zeroes[row])):
                    zeroes[row][i] = False

            for column in matched_columns:
                for i in range(len(zeroes)):
                    zeroes[i][column] = False

            # Save Results
            self.save_results(zip(matched_rows, matched_columns))

        # Calculate total potential
        value = 0
        print(self.input_matrix)
        for (row, column) in self.results:
            
            value += self.input_matrix[row][column]

        self.totalPotential = value

    def transpose(self, matrix):

        matrix_t = [[0]*len(matrix) for i in range(len(matrix[0]))]

        for i, row in enumerate(matrix):
            for j, ele in enumerate(row):
                matrix_t[j][i] = ele 

        return matrix_t
            
    def find_matches(self, zeroes):

        marked_rows = []
        marked_columns = []

        # Mark rows and columns with matches
        for index, row in enumerate(zeroes):
            row_index = [index]
            if sum([int(e) for e in row]) == 1:
                for idx, col in enumerate(row):
                    if col == True:
                        column_index = [idx]

                marked_rows, marked_columns = self.mark_rows_and_columns(marked_rows, marked_columns, row_index,
                                                                           column_index)

      
        zeroes_t = self.transpose(zeroes)

        for index, column in enumerate(zeroes_t):
            column_index = [index]
            if sum([int(e) for e in column]) == 1:
                for idx, row in enumerate(column):
                    if row == True:
                        row_index = [idx]

                marked_rows, marked_columns = self.mark_rows_and_columns(marked_rows, marked_columns, row_index,
                                                                           column_index)

        return marked_rows, marked_columns


    def mark_rows_and_columns(self, marked_rows, marked_columns, row_index, column_index):
       
        new_marked_rows = marked_rows
        new_marked_columns = marked_columns

        row_flag = len(marked_rows) == 0 and len(row_index) == 0
        for i in range(min(len(marked_rows),len(row_index) == 0)):
            if marked_rows[i] == row_index[i]:
                row_flag = True
                break

        col_flag = len(marked_columns) == 0 and len(column_index) == 0
        for i in range(min(len(marked_columns),len(column_index) == 0)):
            if marked_columns[i] == column_index[i]:
                col_flag = True
                break

        if row_flag and col_flag:
            new_marked_rows = marked_rows + row_index
            new_marked_columns = marked_columns + column_index

        return new_marked_rows, new_marked_columns       


    def select_arbitrary_match(self, zeroes):

        rows = []
        columns = []
        for i,row in enumerate(zeroes):
            for j, ele in enumerate(row):
                if ele == True:
                    rows.append(i)
                    columns.append(j)

        zeroes_t = self.transpose(zeroes)
    
        zero_count = []
        for index, row in enumerate(rows):
            total_zeros = sum([int(e) for e in zeroes[row]]) + sum([int(e) for e in zeroes_t[columns[index]]])
            zero_count.append(total_zeros)

    
        indices = zero_count.index(min(zero_count))
        row = [rows[indices]]
        column = [columns[indices]]

        return row, column
        
    def save_results(self, result_lists):
        
        for result in result_lists:
            row, column = result

            if row < self.size[0] and column < self.size[1]:
                new_result = (int(row), int(column))
                self.results.append(new_result)


class CoverZeros:

    def __init__(self, matrix):
        matrix = np.array(matrix)
        
        self.zeroes = (matrix == 0)
        self.shape = matrix.shape

        self.choices = np.zeros(self.shape, dtype=bool)

        self.marked_rows = []
        self.marked_columns = []

        self.solve()

        self.covered_rows = list(set(range(self.shape[0])) - set(self.marked_rows))
        self.covered_columns = self.marked_columns

    def get_covered_rows(self):
        return self.covered_rows

    def get_covered_columns(self):
        return self.covered_columns

    def solve(self):

        while True:
            # Erase all marks.
            self.marked_rows = []
            self.marked_columns = []

            # Mark all rows in which no choice .
            for index, row in enumerate(self.choices):
                if not row.any():
                    self.marked_rows.append(index)

            # If no marked rows then finish.
            if not self.marked_rows:
                return True

            # Mark all columns not already marked which have zeros in marked rows.
            num_marked_columns = self.mark_new_columns()

            # If no new marked columns then finish.
            if num_marked_columns == 0:
                return True

            # While there is some choice in every marked column.
            while self.choice_in_marked_columns():
            
                # Mark all rows not already marked which have choices in marked columns.
                num_marked_rows = self.mark_new_rows()

                # If no new marks then Finish.
                if num_marked_rows == 0:
                    return True

                # Mark all columns not already marked which have zeros in marked rows.
                num_marked_columns = self.mark_new_columns()

                # If no new marked columns then finish.
                if num_marked_columns == 0:
                    return True

            
            # Find a marked column that does not have a choice.
            choice_column_index = self.find_column_without_choice()

            while choice_column_index is not None:
                # Find a zero in the column indexed that does not have a row with a choice.
                choice_row_index = self.find_row_without_choice(choice_column_index)

                
                new_choice_column_index = None
                if choice_row_index is None:
                    
                    choice_row_index, new_choice_column_index = \
                        self.find_best_choice_row(choice_column_index)

                  
                    self.choices[choice_row_index, new_choice_column_index] = False

                
                self.choices[choice_row_index, choice_column_index] = True

                choice_column_index = new_choice_column_index

    def mark_new_columns(self):
        num_marked_columns = 0

        for index, column in enumerate(self.zeroes.T):
            if index not in self.marked_columns:
                if column.any():
                    row_indices, = np.where(column)
                    zeros_in_marked_rows = (set(self.marked_rows) & set(row_indices)) != set([])
                    if zeros_in_marked_rows:
                        self.marked_columns.append(index)
                        num_marked_columns += 1

        return num_marked_columns

    def mark_new_rows(self):
        num_marked_rows = 0

        for index, row in enumerate(self.choices):
            if index not in self.marked_rows:
                if row.any():
                    column_index, = np.where(row)
                    if column_index in self.marked_columns:
                        self.marked_rows.append(index)
                        num_marked_rows += 1

        return num_marked_rows

    def choice_in_marked_columns(self):

        for column_index in self.marked_columns:
            if not self.choices[:, column_index].any():
                return False

        return True

    def find_column_without_choice(self):
        for column_index in self.marked_columns:
            if not self.choices[:, column_index].any():
                return column_index

        print("Algorithm has failed to find a column without a choice.")
        exit()

    def find_row_without_choice(self, choice_column_index):
        row_indices, = np.where(self.zeroes[:, choice_column_index])
        
        for row_index in row_indices:
            if not self.choices[row_index].any():
                return row_index

        return None

    def find_best_choice_row(self, choice_column_index):
        row_indices, = np.where(self.zeroes[:, choice_column_index])

        for row_index in row_indices:
            column_indices, = np.where(self.choices[row_index])
            column_index = column_indices[0]
            if self.find_row_without_choice(column_index) is not None:
                return row_index, column_index

        from random import shuffle

        shuffle(row_indices)
        column_index, = np.where(self.choices[row_indices[0]])
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
print(h.results)
print(h.totalPotential)
# cz = CoverZeros(h.cost_matrix)
# print(len(cz.get_covered_columns()) + len(cz.get_covered_rows()))