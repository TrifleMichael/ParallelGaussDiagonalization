f = open("word")

class Letter:
    def __init__(self, i, j, k, index, label):
        self.i = int(i)
        self.j = int(j)
        self.k = int(k)
        self.index = index
        self.label = label
        self.dependant = []
        self.foataInd = -1

    def checkDependancy(self, other):
        if (
                [self.i, self.k] == [other.j, other.k]
                or [self.i, self.k] == [other.i, other.j]
                or [self.i, self.k] == [other.j, other.j]
        ):
            if other not in self.dependant:
                self.dependant.append(other)

        if (
                [other.i, other.k] == [self.j, self.k]
                or [other.i, other.k] == [self.i, self.j]
                or [other.i, other.k] == [self.j, self.j]
        ):
            if other not in self.dependant:
                self.dependant.append(other)

    def bindDependancies(self, other):
        if other not in self.dependant:
            self.dependant.append(other)
        if self not in other.dependant:
            other.dependant.append(self)

    def isDependant(self, other):
        return self in other.dependant

    def isSecondHandDependant(self, other):
        for eq in self.dependant:
            for eq2 in eq.dependant:
                if eq2 == other:
                    return True
        return False


# Reading file
letters = []
word = []
ind = 0

for i, line in enumerate(f):
    line = line[:-1].split(",")
    letters.append(Letter(line[0], line[1], line[2], ind, "Temporary Label"))
    ind += 1

f.close()

# Calculating dependancies
eqNum = len(letters)
for i in range(eqNum):
    for j in range(i, eqNum):
        letters[i].checkDependancy(letters[j])


# Calculating dependacy and independancy sets
def DSet():
    string = "Sym({"
    for i in range(eqNum):
        for j in range(i, eqNum):
            if letters[i].isDependant(letters[j]):
                string += "(" + letters[i].label + "," + letters[j].label + "),"
    string = string[:-1] + "})+"
    return string


def ISet():
    string = "Sym({"
    for i in range(eqNum):
        for j in range(i + 1, eqNum):
            if not letters[i].isDependant(letters[j]):
                string += "(" + letters[i].label + "," + letters[j].label + "),"
    string = string[:-1] + "})+"
    return string


class LabeledEquation:
    def __init__(self, uniqueLabel, equation):
        self.equation = equation
        self.uniqueLabel = uniqueLabel


class FoataTree:
    def __init__(self, word):
        self.ind = 0
        self.layers = []
        for label in word:
            for eq in letters:
                if eq.label == label:
                    self.addEquation(eq)

    def addEquation(self, equation):
        lastLayerWithDependancy = -1
        for i, l in enumerate(self.layers):
            for eq in l:
                if equation.isDependant(eq.equation):
                    lastLayerWithDependancy = i
        if lastLayerWithDependancy == len(self.layers) - 1:
            self.layers.append([])
        self.layers[lastLayerWithDependancy + 1].append(LabeledEquation(self.ind, equation))
        self.ind += 1

    def printTree(self):
        string = "FNF(given_word) = {"
        for l in self.layers:
            string += "("
            for eq in l:
                string += eq.equation.label + ","
            string = string[:-1] + "),"
        string = string[:-1] + "}"
        print(string)


foataTree = FoataTree(word)