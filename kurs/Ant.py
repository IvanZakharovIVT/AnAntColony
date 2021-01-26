class Ant:
    """Класс муравей.
Конструктор ничего не принимает.
    """
    
    def __init__(self):
        self.S = []

    def addState(self, a, S):
        """Метод для перехода на новое состояние.
        Метод принимает текущее состояние.
        """

        self.S.append(a)
        s_min = 99
        s_i = -1
        for sc in S:
            if sc not in self.S:
                if S[sc] < s_min:
                    s_min = S[sc]
                    s_i = sc
        return s_i

    def __repr__(self):
        ret = ""
        for s in self.S:
            ret += f"S{s} "
        return ret.strip()

def generateTests(Graph):
    """Генерация тестов муравьиным алгоритмом.
        
        Keyword arguments:
        Graph -- граф-представление UML схемы

    """

    stateCount = len(Graph)

    stateList = []
    out = []
    while len(stateList) < stateCount:
        i = 0
        ant = Ant()
        while i >= 0:
            i1 = ant.addState(i, Graph[i])
            if i1 >= 0:
                Graph[i][i1] += 1
            i = i1
        out.append(ant.S)
        stateList = list(set(stateList + ant.S))
    return out