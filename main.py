class Matrix:
    def __init__(self, name: str, mat=None):
        self.name = name
        if mat is not None:
            self.matrix = mat                                                   # матрица
            self.matrix_param = self.check_matrix_param()                       # параметры матрицы
            self.matrix_transposed, self.matrix_param_t = self.matrix_trans()   # транспонированная матрица и парам
            self.zeros = self.count_of_zeros()                                  # количество нулей в строках и столб
            self.determinant = self.det_a()                                     # детерминант матрицы
        else:
            self.array_enter()                                                  # ввод матрицы

    def array_enter(self):
        while True:  # цикл для ввода параметров матрицы
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
        for n in range(n_size):  # цикл для воода матрицы
            while True:
                n_string = input(f'Enter {n + 1} string:\n').strip().split()
                if len(n_string) == m_size:
                    if all(Matrix.isanum(i) for i in n_string):
                        n_string = [int(i) for i in n_string]
                        matrix.append(n_string)
                        break
                print('wrong string')
        print()
        self.matrix = matrix  # отправка значений в класс
        self.matrix_param = [n_size, m_size]
        self.matrix_transposed, self.matrix_param_t = self.matrix_trans()
        self.zeros = self.count_of_zeros()
        self.determinant = self.det_a()

    def check_matrix_param(self, matrix=None):
        if matrix is not None:
            return [len(matrix), len(matrix[0])]        # параметры заданной матрицы
        return [len(self.matrix), len(self.matrix[0])]  # параметры матрицы

    def matrix_trans(self, matrix=None):
        if matrix is None:              # проверка на отсутствие матрицы
            matrix = self.matrix.copy()
            param = self.matrix_param
        else:                           # задание матрицы, если она есть в аргументах
            matrix = matrix.copy()
            param = self.check_matrix_param(matrix)
        matrix_t = []
        temp = []
        for m in range(param[1]):  # транспонирование
            for n in range(param[0]):
                temp.append(matrix[n][m])
            matrix_t.append(temp)
            temp = []
        matrix_param = [len(matrix_t), len(matrix_t[0])]  # параметры транспонированной матрицы
        return matrix_t, matrix_param

    def print_m(self, arg=0, matrix=None):
        match arg:
            case 0:                                             # обычная печать матрицы
                matrix = self.matrix.copy()
                matrix_param = self.matrix_param.copy()
            case 1:                                             # обычная печать транспонированной матрицы
                matrix = self.matrix_transposed.copy()
                matrix_param = self.matrix_param_t.copy()
            case 2:                                             # заданная печать печать матрицы
                matrix_param = self.check_matrix_param(matrix)
            case _:                                             # печать матрицы, если аргумент странный
                matrix, matrix_param = [1], [1, 1]
        if sum(matrix_param) == 2:                              # если матрица еденичная -> печать значения
            print(f'|{matrix[0][0]}|')
        else:
            len_n, len_m = matrix_param
            max_d = len(str(max([max(a) for a in matrix])))
            min_d = len(str(min([min(a) for a in matrix])))
            max_len = max(max_d, min_d)     # поиск максимальной длинны числа для регулировки печати
            for n in range(len_n):          # печать матрицы
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
            zeros[0].append(i.count(0))  # количество нулей по n строкам
        for i in self.matrix_transposed:
            zeros[1].append(i.count(0))  # количество нулей по m строкам
        return zeros

    def det_a(self, matrix=None):
        if self.matrix_param[0] != self.matrix_param[1]:  # если матрица не квадратная -> детерминант не ищем
            return 0
        det = []
        coords = [0, 1]
        max_zeros = -1
        if matrix is None:  # ищем детерминант для матрицы из класса
            matrix = self.matrix.copy()
            for attitude, att in enumerate(self.zeros):
                for string, num_of_zeros in enumerate(att):
                    if max_zeros < num_of_zeros:
                        max_zeros = num_of_zeros
                        coords = [attitude, string]  # координаты для разложения матрицы по n/m с большим кол-вом нулей
            match coords[0]:
                case 0:
                    matrix = self.matrix.copy()             # 0 для разложения по n
                case 1:
                    matrix = self.matrix_transposed.copy()  # 1 для разложения по m
            if sum(self.matrix_param) == 2:
                return self.matrix[0][0]                    # детерминант матрицы 1х1
            for i, num in enumerate(matrix[coords[1]]):     # поиск детерминанта по формуле
                if num != 0:
                    det_part = num * (-1) ** (i + coords[1]) * self.det_a(self.get_minor(coords[1] + 1, i + 1, matrix))
                    det.append(det_part)
        else:               # ищем детерминант для заданной матрицы
            temp = Matrix('temp', matrix)
            # for attitude, att in enumerate(temp.zeros):  <- пример плохого решения
            #     for string, num_of_zeros in enumerate(att):
            #         if max_zeros < num_of_zeros:
            #             max_zeros = num_of_zeros
            #             coords = [attitude, string]
            # match coords[0]:
            #     case 0:
            #         matrix = temp.matrix.copy()
            #     case 1:
            #         matrix = temp.matrix_transposed.copy()
            # if sum(temp.matrix_param) == 2:
            #     return temp.matrix[0][0]
            # for i, num in enumerate(matrix[coords[1]]):
            #     if num != 0:
            #         det_part = num * (-1) ** (i + coords[1]) * temp.det_a(temp.get_minor(coords[1] + 1, i + 1, matrix))
            #         det.append(det_part)
            return temp.determinant
        if not det:
            det.append(0)

        return sum(det)  # возвращение детерминанта

        # доделай это всё до нормального вида - сделано
        # сделай поиск максимального количества нолей - сделано
        # сделай разложение по строке с максимальным количеством нолей - сделано
        # сделай простые преобразования матрицы - сделано

    def simple_conversions(self, n_source, n_to_conv, digit, transposed=False, matrix=None):
        if matrix is None:  # простые преобразования для матрицы из класса
            if transposed:  # преобразование по m
                matrix = self.matrix_transposed.copy()
            else:           # преобразование по n
                matrix = self.matrix.copy()
        else:               # простые преобразования для заданной матрицы
            if transposed:  # преобразование по m
                matrix, param = self.matrix_trans(matrix)
            else:           # преобразование по n
                matrix = matrix.copy()
        n_source_list = matrix[n_source-1]      # строчка для сложения
        n_to_conv_list = matrix[n_to_conv-1]    # строчка для преобразования
        for i in range(len(n_source_list)):     # преобразование каждого элемента строчки для преобразования
            n_to_conv_list[i] = n_to_conv_list[i] + n_source_list[i] * digit
        matrix[n_to_conv-1] = n_to_conv_list    # перезапись строчки в матрце
        if transposed:                          # если транспонированная -> возвращение в обратное состояние
            matrix, param = self.matrix_trans(matrix)
        return matrix                           # возвращение изменённой матрицы

    def simplifying_the_matrix(self, matrix=None):
        if matrix is None:
            matrix = self.matrix
            matrix_t = self.matrix_transposed
            param = self.matrix_param
            param_t = self.matrix_param_t
        else:
            matrix_t, param_t = self.matrix_trans(matrix)
            param = self.check_matrix_param(matrix)
        # сделай поиск единичек
        # сделай создание нулей через симпл конверсионс
        # сделай переменную стоп крана, если упрощений достаточно
        # а также если не нажать стоп кран - матрица максимально упростится
        # упрощение нужно для более быстрого поиска детерминанта
        # больше нулей - меньше считать миноров

    def get_minor(self, n_minor, m_minor, matrix=None):
        if matrix is None:              # для матрицы класса
            matrix = self.matrix.copy()
            param = self.matrix_param
        else:                           # для заданной матрицы
            param = self.check_matrix_param(matrix)
        minor = []
        n_string = []
        for n in range(param[0]):       # нахождение минора по n и m
            if n + 1 != n_minor:
                for m in range(param[1]):
                    if m + 1 != m_minor:
                        n_string.append(matrix[n][m])
            if n_string:
                minor.append(n_string)
            n_string = []
        return minor

    @staticmethod
    def isanum(num: str):
        try:            # проверка значения на возможность интирования
            float(num)
            return True
        except ValueError:
            return False


def main():
    # mat = Matrix('test')
    matttt = Matrix('big_lol', [
        [53, 42, 76, 23, 76],
        [79, 93, 34, 91, 64],
        [27, 23, 73, 29, 23],
        [23, 74, 23, 93, 65],
        [15, 62, 87, 55, 40]])
    matttt.print_m()
    print(f'det = {matttt.determinant}\n')
    matttt.print_m(2, matttt.simple_conversions(5, 3, -1, True))
    mat = Matrix('lol', [
        [0, 3, 4],
        [1, 0, 5],
        [1, 0, 7]])
    matt = Matrix('lol2', [
        [1, 5],
        [7, 3]])
    mattt = Matrix('lol3', [[10]])
    mat.print_m()
    print(f'det = {mat.determinant}\n')
    matt.print_m()
    print(f'det = {matt.determinant}\n')
    mattt.print_m()
    print(f'det = {mattt.determinant}\n')
    matttt.simplifying_the_matrix([[1,2],[5,3]])

    # manual_enter = Matrix('Manual')
    # manual_enter.print_m()
    # print(f'det = {mattt.determinant}\n')


main()
