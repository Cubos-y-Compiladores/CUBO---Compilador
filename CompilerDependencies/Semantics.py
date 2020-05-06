import sys
from Tools.Tools import *
from pip._vendor import colorama
global global_var,global_temp,regular_var,procedures
#TODO: Agregar estructuras vacias
global_var={}
global_temp=[]
local_var={}
local_only=[]
consts={}
procedures=[]
def semantics(p):
    statementQueue=blockSplitter(p)
    for valor in statementQueue:
        if("Procedure" in valor.getName()):
            procName =valor.getChilds()[1].getChilds()[0].getChilds()[0].getToken()
            procParams =parameterTranslator(valor.getChilds()[1].getChilds())
            for procedure in procedures:
                if(procedure[0]==procName and len(procedure[1])==len(procParams)):
                    sameFirmProcedureError(procName, str(len(procParams)))
            procedures.append((procName,procParams,valor))
        elif("Assignment" in valor .getName()):
            assignmentSem(valor.getChilds()[0],"global")
    temp=global_var
    for proc in procedures:
        params=[]
        for param in proc[1]:
            if(not param[0] in params):
                params.append(param[0])
            else:
                paramWithSameNameError(proc[0],param[0])
        procedureSem(proc)
    print("Test")
def assignmentSem(p,scope):
    global global_var,local_var,local_only
    scopeType=scope

    if(scope=="global"):
        scope=global_var
    elif(scope=="local"):
        scope=local_var

    if(p.getName()=="SimpleAssignment"):
        varName=None
        varType=None
        consult=None
        if(p.getChilds()[0].getName()=="Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getToken()
        elif(p.getChilds()[0].getName()=="Identifier1"):
            varName=p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if(not existenceVerifier(varName,scope)):
                outOfScopeError(varName)
            consult=consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0],scope,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0]))
            varType=list(consult.values())[0]
        if (consult==None and varName in scope):
            varType = scope[varName]
        elif(scopeType=="local" and consult==None):
            local_only.append(varName)
        if(scopeType=="global" or not noneVerifier(varName,scope)):
            if(p.getChilds()[2].getName()=="Acont0"):
               value=tokenTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0].getToken())
               if(typeVerifier(varType,value)):
                   if(consult==None):
                        scope[varName]=value
                   else:
                       scope[varName]=structureUpdater(value,scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
               else:
                   if(consult==None):
                       alreadyDefinedVarError(varName,scope[varName])
                   alreadyDefinedVarError(list(consult.keys())[0],list(consult.values())[0])

            elif (p.getChilds()[2].getName() == "Acont1"):
                value=None
                temp =p.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0]
                if (temp.getName() == "Factor1"):
                    var=temp.getChilds()[0].getToken()
                    if(not noneVerifier(var,scope)):
                        if(var in scope):
                            value=scope[var]
                        else:
                            outOfScopeError(var)
                else:
                    if(valueValidator(p.getChilds()[2].getChilds()[0],scope)):
                        value=tokenTranslator(arithmeticTranslator(p.getChilds()[2].getChilds()[0],scope))
                if(value!=None):
                    if (typeVerifier(varType, value)):
                        if (consult == None):
                            scope[varName] = value
                        else:
                            scope[varName] = structureUpdater(value, scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
                    else:
                        if (consult == None):
                            alreadyDefinedVarError(varName, scope[varName])
                        alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])


            elif (p.getChilds()[2].getName() == "Acont2"):
               value=None
               if(not p.getChilds()[2].getChilds()[0].getName()=="EmptyList"):
                   value=listTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               else:
                   value=[]

               if (typeVerifier(varType, value)):
                   if(consult==None):
                       scope[varName] = value
                   else:
                       val=structureUpdater(value,scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
                       if( not matBoundVerifier(val)):
                           modifyingMatrixWithDifferentSizeLineError(str(list(consult.keys())[0]),value,varName)
                       scope[varName]=val
               else:
                   if (consult == None):
                       alreadyDefinedVarError(varName, scope[varName])
                   alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])

            elif (p.getChilds()[2].getName() == "Acont3"):
               value=matTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               if(not matBoundVerifier(value)):
                   differentDimensionsMatError(value)

               if (typeVerifier(varType, value)):
                   if (consult == None):
                       scope[varName] = value
                   else:
                       if(threeDMatrixVerifier(scope[varName])):
                           if(len(list(consult.values())[0])==len(value)):
                                scope[varName] = structureUpdater(value, scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
                           else:
                               differentMatOnThreeDMatError(list(consult.keys())[0], value)
               else:
                   if (consult == None):
                       alreadyDefinedVarError(varName, scope[varName])
                   alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])

            elif (p.getChilds()[2].getName() == "Acont4"):
               value=threeDmatTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               if (not matBoundVerifier(value)):
                   differentDimensionsMatError(value)
               if (typeVerifier(varType, value)):
                   if (consult == None):
                       scope[varName] = value
                   else:
                       scope[varName] = structureUpdater(value, scope[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
               else:
                   if (consult == None):
                       alreadyDefinedVarError(varName, scope[varName])
                   alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])


            elif (p.getChilds()[2].getName() == "Acont5"):
               value=list(consultTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0],scope,expresionTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0])).values())[0]
               if (typeVerifier(varType, value)):
                   if (consult == None):
                       scope[varName] = value
                   else:
                       scope[varName] = structureUpdater(value, scope[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
               else:
                   if (consult == None):
                       alreadyDefinedVarError(varName, scope[varName])
                   alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])

            elif(p.getChilds()[2].getName() == "RangeF"):
                value = functionTranslator(p.getChilds()[2],scope)
                if (typeVerifier(varType, value)):
                    if (consult == None):
                        scope[varName] = value
                    else:
                        scope[varName] = structureUpdater(value, scope[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])

                else:
                    if (consult == None):
                        alreadyDefinedVarError(varName, scope[varName])
                    alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])

    elif (p.getName() == "DoubleAssignment"):
        varList=[]
        valueList=[]
        typeList=[]
        for child in p.getChilds():
            if(child.getName()=="Identifier0"):
                var=str(child.getChilds()[0].getToken())
                varType = None
                if (var in scope):
                    varType = scope[var]
                varList.append(var)
                typeList.append(varType)

            elif(child.getName()=="Identifier1"):
                if(scopeType=="global"):
                    globalConsultError()
                expr = consultTranslator(child.getChilds()[0].getChilds()[0],scope,expresionTranslator(child.getChilds()[0].getChilds()[0]))
                var=list(expr.keys())[0]
                varType =list(expr.values())[0]
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
                valueList.append(list(consultTranslator(child.getChilds()[0].getChilds()[0],scope,expresionTranslator(child.getChilds()[0].getChilds()[0])).values())[0])

            elif (child.getName()=="RangeF"):
                valueList.append(functionTranslator(child,scope))


        ind=0
        while(ind<len(varList)):
            if("[" in varList[ind]):
                varName=nameFetcher(varList[ind])
                expr=exprFetcher(varList[ind])
                flipped=None
                if(":," in expr):
                    flipped=expr
                    flipped.replace(":,","")

                if(typeVerifier(typeList[ind],valueList[ind])):
                    scope[varName]=structureUpdater(valueList[ind],scope[varName],expr,flipped,varName,varList[ind])
                else:
                    alreadyDefinedVarError(varList[ind],typeList[ind])

            elif(scopeType=="global" or not noneVerifier(varList[ind],scope)):
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
    if(not p[2].getChilds()[3].getChilds()[0].isNull()):
        global_temp=globalUsageSem(p[2].getChilds()[3].getChilds()[0])
    local_var=globalFetch(global_var,global_temp)
    params = p[1]
    temp=local_var
    for param in params:
        if(param[0] in local_var):
            paramInGlobalsError(p[0],param[0])

    local_var.update(params)
    temp=global_temp
    temp1=local_var
    temp2=global_var

    procBody = p[2].getChilds()[3].getChilds()[2]
    if(not procBody.isNull()):
        statementQueue=processBodyTranslator(procBody.getChilds())
        for statement in statementQueue:
            if("Assignment" in statement.getName()):
                assignmentSem(statement,"local")

            elif ("Instruction" in statement.getName()):
                instructionSem(statement)
    varViewer()
def instructionSem(p):
    if(p.getName()=="Instruction0"):
        functionSem(p.getChilds()[0])

def functionSem(p):
    global global_var,local_var,procedures
    temp1=global_var
    temp2=local_var
    scope =local_var
    "TODO: Hacer errores que relacionen al valor de las consultas y no a la variable directamente "
    if(p.getName()=="Function0"):
        varName=""
        if(p.getChilds()[0].getChilds()[2].getName()=="Identifier0"):
            varName=p.getChilds()[0].getChilds()[2].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)

        elif(p.getChilds()[0].getChilds()[2].getName()=="Identifier1"):
            varName=p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            if(not noneVerifier(varName,scope)):
                consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0]))

    elif(p.getName()=="Function1"):
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
            if (not noneVerifier(varName, scope)):
                consult=list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).values())[0]


        if(consult!="" and not noneVerifier(varName,scope)):

            if (not isinstance(consult,list)):
                insertOnNotIterableObjectError(list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0])
            if (p.getChilds()[0].getChilds()[4].getName() == "Fcont6"):
                if(matVerifier(consult)):
                    consult = list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0]
                    insertingBoolOnMatObjectError(consult)
                modifyingOnListInsideMatrixError(varName,"inserting")

            elif (p.getChilds()[0].getChilds()[4].getName() == "Fcont7"):
                structure=consult
                if (threeDMatrixVerifier(local_var[varName])):
                    insertingListOnMatInside3DMatError(varName,list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0])
                varName=list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0]

        elif(not noneVerifier(varName,scope)):
            structure = scope[varName]
            if (not isinstance(scope[varName],list)):
                insertOnNotIterableObjectError(varName)
            if (p.getChilds()[0].getChilds()[4].getName() == "Fcont6"):
                if (matVerifier(structure)):
                    insertingBoolOnMatObjectError(varName)
                ind=None
                if(p.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable0"):
                    if(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                        consultOnIndError("Insert")
                    if(not noneVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken(),scope)):
                        if(indVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0],local_var)):
                            ind=local_var[p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken()]
                        else:
                            nonIterableObjectError(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken())

                elif (p.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable1"):
                    ind=int(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken())

                elif (p.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable2"):
                    consultOnIndError("Insert")
                elif (p.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable3"):
                    consultOnIndError("Insert")

                if(ind!=None):
                    value=None
                    if (p.getChilds()[0].getChilds()[4].getChilds()[2].getName() == "Insertable0"):
                        value=tokenTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getToken())

                    elif(p.getChilds()[0].getChilds()[4].getChilds()[2].getName()=="Insertable1"):
                        if(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getName()=="Identifier0"):
                            if(existenceVerifier(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getToken(),local_var)):
                                if(not noneVerifier(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getToken(),local_var)):
                                    value=local_var[p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getToken()]
                                    if(not isinstance(value,bool)):
                                        insertingNotBoolOnListError(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getToken())
                            else:
                                outOfScopeError(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getToken())

                        elif(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getName()=="Identifier1"):
                            value=list(consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0])).values())[0]
                            if(not isinstance(value,bool)):
                                insertingNotListError(list(consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0])

                    if (ind > len(structure)):
                        outOfBoundsError(ind, varName + ".insert(" + str(ind) + "," + str(value) + ")")
                    elif(value!=None):
                        structure.insert(ind, value)
                        scope[varName] = structure


        if (p.getChilds()[0].getChilds()[4].getName() == "Fcont7" and (consult!="" or not noneVerifier(varName,scope))):
                if (matVerifier(structure)):
                    colSize = len(structure)
                    lineSize = len(structure[0])
                    ind = p.getChilds()[0].getChilds()[4].getChilds()[3]
                    struct=None
                    if(p.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable0"):
                        if(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getName()=="Identifier0"):
                            if (not existenceVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken(), local_var)):
                                outOfScopeError(varName)
                            elif(not noneVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken(), local_var)):
                                struct=local_var[p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken()]
                                if(threeDMatrixVerifier(struct) or not isinstance(struct,list)):
                                    insertingNotListError(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getToken())

                        elif(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                            var=p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
                            if (not existenceVerifier(var, local_var)):
                                outOfScopeError(var)
                            elif (not noneVerifier(var,local_var)):
                                structure_consult = list(consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).values())[0]
                                expr=list(consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0]
                                if(threeDMatrixVerifier(structure_consult)or not isinstance(structure_consult,list)):
                                    insertingNotListError(expr)
                                struct=structure_consult

                    elif(p.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Iterable1"):
                        insertingNotListError((p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken()))

                    elif (p.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable2"):
                        if(consult!=""):
                            if(not matrixVerifier(consult)):
                                insertingNotListError(list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0])
                        else:
                            if(not matrixVerifier(scope[varName])):
                                insertingNotListError(varName)
                        struct = listTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds())

                    elif (p.getChilds()[0].getChilds()[4].getChilds()[0].getName() == "Iterable3"):
                        if (consult != ""):
                            if (not threeDMatrixVerifier(consult)):
                                insertingNotMatrixError(list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0])
                        else:
                            if (not threeDMatrixVerifier(scope[varName])):
                                insertingNotMatrixError(varName)
                        struct = matTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds())


                    if(not struct==None):
                        if (not ind.isNull()):
                            ind = None
                            if (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable0"):
                                if(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getName()=="Identifier0"):
                                    if (indVerifier(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0], local_var)):
                                        if(not noneVerifier(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken(),local_var)):
                                            ind = local_var[p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken()]
                                    else:
                                        nonIterableObjectError(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken())

                                elif (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getName() == "Identifier1"):
                                    var = p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
                                    if (not existenceVerifier(var, local_var)):
                                        outOfScopeError(var)
                                    elif (not noneVerifier(var, local_var)):
                                        expr = list(consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0])).keys())[0]
                                        nonIterableObjectError(expr)


                            elif (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable1"):
                                ind = int(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getToken())

                            elif(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable2"):
                                consultOnIndError("Insert")
                            elif (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName() == "Iterable3 "):
                                consultOnIndError("Insert")

                            if(ind!=None):
                                if (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 0):
                                    if(listVerifier(struct)):
                                        if (len(struct) != lineSize):
                                            differentSizeInsertion(str(struct), varName + ".insert(" + str(struct) + ",0,"+str(ind)+")")
                                        elif (ind > colSize):
                                            outOfBoundsError(ind, varName + ".insert(" + str(struct) + ",0," + str(ind) + ")")
                                        matrixInserter(0,struct,structure,ind)

                                    elif(matrixVerifier(struct)):
                                        lineSize=len(structure[0][0])
                                        colSize=len(structure[0])
                                        heightSize=len(structure)
                                        if (len(struct) != colSize or len(struct[0])!=lineSize):
                                            differentSizeInsertion(str(struct),varName + ".insert(" + str(struct) + ",0," + str(ind) + ")")
                                        elif (ind > heightSize):
                                            outOfBoundsError(ind, varName + ".insert(" + str(struct) + ",0," + str(ind) + ")")
                                        matrixInserter(0, struct, structure, ind)

                                elif (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 1):
                                    if(listVerifier(struct)):
                                        if (len(struct) != colSize):
                                            differentSizeInsertion(str(struct), varName + ".insert(" + str(struct) + ",1,"+str(ind)+")")
                                        elif (ind > lineSize):
                                            outOfBoundsError(ind, varName + ".insert(" + str(struct) + ",1," + str(ind) + ")")

                                        matrixInserter(1,struct,structure,ind)
                                    elif (matrixVerifier(struct)):
                                        lineSize = len(structure[0][0])
                                        colSize = len(structure[0])
                                        heightSize = len(structure)
                                        if (len(struct[0]) != lineSize or len(struct) != heightSize):
                                            differentSizeInsertion(str(struct),varName + ".insert(" + str(struct) + ",1," + str(ind) + ")")
                                        elif (ind > colSize):
                                            outOfBoundsError(ind, varName + ".insert(" + str(struct) + ",0," + str(ind) + ")")
                                        matrixInserter(1, struct, structure, ind)
                                else:
                                    wrongOperationNumberError("Insertion")

                        elif (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 0):
                            if (len(struct) != lineSize):
                                differentSizeInsertion(str(struct), varName + ".insert(" + str(struct) + ",0)")
                            else:
                                matrixInserter(0, struct,structure,colSize)

                        elif (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 1):
                            if (len(struct) != colSize):
                                differentSizeInsertion(str(struct), varName + ".insert(" + str(struct) + ",1)")
                            else:
                                matrixInserter(1, struct,structure,lineSize)
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
            if(not noneVerifier(varName,local_var)):
                consult = list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).values())[0]

        if (consult!=None):
            if (not isinstance(consult,list)):
                delOnNotIterableObjectError(varName)
            modifyingOnListInsideMatrixError(varName,"deleting")

        elif(not noneVerifier(varName,local_var)):
            if(not isinstance(scope[varName],list)):
                delOnNotIterableObjectError(varName)

            ind=None
            indrep=None
            if(p.getChilds()[0].getChilds()[4].getName()=="Iterable0"):
                if(p.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Identifier0"):
                    if (not noneVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken(), local_var)):
                        if (indVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0], local_var)):
                            ind = int(local_var[p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken()])
                            indrep=p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken()
                        else:
                            nonIterableObjectError(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getToken())
                elif(p.getChilds()[0].getChilds()[4].getChilds()[0].getName()=="Identifier1"):
                    consultOnIndError("del")
            elif((p.getChilds()[0].getChilds()[4].getName()=="Iterable1")):
                ind=int(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken())
                indrep=ind
            else:
                consultOnIndError("del")
            if(ind!=None):
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
            if(not noneVerifier(varName,local_var)):
                consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0]))



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
            if (not noneVerifier(varName, local_var)):
                consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]))

        if(consult!=None):
            local_var[varName]=structureUpdater(nope(list(consult.values()))[0],local_var[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])

        elif(not noneVerifier(varName, local_var)):
            if(not(isinstance(local_var[varName],list) or isinstance(local_var[varName],bool))):
                negOnNotBooleanError(varName)
            local_var[varName]=nope(local_var[varName])

    elif (p.getName() == "Function5"):
        varName = None
        consult = None
        typeTF=p.getChilds()[0].getChilds()[2].getChilds()[0].getToken()
        if (p.getChilds()[0].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
        elif (p.getChilds()[0].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            if(not noneVerifier(varName, local_var)):
                consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]))

        if(consult!=None):
            local_var[varName] = structureUpdater(tF(consult,typeTF), local_var[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])

        elif(not noneVerifier(varName, local_var)):
            if(not(isinstance(local_var[varName],list) or isinstance(local_var[varName],bool))):
                tfOnNotBooleanError(varName)
            local_var[varName] = tF(local_var[varName],typeTF)

    elif (p.getName() == "Function6"):
        varName = ""
        consult = ""
        if (p.getChilds()[0].getChilds()[2].getChilds()[0].getName() == "Identifier0"):
            varName = p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
        elif (p.getChilds()[0].getChilds()[2].getChilds()[0].getName() == "Identifier1"):
            varName = p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if (not existenceVerifier(varName, local_var)):
                outOfScopeError(varName)
            if(not noneVerifier(varName, local_var)):
                consult = list(consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0])).values())[0]

        if (consult != ""):
            print("Test")
        elif(not noneVerifier(varName, local_var)):
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
                    if(not noneVerifier(varName, local_var)):
                        ind=local_var[varName]
                    if (not ind==None and not isinstance(ind, int)):
                        boolOnTempError(varName)
                elif (p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getName()=="Identifier1"):
                    consult = list(consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0]
                    boolOnTempError(consult)

            elif (p.getChilds()[0].getChilds()[2].getChilds()[0].getName() == "Iterable1"):
                ind= int(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getToken())
            else:
                consultOnIndError("delay")


    elif (p.getName() == "Function8"):
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
            if(not noneVerifier(varName, local_var)):
                consult =list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).values())[0]


        if (consult!=None):
            if (not matVerifier(consult)):
                shapeOnNotMatrixError(list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])).keys())[0])
        elif(not noneVerifier(varName, local_var)):
            if (not matVerifier(local_var[varName])):
                shapeOnNotMatrixError(varName)

    elif (p.getName() == "Function9"):
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
            if(not noneVerifier(varName, local_var)):
                consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]))

        if (consult != None):
            if (not matrixVerifier(list(consult.values())[0])):
                deleteOnNotMatrixError(list(consult.keys())[0])
            deleteOnMatrixInside3DMatError(list(consult.keys())[0])

        elif(not noneVerifier(varName, local_var)):
            if(not matVerifier(local_var[varName])):
                deleteOnNotMatrixError(varName)
            mat=local_var[varName]
            bounds = matBoundsFetcher(mat)
            ind=None
            if(p.getChilds()[0].getChilds()[4].getName()=="Indice0"):
                ind=int(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken())
            elif(p.getChilds()[0].getChilds()[4].getName()=="Indice1"):
                if (not existenceVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken(), local_var)):
                    outOfScopeError(varName)
                if(not noneVerifier(p.getChilds()[0].getChilds()[4].getChilds()[0].getToken(), local_var)):
                    ind=int(local_var[p.getChilds()[0].getChilds()[4].getChilds()[0].getToken()])
            if(ind!=None):
                if (int(p.getChilds()[0].getChilds()[6].getToken()) == 0):
                    if (bounds[0] <= ind):
                        outOfBoundsError(ind, varName + ".delete(" + str(ind) + ",0)")
                    local_var[varName]=matrixDeleter(0,ind,mat)
                elif (int(p.getChilds()[0].getChilds()[6].getToken()) == 1):
                    if (bounds[1] <= ind):
                        outOfBoundsError(ind, varName + ".delete(" + str(ind) + ",1)")
                    local_var[varName] = matrixDeleter(1, ind, mat)
                else:
                    wrongOperationNumberError("Delete")
    elif (p.getName() == "Function10"):
        procName=p.getChilds()[0].getChilds()[1].getChilds()[0].getChilds()[0].getToken()
        procParams=parameterCallTranslator([p.getChilds()[0].getChilds()[1].getChilds()[2]],local_var)
        temp=procedures
        definedProcs=procNameFetcher(procedures)
        if(not procName in definedProcs):
            notDefinedProcedureCallError(procName)
        params=procParamsFetcher(procName,procedures)
        exists=False
        for valor in params:
            if(len(valor)==len(procParams)):
                exists=True
                break;
        if(not exists):
            notDefinedProcedureCallError(procName)



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