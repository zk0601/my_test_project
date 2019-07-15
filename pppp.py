
class Solution(object):
    def __init__(self, row):
        self.row = row
        self.count = 0

    def get_other(self, num):
        if num % 2 == 0:
            return num + 1
        else:
            return num - 1

    def func(self):
        for i in range(0, len(self.row), 2):
            if self.row.index(self.get_other(self.row[i])) == i+1:
                continue
            i_index = i
            i_name = self.row[i_index]
            i_lover_name = self.get_other(i_name)
            i_lover_index = self.row.index(i_lover_name)

            i_table_index = i+1
            i_table_name = self.row[i_table_index]
            i_table_lover_name = self.get_other(i_table_name)
            # i_table_lover_index = self.row.index(i_table_lover_name)

            i_lover_table_index = self.get_other(i_lover_index)
            i_lover_table_name = self.row[i_lover_table_index]

            if i_table_lover_name == i_lover_table_name:
                self.row[i_lover_index], self.row[i_table_index] = i_table_name, i_lover_name
                self.count += 1

        for i in range(0, len(self.row), 2):
            if self.row.index(self.get_other(self.row[i])) == i+1:
                continue
            i_index = i
            i_name = self.row[i_index]
            i_lover_name = self.get_other(i_name)
            i_lover_index = self.row.index(i_lover_name)

            i_table_index = i+1
            i_table_name = self.row[i_table_index]

            self.row[i_lover_index], self.row[i_table_index] = i_table_name, i_lover_name
            self.count += 1

        return self.count


if __name__ == '__main__':
    a= Solution([3,2,0,1])
    a.func()