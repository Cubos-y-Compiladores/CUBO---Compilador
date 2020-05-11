import sys
from Tools.Tools import *
from pip._vendor import colorama
global global_var,global_temp,regular_var,procedures
#TODO: Agregar estructuras vacias
global_var={}
global_temp=[]
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
            assignmentSem(valor.getChilds()[0],"global",[],[],False)
    temp=global_var
    for proc in procedures:
        params=[]
        for param in proc[1]:
            if(not param[0] in params):
                params.append(param[0])
            else:
                paramWithSameNameError(proc[0],param[0])
        procedureSem(proc)
def assignmentSem(p,scope,local_var,local_only,called):
    global global_var,consts
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
            if(noneVerifier(varName,scope)):
                return None
            consult=consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0],scope,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0]),called)
            if(consult==None):
                return None
            varType = list(consult.values())[0]
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
                   elif (consult["Aux"] != None):
                           scope[varName]=structureUpdater(value,scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
               else:
                   if(consult==None):
                       alreadyDefinedVarError(varName,scope[varName])
                   if (consult["Aux"] != None):
                       alreadyDefinedVarError(list(consult.keys())[0],list(consult.values())[0])

            elif (p.getChilds()[2].getName() == "Acont1"):
                value=None
                temp =p.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0]
                if (temp.getName() == "Factor1"):
                    var=temp.getChilds()[0].getToken()
                    if(not noneVerifier(var,scope)):

                        if(var in scope):
                            value =scope[var]
                            if(matVerifier(value)):
                                if(not matBoundVerifier(value)):
                                    if(matrixVerifier(value)):
                                        differentDimensionsMatError(var)
                                    differentMatOnThreeDMatError(var)
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
                            if (consult["Aux"] != None):
                                scope[varName] = structureUpdater(value, scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
                    else:
                        if (consult == None):
                            alreadyDefinedVarError(varName, scope[varName])
                        if (consult["Aux"] != None):
                            alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])


            elif (p.getChilds()[2].getName() == "Acont2"):
               value=None
               if(not p.getChilds()[2].getChilds()[0].getName()=="EmptyList"):
                   value=listTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               else:
                   value=[]
               dimensionConstVerifier(value,consts)
               if (typeVerifier(varType, value)):
                   if(consult==None):
                       scope[varName] = value
                   else:
                       if (consult["Aux"] != None):
                           val=structureUpdater(value,scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
                           if( not matBoundVerifier(val)):
                               modifyingMatrixWithDifferentSizeLineError(str(list(consult.keys())[0]),value,varName)
                           scope[varName]=val
               else:
                   if (consult == None):
                       alreadyDefinedVarError(varName, scope[varName])
                   if (consult["Aux"] != None):
                       alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])

            elif (p.getChilds()[2].getName() == "Acont3"):
               value=matTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               if(not matBoundVerifier(value)):
                   differentDimensionsMatError(value)
               dimensionConstVerifier(value,consts)
               if (typeVerifier(varType, value)):
                   if (consult == None):
                       scope[varName] = value
                   else:
                       if (consult["Aux"] != None):
                           if(threeDMatrixVerifier(scope[varName])):
                               if(len(list(consult.values())[0])==len(value)):
                                    scope[varName] = structureUpdater(value, scope[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
                               else:
                                   differentMatOnThreeDMatError(list(consult.keys())[0], value)
               else:
                   if (consult == None):
                       alreadyDefinedVarError(varName, scope[varName])
                   if (consult["Aux"] != None):
                       alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])

            elif (p.getChilds()[2].getName() == "Acont4"):
               value=threeDmatTranslator(p.getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               if (not matBoundVerifier(value)):
                   differentDimensionsMatError(value)
               dimensionConstVerifier(value,consts)
               if (typeVerifier(varType, value)):
                   if (consult == None):
                       scope[varName] = value
                   else:
                       if (consult["Aux"] != None):
                           scope[varName] = structureUpdater(value, scope[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
               else:
                   if (consult == None):
                       alreadyDefinedVarError(varName, scope[varName])

                   if (consult["Aux"] != None):
                       alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])


            elif (p.getChilds()[2].getName() == "Acont5"):
               consultName=p.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
               if(not noneVerifier(consultName,scope)):
                   con=consultTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0],scope,expresionTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0]),called)
                   if(con==None):
                       return None
                   value=list(con.values())[0]
                   if (typeVerifier(varType, value)):
                       if (consult == None):
                           scope[varName] = value
                       else:
                           if (consult["Aux"] != None):
                               scope[varName] = structureUpdater(value, scope[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])
                   else:
                       if (consult == None):
                           alreadyDefinedVarError(varName, scope[varName])

                       if (consult["Aux"] != None):
                           alreadyDefinedVarError(list(consult.keys())[0], list(consult.values())[0])

            elif(p.getChilds()[2].getName() == "RangeF"):
                value = functionTranslator(p.getChilds()[2],scope)
                if (typeVerifier(varType, value)):
                    if (consult == None):
                        scope[varName] = value
                    else:
                        if (consult["Aux"] != None):
                            scope[varName] = structureUpdater(value, scope[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])

                else:
                    if (consult == None):
                        alreadyDefinedVarError(varName, scope[varName])
                    if (consult["Aux"] != None):
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
                expr = consultTranslator(child.getChilds()[0].getChilds()[0],scope,expresionTranslator(child.getChilds()[0].getChilds()[0]),called)
                if(expr==None):
                    return None
                if(expr["Aux"]==None):
                    varList.append(None)
                    typeList.append(None)
                else:
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
                value=listTranslator(child.getChilds()[0].getChilds()[1].getChilds())
                dimensionConstVerifier(value,consts)
                valueList.append(value)

            elif (child.getName()=="Acont3"):
                value=matTranslator(child.getChilds()[0].getChilds()[1].getChilds())
                if(not matBoundVerifier(value)):
                    differentDimensionsMatError(value)
                dimensionConstVerifier(value,consts)
                valueList.append(value)

            elif (child.getName()=="Acont4"):
                value=threeDmatTranslator(child.getChilds()[0].getChilds()[1].getChilds())
                if (not matBoundVerifier(value)):
                    differentDimensionsMatError(value)
                dimensionConstVerifier(value, consts)
                valueList.append(value)

            elif(child.getName()=="Acont5"):
                value=consultTranslator(child.getChilds()[0].getChilds()[0],scope,expresionTranslator(child.getChilds()[0].getChilds()[0]),called)
                if(value==None):
                    return None
                if(value["Aux"]==None):
                    valueList.append("None")
                else:
                    valueList.append(list(value.values())[0])

            elif (child.getName()=="RangeF"):
                valueList.append(functionTranslator(child,scope))


        ind=0
        while(ind<len(varList)):
            if(varList[ind]!=None and valueList[ind]!=None):
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
    return(local_var,local_only)


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
    global procedures,global_temp,global_var
    local_var={}
    local_only=[]
    global_temp=[]
    call=False
    if(not p[2].getChilds()[3].getChilds()[0].isNull()):
        global_temp=globalUsageSem(p[2].getChilds()[3].getChilds()[0])
    local_var=globalFetch(global_var,global_temp)
    params = p[1]
    tempParams = params.copy()
    temp=tuple(tempParams)
    tempParams="("
    for valor in temp:
        tempParams+=str(valor)
    tempParams+=")"
    t="\&"
    t=t.replace("&","")
    tempParams=tempParams.replace(t,"")


    temp=local_var
    for param in params:
        if(param[0] in local_var):
            paramInGlobalsError(p[0],param[0])
        if(not call and param[1]!=None):
            call=True

    local_var.update(params)
    temp=global_temp
    temp1=local_var
    temp2=global_var

    procBody = p[2].getChilds()[3].getChilds()[2]
    if(not procBody.isNull()):
        statementQueue=processBodyTranslator(procBody.getChilds())
        for statement in statementQueue:
            if("Assignment" in statement.getName()):
                assignmentSem(statement,"local",local_var,local_only,call)

            elif ("Instruction" in statement.getName()):
                backup =(local_var.copy(), local_only.copy())
                instructionSem(statement, local_var, local_only,call)
                localsUpdater(backup, local_var, global_var)
                local_var = backup[0]
                local_only = backup[1]
    globalUpdater(local_var, global_var, local_only)
    if(call):
        varViewer(local_var,"Procedure Call: "+str(p[0])+" "+str(tempParams))
    else:
        varViewer(local_var,"Procedure Revision: "+str(p[0])+" "+str(tempParams))
def instructionSem(p,local_var,local_only,called):
    dicts=None
    if(p.getName()=="Instruction0"):
        return functionSem(p.getChilds()[0],local_var,local_only,called)

    elif (p.getName()=="Instruction1"):
       varName=p.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
       if(not existenceVerifier(varName,local_var)):
           outOfScopeError(varName)

    elif (p.getName() == "Instruction2"):
        cycleSem(p.getChilds()[0].getChilds()[0],local_var,local_only,called)

    elif(p.getName()=="Instruction3"):
        statementSem(p.getChilds()[0],local_var,local_only,called)
    return (local_var,local_only)
def cycleSem(p,local_var,local_only,called):
    iterable=None
    if(p.getChilds()[3].getName()=="Iterable0"):
        if(p.getChilds()[3].getChilds()[0].getName()=="Identifier0"):
            varName=p.getChilds()[3].getChilds()[0].getChilds()[0].getToken()
            if(not existenceVerifier(varName,local_var)):
                outOfScopeError(varName)
            elif(not (listVerifier(local_var[varName]) or isinstance(local_var[varName],int))):
                notIterableObjectOnFor(varName)
            iterable=(varName,local_var[varName])

        elif(p.getChilds()[3].getChilds()[0].getName()=="Identifier1"):
            varName=p.getChilds()[3].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if(not existenceVerifier(varName,local_var)):
                outOfScopeError(varName)
            consult=consultTranslator(p.getChilds()[3].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[3].getChilds()[0].getChilds()[0].getChilds()[0]),called)
            if(consult==None):
                return None
            iterable=(list(consult.keys())[0],list(consult.values())[0])

    elif(p.getChilds()[3].getName()=="Iterable1"):
        iterable=("INT",int(p.getChilds()[3].getChilds()[0].getToken()))

    elif(p.getChilds()[3].getName()=="Iterable2"):
        iterable=("LIST",listTranslator(p.getChilds()[3].getChilds()[0].getChilds()))
        print("Test")

    exec(p.getChilds()[1].getToken()+"=0")
    step=None
    if(p.getChilds()[4].isNull()):
        step=1
    else:
        step=int(p.getChilds()[4].getChilds()[1].getToken())
    if(p.getChilds()[6].isNull()):
        if(iterable[0]=="INT" or iterable[0]=="LIST"):
            nullCycleBody("for "+p.getChilds()[1].getToken()+" in "+str(iterable[1])+" Step "+str(eval(p.getChilds()[1].getToken())))
        nullCycleBody("for "+p.getChilds()[1].getToken()+" in "+str(iterable[0])+" Step "+str(eval(p.getChilds()[1].getToken())))
    if(iterable[1]!=None):
        lineQueue = processBodyTranslator(p.getChilds()[6].getChilds())
        for line in lineQueue:
            if ("SimpleAssignment" in line.getName() or "DoubleAssignment" in line.getName()):
                assignmentSem(line, "local", local_var, local_only)
            elif (line.getName() == "Instruction3"):
                backup = (local_var.copy(), local_only.copy())
                instructionSem(line, local_var, local_only,called)
                localsUpdater(backup, local_var, global_var)
                local_var = backup[0]
                local_only = backup[1]

            elif ("Instruction" in line.getName()):
                instructionSem(line, local_var, local_only)
def statementSem(p,local_var,local_only,called):
    iterable=None
    consult=None
    bifValue=None
    if(p.getChilds()[2].getName()=="Iterable0"):
        if(p.getChilds()[2].getChilds()[0].getName()=="Identifier0"):
            varName=p.getChilds()[2].getChilds()[0].getChilds()[0].getToken()
            if(not existenceVerifier(varName,local_var)):
                outOfScopeError(varName)
            iterable=(varName,local_var[varName])

        elif(p.getChilds()[2].getChilds()[0].getName()=="Identifier1"):
            varName=p.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
            if(not existenceVerifier(varName,local_var)):
                outOfScopeError(varName)
            expr=expresionTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0])
            if(not noneVerifier(varName,local_var)):
                consult=consultTranslator(p.getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expr,called)
                if(consult==None):
                    return None
                iterable=(expr,consult[expr])
            else:
                iterable=(expr,None)

    elif(p.getChilds()[2].getName()=="Iterable1"):
        iterable=("Iterable",int(p.getChilds()[2].getChilds()[0].getToken()))

    elif(p.getChilds()[2].getName()=="Iterable2"):
        iterable=("List",listTranslator(p.getChilds()[2].getChilds()[0].getChilds()))

    operator=tokenTranslator(p.getChilds()[3].getChilds()[0].getToken())

    if(p.getChilds()[4].getName()=="BifValue0"):
        bifValue=("Bool",tokenTranslator(p.getChilds()[4].getChilds()[0].getChilds()[0].getToken()))

    elif(p.getChilds()[4].getName()=="BifValue1"):
        arithmetic=None
        if(p.getChilds()[4].getChilds()[0].getName()=="Arithmetic0"):
            if(p.getChilds()[4].getChilds()[0].getChilds()[0].getName()=="Term0"):
                if(p.getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getName()=="Factor1"):
                    varName=p.getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
                    if(not existenceVerifier(varName,local_var)):
                        outOfScopeError(varName)
                    bifValue=(varName,local_var[varName])
                elif(valueValidator(p.getChilds()[4].getChilds()[0],local_var)):
                    arithmetic=arithmeticTranslator(p.getChilds()[4].getChilds()[0],local_var)
            elif(valueValidator(p.getChilds()[4].getChilds()[0],local_var)):
                arithmetic = arithmeticTranslator(p.getChilds()[4].getChilds()[0], local_var)
        elif(valueValidator(p.getChilds()[4].getChilds()[0],local_var)):
            arithmetic = arithmeticTranslator(p.getChilds()[4].getChilds()[0], local_var)

        if(arithmetic!=None):
            bifValue=("Arithmetic",tokenTranslator(arithmetic))
        elif(bifValue==None):
            bifValue=("Arithmetic",None)
    if(iterable[1]!=None and bifValue[1]!=None):
        statement=False
        if(not isinstance(iterable[1],list)):
            statement=eval(str(iterable[1])+str(operator)+str(bifValue[1]))
        else:
            if(listVerifier(iterable[1])):
                for valor in iterable[1]:
                    if(eval(str(valor)+str(operator)+str(bifValue[1]))):
                        statement=True
                        break
            elif(matrixVerifier(iterable[1])):
                breaker=False
                for line in iterable[1]:
                    for col in line:
                        if (eval(str(col) + str(operator) + str(bifValue[1]))):
                            statement=True
                            breaker=True
                            break;
                    if(breaker):
                        break
            elif (threeDMatrixVerifier(iterable[1])):
                breaker=False
                for mat in iterable[1]:
                    for line in mat:
                        for col in line:
                            if (eval(str(col) + str(operator) + str(bifValue[1]))):
                                statement = True
                                breaker = True
                                break;
                        if (breaker):
                            break
                    if(breaker):
                        break
        if(statement):
            if(p.getChilds()[7].isNull()):
                if("Arithmetic" in bifValue[0] or "Bool" in bifValue[0]):
                    if (not ("Iterable" in iterable[0] or "List" in iterable[0])):
                        nullStatementBody("if("+str(iterable[0]+str(operator)+str(bifValue[1])+")"))
                    nullStatementBody("if(" + str(iterable[1] + str(operator) + str(bifValue[1]) + ")"))
                if (not ("Iterable" in iterable[0] or "List" in iterable[0])):
                    nullStatementBody("if(" + str(iterable[0]) + str(operator) + str(bifValue[0]) + ")")
                nullStatementBody("if(" + str(iterable[1]) + str(operator) + str(bifValue[0]) + ")")

            lineQueue=processBodyTranslator(p.getChilds()[7].getChilds())
            for line in lineQueue:
               if("SimpleAssignment" in line.getName() or "DoubleAssignment" in line.getName()):
                   assignmentSem(line,"local",local_var,local_only,called)
               elif(line.getName()=="Instruction3"):
                   backup=(local_var.copy(),local_only.copy())
                   instructionSem(line,local_var,local_only,called)
                   localsUpdater(backup,local_var,global_var)
                   local_var=backup[0]
                   local_only=backup[1]

               elif("Instruction" in line.getName()):
                   instructionSem(line,local_var,local_only)

    if(not p.getChilds()[9].isNull()):
        if(not p.getChilds()[9].getChilds()[2].isNull()):
            lineQueue = processBodyTranslator(p.getChilds()[9].getChilds()[2].getChilds())
            for line in lineQueue:
                if ("SimpleAssignment" in line.getName() or "DoubleAssignment" in line.getName()):
                    assignmentSem(line, "local", local_var, local_only)
                elif (line.getName() == "Instruction3"):
                    backup = (local_var.copy(), local_only.copy())
                    instructionSem(line, local_var, local_only)
                    localsUpdater(backup, local_var, global_var)
                    local_var = backup[0]
                    local_only = backup[1]

                elif ("Instruction" in line.getName()):
                    instructionSem(line, local_var, local_only)
        else:
            nullStatementBody("ELSE")
    return (local_var,local_only)



def functionSem(p,local_var,local_only,called):
    global global_var,procedures
    temp1=global_var
    temp2=local_var
    scope =local_var
    called=False
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
                consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0]),called)

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
                consult=consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                if(consult==None or consult["Aux"]==None):
                    return None
                consult=list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called).values())[0]


        if(consult!="" and not noneVerifier(varName,scope)):

            if (not isinstance(consult,list)):
                insertOnNotIterableObjectError(expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]))
            if (p.getChilds()[0].getChilds()[4].getName() == "Fcont6"):
                if(matVerifier(consult)):
                    consult =expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
                    insertingBoolOnMatObjectError(consult)
                modifyingOnListInsideMatrixError(varName,"inserting")

            elif (p.getChilds()[0].getChilds()[4].getName() == "Fcont7"):
                structure=consult
                if (threeDMatrixVerifier(local_var[varName])):
                    insertingListOnMatInside3DMatError(varName,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]))
                varName=expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])

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
                            con=consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                            if(con==None):
                                return None
                            value=list(con.values())[0]
                            if(not isinstance(value,bool)):
                                insertingNotListError(expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0]))

                    if (ind > len(structure) and called):
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
                                con=consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                                if(con==None):
                                    return None
                                structure_consult = list(con.values())[0]
                                expr=expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
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
                                insertingNotMatrixError(expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]))
                        else:
                            if (not threeDMatrixVerifier(scope[varName])):
                                insertingNotMatrixError(varName)
                        struct = matTranslator(p.getChilds()[0].getChilds()[4].getChilds()[0].getChilds()[0].getChilds())


                    if(not struct==None):
                        if (not ind.isNull()):
                            ind = None
                            if (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getName()=="Iterable0"):
                                if(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getName()=="Identifier0"):
                                    if (not noneVerifier(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken(), local_var)):
                                        if (indVerifier(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0], local_var)):
                                                ind = local_var[p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken()]
                                        else:
                                            nonIterableObjectError(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getToken())

                                elif (p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getName() == "Identifier1"):
                                    var = p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0].getChilds()[0].getToken()
                                    if (not existenceVerifier(var, local_var)):
                                        outOfScopeError(var)
                                    elif (not noneVerifier(var, local_var)):
                                        con=consultTranslator(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[4].getChilds()[3].getChilds()[1].getChilds()[0].getChilds()[0]),called)
                                        if(con==None):
                                            return None
                                        expr = list(con.keys())[0]
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
                                        elif (ind > colSize and called):
                                            outOfBoundsError(ind, varName + ".insert(" + str(struct) + ",0," + str(ind) + ")")
                                        matrixInserter(0,struct,structure,ind)

                                    elif(matrixVerifier(struct)):
                                        lineSize=len(structure[0][0])
                                        colSize=len(structure[0])
                                        heightSize=len(structure)
                                        if (len(struct) != colSize or len(struct[0])!=lineSize):
                                            differentSizeInsertion(str(struct),varName + ".insert(" + str(struct) + ",0," + str(ind) + ")")
                                        elif (ind > heightSize and called):
                                            outOfBoundsError(ind, varName + ".insert(" + str(struct) + ",0," + str(ind) + ")")
                                        matrixInserter(0, struct, structure, ind)

                                elif (int(p.getChilds()[0].getChilds()[4].getChilds()[2].getToken()) == 1):
                                    if(listVerifier(struct)):
                                        if (len(struct) != colSize):
                                            differentSizeInsertion(str(struct), varName + ".insert(" + str(struct) + ",1,"+str(ind)+")")
                                        elif (ind > lineSize and called):
                                            outOfBoundsError(ind, varName + ".insert(" + str(struct) + ",1," + str(ind) + ")")

                                        matrixInserter(1,struct,structure,ind)
                                    elif (matrixVerifier(struct)):
                                        lineSize = len(structure[0][0])
                                        colSize = len(structure[0])
                                        heightSize = len(structure)
                                        if (len(struct[0]) != lineSize or len(struct) != heightSize):
                                            differentSizeInsertion(str(struct),varName + ".insert(" + str(struct) + ",1," + str(ind) + ")")
                                        elif (ind > colSize and called):
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
                consult=consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                if(consult==None or consult["Aux"]==None):
                    return None
                consult = list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called).values())[0]

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
                if(ind>=len(structure) and called):
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
                consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0]),called)



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
                consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                if(consult==None or consult["Aux"]==None):
                    return None

        if(consult!=None):
            local_var[varName]=structureUpdater(nope(list(consult.values())[0]),local_var[varName],consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])

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
                consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                if(consult!=None or consult["Aux"]==None):
                    return None

        if(consult!=None):
            local_var[varName] = structureUpdater(tF(list(consult.values())[0],typeTF), local_var[varName], consult["Aux"],consult["Flipped"],varName,list(consult.keys())[0])

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
                consult=consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0], local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                if(consult==None or consult["Aux"]==None):
                    return None
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
                    consult=consultTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                    if(consult==None or consult["Aux"]==None):
                        return None
                    consult =expresionTranslator(p.getChilds()[0].getChilds()[2].getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0])
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
                consult=consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                if(consult!=None or consult["Aux"]==None):
                    return None
                consult =list(consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called).values())[0]


        if (consult!=None):
            if (not matVerifier(consult)):
                shapeOnNotMatrixError(expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]))
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
                consult =consultTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0],local_var,expresionTranslator(p.getChilds()[0].getChilds()[0].getChilds()[0].getChilds()[0]),called)
                if(consult==None or consult["Aux"]==None):
                    return None

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
                    if (bounds[0] <= ind and called):
                        outOfBoundsError(ind, varName + ".delete(" + str(ind) + ",0)")
                    local_var[varName]=matrixDeleter(0,ind,mat)
                elif (int(p.getChilds()[0].getChilds()[6].getToken()) == 1):
                    if (bounds[1] <= ind and called):
                        outOfBoundsError(ind, varName + ".delete(" + str(ind) + ",1)")
                    local_var[varName] = matrixDeleter(1, ind, mat)
                else:
                    wrongOperationNumberError("Delete")
    elif (p.getName() == "Function10"):
        temp=procedures
        procName=p.getChilds()[0].getChilds()[1].getChilds()[0].getChilds()[0].getToken()
        usedProc = None
        exists = False
        callParams=None
        for proc in procedures:
            if(procName==proc[0]):
                callParams=parameterCallTranslator(p.getChilds()[0].getChilds()[1].getChilds()[2].getChilds(),local_var)
                if(len(proc[1])==len(callParams)):
                    exists=True
                    usedProc=proc
                    break
        if(exists):
            tempParams=[]
            ind=0
            for callP in callParams:
                tempParams.append((usedProc[1][ind][0],callP))
                ind+=1
            tempProc=(usedProc[0],tempParams,usedProc[2])
            procedureSem(tempProc)
            local_var=globalUpdater(local_var,global_var,local_only)
            called=True
        else:
            notDefinedProcedureCallError(procName)


    if(not called):
        globalUpdater(global_var,local_var,local_only)
    return(local_var,local_only)




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

def varViewer(local_var,title):
    print(title+"\n")
    print("---------Global Scope---------")
    keys = list(global_var.keys())
    for test in keys:
        print(str(test) + ": " + str(global_var[test]))
    print("\n\n")
    print("---------Local Scope---------")
    keys = list(local_var.keys())
    for test in keys:
        print(str(test) + ": " + str(local_var[test]))
    print("\n\n")