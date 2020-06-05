import sys
from pip._vendor import colorama
from os import mkdir,listdir,getcwd,path,remove
from CompilerDependencies.TreeGen import *
global directory
global directory
directory=""
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
    elif(token=="NE"):
        return "!="
    elif(token=="LT"):
        return "<"
    elif(token=="GT"):
        return ">"
    elif (token=="LTE"):
        return "<="
    elif(token=="GTE"):
        return ">="
    elif(token=="COMPARE"):
        return "=="

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
        if (valor.isNull()):
            return []
        if (valor.getName() == "ListV"):
            lista.append(tokenTranslator(valor.getChilds()[0].getChilds()[0].getToken()))

        elif (valor.getName() == "ListT0"):
            lista.extend(listTranslator(valor.getChilds()))

        elif (valor.getName() == "ListT1"):
            lista.extend(listTranslator(valor.getChilds()))
            return lista
        elif(valor.getName()=="EmptyList"):
            return []
    return lista

def matTranslator(valores):
    matriz=[]
    for valor in valores:
        if (valor.getName() == "MatV"):
            if(not valor.getChilds()[0].getName()=="EmptyList"):
                matriz.append(listTranslator(valor.getChilds()[0].getChilds()[1].getChilds()))
            else:
                matriz.append([])

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

def realArithmeticTranslator(operacion):
    result = ""
    for valor in operacion:
        if (not valor.isToken()):
            result += realArithmeticTranslator(valor.getChilds())
        else:
            if(valor.getName()=="Id"):
                result += str(valor.getToken())
            else:
                result += str(tokenTranslator(valor.getToken()))
    return result

def consultTranslator(consult,dictionary,expr):
    translation={}
    var = consult.getChilds()[0].getToken()
    if (not existenceVerifier(var, dictionary)):
        outOfScopeError(var)

    if(emptyVerifier(dictionary[var])):
        consult
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
                    if(not noneVerifier(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken(),dictionary)):
                        ind=dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                        indExpr=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
                else:
                    nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            if(abs(ind)>=len(dictionary[var])):
                outOfBoundsError(indExpr,expr,ind)
            translation[expr]=dictionary[var][ind]
            if(ind !=None):
                translation["Aux"]="["+str(ind)+"]"
            else:
                translation["Aux"]=None
            translation["Flipped"]=None
            return translation
        elif(consult.getChilds()[1].getName()=="ListConsultT1"):
            inf=None
            sup=None
            if(consult.getChilds()[1].getChilds()[1].getName()=="Indice0"):
                inf=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())

            elif(consult.getChilds()[1].getChilds()[1].getName()=="Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken(), dictionary)):
                    if (not indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
                    inf = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]

            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                sup=int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
            elif (consult.getChilds()[1].getChilds()[3].getName()=="Indice1"):
                if(not noneVerifier(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken(),dictionary)):
                    if (not indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
                    sup= dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
            translation[expr]=dictionary[var][inf:sup]
            if(inf!=None):
                translation["Aux"]="["+str(inf)+":"+str(sup)+"]"
            else:
                translation["Aux"] =None
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
                if (not noneVerifier(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                        ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                        ind1Expr=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())

            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind2 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
                ind2Expr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                        ind2 = dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
                        ind2Expr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
            if(ind1!=None):
                if (ind1 >= len(dictionary[var])):
                    outOfBoundsError(ind1Expr, expr,ind1)
                elif(ind2>= len(dictionary[var][ind1])):
                    outOfBoundsError(ind2Expr,expr,ind2)
                translation[expr] = dictionary[var][ind1][ind2]
                translation["Aux"]="[" + str(ind1) + "][" + str(ind2) + "]"
            else:
                translation["Aux"]=None

            translation["Flipped"] = None
            return translation

        elif (consult.getChilds()[1].getName() == "MatConsultT1"):
            indExpr=None
            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind1 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
                indExpr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                        ind1 = int(dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()])
                        indExpr=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
            translation[expr] = colFetcher(dictionary[var], ind1)
            if(ind1!=None):
                if(ind1>=len(dictionary[var][0])):
                    outOfBoundsError(indExpr,expr,ind1)
                translation["Aux"] = "[:," + str(ind1) + "]"
                translation["Flipped"] = "[" + str(-(ind1 + 1)) + "]"
            else:
                translation["Aux"]=None
                translation["Flipped"]=None
            return translation

        elif (consult.getChilds()[1].getName() == "MatConsultT2"):
            indExpr = None
            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind1 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())
                indExpr = consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                        ind1 = dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
                        indExpr = consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())

            if(ind1!=None):
                if (ind1 >= len(dictionary[var][0])):
                    outOfBoundsError(indExpr, expr,ind)
                dictionary["Temp"] =colFetcher(dictionary[var],ind1)
                tempConsult = consultTranslator(NonTerminalNode("ListConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[5]]),dictionary,expr)
                del dictionary["Temp"]
                translation[expr] = list(tempConsult.values())[0]
                if(tempConsult["Aux"]==None):
                    translation["Aux"] = None
                    translation["Flipped"] = None
                    return translation

                translation["Aux"]="[:,"+str(ind1)+"]"+tempConsult["Aux"]
                translation["Flipped"]="["+str(-(ind1+1))+"]"+tempConsult["Aux"]
            else:
                translation["Aux"]=None
                translation["Flipped"]=None
            return translation

        elif(consult.getChilds()[1].getName()=="MatConsultT3"):
            if(consult.getChilds()[1].getChilds()[1].getName()=="Indice0"):
                ind1=int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            elif (consult.getChilds()[1].getChilds()[1].getName() == "Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                        ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            if(ind1!=None):
                ind1Expr = consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
                if (ind1 >= len(dictionary[var])):
                    outOfBoundsError(ind1Expr, expr,ind1)
                dictionary["Temp"]=dictionary[var][ind1]
                tempConsult=consultTranslator(NonTerminalNode("ListConsult",[TerminalNode("Id","Temp"),consult.getChilds()[1].getChilds()[3]]),dictionary,expr)
                del dictionary["Temp"]
                if(tempConsult["Aux"]==None):
                    translation["Aux"]=None
                    translation["Flipped"]=None
                    return translation

                translation[expr]=list(tempConsult.values())[0]
                ind = 0
                for valor in expr:
                    if (valor == "["):
                        expr = expr[ind: ]
                        break
                    ind+=1
                translation["Aux"] = "["+str(ind1)+"]"+tempConsult["Aux"]
                translation["Flipped"] = None
            else:
                translation["Aux"]=None
                translation["Flipped"]=None
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
                if (not noneVerifier(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                        ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())

            if (consult.getChilds()[1].getChilds()[3].getName() == "Indice0"):
                ind2 = int(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())

            elif (consult.getChilds()[1].getChilds()[3].getName() == "Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[3], dictionary)):
                        ind2 = dictionary[consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()]
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken())

            if (consult.getChilds()[1].getChilds()[5].getName() == "Indice0"):
                ind3 = int(consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken())

            elif (consult.getChilds()[1].getChilds()[5].getName() == "Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken(), dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[5], dictionary)):
                        ind3 = dictionary[consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken()]
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken())

            if(ind1!=None):
                if(ind1>=len(dictionary[var])):
                    outOfBoundsError(ind1Expr,expr,ind1)

                elif(ind2>=len(dictionary[var][ind1])):
                    outOfBoundsError(ind2Expr,expr,ind2)

                elif(ind3>=len(dictionary[var][ind2])):
                    outOfBoundsError(ind3Expr,expr,ind3)

                translation[expr]=dictionary[var][ind1][ind2][ind3]
                translation["Aux"]="["+str(ind1)+"]["+str(ind2)+"]["+str(ind3)+"]"
                translation["Flipped"] = None
            else:
                translation["Aux"]=None
                translation["Flipped"]=None
            return translation

        elif(consult.getChilds()[1].getName()=="ThreeDMatConsultT1"):
            ind1 = None
            ind1Expr = consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()

            dimensionVerifier(var, dictionary, "ThreeDMatConsult")
            if (consult.getChilds()[1].getChilds()[1].getName() == "Indice0"):
                ind1 = int(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            elif (consult.getChilds()[1].getChilds()[1].getName() == "Indice1"):
                if (not noneVerifier(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken(),dictionary)):
                    if (indVerifier(consult.getChilds()[1].getChilds()[1], dictionary)):
                        ind1 = dictionary[consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()]
                    else:
                        nonIterableObjectError(consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken())
            if(ind1!=None):
                if (ind1 >= len(dictionary[var])):
                    outOfBoundsError(ind1Expr, expr,ind1)

                dictionary["Temp"] = dictionary[var][ind1]
                tempConsult = consultTranslator(NonTerminalNode("MatConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[3]]),dictionary,expr)
                if("Temp" in dictionary):
                    del dictionary["Temp"]
                if(tempConsult["Aux"]==None):
                    translation["Aux"]=None
                    translation["Flipped"]=None
                    return translation
                translation[expr] = list(tempConsult.values())[0]
                translation["Aux"]="["+str(ind1)+"]"+tempConsult["Aux"]
                if(not tempConsult["Flipped"]==None):
                    translation["Flipped"]="["+str(ind1)+"]"+tempConsult["Flipped"]
                else:
                    translation["Flipped"]="["+str(ind1)+"]"+tempConsult["Aux"]
            else:
                translation["Aux"]=None
                translation["Flipped"]=None
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

def realExpresionTranslator(consult):
    if (consult.getName() == "ListConsult"):
        if (consult.getChilds()[1].getName() == "ListConsultT0"):
            ind = consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            return ("[" + ind + "]",None)

        elif (consult.getChilds()[1].getName() == "ListConsultT1"):
            inf = consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            sup = consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            return ("[" + inf + ":" + sup + "]",None)

    elif (consult.getName() == "MatConsult"):
        if (consult.getChilds()[1].getName() == "MatConsultT0"):
            ind1=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            ind2=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            return ("[" + ind1 + "][" + ind2 + "]",None)

        elif (consult.getChilds()[1].getName() == "MatConsultT1"):
            ind=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            return ("[:,"+ind+"]","["+str(-(int(ind)+1))+"]")

        elif (consult.getChilds()[1].getName() == "MatConsultT2"):
            ind=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            rest=realExpresionTranslator(NonTerminalNode("ListConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[5]]))
            return ("[:,"+str(ind)+"]"+rest[0],"["+str(-(int(ind)+1))+"]"+rest[0])

        elif(consult.getChilds()[1].getName()=="MatConsultT3"):
            ind1= consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            return ("["+ind1+"]"+realExpresionTranslator(NonTerminalNode("ListConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[3]]))[0],None)

    elif (consult.getName() == "ThreeDMatConsult"):
        if(consult.getChilds()[1].getName()=="ThreeDMatConsultT0"):
            ind1=consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            ind2=consult.getChilds()[1].getChilds()[3].getChilds()[0].getToken()
            ind3=consult.getChilds()[1].getChilds()[5].getChilds()[0].getToken()

            return("["+ind1+"]["+ind2+"]["+ind3+"]",None)

        elif(consult.getChilds()[1].getName()=="ThreeDMatConsultT1"):
            ind1= consult.getChilds()[1].getChilds()[1].getChilds()[0].getToken()
            rest=realExpresionTranslator(NonTerminalNode("MatConsult", [TerminalNode("Id", "Temp"), consult.getChilds()[1].getChilds()[3]]))
            if(rest[1]!=None):
                return ("["+ind1+"]"+rest[0],"["+ind1+"]"+rest[1])
            return ("[" + ind1 + "]" + rest[0], "[" + ind1 + "]" + rest[0])



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

def realFunctionTranslator(function):
    if(function.getName() == "RangeF"):
        size=None
        if (function.getChilds()[2].getName() == "Iterable0"):
            size =function.getChilds()[2].getChilds()[0].getChilds()[0].getToken()

        elif(function.getChilds()[2].getName() == "Iterable1"):
            size = function.getChilds()[2].getChilds()[0].getToken()

        boolValue=tokenTranslator(function.getChilds()[4].getChilds()[0].getToken())
        return "ranger("+str(size)+","+str(boolValue)+")"


def emptyVerifier(structure):
    if(listVerifier(structure)):
        if(len(structure)==0):
            return True
    elif(matVerifier(structure)):
        return emptyVerifier(structure[0])


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
            if(param.getChilds()[0].getChilds()[0].getName()=="Iterable0"):
                if(param.getChilds()[0].getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                    if(not param.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken() in scope):
                        outOfScopeError(param.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken())
                    output.append(scope[param.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()])

                elif(param.getChilds()[0].getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                    output.append(list(consultTranslator(param.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],scope,expresionTranslator(param.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).values())[0])


            elif(param.getChilds()[0].getChilds()[0].getName()=="Iterable1"):
                output.append(int(param.getChilds()[0].getChilds()[0].getChilds()[0].getToken()))

            elif (param.getChilds()[0].getChilds()[0].getName() == "Iterable2"):
                if(param.getChilds()[0].getChilds()[0].getChilds()[0].getName()=="EmptyList"):
                    output.append([])
                else:
                    output.append(listTranslator(param.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()))

            elif (param.getChilds()[0].getName() == "AssignableParam1"):
               output.append(matTranslator(param.getChilds()[0].getChilds()[0].getChilds()))

            elif (param.getChilds()[0].getName() == "AssignableParam2"):
               output.append(threeDmatTranslator(param.getChilds()[0].getChilds()[0].getChilds()))

            elif (param.getChilds()[0].getName() == "AssignableParam3"):
                output.append(tokenTranslator(param.getChilds()[0].getChilds()[0].getChilds()[0].getToken()))

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
    if(not isinstance(estructure,list)):
        nonIterableObjectError(var)

    if(len(estructure)==0 or isinstance(estructure[0],bool)):
        output=[True,False,False]

    elif (isinstance(estructure[0],list)):
        if(not len(estructure[0])==0 and isinstance(estructure[0][0],list)):
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
    outOfScopeError(ind.getChilds()[0].getToken())

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
def structureUpdater(value,structure,expresion,flipped,varName,originalExpr):
    if(":," in expresion):
        structure=matrixFliper(structure,"L")
        temp=eval("structure"+str(flipped))
        if(isinstance(value,int) or len(temp)==len(value)):
            exec("structure"+str(flipped)+"="+str(value))
            structure=matrixFliper(structure,"R")
        else:
            modifyingMatrixWithDifferentSizeLineError(originalExpr,value,varName)
    else:
        temp=eval("structure"+str(expresion))
        if (isinstance(value,int) or len(temp) == len(value)):
            exec("structure"+str(expresion)+"="+str(value))
        else:
            modifyingMatrixWithDifferentSizeLineError(originalExpr,value, varName)
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
def localsUpdater(backup,local_var,global_var):
    for key in list(backup[0].keys()):
        if(key in local_var):
            backup[0][key]=local_var[key]
    globalUpdater(backup[0],global_var,backup[1])
    return backup

def dimensionConstVerifier(value,consts):
    if(listVerifier(value)):
        if(len(value)>consts["Dim1"]):
            constDifferentDimensionError(value)

    elif(matrixVerifier(value)):
        if(len(value)>consts["Dim0"] or len(value[0])>consts["Dim1"]):
            constDifferentDimensionError(value)

    elif(threeDMatrixVerifier(value)):
        if(len(value)>consts["Cubo"] or len(value[0])>consts["Dim0"] or len(value[0][0])>consts["Dim1"]):
            constDifferentDimensionError(value)
def mainBlockSplitter(p):
    output=[]
    for line in p:
        if(line.isNull()):
            return output
        elif(line.getName()=="MainBlock"):
            output.extend(mainBlockSplitter(line.getChilds()))
        elif(line.getName()=="MainContent0"):
            output.append(line.getChilds()[0])
        elif(line.getName()=="MainContent1"):
            output.append(line.getChilds()[0])



    return output


class CodeGenerator():
    def __init__(self,fileName):
        self.fileName=fileName
        self.directory=self.initializer()

    def initializer(self):
        print("test")

def dirInitializer():
    global directory
    directory=getcwd()+"\CodeGeneration"
    if (not path.exists(directory)):
        mkdir(directory)
        print("CodeGeneration folder created successfully!")
    directory=directory+"\CodeFile.txt"
    open(directory,"w")
    file=open(directory,"r+")
    file.truncate(0)
    file.close()

def globalWriter(scope):
    global directory
    globalVars=list(scope.keys())
    globalVals=list(scope.values())
    globalString="global "
    for valor in globalVars:
        globalString+=str(valor)+","
    globalString=globalString[0:len(globalString)-1]
    with open (directory,"a") as file:
        file.write(globalString+"\n")
        ind=0
        for valor in globalVars:
            file.write(valor +"="+str(globalVals[ind])+"\n")
            ind+=1
        file.close()
def procWriter(proc):
    global directory
    paramString="("
    for param in proc[1]:
        paramString+=param[0]+","
    paramString=paramString[0:len(paramString)-1]+"):"
    globals=None
    glb=""
    if(not proc[2].getChilds()[3].getChilds()[0].isNull()):
        globals=globalSplitter(proc[2].getChilds()[3].getChilds()[0].getChilds()[1].getChilds())
        for valor in globals:
            glb+=valor+","
        glb=glb[0:len(glb)-1]
    tabs=1
    with open(directory, "a") as file:
        file.write("\ndef "+proc[0]+paramString+"\n")
        if(globals!=None):
            file.write(tabs*"\t"+"global "+glb+"\n\n")
        queue=processBodyTranslator(proc[2].getChilds()[3].getChilds()[2].getChilds())
        file.close()
        for line in queue:
            if("Assignment" in line.getName()):
                assignmentWriter(line,tabs)
            elif("Instruction" in line.getName()):
                instructionWriter(line,tabs)

def instructionWriter(line,tabs):
    if(line.getName()=="Instruction0"):
        functionWriter(line.getChilds()[0],tabs)
def functionWriter(func,tabs):
    global directory
    varname=""
    with open(directory,"a") as file:
        if(func.getName()=="Function0"):
            if(func.getChilds()[0].getChilds()[2].getName()=="Identifier0"):
                file.write(tabs*"\t"+"typer("+func.getChilds()[0].getChilds()[2].getChilds()[0].getToken()+")\n")

            elif(func.getChilds()[0].getChilds()[2].getName()=="Identifier1"):
                expr=realExpresionTranslator(func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0])
                if(not ":," in expr[0]):
                    file.write(tabs*"\t"+"typer("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+")\n")
                else:
                    file.write(tabs*"\t"+"Temp=matrixFlipper("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                    file.write(tabs*"\t"+"typer(Temp"+expr[1]+")\n")
                    file.write(tabs*"\t"+"del Temp\n")

        elif(func.getName()=="Function1"):
            output=""
            if(func.getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                output=tabs*"\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
                varname=func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()

            elif(func.getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                expr=realExpresionTranslator(func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                output=tabs*"\t"
                if(not ":," in expr[0]):
                    output+=func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]
                    varname=func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]
                else:
                    file.write(tabs*"\t"+"TempVar=matrixFlipper("+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                    output+="TempVar"+expr[1]
                    varname="TempVar"+expr[1]

            if (func.getChilds()[0].getChilds()[4].getName() == "Fcont6"):
                output+=".insert("
                if (func.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable1"):
                    output += func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken() + ","
                elif (func.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable0"):
                    output += func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[
                                  0].getToken() + ","

                if (func.getChilds()[0].getChilds()[4].getChilds()[2].getName() == "Insertable0"):
                    output += func.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[
                                  0].getName().replace("V", "") + ")\n"
                    file.write(output)
                elif (func.getChilds()[0].getChilds()[4].getChilds()[2].getName() == "Insertable1"):
                    if (func.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getName() == "Identifier0"):
                        output += func.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[
                                      0].getToken() + ")\n"
                        file.write(output)
                    elif (func.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getName() == "Identifier1"):
                        expr = realExpresionTranslator(
                            func.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[
                                0])
                        if (not ":," in expr[0]):
                            output += \
                            func.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[
                                0].getChilds()[0].getToken() + expr[0] + ")\n"
                            file.write(output)
                        else:
                            file.write(tabs * "\t" + "Temp=matrixFlipper(" +
                                       func.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[
                                           0].getChilds()[0].getChilds()[0].getToken() + ''',"L")''' + "\n")
                            output += "Temp" + expr[1] + ")\n"
                            file.write(output)
                            file.write(tabs * "\t" + "del Temp\n")

            elif (func.getChilds()[0].getChilds()[4].getName() == "Fcont7"):
                output=tabs*"\t"+varname+"=inserter("+varname+","
                if(func.getChilds()[0].getChilds()[4].getChilds()[3].isNull()):
                    if(func.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable0"):
                        if(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                            output+=func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+","+func.getChilds()[0].getChilds()[4].getChilds()[2].getToken()+",None)\n"
                            file.write(output)
                        elif(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                            expr = realExpresionTranslator(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                            if (not ":," in expr[0]):
                                output += func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + expr[0] + "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + ",None)\n"
                                file.write(output)

                            else:
                                file.write(tabs*"\t"+"Temp=matFlipper("+func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                                output+="Temp"+expr[1]+","+ func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + ",None)\n"
                                file.write(output)
                                file.write(tabs*"\t"+"del Temp\n")

                    elif(func.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable2"):
                        list=listTranslator(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds())
                        output+=str(list)+","+func.getChilds()[0].getChilds()[4].getChilds()[2].getToken()+",None)\n"
                        file.write(output)

                    elif (func.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable3"):
                        mat=matTranslator(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds())
                        output+=str(mat)+","+func.getChilds()[0].getChilds()[4].getChilds()[2].getToken()+",None)\n"
                        file.write(output)
                else:
                    if (func.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable0"):
                        if (func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getName() == "Identifier0"):
                            if(func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable0"):
                                output += func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + ","+func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken()+")\n"
                            elif(func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable1"):
                                output += func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getToken() + ")\n"
                            file.write(output)
                        elif (func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getName() == "Identifier1"):
                            expr=realExpresionTranslator(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                            if(not ":," in expr[0]):
                                if (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable0"):
                                    output += func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + expr[0] + "," +func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken() + ")\n"

                                elif (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable1"):
                                    output += func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0] + "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + "," +func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getToken() + ")\n"
                                file.write(output)
                            else:
                                file.write(tabs*"\t"+"Temp=matFlipper("+func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                                if (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable0"):
                                    output+="Temp"+expr[1]+","+ func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + ","+func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken()+")\n"
                                elif (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable1"):
                                    output += "Temp"+expr[1]+"," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getToken() + ")\n"
                                file.write(output)
                                file.write(tabs*"\t"+"del Temp\n")




                    elif (func.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable2"):
                        list = listTranslator(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds())
                        if (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable0"):
                            output += str(list) + "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + ","+func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken()+")\n"
                        elif (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable1"):
                            output += str(list)+ "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[ 0].getToken() + ")\n"
                        file.write(output)

                    elif (func.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable3"):
                        mat = matTranslator(func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds())
                        if (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable0"):
                            output += str(mat) + "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken() + ")\n"
                        elif (func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable1"):
                            output += str(mat) + "," + func.getChilds()[0].getChilds()[4].getChilds()[2].getToken() + "," + func.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getToken() + ")\n"
                        file.write(output)


            if("TempVar" in output):
                file.write(tabs*"\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+'''=matrixFlipper(TempVar,"R")'''+"\n")
                file.write(tabs*"\t"+"del TempVar\n")

        elif (func.getName() == "Function2"):
            output=tabs*"\t"
            if(func.getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                output+=func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+".pop("
            elif(func.getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                expr=realExpresionTranslator(func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                if(not ":," in expr[0]):
                    output+=func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+".pop("
                else:
                    file.write(tabs*"\t"+"Temp=matrixFlipper("+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                    output+="Temp"+expr[1]+".pop("


            if(func.getChilds()[0].getChilds()[4].getName()=="Iterable0"):
                output+=func.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken()+")\n"

            elif(func.getChilds()[0].getChilds()[4].getName()=="Iterable1"):
                output+=func.getChilds()[0].getChilds()[4].getChilds()[0].getToken()+")\n"
            file.write(output)
            if("Temp" in output):
                file.write(tabs*"\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+'''=matrixFlipper(Temp,"R")'''+"\n")
                file.write(tabs*"\t"+"del Temp\n")

        elif (func.getName() == "Function3"):
            if(func.getChilds()[0].getChilds()[2].getName()=="Identifier0"):
                file.write(tabs*"\t"+"length("+func.getChilds()[0].getChilds()[2].getChilds()[0].getToken()+")\n")
            elif(func.getChilds()[0].getChilds()[2].getName()=="Identifier1"):
                expr=realExpresionTranslator(func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0])
                if(not ":," in expr[0]):
                    file.write(tabs*"\t"+"length("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+")\n")
                else:
                    file.write(tabs*"\t"+"Temp=matrixFlipper("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                    file.write(tabs*"\t"+"length(Temp"+expr[1]+")\n")
                    file.write(tabs*"\t"+"del Temp\n")

        elif (func.getName() == "Function4"):
            if (func.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
                file.write(tabs * "\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+"=neg("+func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+")\n")

            elif (func.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
                expr = realExpresionTranslator(func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                if (not ":," in expr[0]):
                    file.write(tabs * "\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+"=neg("+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+")\n")
                else:
                    file.write(tabs * "\t" + "Temp=matrixFlipper(" +func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + ''',"L")''' + "\n")
                    file.write(tabs * "\t" + "Temp"+expr[1]+"=neg(Temp"+expr[1]+")\n")
                    file.write(tabs*"\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+'''=matrixFlipper(Temp,"R")'''+"\n")
                    file.write(tabs * "\t" + "del Temp\n")

        elif (func.getName() == "Function5"):
            output=tabs*"\t"
            if(func.getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                output+=func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+"="+func.getChilds()[0].getChilds()[2].getChilds()[0].getToken()+"("+func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+")\n"
                file.write(output)
            elif(func.getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                expr=realExpresionTranslator(func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                if(not ":," in expr[0]):
                    output+=func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+"="+func.getChilds()[0].getChilds()[2].getChilds()[0].getToken()+"("+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+")\n"
                    file.write(output)
                else:
                    file.write(tabs*"\t"+"Temp=matrixFlipper("+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                    file.write(tabs*"\t"+"Temp"+expr[1]+"="+func.getChilds()[0].getChilds()[2].getChilds()[0].getToken()+"(Temp"+expr[1]+")\n")
                    file.write(tabs*"\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+'''=matrixFlipper(Temp,"R")'''+"\n")
                    file.write(tabs*"\t"+"del Temp\n")

        elif (func.getName() == "Function6"):
            output=tabs*"\t"
            if(func.getChilds()[0].getChilds()[2].getChilds()[0].getName()=="Identifier0"):
                if(func.getChilds()[0].getChilds()[2].getName()=="Fcont1"):
                    output+="blink("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getToken()+","+func.getChilds()[0].getChilds()[2].getChilds()[2].getChilds()[0].getName().replace("V","")+")\n"
                    file.write(output)

                elif(func.getChilds()[0].getChilds()[2].getName()=="Fcont0"):
                   output+="blink("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getToken()+","+func.getChilds()[0].getChilds()[2].getChilds()[2].getToken()+''',"'''+func.getChilds()[0].getChilds()[2].getChilds()[4].getChilds()[0].getName()+'''",'''+func.getChilds()[0].getChilds()[2].getChilds()[6].getChilds()[0].getName().replace("V","")+")\n"
                   file.write(output)

            elif(func.getChilds()[0].getChilds()[2].getChilds()[0].getName()=="Identifier1"):
                expr=realExpresionTranslator(func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0])
                if(not ":," in expr[0]):
                    if (func.getChilds()[0].getChilds()[2].getName() == "Fcont1"):
                        output += "blink(" + func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+ "," + func.getChilds()[0].getChilds()[2].getChilds()[2].getChilds()[0].getName().replace("V", "") + ")\n"
                        file.write(output)

                    elif (func.getChilds()[0].getChilds()[2].getName() == "Fcont0"):
                        output += "blink(" + func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+ "," + func.getChilds()[0].getChilds()[2].getChilds()[2].getToken() + ''',"''' + func.getChilds()[0].getChilds()[2].getChilds()[4].getChilds()[0].getName() + '''",''' + func.getChilds()[0].getChilds()[2].getChilds()[6].getChilds()[0].getName().replace("V", "") + ")\n"
                        file.write(output)
                else:
                    file.write(tabs*"\t"+"Temp=matrixFlipper("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                    if (func.getChilds()[0].getChilds()[2].getName() == "Fcont0"):
                        output += "blink(Temp" +expr[1] + "," + func.getChilds()[0].getChilds()[2].getChilds()[2].getToken() + ''',"''' + func.getChilds()[0].getChilds()[2].getChilds()[4].getChilds()[0].getName() + '''",''' + func.getChilds()[0].getChilds()[2].getChilds()[6].getChilds()[0].getName().replace("V","") + ")\n"
                        file.write(output)

                    elif (func.getChilds()[0].getChilds()[2].getName() == "Fcont1"):
                        output += "blink(Temp" +expr[1]+"," + func.getChilds()[0].getChilds()[2].getChilds()[2].getChilds()[0].getName().replace("V", "") + ")\n"
                        file.write(output)
                    file.write(tabs*"\t"+"del Temp \n")

        elif (func.getName() == "Function7"):
            if(func.getChilds()[0].getChilds()[2].isNull()):
                file.write(tabs*"\t"+"delay()\n")
            else:
                if(func.getChilds()[0].getChilds()[2].getChilds()[0].getName()=="Iterable0"):
                    file.write(tabs * "\t" + "delay("+func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"'''+func.getChilds()[0].getChilds()[2].getChilds()[2].getChilds()[0].getName()+''''")'''+"\n")

                elif(func.getChilds()[0].getChilds()[2].getChilds()[0].getName()=="Iterable1"):
                    file.write(tabs * "\t" + "delay(" + func.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getToken() + ''',"''' +func.getChilds()[0].getChilds()[2].getChilds()[2].getChilds()[0].getName() + ''''")''' + "\n")

        elif (func.getName() == "Function8"):
            if(func.getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                file.write(tabs*"\t"+func.getChilds()[0].getChilds()[2].getChilds()[0].getName().replace("S","s")+"("+func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+")\n")

            elif(func.getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                expr=realExpresionTranslator(func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                if(not ":," in expr[0]):
                    file.write(tabs * "\t" + func.getChilds()[0].getChilds()[2].getChilds()[0].getName().replace("S","s")+"(" +func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+ ")\n")
                else:
                    file.write(tabs*"\t"+"Temp=matrixFlipper("+func.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                    file.write(tabs*"\t"+func.getChilds()[0].getChilds()[2].getChilds()[0].getName().replace("S","s")+"(Temp"+expr[1]+")\n")

        elif (func.getName() == "Function9"):
            if(func.getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                file.write(tabs*"\t"+func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+"=delete("+func.getChilds()[0].getChilds()[0].getChilds()[0].getToken()+","+(func.getChilds()[0].getChilds()[4].getChilds()[0].getToken())+","+func.getChilds()[0].getChilds()[6].getToken()+")\n")

        file.write("\n")
        file.close()


def assignmentWriter(line,tabs):
    global directory
    with open(directory,"a") as file:
        if(line.getName()=="SimpleAssignment"):
            simpleLine=tabs*"\t"
            cont = None
            if (line.getChilds()[2].getName()=="Acont0"):
                cont = line.getChilds()[2].getChilds()[0].getChilds()[0].getName().replace("V", "")

            elif (line.getChilds()[2].getName()=="Acont1"):
                cont = realArithmeticTranslator(line.getChilds()[2].getChilds()[0].getChilds())

            elif (line.getChilds()[2].getName()=="Acont2"):
                cont = str(listTranslator(line.getChilds()[2].getChilds()[0].getChilds()))

            elif (line.getChilds()[2].getName()=="Acont3"):
                cont=str(matTranslator(line.getChilds()[2].getChilds()[0].getChilds()))

            elif (line.getChilds()[2].getName()=="Acont4"):
                cont = str(threeDmatTranslator(line.getChilds()[2].getChilds()[0].getChilds()))

            elif(line.getChilds()[2].getName()=="RangeF"):
                cont=realFunctionTranslator(line.getChilds()[2])


            if(line.getChilds()[0].getName()=="Identifier0"):
                simpleLine+=line.getChilds()[0].getChilds()[0].getToken()+"="
                if(cont==None):
                    expr=realExpresionTranslator(line.getChilds()[2].getChilds()[0].getChilds()[0])
                    if(":," in expr[0]):
                        file.write(tabs*"\t"+"Temp=matrixFlipper("+line.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                        file.write(tabs*"\t"+"Temp=Temp"+expr[1]+"\n")
                        file.write(simpleLine+"Temp\n")
                        file.write(tabs*"\t"+"del Temp\n")
                    else:
                        file.write(simpleLine+expr[0]+"\n")
                else:
                    file.write(simpleLine+cont+"\n")

            elif(line.getChilds()[0].getName()=="Identifier1"):
                expr=realExpresionTranslator(line.getChilds()[0].getChilds()[0].getChilds()[0])
                if(":," in expr[0]):
                    if(cont!=None):
                        file.write(tabs*"\t"+"Temp=matrixFlipper("+line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                        file.write(tabs*"\t"+"Temp"+expr[1]+"="+cont+"\n")
                        file.write(tabs*"\t"+line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+"=matrixFlipper(Temp,"+'''"R")'''+"\n")
                        file.write(tabs*"\t"+"del Temp\n")
                    else:
                        exprCont=realExpresionTranslator(line.getChilds()[2].getChilds()[0].getChilds()[0])
                        if(":," in exprCont[0]):
                            file.write(tabs*"\t"+"TempCont=matrixFlipper("+line.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                            file.write(tabs*"\t"+"TempCont=TempCont"+exprCont[1]+"\n")
                            file.write(tabs*"\t"+"TempVar=matrixFlipper("+line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+''',"L")'''+"\n")
                            file.write(tabs*"\t"+"TempVar"+expr[1   ]+"=TempCont\n")
                            file.write(tabs*"\t"+line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+'''=matrixFlipper(TempVar,"R")'''+"\n")
                            file.write(tabs*"\t"+"del TempVar \n")
                            file.write(tabs*"\t"+"del TempCont\n")
                        else:
                            file.write(tabs * "\t" + "TempVar=matrixFlipper(" +line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + ''',"L")'''+"\n")
                            file.write(tabs * "\t" + "TempVar="+line.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+exprCont[1]+"\n")
                            file.write(tabs * "\t" + line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + '''=matrixFlipper(TempVar,"R")'''+"\n")
                            file.write(tabs * "\t" + "del TempVar \n")
                else:
                    if(cont!=None):
                        file.write(tabs*"\t"+line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+"="+cont+"\n")
                    else:
                        exprCont = realExpresionTranslator(line.getChilds()[2].getChilds()[0].getChilds()[0])
                        if(":," in exprCont[0]):
                            file.write(tabs * "\t" + "TempCont=matrixFlipper(" +line.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + ''',"L")'''+"\n")
                            file.write(tabs * "\t" + line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+expr[0]+"=TempCont"+exprCont[1]+"\n")
                            file.write(tabs*"\t"+"del TempCont\n")
                        else:
                            file.write(tabs * "\t" + line.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken() + expr[0] + "=" + line.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()+exprCont[0] + "\n")

        elif(line.getName()=="DoubleAssignment"):
            pairs=[(line.getChilds()[0],line.getChilds()[4]),(line.getChilds()[2],line.getChilds()[6])]
            for assignment in pairs:
                assignmentWriter(NonTerminalNode("SimpleAssignment",[assignment[0],TerminalNode("Assign","ASSIGN"),assignment[1]]),tabs)
        file.write("\n")
        file.close()








def constDifferentDimensionError(value):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The structure "+str(value)+" was defined without following the dimension constants specs, therefore it's forbidden")
    sys.exit()

def outOfBoundsError(index,iterable,value):
    if(not index.isdigit()):
        print(colorama.Fore.RED + "SEMANTIC ERROR: Index "+str(index)+" in "+ str(iterable)+", where "+str(index)+"="+str(value)+",out of bounds ")
    else:
        print(colorama.Fore.RED + "SEMANTIC ERROR: Index " + str(index) + " in " + str(iterable) + " out of bounds ")
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

def differentDimensionsThreeDMatError(value):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The 3Dmatrix "+str(value)+" has invalid matrixes within, therefore it's not a valid matrix")
    sys.exit()

def differentMatOnThreeDMatError(value,value1):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The matrix stored in "+value+" has a different size than "+str(value1)+", so it can't be replaced since it is inside a 3DMatrix")
    sys.exit()

def modifyingMatrixWithDifferentSizeLineError(expr,value,varName):
    print(colorama.Fore.RED + "SEMANTIC ERROR: Modifying "+str(varName)+" by changing "+str(expr)+" with "+str(value)+" would alter it's integrity")
    sys.exit()

def insertingListOnMatInside3DMatError(varName,expr):
    print(colorama.Fore.RED + "SEMANTIC ERROR: "+expr+" is a Matrix object and inserting a list on it would alter "+varName+"'s integrity")
    sys.exit()

def nullStatementBody(statement):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The body in statement "+statement+" can't be Null")
    sys.exit()

def nullCycleBodyError(statement):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The body in cycle "+statement+" can't be Null")
    sys.exit()

def notIterableObjectOnFor(varName):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in "+varName+" is not an iterable object, therefore it can't be used for iterations in FOR cycles")
    sys.exit()

def declaringVariablesOnMainError():
    print(colorama.Fore.RED + "SEMANTIC ERROR: Declaring any kind of variable inside the main scope is forbidden")
    sys.exit()

def notDefinedCubeError(varName):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The variable "+varName+" hasn't been defined in the global scope, therefore it can't be used as a compiling cube")
    sys.exit()

def notaCubeError(varName):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored in " + varName + " is not a cube, therefore it can't be used as a compiling cube")
    sys.exit()

def notaCubeError1(cube):
    print(colorama.Fore.RED + "SEMANTIC ERROR: The value stored " +cube+ " is not a cube, therefore it can't be used as a compiling cube")
    sys.exit()