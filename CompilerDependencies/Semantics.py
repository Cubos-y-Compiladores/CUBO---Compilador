import sys
from Tools.Tools import *
from pip._vendor import colorama
global global_var,regular_var
global_var={}
local_var={}
consts={}
procedures={}
def AssignmentSem(p,scope):
    global global_var,local_var
    scopeType=scope
    if(scope=="global"):
        scope=global_var
    elif(scope=="local"):
        scope=local_var

    if(p[2].getName()=="SimpleAssignment"):
        varName = p[2].getChilds()[0].getChilds()[0].getToken()
        varType = ""
        if (varName in scope):
            varType = type(scope[varName])

        if(p[2].getChilds()[2].getName()=="Acont0"):
           value=tokenTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[0].getToken())
           if(typeVerifier(varType,value)):
                scope[varName]=value
           else:
               alreadyDefinedVarError(varName,varType)

        elif (p[2].getChilds()[2].getName() == "Acont1"):
            value=""
            temp =p[2].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0]
            if (temp.getName() == "Factor1"):
                var=temp.getChilds()[0].getToken()
                if(var in scope):
                    value=scope[var]
                else:
                    outOfScopeError(var)
            else:
                value=tokenTranslator(arithmeticTranslator(p[2].getChilds()[2].getChilds()[0],scope))

            if (typeVerifier(varType, value)):
               scope[varName] = value
            else:
               alreadyDefinedVarError(varName, varType)
            print("Test")

        elif (p[2].getChilds()[2].getName() == "Acont2"):
           value=listTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
               alreadyDefinedVarError(varName, varType)

        elif (p[2].getChilds()[2].getName() == "Acont3"):
           value=matTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
               alreadyDefinedVarError(varName, varType)

        elif (p[2].getChilds()[2].getName() == "Acont4"):
           value=threeDmatTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
               alreadyDefinedVarError(varName, varType)


        elif (p[2].getChilds()[2].getName() == "Acont5"):
           value=list(consultTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[0],scope).values())[0]
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
               alreadyDefinedVarError(varName, varType)

    elif (p[2].getName() == "DoubleAssignment"):
        varList=[]
        valueList=[]
        typeList=[]
        for child in p[2].getChilds():
            if(child.getName()=="Identifier0"):
                var=str(child.getChilds()[0].getToken())
                varType = ""
                if (var in scope):
                    varType = type(scope[var])
                varList.append(var)
                typeList.append(varType)

            elif(child.getName()=="Identifier1"):
                if(scopeType=="global"):
                    globalConsultError()
                expr = consultTranslator(str(child.getChilds()[0].getToken()),scope)
                var=str(expr.keys()[0])
                varType =type(expr.values()[0])
                varList.append(var)
                typeList.append(varType)


            elif (child.getName() == "Acont0"):
                valueList.append(tokenTranslator(child.getChilds()[0].getChilds()[0].getToken()))

            elif (child.getName() == "Acont1"):
                value = ""
                temp =child.getChilds()[0].getChilds()[0].getChilds()[0]
                if (temp.getName() == "Factor1"):
                    var = temp.getChilds()[0].getToken()
                    if (var in scope):
                        value = scope[var]
                    else:
                        outOfScopeError(var)
                else:
                    value = tokenTranslator(arithmeticTranslator(child.getChilds()[0],scope))
                valueList.append(value)
                print("test")

            elif (child.getName() == "Acont2"):
                valueList.append(listTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

            elif (child.getName() == "Acont3"):
                valueList.append(matTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

            elif (child.getName() == "Acont4"):
                valueList.append(threeDmatTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

            elif(child.getName()=="Acont5"):
                valueList.append(list(consultTranslator(child.getChilds()[0].getChilds()[0],scope).values())[0])

        ind=0
        while(ind<len(varList)):
            if(typeVerifier(typeList[ind],valueList[ind])):
                scope[varList[ind]]=valueList[ind]
            else:
                alreadyDefinedVarError(varList[ind],typeList[ind])
            ind+=1

def constBSem(p):
    global consts
    const_list=[p[1],p[2],p[3],p[4],p[5]]

    for const in const_list:
        if(const.getChilds()[0].getName()=="Timer"):
            if("Timer" in consts):
                alreadyDefinedConstError("Timer_Const")

            else:
                consts["Timer"]=int(const.getChilds()[2].getToken())

        elif (const.getChilds()[0].getName() == "RangoTimer"):
            if ("RangoTimer" in consts):
                alreadyDefinedConstError("RangoTimer_Const")

            else:
                consts["RangoTimer"] = str(const.getChilds()[2].getChilds()[0].getName())

        elif (const.getChilds()[0].getName()== "Dim0"):
            if ("Dim0" in consts):
                alreadyDefinedConstError("DimFilas_Const")

            else:
                consts["Dim0"] = int(const.getChilds()[2].getToken())

        elif (const.getChilds()[0].getName() == "Dim1"):
            if ("Dim1" in consts):
                alreadyDefinedConstError("DimColumnas_Const")

            else:
                consts["Dim1"] = int(const.getChilds()[2].getToken())

        elif (const.getChilds()[0].getName()== "Cubo"):
            if ("Cubo" in consts):
                alreadyDefinedConstError("Cubo_Const")

            else:
                consts["Cubo"] = int(const.getChilds()[2].getToken())

    temp=consts
    print("Test")

def typeVerifier(varType,value):
    if (varType == "" or varType == type(value)):
        return True
    return False
