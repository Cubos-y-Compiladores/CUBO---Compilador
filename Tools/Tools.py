import sys
from pip._vendor import colorama

def tokenTranslator(token):
    if (token == "TRUE"):
        return True
    elif (token == "FALSE"):
        return False
    elif (token == "PLUS"):
        return "+"
    elif (token == "MINUS"):
        return"-"
    elif (token == "TIMES"):
        return"*"
    elif (token == "DIVIDE"):
        return"/"
    elif (token == "EXP"):
        return"**"
    elif (token == "DIVENT"):
        return"//"
    elif (token == "MOD"):
        return"%"
    elif (token == "LPARENT"):
        return"("
    elif (token == "RPARENT"):
        return")"

    else:
        token=token.split()
        result=""
        for valor in token:
            if(valor.isdigit()):
                result+=str(valor)
            else:
                result+=tokenTranslator(valor)
        return eval(result)


def listTranslator(valores):
    lista = []
    for valor in valores:
        if (valor.getName() == "ListV"):
            lista.append(tokenTranslator(valor.getChilds()[0].getChilds()[0].getToken()))

        elif (valor.getName() == "ListT0"):
            lista.extend(listTranslator(valor.getChilds()))

        elif (valor.getName() == "ListT1"):
            lista.extend(listTranslator(valor.getChilds()))
            return lista
    return lista

def matTranslator(valores):
    matriz=[]
    for valor in valores:
        if (valor.getName() == "MatV"):
            matriz.append(listTranslator(valor.getChilds()[0].getChilds()[1].getChilds()))

        elif (valor.getName() == "MatT0"):
            matriz.extend(matTranslator(valor.getChilds()))

        elif (valor.getName() == "MatT1"):
            matriz.extend(matTranslator(valor.getChilds()))
    return matriz

def threeDmatTranslator(valores):
    ThreeDmat=[]
    for valor in valores:
        if(valor.getName()=="ThreeDMatV"):
            ThreeDmat.append(matTranslator(valor.getChilds()[0].getChilds()[1].getChilds()))

        elif(valor.getName()=="ThreeDMatT0"):
            ThreeDmat.extend(threeDmatTranslator(valor.getChilds()))

        elif(valor.getName()=="ThreeDMatT1"):
            ThreeDmat.extend(threeDmatTranslator(valor.getChilds()))

    return ThreeDmat

def arithmeticTranslator(operacion,dictionary):
    result=""
    operacion=operacion.getChilds()
    for valor in operacion:
        if(not valor.isToken()):
            result+=arithmeticTranslator(valor,dictionary)
        else:
            token = valor.getToken()
            if(valor.getName()=="Id"):
                if(token in dictionary):
                    if(str(type(dictionary[token]))=="<class 'int'>"):
                        result+=str(dictionary[token])+" "
                    else:
                        nonArithmeticVariableError(token)
                else:
                    outOfScopeError(token)

            else:
                result+=str(token)+" "


    return result

def consultTranslator(consult,localdictionary,globallocallist,globaldictionary,scopeType):
    translation={}
    dictionary={}
    if(scopeType=="local"):
        if(consult.getChilds()[0].getToken() not in localdictionary and consult.getChilds()[0].getToken() not in globallocallist):
            outOfAnyScopeError(consult.getChilds()[0].getToken())
        dictionary=localdictionary.copy()
        for valor in globallocallist:
            dictionary[valor]=globaldictionary[valor]

    elif(scopeType=="global"):
        if (consult.getChilds()[0].getToken() not in globaldictionary ):
            outOfScopeError(consult.getChilds()[0].getToken())
        dictionary = globaldictionary.copy()

    if(not isinstance(dictionary[consult.getChilds()[0].getToken()],list)):
        nonIterableObjectError(consult.getChilds()[0].getToken())

    elif(consult.getName()=="ListConsult"):
        var = consult.getChilds()[0].getToken()
        dimensionVerifier(var,dictionary,"ListConsult")
        ind=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
        expr=var+"["+str(ind)+"]"
        if(abs(ind)>=len(dictionary[var])):
            outOfBoundsError(ind,expr)
        translation[expr]=dictionary[var][ind]
        return translation

    elif (consult.getName() == "MatConsult"):
        var = consult.getChilds()[0].getToken()
        dimensionVerifier(var, dictionary, "MatConsult")
        ind1=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
        ind2=int(consult.getChilds()[1].getChilds()[3].getChilds()[1].getChilds()[0].getToken())
        expr=var+"["+str(ind1)+"]"+"["+str(ind2)+"]"
        if(ind1>=len(dictionary[var]) ):
            outOfBoundsError(ind1,expr)
        elif(ind2>=len(dictionary[var][ind1])):
            outOfBoundsError(ind2,expr)

        translation[expr]=dictionary[var][ind1][ind2]
        return translation

    elif (consult.getName() == "ThreeDMatConsult"):
        var = consult.getChilds()[0].getToken()
        dimensionVerifier(var, dictionary, "ThreeDMatConsult")
        ind1=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
        ind2=int(consult.getChilds()[1].getChilds()[3].getChilds()[1].getChilds()[0].getToken())
        ind3=int(consult.getChilds()[1].getChilds()[3].getChilds()[3].getChilds()[1].getChilds()[0].getToken())
        expr=var+"["+str(ind1)+"]"+"["+str(ind2)+"]"+"["+str(ind3)+"]"
        if (ind1 >= len(dictionary[var])):
            outOfBoundsError(ind1, expr)
        elif (ind2 >= len(dictionary[var][ind1])):
            outOfBoundsError(ind2, expr)
        elif (ind3 >= len(dictionary[var][ind1][ind2])):
            outOfBoundsError(ind3, expr)
        translation[expr]=dictionary[var][ind1][ind2][ind3]
        return translation

def functionTranslator(function):
    if(function.getName() == "RangeF"):
        size=int(function.getChilds()[2].getToken())
        boolValue=tokenTranslator(function.getChilds()[4].getChilds()[0].getToken())
        output=[]
        for v in range(size):
            output.append(boolValue)
        return output

def parameterTranslator(parameters):
    output=[]
    for param in parameters:
        if(param.getName()=="ProcParam"):
            output.append(param.getChilds()[0].getToken())

        elif(param.getName()=="Parameter0"):
            output.append(param.getChilds()[0].getChilds()[0].getToken())

        elif(param.getName()=="Parameter1"):
            output.extend(parameterTranslator(param.getChilds()))
    return output

def processBodyTranslator(procLines):
   queue=[]
   for valor in procLines:
       if(valor.isNull()):
           break

       elif("AltContent" in valor.getName()):
           queue.append(valor.getChilds()[0])

       elif(valor.getName()=="AltBlock"):
         queue.extend(processBodyTranslator(valor.getChilds()))

   return queue
def globalSplitter(globals):
    output=[]
    for valor in globals:
        if(valor.getName()=="Id"):
            output.append(valor.getToken())
        elif(valor.getName()=="GlobalTerm0"):
            output.extend(globalSplitter(valor.getChilds()))
        elif(valor.getName()=="GlobalTerm1"):
            output.append(valor.getChilds()[0].getToken())
    return output
def dimensionVerifier(var,dictionary,consultType):
    estructure=dictionary[var]
    output=[]
    types=["List","Matrix","3D Matrix"]
    temp=type(estructure)
    temp2=type(True)
    if(type(estructure)!=type([])):
        nonIterableObjectError(var)

    elif(type(estructure[0])==type(True)):
        output=[True,False,False]

    elif (type(estructure[0]) == type([])):
        if(type(estructure[0][0])==type([])):
            output=[True,True,True]
        else:
            output = [True, True, False]

    ind=-1
    for value in output:
        if(value==False):
            break
        ind+=1
    if(consultType=="ListConsult" and output[0]==False):
        incompatibleConsultError(var,consultType,types[ind])
    elif(consultType=="MatConsult" and output[1]==False):
        incompatibleConsultError(var, consultType, types[ind])
    elif (consultType == "ThreeDMatConsult" and output[2] == False):
        incompatibleConsultError(var, consultType, types[ind])

def typeVerifier(varType,value):
    if (varType == "" or varType == type(value)):
        return True
    return False
def existenceVerifier(var,localScope,localGlobalScope):
    if(var in localScope or var in localGlobalScope):
        return True
    return False
def matVerifier(var):
    if (type(var) == type([])):
        if (type(var[0]) == type([])):
            return True
    return False

def matrixVerifier(var):
    if(type(var)==type([])):
        if(type(var[0])==type([])):
            if (type(var[0][0]) == type([])):
                return False
            return True
    return False

def threeDMatrixVerifier(var):
    if (type(var) == type([])):
        if (type(var[0]) == type([])):
            if (type(var[0][0]) == type([])):
                return True
            return False
    return False

def matBoundsVerifier(mat):
    if(matrixVerifier(mat)):
        return[len(mat),len(mat[0])]

    elif(threeDMatrixVerifier(mat)):
        return[len(mat[0]),len(mat[0][0]),len(mat)]

def outOfBoundsError(index,iterable):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Index "+str(index)+" in "+ str(iterable)+" out of bounds ")
    sys.exit()

def outOfGlobalScopeError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + str(var) + " hasn't been defined in the global scope")
    sys.exit()

def outOfScopeError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + str(var) + " hasn't been defined in this scope")
    sys.exit()

def nonIterableObjectError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + str(var) + " is not an iterable object")
    sys.exit()

def alreadyDefinedVarError(var,varContent):
    if(str(type(varContent))=="<class 'int'>"):
        varType="INT"
    elif (str(type(varContent))=="<class 'bool'>"):
        varType="BOOL"
    elif (str(type(varContent))=="<class 'list'>"):
        if(threeDMatrixVerifier(varContent)):
            varType = "3DMATRIX"
        elif(matrixVerifier(varContent)):
            varType = "MATRIX"
        else:
            varType="LIST"
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + str(var) + " already exists in this scope as a "+varType+ " variable")
    sys.exit()

def alreadyDefinedConstError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The configuration constant " + var + " has already been defined ")
    sys.exit()

def globalConsultError():
    print(colorama.Fore.RED + "SEMANTIC ERROR: List and Matrix positions can't be defined as global variables")
    sys.exit()

def nonArithmeticVariableError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: variable "+str(var)+" is not a variable arithmetical operations can be done with")
    sys.exit()

def sameFirmProcedureError(procName,parLen):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The procedure " + procName + " has already been defined with "+ parLen +" parameters")
    sys.exit()

def outOfAnyScopeError(var):
    print( colorama.Fore.RED + "SEMANTIC ERROR: The variable "+var+" hasn't been defined in the local or global scope")
    sys.exit()

def insertOnNotIterableObjectError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + var + " is not an iterable object, therefore insertion operations can't be performed on it")
    sys.exit()

def insertingBoolOnMatObjectError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + var + " is a matrix or 3Dmatrix object, therefore the insertion of boolean values is forbidden")
    sys.exit()

def insertingListOnNoMatObjectError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + var + " is a not matrix object, therefore the insertion of list values is forbidden")
    sys.exit()

def delOnNotIterableObjectError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + var + " is not an iterable object, therefore del operations can't be performed on it")
    sys.exit()

def incompatibleConsultError(var,consultType,type):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + var + " is a "+type+ " and "+consultType+"s can't be made on it ")
    sys.exit()

def negOnNotBooleanError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + var + " is not a boolean or list object, therefore it can't be denied with Neg")
    sys.exit()

def tfOnNotBooleanError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + var + " is not a boolean or list object, therefore the function T or F can't be used on it ")
    sys.exit()

def BlinkOnNotBooleanError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + var + " is not a boolean or list object, therefore the function Blink can't be used on it ")
    sys.exit()

def shapeOnNotMatrixError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value in " + var + " is not a Matrix object, therefore the function Shape can't be used on it ")
    sys.exit()

def deleteOnNotMatrixError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value in " + var + " is not a Matrix object, therefore the function Delete can't be used on it ")
    sys.exit()

def wrongOperationNumberError(operation):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The "+ operation +" operation only accepts 1 or 0 in the operation type index")
    sys.exit()

def differentSizeInsertion(list,functionStat):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The list" + list + " in "+functionStat+" is not the same size as the others in the stucture it is being tried to insert")
    sys.exit()

def insertingOnListInsideMatrixError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in "+var+" is a Matrix or a 3DMatrix object and inserting an element in one of it's Lists would alter it's integrity ")
    sys.exit()