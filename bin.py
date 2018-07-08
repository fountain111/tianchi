class Bin:
    def __init__(self):
        self.capacity = 20

        self.contents = []

    def put_item(self,weights):
        if (weights <= self.capacity) & (self.capacity!=0):

            self.capacity -= weights
            self.contents.append(weights)
            return self
        else:
            print('not enough space')

            return False

def first_fit(weights,bin):
    if(bin.put_item(weights)==False):
        return False
        #print('create new bin:',bin.capacity,bin.contents)

    else:
        print('rest capacity and contents:',bin.capacity,bin.contents)
    return bin


weights = [1,3,4,19]

bin = Bin()
list_ = [bin]


while weights:
    weight = weights.pop()
    print('weight:',weight)

    if first_fit(weight,bin):
        #list_.append(first_fit(weight,bin))
        print('fit ok')
    else:
        bin = Bin()
        list_.append(bin)
        first_fit(weight,bin)
    #list_.append(bin)

while list_:
    print(list_.pop().contents)


