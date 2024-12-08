
class Data :

    lines = []
    leftArray = []
    RightArray = []
    result = 0


    def __init__(self):
        file = open('data.txt', 'r')
        self.lines = file.readlines()
        file.close()
        self.separteLines()

    def separteLines(self):
        for i in range(len(self.lines)):
             # print(str(i) + " : " + lines[i])
            data = self.lines[i].split('   ')
            self.leftArray.append(data[0].replace('\n', ''))
            self.RightArray.append(data[1].replace('\n', ''))

    def getSmallestDiff(self):
        left = min(self.leftArray)
        right = min(self.RightArray)
        if (left < right):
            result = int(right) - int(left)
        else :
            result = int(left) - int(right)

        self.leftArray.remove(left)
        self.RightArray.remove(right)

        return result

    def getResultPartOne(self):
        for i in range( len(self.leftArray)):
            val = self.getSmallestDiff()
            self.result += val
        return self.result

    def getResultPartTwo(self):
        tampon = 0
        for i in range( len(self.leftArray)):
            for y in range(len(self.RightArray)):
                if(self.leftArray[i] == self.RightArray[y]):
                    tampon += 1
            a = tampon * int(self.leftArray[i])
            self.result += a
            tampon = 0

        return self.result