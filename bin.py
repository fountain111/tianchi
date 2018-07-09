class Bin:
    def __init__(self,id,disk,cpu):
        self.id = id
        self.disk_capacity = disk
        self.cpu_capacity = cpu
        self.disk_contents = []
        self.cpu_contents = []

    def put_item(self,weights):
        if (weights <= self.capacity) & (self.capacity!=0):

            self.disk_capacity -= weights['disk']
            self.cpu_capacity -= weights['cpu']


            self.cpu_contents.append(weights)['cpu']
            self.disk_contents.append(weights)['disk']

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


# CPU 50%,


print(dict_.disk)

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


