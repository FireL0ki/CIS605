
class Presidents:

    def __init__(self, presidents):
        self.__presidents = presidents

    def num_times_president(self, peron):
        return self.__presidents.count(person)
    
    def num_times_back_to_back_presidents(self):
        num_times = 0

        for index in range(len(self.__presidents)-1):
            if self.__presidents[index] == self.__presidents[index+1]:
                num_times += 1
        return num_times

