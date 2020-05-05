import sys
from pip._vendor import colorama
from CompilerDependencies.TreeGen import *

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
                    if(isinstance(dictionary[token],int)and not isinstance(dictionary[token],bool)):
                        result+=str(dictionary[token])+" "
                    else:
                        nonArithmeticVariableError(token)
                else:
                    outOfScopeError(token)

            else:
                result+=str(token)+" "


    return result

def consultTranslator(consult,dictionary,expr):
    translation={}
    var = consult.getChilds()[0].getToken()
    if(not isinstance(dictionary[consult.getChilds()[0].getToken()],list)):
        nonIterableObjectError(consult.getChilds()[0].getToken())

    elif(consult.getName()=="ListConsult"):
        ind=None
        indExpr=None
        dimensionVerifier(var,dictionary,"ListConsult")
        if(consult.getChilds()[1].getName()=="ListConsultT0"):
            if(consult.getChilds()[1].getChilds()[1].getName()=="Indice0"):
                ind=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
                indExpr=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()

            elif(consult.getChilds()[1].getChilds()[1].getName()=="Indice1"):
                if(indVerifier(consult.getChilds()[1].getChilds()[1],dictionary)):
                    ind=dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                    indExpr=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            if(abs(ind)>=len(dictionary[var])):
                outOfBoundsError(indExpr,expr)
            translation[expr]=dictionary[var][ind]
            translation["Aux"]="["+str(ind)+"]"
            translation["Flipped"]=None
            return translation
        elif(consult.getChilds()[1].getName()=="ListConsultT1"):
            inf=None
            sup=None
            if(consult.getChilds()[1].getChilds()[1].getName()=="Indice0"):
                inf=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())

            elif(consult.getChilds()[1].getChilds()[1].getName()=="Indice1"):
                if(not indVerifier(consult.getChilds()[1].getChilds()[1],dictionary)):
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
                inf=dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]

            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                sup=int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
            elif (consult.getChilds()[1].getChilds()[3].getName()=="Indice1"):
                if (not indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
                sup= dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
            translation[expr]=dictionary[var][inf:sup]
            translation["Aux"]="["+str(inf)+":"+str(sup)+"]"
            translation["Flipped"]=None
            return translation

    elif (consult.getName() == "MatConsult"):
        ind1=None
        ind2=None
        dimensionVerifier(var, dictionary, "MatConsult")
        if (consult.getChilds()[1].getName() == "MatConsultT0"):
            ind1Expr=None
            ind2Expr=None
            if (consult.getChilds()[1].getChilds()[1].getName() == "Indice0"):
                ind1 = int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
                ind1Expr=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            elif (consult.getChilds()[1].getChilds()[1].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                    ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                    ind1Expr=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())

            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind2 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
                ind2Expr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                    ind2 = dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
                    ind2Expr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
            if (ind1 >= len(dictionary[var])):
                outOfBoundsError(ind1Expr, expr)
            elif(ind2>= len(dictionary[var][ind1])):
                outOfBoundsError(ind2Expr,expr)
            translation[expr]=dictionary[var][ind1][ind2]
            translation["Aux"]="["+str(ind1)+","+str(ind2)+"]"
            translation["Flipped"] = None
            return translation

        elif (consult.getChilds()[1].getName() == "MatConsultT1"):
            indExpr=None
            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind1 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
                indExpr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                    ind1 = dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
                    indExpr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
            if(ind1>=len(dictionary[var][0])):
                outOfBoundsError(indExpr,expr)
            translation[expr]=colFetcher(dictionary[var],ind1)
            translation["Aux"]="[:,"+str(ind1)+"]"
            translation["Flipped"]="["+str(-(ind1+1))+"]"
            return translation

        elif (consult.getChilds()[1].getName() == "MatConsultT2"):
            indExpr = None
            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind1 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
                indExpr = consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                    ind1 = dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
                    indExpr = consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())

            if (ind1 >= len(dictionary[var][0])):
                outOfBoundsError(indExpr, expr)

            dictionary["Temp"] =colFetcher(dictionary[var],ind1)
            tempConsult = consultTranslator(NonTerminalNode("ListConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[5]]),dictionary,expr)
            del dictionary["Temp"]
            translation[expr] = list(tempConsult.values())[0]
            ind=0
            for valor in expr:
                if(valor=="["):
                    expr=expr[ind:]
                    break
            translation["Aux"]=expr
            ind=0
            for valor in expr:
                if(valor=="]"):
                    expr=expr[ind:]
                    break
                ind+=1
            translation["Flipped"]="["+str(-(ind1+1))+expr
            return translation

        elif(consult.getChilds()[1].getName()=="MatConsultT3"):
            if(consult.getChilds()[1].getChilds()[1].getName()=="Indice0"):
                ind1=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            elif (consult.getChilds()[1].getChilds()[1].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                    ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            ind1Expr = consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            if (ind1 >= len(dictionary[var])):
                outOfBoundsError(ind1Expr, expr)
            dictionary["Temp"]=dictionary[var][ind1]
            tempConsult=consultTranslator(NonTerminalNode("ListConsult",[TerminalNode("Id","Temp"),consult.getChilds()[1].getChilds()[3]]),dictionary,expr)
            del dictionary["Temp"]
            translation[expr]=list(tempConsult.values())[0]
            ind = 0
            for valor in expr:
                if (valor == "["):
                    expr = expr[ind: ]
                    break
                ind+=1
            translation["Aux"] = expr
            translation["Flipped"] = None
            return translation

    elif (consult.getName() == "ThreeDMatConsult"):
        if (consult.getChilds()[1].getName() == "ThreeDMatConsultT0"):
            ind1=None
            ind2=None
            ind3=None
            ind1Expr=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            ind2Expr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            ind3Expr=None

            if(consult.getChilds()[1].getChilds()[1].getName()=="Indice0"):
                ind1=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())


            elif(consult.getChilds()[1].getChilds()[1].getName()=="Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                    ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())

            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind2 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())

            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                    ind2 = dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())

            if (consult.getChilds()[1].getChilds()[5].getName() == "Indice0"):
                ind3 = int(consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken())

            elif (consult.getChilds()[1].getChilds()[5].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[5], dictionary)):
                    ind3 = dictionary[consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken()]
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken())

            if(ind1>=len(dictionary[var])):
                outOfBoundsError(ind1Expr,expr)

            elif(ind2>=len(dictionary[var][ind1])):
                outOfBoundsError(ind2Expr,expr)

            elif(ind3>=len(dictionary[var][ind2])):
                outOfBoundsError(ind3Expr,expr)

            translation[expr]=dictionary[var][ind1][ind2][ind3]
            translation["Aux"]="["+str(ind1)+"]["+str(ind2)+"]["+str(ind3)+"]"
            translation["Flipped"] = None
            return translation

        elif(consult.getChilds()[1].getName()=="ThreeDMatConsultT1"):
            ind1 = None
            ind1Expr = consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()

            dimensionVerifier(var, dictionary, "ThreeDMatConsult")
            if (consult.getChilds()[1].getChilds()[1].getName() == "Indice0"):
                ind1 = int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            elif (consult.getChilds()[1].getChilds()[1].getName() == "Indice1"):
                if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                    ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            if (ind1 >= len(dictionary[var])):
                outOfBoundsError(ind1Expr, expr)

            dictionary["Temp"] = dictionary[var][ind1]
            tempConsult = consultTranslator(NonTerminalNode("MatConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[3]]),dictionary,expr)
            if("Temp" in dictionary):
                del dictionary["Temp"]
            translation[expr] = list(tempConsult.values())[0]
            ind = 0
            for valor in expr:
                if (valor == "["):
                    expr = expr[ind:]
                    break
                ind += 1
            if(":," in expr):
                expr=expr.replace(":,","")
                expr=expr.split("][")
                if(len(expr)==2):
                    flip=""
                    altern=""
                    expr[0]=expr[0].replace("[","")
                    expr[1]=expr[1].replace("]","")
                    if(expr[0].isdigit()):
                        flip+="["+expr[0]+"]"
                        altern+="["+expr[0]+"]"
                    else:
                        flip+="["+dictionary[expr[0]]+"]"
                        altern+="["+dictionary[expr[0]]+"]"
                    if (expr[1].isdigit()):
                        flip +="["+str(-(int(expr[1])+1))+"]"
                        altern+="["+str(-(int(expr[1])+1))+"]"
                    else:
                        flip +="["+str(-(int(dictionary[expr[1]])+1))+"]"
                        altern +="["+str(-(int(dictionary[expr[1]])+1))+"]"
                    translation["Aux"]=altern
                    translation["Flipped"]=flip
                elif(len(expr)==3):
                    altern=""
                    flip=""
                    if(":" in expr[2]):
                        expr[0]=expr[0].replace("[","")
                        expr[2]=expr[2].replace("]","")
                        expr.append(expr[2].split(":"))
                        expr.pop(2)

                        if(expr[0].isdigit()):
                            altern+="["+expr[0]+"]"
                            flip +="["+expr[0]+"]"
                        else:
                            altern+="["+str(dictionary[expr[0]])+"]"
                            flip+="["+str(dictionary[expr[0]])+"]"

                        if (expr[1].isdigit()):
                            altern += "[:,"+str(expr[1])+"]"
                            flip += "["+str(-(int(expr[1])+1))+"]"
                        else:
                            altern += "[:,"+str(dictionary[expr[1]])+"]"
                            flip += "["+str(-(dictionary[expr[1]]+1))+"]"

                        if(expr[2][0].isdigit()):
                            altern+="["+expr[2][0]+":"
                            flip+="["+expr[2][0]+":"
                        else:
                            altern += "["+str(dictionary[expr[2][0]])+":"
                            flip+= "["+str(dictionary[expr[2][0]])+":"
                        if (expr[2][1].isdigit()):
                            altern +=expr[2][1] + "]"
                            flip+=expr[2][1] + "]"
                        else:
                            altern +=str(dictionary[expr[2][0]])+"]"
                            flip+=str(dictionary[expr[2][0]])+"]"
                        translation["Aux"]=altern
                        translation["Flipped"]=flip
                    else:
                        expr[0]=expr[0].replace("[","")
                        expr[2]=expr[2].replace("]","")

                        if(expr[0].isdigit()):
                            altern+="["+expr[0]+"]"
                            flip+="["+expr[0]+"]"
                        else:
                            altern+="["+str(dictionary[expr[0]])+"]"
                            flip +="["+str(dictionary[expr[0]])+"]"

                        if (expr[1].isdigit()):
                            altern += "[:,"+expr[1]+"]"
                            flip += "["+str(-(int(expr[1])+1))+"]"
                        else:
                            altern += "[:,"+str(dictionary[expr[1]])+"]"
                            flip += "["+str(-(dictionary[expr[1]]+1))+"]"

                        if (expr[2].isdigit()):
                            altern+="["+expr[2]+"]"
                            flip+="["+expr[2]+"]"
                        else:
                            altern+="["+str(dictionary[expr[2]])+"]"
                            flip+="["+str(dictionary[expr[2]])+"]"
                        translation["Aux"]=altern
                        translation["Flipped"]=flip


                    return translation

            else:
                translation["Flipped"] = None

            if("," in expr):
                expr=expr.split("][")
                expr[0]=expr[0].replace("[","")
                expr[1]=expr[1].replace("]","")
                expr.extend(expr[1].split(","))
                expr.pop(1)
                altern=""
                for valor in expr:
                    if(valor.isdigit()):
                        altern+="["+valor+"]"
                    else:
                        altern+="["+str(dictionary[valor])+"]"
                translation["Aux"]=altern
            elif(":" in expr):
                expr = expr.split("][")
                expr[0] = expr[0].replace("[", "")
                expr[2] = expr[2].replace("]", "")
                expr.append(expr[2].split(":"))
                expr.pop(2)
                altern = ""
                for valor in expr:
                    if (len(valor) == 2):
                        if (valor[0].isdigit()):
                            altern += "[" + valor[0] + ":"
                        else:
                            altern += "[" + str(dictionary[valor[0]]) + ":"
                        if (valor[1].isdigit()):
                            altern += valor[1] + "]"
                        else:
                            altern += str(dictionary[valor[1]]) + "]"
                    elif (valor.isdigit()):
                        altern += "[" + valor + "]"
                    else:
                        altern += "[" + str(dictionary[valor]) + "]"
                translation["Aux"] = altern
            else:
                altern=""
                expr=expr.split("][")
                expr[0]=expr[0].replace("[","")
                expr[2]=expr[2].replace("]","")
                for valor in expr:
                    if(valor.isdigit()):
                        altern+="["+valor+"]"
                    else:
                        altern +="["+str(dictionary[valor])+"]"
                translation["Aux"]=altern
            return translation
def expresionTranslator(consult):
    varName = consult.getChilds()[0].getToken()
    if (consult.getName() == "ListConsult"):
        if (consult.getChilds()[1].getName() == "ListConsultT0"):
            ind =consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            if(varName!="Temp"):
                return varName+"["+ind+"]"
            return "["+ind+"]"

        elif (consult.getChilds()[1].getName() == "ListConsultT1"):
            inf=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            sup=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            if(varName!="Temp"):
                return varName+"["+inf+":"+sup+"]"
            return "["+inf+":"+sup+"]"

    elif (consult.getName() == "MatConsult"):
        if (consult.getChilds()[1].getName() == "MatConsultT0"):
            ind1=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            ind2=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            if(varName=="Temp"):
                return"["+ind1+","+ind2+"]"
            return varName+"[" + ind1 + "," + ind2 + "]"

        elif (consult.getChilds()[1].getName() == "MatConsultT1"):
            ind=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            if(varName=="Temp"):
                return "[:,"+ind+"]"
            return varName+"[:,"+ind+"]"

        elif (consult.getChilds()[1].getName() == "MatConsultT2"):
            ind=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            output=""
            if(varName=="Temp"):
                output+="[:,"+ind+"]"
            else:
                output+=varName+"[:,"+ind+"]"
            output+= expresionTranslator(NonTerminalNode("ListConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[5]]))
            return output

        elif(consult.getChilds()[1].getName()=="MatConsultT3"):
            ind1= consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            output=""
            if(varName=="Temp"):
                output+="["+ind1+"]"
            else:
                output+=varName+"["+ind1+"]"
            output+=expresionTranslator(NonTerminalNode("ListConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[3]]))
            return output
    elif (consult.getName() == "ThreeDMatConsult"):
        if(consult.getChilds()[1].getName()=="ThreeDMatConsultT0"):
            ind1=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            ind2=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            ind3=consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken()

            return varName+"["+ind1+"]["+ind2+"]["+ind3+"]"

        elif(consult.getChilds()[1].getName()=="ThreeDMatConsultT1"):
            ind1= consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            output=varName+"["+ind1+"]"
            output +=expresionTranslator(NonTerminalNode("MatConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[3]]))
            return output



def colFetcher(mat,ind):
    output=[]
    for valor in mat:
        output.append(valor[ind])
    return output
def functionTranslator(function,scope):
    if(function.getName() == "RangeF"):
        size=None
        if (function.getChilds()[2].getName() == "Iterable0"):
            if (indVerifier(function.getChilds()[2].getChilds()[0], scope)):
                size = scope[function.getChilds()[2].getChilds()[0].getChilds()[0].getToken()]
            else:
                nonIterableObjectError("Test")
        elif(function.getChilds()[2].getName() == "Iterable1"):
            size = int(function.getChilds()[2].getChilds()[0].getToken())


        boolValue=tokenTranslator(function.getChilds()[4].getChilds()[0].getToken())
        output=[]
        for v in range(size):
            output.append(boolValue)
        return output

def parameterTranslator(parameters):
    output=[]
    for param in parameters:
        if(param.getName()=="ProcParam"):
            output.append((param.getChilds()[0].getToken(),None))

        elif(param.getName()=="Parameter0"):
            output.append((param.getChilds()[0].getChilds()[0].getToken(),None))

        elif(param.getName()=="Parameter1"):
            output.extend(parameterTranslator(param.getChilds()))
    return output

def parameterCallTranslator(parameters,scope):
    output = []
    for param in parameters:
        if (param.getName() == "CallParam"):
            if(param.getChilds()[0].getName()=="Iterable0"):
                if(param.getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                    if(not param.getChilds()[0].getChilds()[0].getChilds()[0].getToken() in scope):
                        outOfScopeError(param.getChilds()[0].getChilds()[0].getChilds()[0].getToken())
                    output.append(scope[param.getChilds()[0].getChilds()[0].getChilds()[0].getToken()])

                elif(param.getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                    output.append(list(consultTranslator(param.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],scope).values())[0])


            elif(param.getChilds()[0].getName()=="Iterable1"):
                output.append(int(param.getChilds()[0].getChilds()[0].getToken()))

        elif (param.getName() == "Param0"):
            output.extend(parameterCallTranslator(param.getChilds(),scope))

        elif (param.getName() == "Param1"):
            output.extend(parameterCallTranslator(param.getChilds(),scope))
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
    if(not isinstance(estructure,list)):
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
    if(varType==None):
        return True
    if(isinstance(varType,bool) and isinstance(value,bool)):
        return True
    elif(isinstance(varType,int) and isinstance(value,int) and not(isinstance(varType,bool) or isinstance(value,bool))):
        return True
    elif (isinstance(varType,list) and isinstance(value,list)):
        if(matVerifier(varType) and matVerifier(value)):
            if(matrixVerifier(varType) and matrixVerifier(value)):
                return True
            elif(threeDMatrixVerifier(varType) and threeDMatrixVerifier(value)):
                return True
        if(listVerifier(varType) and listVerifier(value)):
            return True
    return False


def existenceVerifier(var,scope):
    if(var in scope):
        return True
    return False
def listVerifier(var):
    if(isinstance(var,list)):
        if(isinstance(var[0],bool)):
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

def matBoundsFetcher(mat):
    if(matrixVerifier(mat)):
        return[len(mat),len(mat[0])]

    elif(threeDMatrixVerifier(mat)):
        return[len(mat[0]),len(mat[0][0]),len(mat)]

def indVerifier(ind,scope):
    if(ind.getChilds()[0].getToken() in scope):
        if(isinstance(scope[ind.getChilds()[0].getToken()],int) and not isinstance(scope[ind.getChilds()[0].getToken()],bool)):
            return True
        return False
    outOfScopeError(ind.getChilds()[0].getChilds()[0].getToken())

def globalFetch(globalScope,varList):
    output={}
    for valor in varList:
        if(valor in globalScope):
            output[valor]=globalScope[valor]
    return output

def scopeSelector(globalScope,localScope,var):
    scope = ""
    if (var in globalScope):
        scope = globalScope
    elif (var in localScope):
        scope = localScope
    return scope

def matrixInserter(type,listed,mat,ind):
    if(type==0):
       mat.insert(ind,listed)

    elif(type==1):
        index=0
        for valor in mat:
            valor.insert(ind,listed[index])
            index+=1
    return mat


def globalUpdater(globalD,localD,localList):
    for valor in localD:
        if(valor in globalD and valor not in localList):
            globalD[valor]=localD[valor]
    return globalD

def nope(structure):
    if(isinstance(structure,list)):
        if(matVerifier(structure)):
            col = 0
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
def structureUpdater(value,structure,expresion,flipped):
    if(":," in expresion):
        structure=matrixFliper(structure,"L")
        exec("structure"+str(flipped)+"="+str(value))
        structure=matrixFliper(structure,"R")
    else:
        temp="structure"+str(expresion)+"="+str(value)
        exec("structure"+str(expresion)+"="+str(value))
    return structure
def matrixFliper(structure,type):
    output=[]
    if(type=="L"):
        if(matrixVerifier(structure)):
            ind = -1
            for valor in range(len(structure)):
                newList=[]
                for line in structure:
                    newList.append(line[ind])
                ind-=1
                output.append(newList)
        elif(threeDMatrixVerifier(structure)):
            for valor in structure:
                output.append(matrixFliper(valor,type))
    elif(type=="R"):
        if (matrixVerifier(structure)):
            ind =0
            for valor in range(len(structure)):
                newList = []
                for line in structure:
                    newList.insert(0,line[ind])
                ind += 1
                output.append(newList)
        elif (threeDMatrixVerifier(structure)):
            for valor in structure:
                output.append(matrixFliper(valor, type))
    return output


def exprFetcher(expr):
    ind=0
    for valor in expr:
        if(valor=="["):
            expr=expr[ind,:]
            break
        ind+=1
    return expr
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
def matrixDeleter(type,ind,mat):
    if(matrixVerifier(mat)):
        if(type==0):
            mat.pop(ind)
        else:
            for valor in mat:
                valor.pop(ind)
    else:
        if(type==0):
            for matrix in mat:
                matrix.pop(ind)
        else:
            for matrix in mat:
                for line in matrix:
                    line.pop(ind)

    return mat

def blockSplitter(block):
    statementQueue=[]
    if(block.isNull()):
        return statementQueue
    statementQueue.append(block.getChilds()[0])
    statementQueue.extend(blockSplitter(block.getChilds()[1]))
    return statementQueue

def procNameFetcher(procedures):
    procs=[]
    for procedure in procedures:
        procs.append(procedure[0])
    return procs

def procParamsFetcher(procName,procedures):
    params=[]
    for proc in procedures:
        if(proc[0]==procName):
            params.append(proc[1])
    return params

def noneVerifier(varName,scope):
    if (not varName in scope):
        return False
    if(scope[varName]==None):
        return True
    return False

def valueValidator(value,scope):
    value = value.getChilds()
    output=True
    for valor in value:
        if (not valor.isToken()):
            output= valueValidator(valor,scope)
            if(not output):
                break
        else:
            token = valor.getToken()
            if (valor.getName() == "Id"):
                if (token in scope):
                    if (noneVerifier(token,scope)):
                        output=False
                else:
                    outOfScopeError(token)
    return output
def nameFetcher(consult):
    output=""
    for valor in consult:
        if(valor=="["):
            break
        output+=valor
    return output
def matBoundVerifier(mat):
    struct=None
    if(matrixVerifier(mat)):
        struct="Mat"
    elif(threeDMatrixVerifier(mat)):
        struct="3dMat"

    if(struct=="Mat"):
        line=len(mat[0])
        for valor in mat:
            if(len(valor)!=line):
                return False
    elif(struct=="3dMat"):
        for valor in mat:
            if(not matBoundVerifier(valor)):
                return False
    return True

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
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + str(var) + " is not an iterable object")
    sys.exit()

def alreadyDefinedVarError(var,varContent):
    if(isinstance(varContent,bool)):
        varType="BOOL"
    elif (isinstance(varContent,int)):
        varType="INT"
    elif (isinstance(varContent,list)):
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
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + var + " is not an iterable object, therefore insertion operations can't be performed on it")
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
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + var + " is not a boolean or list object, therefore it can't be denied with Neg")
    sys.exit()

def tfOnNotBooleanError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in  " + var + " is not a boolean or list object, therefore the function T or F can't be used on it ")
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

def modifyingOnListInsideMatrixError(var,operation):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in "+var+" is a Matrix or a 3DMatrix object and "+operation+" an element in one of it's Lists would alter it's integrity ")
    sys.exit()

def boolOnTempError(consult):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + consult + " is either a list or a boolean and both of this data types are forbiden in the delay time index")
    sys.exit()

def deleteOnMatrixInside3DMatError(consult):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + consult + " is a matrix inside a 3Dmatrix object, therefore the deletion of one of it's lists would alter it's integrity")
    sys.exit()

def notDefinedProcedureCallError(procName):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Procedure "+procName+" hasn't been defined with the used firm")
    sys.exit()
def paramWithSameNameError(name,param):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Procedure "+name+" has 2 or more parameters labeled as "+param+" .All parameters must be labelled with different names")
    sys.exit()
def paramInGlobalsError(proc,param):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Parameter "+param+" in procedure "+proc+" has already been defined as a global variable")
    sys.exit()

def consultOnIndError(operation):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Non integer values are forbidden on the index value of "+operation+" operations")
    sys.exit()

def insertingNotListError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in "+var+" is not a List object and insertion operations on a Matrix only support list objects " )
    sys.exit()

def insertingNotMatrixError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in "+var+" is not a Matrix object and insertion operations on a 3DMatrix only support list objects " )
    sys.exit()

def insertingNotBoolOnListError(var):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + var + " is not a Bool object, therefore it can't be inserted on a List object")
    sys.exit()

def insertingNotBoolOnListError1():
    print(colorama.Fore.RED + "SEMANTIC ERROR: Inserting non-Boolean values on lists is forbidden")
    sys.exit()

def differentDimensionsMatError(value):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The matrix "+str(value)+" has lines with different sizes, therefore it's not a valid matrix")
    sys.exit()
def differentMatOnThreeDMatError(value,value1):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The matrix stored in "+value+" has a different size than "+str(value1)+", so it can't be replaced since it is inside a 3DMatrix")
    sys.exit()

def modifyingMatrixWithDifferentSizeLineError(expr,value,varName):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Modifying "+varName+" by changing "+expr+" with "+str(value)+" would alter it's integrity")
    sys.exit()

def insertingListOnMatInside3DMatError(varName,expr):
    print(colorama.Fore.RED + "SEMANTIC ERROR: "+expr+" is a Matrix object and inserting a list on it would alter "+varName+"'s integrity")
    sys.exit()
