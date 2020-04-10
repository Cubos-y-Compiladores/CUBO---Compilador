import sys
from Tools.Tools import *
from pip._vendor import colorama
global global_var,regular_var
global_var={}
regular_var={}
def globalAssignmentSem(p):
    global global_var
    temp=global_var
    varName=p[2].getChilds()[0].getChilds()[0].getToken()
    if(varName in global_var):
       alreadyDefinedVarError(varName)

    else:
       if(p[2].getName()=="SimpleAssignment"):
           if(p[2].getChilds()[2].getName()=="Acont0"):
               global_var[varName]=tokenTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[0].getToken())
               p[2].getChilds()[0].getChilds()[0].setType("NumbVar")

           elif (p[2].getChilds()[2].getName() == "Acont1"):
               global_var[varName]=tokenTranslator(arithmeticTranslator(p[2].getChilds()[2].getChilds()[0],global_var))
               p[2].getChilds()[0].getChilds()[0].setType("NumbVar")

           elif (p[2].getChilds()[2].getName() == "Acont2"):
               global_var[varName] =listTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               p[2].getChilds()[0].getChilds()[0].setType("ListVar")

           elif (p[2].getChilds()[2].getName() == "Acont3"):
               global_var[varName]=matTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               p[2].getChilds()[0].getChilds()[0].setType("MatVar")

           elif (p[2].getChilds()[2].getName() == "Acont4"):
               global_var[varName]=threeDmatTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[1].getChilds())
               p[2].getChilds()[0].getChilds()[0].setType("ThreeDMatVar")

           elif (p[2].getChilds()[2].getName() == "Acont5"):
               global_var[varName]=consultTranslator(p[2].getChilds()[2].getChilds()[0].getChilds()[0],global_var)
               print("test")

       elif (p[2].getName() == "DoubleAssignment"):
            varList=[]
            valueList=[]
            for child in p[2].getChilds():
                if(child.getName()=="Identifier0"):
                    varList.append(child.getChilds()[0].getToken())

                elif(child.getName()=="Identifier1"):
                    print(colorama.Fore.RED + "SEMANTIC ERROR: List and Matrix positions can't be defined as global variables")
                    sys.exit()
                elif (child.getName() == "Acont0"):
                    valueList.append(tokenTranslator(child.getChilds()[0].getChilds()[0].getToken()))

                elif (child.getName() == "Acont1"):
                    valueList.append(tokenTranslator(arithmeticTranslator(child.getChilds()[0],global_var)))
                    print("test")

                elif (child.getName() == "Acont2"):
                    valueList.append(listTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

                elif (child.getName() == "Acont3"):
                    valueList.append(matTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

                elif (child.getName() == "Acont4"):
                    valueList.append(threeDmatTranslator(child.getChilds()[0].getChilds()[1].getChilds()))

                elif(child.getName()=="Acont5"):
                    if (child.getChilds()[0].getChilds()[0].getName() == "ListConsult"):
                        temp = child.getChilds()[0].getChilds()[0].getChilds()[0].getToken()
                        if (temp not in global_var):
                            print(
                                colorama.Fore.RED + "SEMANTIC ERROR: The variable " + temp + " hasn't been defined in this scope")
                            sys.exit()

                        else:
                            indice=child.getChilds()[0].getChilds()[0].getChilds()[1].getChilds()[1].getChilds()[0].getToken()
                            valueList.append(global_var[temp][indice])

            ind=0
            while(ind<len(varList)):
                global_var[varList[ind]]=valueList[ind]
                ind+=1



