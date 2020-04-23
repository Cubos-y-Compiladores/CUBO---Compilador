import sys
from Tools.Tools import *
from pip._vendor import colorama
global global_var,global_temp,regular_var,procedures
global_var={}
global_temp=[]
local_var={}
local_only=[]
consts={}
procedures={}
def assignmentSem(p,scope):
    global global_var,local_var,local_only
    scopeType=scope

    if(scope=="global"):
        scope=global_var
    elif(scope=="local"):
        scope=local_var

    if(p.getName()=="SimpleAssignment"):
        varName = p.getChilds()[0].getChilds()[0].getToken()
        varType = ""
        if (varName in scope):
            varType = type(scope[varName])
        elif(scopeType=="local"):
            local_only.append(varName)

        if(p.getChilds()[2].getName()=="Acont0"):
           value=tokenTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0].getToken())
           if(typeVerifier(varType,value)):
                scope[varName]=value
           else:
               alreadyDefinedVarError(varName,scope[varName])

        elif (p.getChilds()[2].getName() == "Acont1"):
            value=""
            temp =p.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0]
            if (temp.getName() == "Factor1"):
                var=temp.getChilds()[0].getToken()
                if(var in scope):
                    value=scope[var]
                else:
                    outOfScopeError(var)
            else:
                value=tokenTranslator(arithmeticTranslator(p.getChilds()[2].getChilds()[0],scope))

            if (typeVerifier(varType, value)):
               scope[varName] = value
            else:
               alreadyDefinedVarError(varName,scope[varName])


        elif (p.getChilds()[2].getName() == "Acont2"):
           value=listTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
               alreadyDefinedVarError(varName,scope[varName])

        elif (p.getChilds()[2].getName() == "Acont3"):
           value=matTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
              alreadyDefinedVarError(varName,scope[varName])

        elif (p.getChilds()[2].getName() == "Acont4"):
           value=threeDmatTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
              alreadyDefinedVarError(varName,scope[varName])


        elif (p.getChilds()[2].getName() == "Acont5"):
           value=list(consultTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0],scope).values())[0]
           if (typeVerifier(varType, value)):
               scope[varName] = value
           else:
              alreadyDefinedVarError(varName,scope[varName])

        elif(p.getChilds()[2].getName() == "RangeF"):
            value = functionTranslator(p.getChilds()[2],scope)
            if (typeVerifier(varType, value)):
                scope[varName] = value

            else:
               alreadyDefinedVarError(varName,scope[varName])

    elif (p.getName() == "DoubleAssignment"):
        varList=[]
        valueList=[]
        typeList=[]
        for child in p.getChilds():
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


            elif (child.getName()=="Acont0"):
                valueList.append(tokenTranslator(child.getChilds()[0].getChilds()[0].getToken()))

            elif (child.getName()=="Acont1"):
                value = ""
                temp =child.getChilds()[0].getChilds()[0].getChilds()[0]
                if (temp.getName()=="Factor1"):
                    var = temp.getChilds()[0].getToken()
                    if (var in scope):
                        value = scope[var]
                    else:
                        outOfScopeError(var)
                else:
                    value = tokenTranslator(arithmeticTranslator(child.getChilds()[0],scope))
                valueList.append(value)

            elif (child.getName()=="Acont2"):
                valueList.append(listTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

            elif (child.getName()=="Acont3"):
                valueList.append(matTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

            elif (child.getName()=="Acont4"):
                valueList.append(threeDmatTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

            elif(child.getName()=="Acont5"):
                valueList.append(list(consultTranslator(child.getChilds()[0].getChilds()[0],scope).values())[0])

            elif (child.getName()=="RangeF"):
                valueList.append(functionTranslator(child,scope))


        ind=0
        while(ind<len(varList)):
            if(typeVerifier(typeList[ind],valueList[ind])):
                scope[varList[ind]]=valueList[ind]
            else:
                alreadyDefinedVarError(varList[ind],scope[varList[ind]])
            ind+=1
    globalUpdater(global_var,local_var,local_only)


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

def procedureSem(p):
    global procedures,local_var,global_temp,global_var
    local_var={}
    local_only=[]
    global_temp=[]
    if(not p[4].getChilds()[0].isNull()):
        global_temp=globalUsageSem(p[4].getChilds()[0])
    local_var=globalFetch(global_var,global_temp)
    procName=p[2].getChilds()[0].getChilds()[0].getToken()
    procParams=parameterTranslator(p[2].getChilds()[2].getChilds())
    procBody=p[4].getChilds()[2]

    if(procName in procedures and len(procedures[procName])==len(procParams)):
        sameFirmProcedureError(procName,str(len(procParams)))
    procedures[procName]=procParams

    if(not procBody.isNull()):
        statementQueue=processBodyTranslator(procBody.getChilds())
        for statement in statementQueue:
            if("Assignment" in statement.getName()):
                assignmentSem(statement,"local")

            elif ("Instruction" in statement.getName()):
                instructionSem(statement)

def instructionSem(p):
    if(p.getName()=="Instruction0"):
        functionSem(p.getChilds()[0])

def functionSem(p):
    global global_var,local_var
    temp1=global_var
    temp2=local_var
    scope =local_var
    "TODO: Hacer errores que relacionen al valor de las consultas y no a la variable directamente "
    if(p.getName()=="Function0"):
        varName=""
        if(p.getChilds()[0].getChilds()[2].getName()=="Identifier0"):
            varName=p.getChilds()[0].getChilds()[2].getChilds()[0].getToken()

        elif(p.getChilds()[0].getChilds()[2].getName()=="Identifier1"):
            varName=p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0],local_var)

        if(not existenceVerifier(varName,local_var)):
            outOfScopeError(varName)
    elif(p.getName()=="Function1"):
        #TODO: Actualizar las variables modificadas
        varName = ""
        consult=""
        structure=None
        if (p.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
        elif (p.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            consult=list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var).values())[0]


        if(consult!=""):

            if (type(consult) != type([])):
                insertOnNotIterableObjectError(varName)
            if (p.getChilds()[0].getChilds()[4].getName() == "Fcont6"):

                if(matVerifier(consult)):
                    consult = list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var).keys())[0]
                    insertingBoolOnMatObjectError(consult)
                modifyingOnListInsideMatrixError(varName,"inserting")

            elif (p.getChilds()[0].getChilds()[4].getName() == "Fcont7"):
                structure=consult
                varName=list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var).keys())[0]

        else:
            structure = scope[varName]
            if (not typeVerifier(type([]),scope[varName])):
                insertOnNotIterableObjectError(varName)
            if (p.getChilds()[0].getChilds()[4].getName() == "Fcont6"):
                if (matVerifier(structure)):
                    insertingBoolOnMatObjectError(varName)
                ind=None
                if(p.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable0"):

                    if(indVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0],local_var)):
                        ind=local_var[p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken()]
                    else:
                        notIterableIndError(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken(), "Insert")

                elif (p.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable1"):
                    ind=int(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken())


                value = tokenTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getToken())
                if (ind > len(structure)):
                    outOfBoundsError(ind, varName + ".insert(" + str(ind) + "," + str(value) + ")")
                else:
                    structure.insert(ind, value)
                    scope[varName] = structure


        if (p.getChilds()[0].getChilds()[4].getName() == "Fcont7"):
                if (matrixVerifier(structure)):
                    colSize = len(structure)
                    lineSize = len(structure[0])
                    ind = p.getChilds()[0].getChilds()[4].getChilds()[3]
                    lista = listTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds())
                    if (not ind.isNull()):
                        ind = None
                        if (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable0"):

                            if (indVerifier(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1], local_var)):
                                ind = local_var[p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken()]

                            else:
                                notIterableIndError(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken(), "Insert")

                        elif (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable1"):
                            ind = int(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getToken())

                        if (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 0):
                            if (ind > colSize):
                                outOfBoundsError(ind, varName + ".insert(" + str(lista) + ",0," + str(ind) + ")")
                            else:
                                matrixInserter(0,lista,structure,ind)

                        elif (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 1):
                            if (ind > lineSize):
                                outOfBoundsError(ind, varName + ".insert(" + str(lista) + ",1," + str(ind) + ")")
                            else:
                                matrixInserter(1,lista,structure,ind)
                        else:
                            wrongOperationNumberError("Insertion")

                    elif (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 0):
                        if (len(lista) != lineSize):
                            differentSizeInsertion(str(lista), varName + ".insert(" + str(lista) + ",0)")
                        else:
                            matrixInserter(0, lista,structure,colSize)

                    elif (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 1):
                        if (len(lista) != colSize):
                            differentSizeInsertion(str(lista), varName + ".insert(" + str(lista) + ",1)")
                        else:
                            matrixInserter(1, lista,structure,lineSize)
                    else:
                        wrongOperationNumberError("Insertion")
                else:
                    insertingListOnNoMatObjectError(varName)


    elif (p.getName() == "Function2"):
        varName = None
        consult = None
        structure=None
        if (p.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            structure=local_var[varName]
        elif (p.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            consult = list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var).values())[0]

        if (consult!=None):
            if (not isinstance(consult,list)):
                delOnNotIterableObjectError(varName)
            modifyingOnListInsideMatrixError(varName,"deleting")
        else:
            if(not isinstance(scope[varName],list)):
                delOnNotIterableObjectError(varName)

            ind=None
            indrep=None
            if(p.getChilds()[0].getChilds()[4].getName()=="Iterable0"):
                if (indVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0], local_var)):
                    ind = int(local_var[p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken()])
                    indrep=p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken()
                else:
                    notIterableIndError(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken(),"Del")
            elif((p.getChilds()[0].getChilds()[4].getName()=="Iterable1")):
                ind=int(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken())
                indrep=ind
            #TODO:Añadir error para indices negativos
            if(ind>=len(structure)):
                outOfBoundsError(ind,varName+".del("+str(indrep)+")")
            structure.pop(ind)




    elif (p.getName() == "Function3"):
        varName =None
        if (p.getChilds()[0].getChilds()[2].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[2].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
        elif (p.getChilds()[0].getChilds()[2].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0], local_var)



    elif (p.getName() == "Function4"):
        varName = None
        consult = None
        if (p.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
        elif (p.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            consult = list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var).values())[0]

        if(consult!=None):
            expresion= list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var).keys())[0]
            local_var[varName]=structureUpdater(nope(consult),local_var[varName],expresion)

        else:
            if(not(isinstance(local_var[varName],list) or isinstance(local_var[varName],bool))):
                negOnNotBooleanError(varName)
            local_var[varName]=nope(local_var[varName])

    elif (p.getName() == "Function5"):
        varName = None
        consult = None
        type=p.getChilds()[0].getChilds()[2].getChilds()[0].getToken()
        if (p.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
        elif (p.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            consult = list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var).values())[0]
        if(consult!=None):
            expresion =list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var).keys())[0]
            local_var[varName] = structureUpdater(tF(consult,type), local_var[varName], expresion)

        else:
            if(not(isinstance(local_var[varName],list) or isinstance(local_var[varName],bool))):
                tfOnNotBooleanError(varName)
            local_var[varName] = tF(local_var[varName],type)

    elif (p.getName() == "Function6"):
        varName = ""
        consult = ""
        #TODO:Hacer un error para un valor de tiempo negativo
        if (p.getChilds()[0].getChilds()[2].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
        elif (p.getChilds()[0].getChilds()[2].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            consult = list(consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0], local_var).values())[0]

        if (consult != ""):
            print("Test")
        else:
            if(not(isinstance(local_var[varName],list) or isinstance(local_var[varName],bool))):
                BlinkOnNotBooleanError(varName)
    elif (p.getName() == "Function7"):
        varName = None
        consult = None
        ind=None
        if(not p.getChilds()[0].getChilds()[2].isNull()):
            if (p.getChilds()[0].getChilds()[2].getChilds()[0].getName() == "Iterable0"):
                if(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                    varName = p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
                    if (not existenceVerifier(varName, local_var)):
                        outOfScopeError(varName)
                    ind=local_var[varName]
                elif (p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                    consult = list(consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var).keys())[0]
                    boolOnTempError(consult)

            elif (p.getChilds()[0].getChilds()[2].getChilds()[0].getName() == "Iterable1"):
                ind= int(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getToken())

            if(not isinstance(local_var[varName],int)):
                    boolOnTempError(varName)

    elif (p.getName() == "Function8"):
        varName = ""
        consult = ""
        if (p.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
        elif (p.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var)

        if (not existenceVerifier(varName, local_var)):
            outOfScopeError(varName)
        if (list(consult.values())[0] != ""):

            if (not matrixVerifier(list(consult.values())[0])):
                shapeOnNotMatrixError(list(consult.keys())[0])
        else:
            if (not matrixVerifier(local_var[varName])):
                shapeOnNotMatrixError(varName)

    elif (p.getName() == "Function9"):
        varName = ""
        consult = ""
        mat=""
        if (p.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
        elif (p.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var)

        if (not existenceVerifier(varName, local_var)):
            outOfScopeError(varName)

        if (consult != ""):

            if (not matVerifier(list(consult.values())[0])):
                deleteOnNotMatrixError(list(consult.keys())[0])
            mat=list(consult.values())[0]

            bounds = matBoundsVerifier(mat)
            if (int(p.getChilds()[0].getChilds()[6].getToken()) == 0):
                line = int(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken())
                if (bounds[0] <= line):
                    outOfBoundsError(line, str(list(consult.keys())[0])+".delete("+str(line)+",0)")
            elif (int(p.getChilds()[0].getChilds()[6].getToken()) == 1):
                column = int(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken())
                if (bounds[1] <= column):
                    outOfBoundsError(column, str(list(consult.keys())[0])+".delete("+str(column)+",1)")

        else:
            if(not matVerifier(local_var[varName])):
                deleteOnNotMatrixError(varName)
            mat=local_var[varName]

            bounds = matBoundsVerifier(mat)
            if (int(p.getChilds()[0].getChilds()[6].getToken()) == 0):
                line = int(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken())
                if (bounds[0] <= line):
                    outOfBoundsError(line, varName + ".delete(" + str(line) + ",0)")
            elif (int(p.getChilds()[0].getChilds()[6].getToken()) == 1):
                column = int(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken())
                if (bounds[1] <= column):
                    outOfBoundsError(column, varName + ".delete(" + str(column) + ",1)")

        if(int(p.getChilds()[0].getChilds()[6].getToken())>1 or int(p.getChilds()[0].getChilds()[6].getToken())<0):
            wrongOperationNumberError()

    globalUpdater(global_var,local_var,local_only)





def globalUsageSem(globalCall):
    global global_var
    globals=globalCall.getChilds()
    output=[]
    for valor in globals:
        if(valor.isNull()):
            break
        elif(valor.getName()=="GlobalTerm0"):
            output.extend(globalSplitter(valor.getChilds()))
        elif(valor.getName()=="GlobalTerm1"):
            output.append(valor.getChilds()[0].getToken())
        elif(valor.getName()=="GlobalCall"):
            output.extend(globalUsageSem(valor))
    for valor in output:
        if(valor not in global_var):
            outOfGlobalScopeError(valor)
    return output

def varViewer():
    print("---------Global Scope---------")
    keys = list(global_var.keys())
    for test in keys:
        print(str(test) + ": " + str(global_var[test]))
    print(" ")
    print(" ")
    print("---------Local Scope---------")
    keys = list(local_var.keys())
    for test in keys:
        print(str(test) + ": " + str(local_var[test]))