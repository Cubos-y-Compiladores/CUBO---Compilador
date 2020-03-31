output= " "
cont = 0
def counterIncreaser():
	global cont
	cont +=1
	return "%d" %cont

class Node():
	pass

class Null(Node):
	def __init__(self):
		self.type = 'void'

	def printer(self,ident):
		print (ident + "Null node")

	def traducir(self):
		global output
		id = counterIncreaser()
		output += id+"[label= "+"Null node"+"]"+"\n\t"

		return id





##########---BLOQUES BASICOS---#########
class Program(Node):
    def __init__(self,name,son1,son2):
        self.name=name
        self.son1=son1
        self.son2=son2

    def printer(self, ident):
        self.son1.printer(" "+ident)
        self.son2.printer(" "+ident)

    def translate(self):
        global output
        id=counterIncreaser()
        son1=self.son1.translate()
        son2=self.son2.translate()

        output += id+"[label= "+self.name+"]"+"\n\t"
        output += id + "->" + son1 + "\n\t"
        output += id + "->" + son2 + "\n\t"

        return "digraph G {\n\t" + output+ "}"

class ConstB(Node):

    def __init__(self,name,son1,son2,son3,son4,son5,son6):
        self.name=name
        self.son1=son1
        self.son2=son2
        self.son3=son3
        self.son4=son4
        self.son5=son5
        self.son6=son6

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)

        if(type(self.son6)==type(tuple())):
            self.son6[0].printer(" " + ident)

        else:
            self.son6.printer(" "+ ident)

    def translate(self):
        global output
        id=counterIncreaser()

        son1=self.son1.translate()
        son2=self.son2.translate()
        son3=self.son3.translate()
        son4=self.son4.translate()
        son5=self.son5.translate()
        if (type(self.son6) == type(tuple())):
            son6=self.son6[0].translate()

        else:
            son6=self.son6.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"

        return id

class Block0(Node):
    def __init__(self,name,son1,son2):
        self.name=name
        self.son1=son1
        self.son2=son2

    def printer(self, ident):
        self.son1.printer(" "+ident)
        if (type(self.son2) == type(tuple())):
            self.son2[0].printer(" " + ident)

        else:
            self.son2.printer(" " + ident)

    def translate(self):
        global output
        id=counterIncreaser()
        son1=self.son1.translate()
        if type(self.son2) == type(tuple()):
            son2=self.son2[0].translate()

        else:
            son2=self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id

class Block1(Node):

    def __init__(self,name,son1,son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printer(self, ident):
        self.son1.printer(" " + ident)
        if (type(self.son2) == type(tuple())):
            self.son2[0].printer(" " + ident)

        else:
            self.son2.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        if (type(self.son2) == type(tuple())):
            son2 = self.son2[0].translate()

        else:
            son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id





##########---BLOQUES ALTERNATIVOS---##########
class p_altBlock(Node):

    def __init__(self,name,son1,son2):
        self.name=name
        self.son1=son1
        self.son2=son2

    def printer(self, ident):
        self.son1.printer(" " + ident)
        if (type(self.son2) == type(tuple())):
            self.son2[0].printer(" " + ident)

        else:
            self.son2.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        if (type(self.son2) == type(tuple())):
            son2 = self.son2[0].translate()

        else:
            son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id

class AltContent0(Node):

    def __init__(self,name,son1):
        self.name=name
        self.son1=son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class p_altContent1(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id





##########---INSTRUCCIONES---##########
class Instruction0(Node):

    def __init__(self,name,son1):
        self.name=name
        self.son1=son1

    def printer(self, ident):
        self.son1.printer(" "+ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id

class Instruction1(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id

class Instruction2(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Instruction3(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id





##########---ASIGNACIONES GLOBALES---##########
class GlobalAssignment(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()
        son1 = self.son1.translate()
        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id





##########---ASIGNACIONES---##########
class SimpleAssignment(Node):

    def __init__(self,name,son1,son2,son3):
        self.name=name
        self.son1=son1
        self.son2=son2
        self.son3=son3

    def printer(self, ident):
        self.son1.printer(" "+ident)
        self.son2.printer(" "+ident)
        self.son3.printer(" "+ident)

    def translate(self):
        global output
        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"

        return id


class DoubleAssignment(Node):

    def __init__(self,name,son1,son2,son3,son4,son5):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"




##########---FUNCIONES---##########
class Function0(Node):

    def __init__(self,name,son1):
        self.name=name
        self.son1=son1

    def printer(self, ident):
        self.son1.printer(" "+ident)
    def translate(self):
        global output

        id = counterIncreaser()

        son1=self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id

class Function1(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function2(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function3(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function4(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function5(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function6(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function7(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function8(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function9(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Function10(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Type(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Range(Node):

    def __init__(self,name,son1,son2):
        self.name=name
        self.son1=son1
        self.son2=son2

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)


    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id


class Insert(Node):

    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id


class Del(Node):

    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id


class Len(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Neg(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class TF(Node):

    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id


class Blink(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Delay(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        if (type(self.son1) == type(tuple())):
            self.son1[0].printer(" " + ident)

        else:
            self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].translate()

        else:
            son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class ShapeArg0(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        if (type(self.son1) == type(tuple())):
            self.son1[0].printer(" " + ident)

        else:
            self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].translate()

        else:
            son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class ShapeArg1(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        if (type(self.son1) == type(tuple())):
            self.son1[0].printer(" " + ident)

        else:
            self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].translate()

        else:
            son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class ShapeArg2(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        if (type(self.son1) == type(tuple())):
            self.son1[0].printer(" " + ident)

        else:
            self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        if type(self.son1) == type(tuple()):
            son1 = self.son1[0].translate()

        else:
            son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id


class Shape(Node):

    def __init__(self, name, son1, son2):
        self.name = name
        self.son1 = son1
        self.son2 = son2

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"

        return id


class Delete(Node):

    def __init__(self,name,son1,son2,son3):
        self.name=name
        self.son1=son1
        self.son2=son2
        self.son3=son3

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"

        return id


class Call(Node):

    def __init__(self, name, son1):
        self.name = name
        self.son1 = son1

    def printer(self, ident):
        self.son1.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"

        return id





##########---CICLOS---##########
class p_cycle0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_for(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_step0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_stepEmp(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---BIFURCACIONES---##########
class p_statement(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_optStatment0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_optStatment1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---PROCEDIMIENTOS---##########
class p_procedure(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_procDec(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_procName(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_parameter0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_parameter1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_emptyParameter(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_procParam0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_body(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mainProcedure(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mainBody(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mainBlock0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_emptyMainblk(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---OPERACIONES ARITMETICAS---##########
class p_arithmetic0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_arithmetic1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_arithmetic2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---TERMINOS---##########
class p_term0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_term1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---FACTORES---##########
class p_factor0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_factor1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_factor2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---CONSTANTES DE CONFIGURACION---##########
class p_const0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_const1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_const2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_const3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---CONTENIDO DE ASIGNACIONES---##########
class p_Acont0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont4(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Acont5(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---CONTENIDO DE FUNCIONES---##########
class p_Fcont0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont4(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont5(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont6(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Fcont7(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---LISTAS Y MATRICES---##########
class p_list(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listEmp(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_listV0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_mat(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_matT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_matT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_matV0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmat(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmatT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmatT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dmatV0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_consult0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output
        ("consult0")


class p_consult1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_consult2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Lstconsult(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_LstconsultT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_LstconsultT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Matconsult(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_MatconsultT3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dMatconsult(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dMatconsultT0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_3dMatconsultT1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---INDICES---##########
class p_indice0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_indice1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Insind0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_InsindEmp(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---DIMENSIONES---##########
class p_dim0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_dim1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---MEDIDAS DE TIEMPO---##########
class p_timeM0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_timeM1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_timeM2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---OPERADORES---##########
class p_addingOp0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_addingOp1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp2(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp3(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_multiplyingOp4(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---VALORES---##########
class p_value0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_value1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Bifvalue0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_Bifvalue1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---RELACIONES---##########
class p_relation0(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation1(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation2(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation3(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation4(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation5(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output


class p_relation6(Node):

    def __init__(self):


def printer(self, ident):
    def translate(self):
        global output





##########---IDENTIFICADORES---##########
class p_identifier0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_identifier1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output





##########---ITERABLES---##########
class p_iterable0(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output


class p_iterable1(Node):

    def __init__(self):

    def printer(self, ident):

    def translate(self):
        global output

##########---TOKENS---##########
class Assign(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print
        ident + "Assign: " + self.name

    def traducir(self):
        global txt
        id = counterIncreaser()

        txt += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Int(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print
        ident + "Int: " + str(self.name)

    def traducir(self):
        global txt
        id = counterIncreaser()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class Id(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print
        ident + "ID: " + self.name

    def traducir(self):
        global txt
        id = counterIncreaser()
        txt += id + "[label= " + self.name + "]" + "\n\t"

        return id

class ShapeF(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print
        ident + "ShapeF: " + str(self.name)

    def traducir(self):
        global txt
        id = counterIncreaser()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class ShapeC(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print
        ident + "ShapeC: " + str(self.name)

    def traducir(self):
        global txt
        id = counterIncreaser()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class ShapeA(Node):
    def __init__(self, name):
        self.name = name

    def imprimir(self, ident):
        print
        ident + "ShapeA: " + str(self.name)

    def traducir(self):
        global txt
        id = counterIncreaser()
        txt += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id