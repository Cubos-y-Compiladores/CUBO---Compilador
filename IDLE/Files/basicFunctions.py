from os import getcwd


def nope(structure):
    if(isinstance(structure,list)):
        if(matVerifier(structure)):
            lin = 0
            if(matrixVerifier(structure)):
                for line in structure:
                    col=0
                    for value in line:
                        structure[lin][col]=not value
                        col+=1
                    lin+=1
            else:
                mat=0
                for matrix in structure:
                    lin=0
                    for line in matrix:
                        col=0
                        for value in line:
                            structure[mat][lin][col]=not value
                            col+=1
                        lin+=1
                    mat+=1
        else:
            ind=0
            for valor in structure:
                structure[ind]=not valor
                ind+=1
    else:
        structure=not structure
    return structure

def tF(structure,type):
    finalValue=None
    if(type=="T"):
        finalValue=True
    elif(type=="F"):
        finalValue=False
    if (isinstance(structure, list)):
        if (matVerifier(structure)):
            col = 0
            lin = 0
            if (matrixVerifier(structure)):
                for line in structure:
                    col = 0
                    for value in line:
                        structure[lin][col] = finalValue
                        col += 1
                    lin += 1
            else:
                mat = 0
                for matrix in structure:
                    lin = 0
                    for line in matrix:
                        col = 0
                        for value in line:
                            structure[mat][lin][col] = finalValue
                            col += 1
                        lin += 1
                    mat += 1
        else:
            ind = 0
            for valor in structure:
                structure[ind] = finalValue
                ind += 1
    else:
        structure = finalValue
    return structure

def Compile(cube, timeM, time):
    output = ""
    mat = 0
    for matrix in cube:
        lin = len(matrix) - 1
        for line in matrix:
            col = 0
            for column in line:
                if (line[col]):
                    output += "point(" + str(mat) + "," + str(col) + "," + str(lin) + ",1);\n"
                #else:
                    #output += "point(" + str(mat) + "," + str(col) + "," + str(lin) + ",0);\n"
                col += 1
            lin -= 1

        if ((mat + 1) % 8 == 0):
            measure = 0
            if (timeM == "Seg"):
                measure += time * 10000
            elif (timeM == "Mil"):
                measure = time * 10
            elif (timeM == "Min"):
                measure = time * 600000
            output += "delay(" + str(measure) + ");\n"
            output += "clear1();\n"
            mat = -1
        mat += 1
    dirWriter(output)

def dirWriter(text):
    dir = getcwd() + "\Output.txt"
    open(dir, "w")
    file = open(dir, "r+")
    file.truncate(0)
    file.close()
    with open(dir, "a") as file:
        file.write(text)
        file.close()
def listVerifier(var):
    if(isinstance(var,list)):
        if(len(var)==0 or isinstance(var[0],bool)):
            return True
    return False
def matVerifier(var):
    if (isinstance(var,list)):
        if (len(var)!=0 and isinstance(var[0],list)):
            return True
    return False

def matrixVerifier(var):
    if(isinstance(var,list)):
        if(len(var)!=0 and isinstance(var[0],list)):
            if (len(var[0])!=0 and isinstance(var[0][0],list)):
                return False
            return True
    return False

def threeDMatrixVerifier(var):
    if (isinstance(var,list)):
        if (len(var)!=0 and isinstance(var[0],list)):
            if (len(var[0])!=0 and isinstance(var[0][0],list)):
                return True
            return False
    return False

def MatrixFliper(structure, type):
    output = []
    if (type == "L"):
        if (matrixVerifier(structure)):
            ind = -1
            for valor in range(len(structure)):
                newList = []
                for line in structure:
                    newList.append(line[ind])
                ind -= 1
                output.append(newList)
        elif (threeDMatrixVerifier(structure)):
            for valor in structure:
                output.append(MatrixFliper(valor, type))
    elif (type == "R"):
        if (self.matrixVerifier(structure)):
            ind = 0
            for valor in range(len(structure)):
                newList = []
                for line in structure:
                    newList.insert(0, line[ind])
                ind += 1
                output.append(newList)
        elif (threeDMatrixVerifier(structure)):
            for valor in structure:
                output.append(MatrixFliper(valor, type))
    return output


def Inserter(type, listed, mat, ind):

    if ind == None:
        ind = len(mat)
    if (type == 0):
        mat.insert(ind, listed)

    elif (type == 1):
        index = 0
        for valor in mat:
            valor.insert(ind, listed[index])
            index += 1
    return mat

def Delete(type, ind, mat):

    if (matrixVerifier(mat)):
        if (type == 0):
            mat.pop(ind)
        else:
            for valor in mat:
                valor.pop(ind)
    else:
        if (type == 0):
            for matrix in mat:
                matrix.pop(ind)
        else:
            for matrix in mat:
                for line in matrix:
                    line.pop(ind)

    return mat

def Typer(value):
    t = ""
    if isinstance(value,list):
        if isinstance(value[0],list):
            if isinstance(value[0][0],list):
                t = "Cube"
            else:
                t = "Matriz"
        else:
            t = "List"

    elif str(value) == "True" or str(value) == "False":
        t = "Bool"
    elif isinstance(value,int):
        t = "Int"
    if mainFrame != None:
        mainFrame.textConsole.AppendText("Variable tipo: " + t + "\n")
    return "Variable tipo: " + t

def Lenght(self,value):
    pass
def Printer(self,value):
    pass


def Neg(value):
    return nope(value)

def T(value):
    t = ""
    if value or not value:
        t = tF(value,"T")
    else:
        t = tF(value,"")
    return t


def F(value):
    t = ""
    if value or not value:
        t = tF(value,"F")
    else:
        t = tF(value,"")
    return t

def Printer(value):
    pass


def Blink(self,value):
    pass
def Delay(self,value):
    pass

def ShapeA(value):
    t = 0
    if isinstance(value,list):
        if isinstance(value[0],list):
            if isinstance(value[0][0],list):
                t = len(value)
    if mainFrame != None:
        mainFrame.textConsole.AppendText("ShapeA Structure: " + str(t) + "\n")
    return t

def ShapeC(value):
    t = 0
    if isinstance(value,list):
        t = len(value)
        if isinstance(value[0],list):
            t = len(value[0])
    if mainFrame != None:
        mainFrame.textConsole.AppendText("ShapeC Structure: " + str(t) + "\n")
    return t

def ShapeF( value):
    t = 0
    if isinstance(value,list):
        t = 1
        if isinstance(value[0],list):
            t = len(value)
    if mainFrame != None:
        mainFrame.textConsole.AppendText("ShapeF Structure: " + str(t) + "\n")
    return t

    def setMainFrame(frame):
        mainFrame = frame
    def getMainFrame(self):
        return mainFrame




