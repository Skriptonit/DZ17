
class Matrix():
    def __init__(self, my_list,my_list2):
        self.my_list = my_list
        self.my_list2 = my_list2

    def __add__(self):
        self.sub_m = []
        self.sub_m2 = []
        for row in range(len(self.my_list)):
            for col in range(len(self.my_list[row])):
                self.sub_m2.append(self.my_list[row][col] + self.my_list2[row][col])
            self.sub_m.append(self.sub_m2)

    def __str__(self):
        polovina1 = self.sub_m2[0:3]
        polovina2 = self.sub_m2[3:7]
        for i  in polovina1:
            print(f"{i}", end=" ")
        print ('\n ')
        for i2 in polovina2:
          print (f"{i2}", end=" ")
        return ' '

M=Matrix([[1,2,3],[4,5,6]],[[6,5,4],[3,2,1]])
M.__add__()
print (M)