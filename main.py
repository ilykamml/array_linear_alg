class Matrix:
    def __init__(self, name: str, mat=None):
        self.name = name
        if mat is not None:
            self.matrix = mat
            self.matrix_param = self.check_matrix_param()
            self.matrix_transposed, self.matrix_param_t = self.matrix_trans()
            self.zeros = self.count_of_zeros()
        else:
            self.array_enter()

    def array_enter(self):
        while True:
            size = input('Enter array size (nxm): ')
            if size == '0':
                exit()
            size_temp = size.split('x')
            if len(size_temp) == 1:
                size_temp.append(size_temp[0])
            for num in size_temp:
                if not num.isdigit():
                    print('Wrong size\n')
                    size_temp = 0
                    break
            if size_temp == 0:
                continue
            break
        n_size, m_size = [int(i) for i in size_temp]
        print()
        matrix = []
        for n in range(n_size):
            while True:
                n_string = input(f'Enter {n + 1} string:\n').strip().split()
                if len(n_string) == m_size:
                    if all(Matrix.isanum(i) for i in n_string):
                        n_string = [int(i) for i in n_string]
                        matrix.append(n_string)
                        break
                print('wrong string')
        print()
        self.matrix = matrix
        self.matrix_param = [n_size, m_size]
        self.matrix_transposed, self.matrix_param_t = self.matrix_trans()
        self.zeros = self.count_of_zeros()

    def check_matrix_param(self):
        return [len(self.matrix), len(self.matrix[0])]

    def matrix_trans(self):
        matrix_t = []
        temp = []
        for n in range(self.matrix_param[0]):
            for m in range(self.matrix_param[1]):
                temp.append(self.matrix[m][n])
            matrix_t.append(temp)
            temp = []
        matrix_param = [len(matrix_t), len(matrix_t[0])]
        return matrix_t, matrix_param

    def print_m(self, arg=0):
        match arg:
            case 0:
                matrix = self.matrix.copy()
                matrix_param = self.matrix_param.copy()
            case 1:
                matrix = self.matrix_transposed.copy()
                matrix_param = self.matrix_param_t.copy()
            case _:
                matrix, matrix_param = [1], [1, 1]
        if sum(matrix_param) == 2:
            print(f'|{matrix[0]}|')
        else:
            len_n, len_m = matrix_param
            max_d = len(str(max([max(a) for a in matrix])))
            min_d = len(str(min([min(a) for a in matrix])))
            max_len = max(max_d, min_d)
            for n in range(len_n):
                for m in range(len_m):
                    len_now = len(str(matrix[n][m]))
                    if m == 0:
                        print(f'|{matrix[n][m]}', end=' ' * (max_len - len_now + 1))
                    elif m == len_m - 1:
                        print(f'{matrix[n][m]}{" " * (max_len - len_now)}|')
                    else:
                        print(f'{matrix[n][m]}', end=' ' * (max_len - len_now + 1))
        print()

    def count_of_zeros(self):
        zeros = [[], []]
        for i in self.matrix:
            zeros[0].append(i.count(0))
        for i in self.matrix_transposed:
            zeros[1].append(i.count(0))
        return zeros

    def det_a(self):
        minors = []
        max_zeros = 0
        for i in self.matrix:
            max_zeros = max(max_zeros, self.matrix.count(0))
        for i, value in enumerate(self.matrix[0]):
            matrix_temp = []
            minor_value = value * (-1)^(i+1) * 0 # доделай это всё до нормального вида
            # сделай поиск максимального количества нолей
            # сделай разложение по строке с максимальным количеством нолей
            # сделай простые преобразования матрицы


    @staticmethod
    def isanum(num: str):
        try:
            float(num)
            return True
        except ValueError:
            return False


def main():
    # mat = Matrix('test')
    # mat.array_enter()
    # mat.print_m()
    # mat.print_m('1')
    # mat.print_m('123')
    # print(mat.zeros)
    mat = Matrix('lol', [[2, 3], [1, 6]])
    mat.print_m()
    mat.print_m(1)


main()
