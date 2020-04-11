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
        if(not valor.getIsToken()):
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

def consultTranslator(consult,dictionary):
    translation={}
    if(consult.getChilds()[0].getToken() not in dictionary):
        outOfScopeError(consult.getChilds()[0].getToken())

    elif(not isinstance(dictionary[consult.getChilds()[0].getToken()],list)):
        nonIterableObjectError(consult.getChilds()[0].getToken())

    elif(consult.getName()=="ListConsult"):
        var = consult.getChilds()[0].getToken()
        ind=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
        expr=var+"["+str(ind)+"]"
        if(abs(ind)>=len(dictionary[var])):
            outOfBoundsError(ind,expr)
        translation[expr]=dictionary[var][ind]
        return(translation)

    elif (consult.getName() == "MatConsult"):
        var = consult.getChilds()[0].getToken()
        ind1=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
        ind2=int(consult.getChilds()[1].getChilds()[3].getChilds()[1].getChilds()[0].getToken())
        expr=var+"["+str(ind1)+"]"+"["+str(ind2)+"]"
        if(ind1>=len(dictionary[var]) ):
            outOfBoundsError(ind1,expr)
        elif(ind2>=len(dictionary[var][ind1])):
            outOfBoundsError(ind2,expr)

        translation[expr]=dictionary[var][ind1][ind2]
        return (translation)

    elif (consult.getName() == "ThreeDMatConsult"):
        var = consult.getChilds()[0].getToken()
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
        return (translation)


def outOfBoundsError(index,iterable):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Index "+str(index)+" in "+ str(iterable)+" out of bounds ")
    sys.exit()

def outOfScopeError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + str(var) + " hasn't been defined in this scope")
    sys.exit()

def nonIterableObjectError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable " + str(var) + " is not an iterable object")
    sys.exit()

def alreadyDefinedVarError(var,varType):
    if(str(varType)=="<class 'int'>"):
        varType="INT"
    elif (str(varType)=="<class 'bool'>"):
        varType="BOOL"
    elif (str(varType)=="<class 'list'>"):
        varType="LIST"
    print(colorama.Fore.RED + "SEMANTIC ERROR: The global variable " + str(var) + " already exists in this scope as a "+varType+ " variable")
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