class Matrix:
    def __init__(self, name: str):
        self.matrix = None
        self.name = name

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

    def print_m(self):
        len_n = len(self.matrix)
        len_m = len(self.matrix[0])
        max_d = len(str(max([max(a) for a in self.matrix])))
        min_d = len(str(min([min(a) for a in self.matrix])))
        max_len = max(max_d, min_d)
        for n in range(len_n):
            for m in range(len_m):
                len_now = len(str(self.matrix[n][m]))
                if m == 0:
                    print(f'|{self.matrix[n][m]}', end=' ' * (max_len - len_now + 1))
                elif m == len_m - 1:
                    print(f'{self.matrix[n][m]}{" " * (max_len - len_now)}|')
                else:
                    print(f'{self.matrix[n][m]}', end=' ' * (max_len - len_now + 1))
        print()

    @staticmethod
    def isanum(num: str):
        try:
            float(num)
            return True
        except ValueError:
            return False


def main():
    mat = Matrix('test')
    mat.array_enter()
    mat.print_m()
    # while True:
    #     size = input('Enter array size (nxm): ')
    #     if size == '0': exit()
    #     size_temp = size.split('x')
    #     if len(size_temp) == 1:
    #         size_temp.append(size_temp[0])
    #     for num in size_temp:
    #         if not num.isdigit():
    #             print('Wrong size\n')
    #             size_temp = True
    #             break
    #     if size_temp == True:
    #         continue
    #     mat = Matrix(array_enter(int(size_temp[0]), int(size_temp[1])))
    #     mat.print_m()


main()
