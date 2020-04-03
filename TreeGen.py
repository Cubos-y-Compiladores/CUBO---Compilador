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

	def translate(self):
		global output
		id = counterIncreaser()
		output += id+"[label= "+"Null"+"]"+"\n\t"

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
class AltBlock(Node):

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


class AltContent1(Node):

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

    def __init__(self, name, son1,son2):
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

    def __init__(self,name,son1,son2,son3,son4,son5,son6,son7):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)
        self.son7.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        son7 = self.son7.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"
        output += id + " -> " + son7 + "\n\t"

        return id



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


class TypeF(Node):

    def __init__(self, name, son1,son2,son3,son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id


class RangeF(Node):

    def __init__(self,name,son1,son2,son3,son4,son5,son6):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)



    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"

        return id


class InsertF(Node):

    def __init__(self, name, son1, son2,son3, son4,son5, son6):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)


    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"

        return id


class DelF(Node):

    def __init__(self, name, son1, son2, son3, son4, son5, son6):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"

        return id


class LenF(Node):

    def __init__(self, name, son1,son2,son3,son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id


class NegF(Node):

    def __init__(self, name, son1,son2,son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class TF(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class BlinkF(Node):

    def __init__(self, name, son1, son2, son3,son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id


class DelayF(Node):

    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

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

    def __init__(self, name, son1, son2,son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class DeleteF(Node):

    def __init__(self,name,son1,son2,son3,son4,son5,son6,son7,son8):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)
        self.son7.printer(" " + ident)
        self.son8.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        son7 = self.son7.translate()
        son8 = self.son8.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"
        output += id + " -> " + son7 + "\n\t"
        output += id + " -> " + son8 + "\n\t"

        return id


class CallF(Node):

    def __init__(self, name, son1,son2):
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





##########---CICLOS---##########
class Cycle(Node):

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


class ForC(Node):

    def __init__(self,name,son1,son2,son3,son4,son5,son6,son7,son8):
        self.name=name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8

    def printer(self, ident):

        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        if (type(self.son5) == type(tuple())):
            self.son5[0].printer(" " + ident)

        else:
            self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)
        if (type(self.son7) == type(tuple())):
            self.son7[0].printer(" " + ident)

        else:
            self.son7.printer(" " + ident)
        self.son8.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        if (type(self.son5) == type(tuple())):
            son5=self.son5[0].translate()

        else:
            son5=self.son5.translate()
        son6 = self.son6.translate()
        if (type(self.son7) == type(tuple())):
            son7=self.son7[0].translate()

        else:
            son7=self.son7.translate()
        son8 = self.son8.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"
        output += id + " -> " + son7 + "\n\t"
        output += id + " -> " + son8 + "\n\t"

        return id


class StepF(Node):

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





##########---BIFURCACIONES---##########
class Statement(Node):

    def __init__(self,name,son1,son2,son3,son4,son5,son6,son7,son8,son9,son10):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7
        self.son8 = son8
        self.son9 = son9
        self.son10 = son10


    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)
        self.son7.printer(" " + ident)
        if (type(self.son8) == type(tuple())):
            self.son8[0].printer(" " + ident)

        else:
            self.son8.printer(" " + ident)
        self.son9.printer(" " + ident)
        if (type(self.son10) == type(tuple())):
            self.son10[0].printer(" " + ident)

        else:
            self.son10.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        son7 = self.son7.translate()
        if (type(self.son8) == type(tuple())):
            son8=self.son8[0].translate()

        else:
            son8=self.son8.translate()

        son9 = self.son9.translate()
        if (type(self.son10) == type(tuple())):
            son10=self.son10[0].translate()

        else:
            son10=self.son10.translate()


        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"
        output += id + " -> " + son7 + "\n\t"
        output += id + " -> " + son8 + "\n\t"
        output += id + " -> " + son9 + "\n\t"
        output += id + " -> " + son10 + "\n\t"

        return id


class OptStatement(Node):

    def __init__(self,name,son1,son2,son3,son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        if (type(self.son3) == type(tuple())):
            self.son3[0].printer(" " + ident)

        else:
            self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        if (type(self.son3) == type(tuple())):
            son3 = self.son3[0].translate()

        else:
            son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id





##########---PROCEDIMIENTOS---##########
class ProcedureP(Node):

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
        return id


class ProcDec(Node):

    def __init__(self,name,son1,son2,son3,son4):
        self.name=name
        self.son1=son1
        self.son2=son2
        self.son3=son3
        self.son4=son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        if (type(self.son3) == type(tuple())):
            self.son3[0].printer(" " + ident)

        else:
            self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)


    def translate(self):
        global output

        id=counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        if (type(self.son3) == type(tuple())):
            son3 = self.son3[0].translate()

        else:
            son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id

class ProcName(Node):

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


class Parameter0(Node):

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


class Parameter1(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        if (type(self.son3) == type(tuple())):
            self.son3[0].printer(" " + ident)

        else:
            self.son3.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        if (type(self.son3) == type(tuple())):
            son3 = self.son3[0].translate()

        else:
            son3 = self.son3.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"

        return id

class ProcParam(Node):

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


class Body(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printer(self, ident):
        self.son1.printer(" " + ident)
        if (type(self.son2) == type(tuple())):
            self.son2[0].printer(" " + ident)

        else:
            self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)


    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        if (type(self.son2) == type(tuple())):
            son2 = self.son2[0].translate()

        else:
            son2 = self.son2.translate()
            son3 = self.son3.translate()


        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"


        return id


class MainProc(Node):

    def __init__(self, name, son1, son2, son3, son4, son5, son6, son7):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)
        if (type(self.son7) == type(tuple())):
            self.son7[0].printer(" " + ident)

        else:
            self.son7.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        if (type(self.son7) == type(tuple())):
            son7 = self.son7[0].translate()

        else:
            son7 = self.son7.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"
        output += id + " -> " + son7 + "\n\t"

        return id

class MainBody(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son3.printer(" " + ident)
        if (type(self.son2) == type(tuple())):
            self.son2[0].printer(" " + ident)

        else:
            self.son2.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son3 = self.son3.translate()
        if (type(self.son2) == type(tuple())):
            son2 = self.son2[0].translate()

        else:
            son2 = self.son2.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"

        return id


class MainBlock(Node):

    def __init__(self, name, son1, son2):
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





##########---OPERACIONES ARITMETICAS---##########
class Arithmetic0(Node):

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


class Arithmetic1(Node):

    def __init__(self, name, son1,son2):
        self.name = name
        self.son1 = son1
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


class Arithmetic2(Node):

    def __init__(self, name, son1, son2,son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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





##########---TERMINOS---##########
class Term0(Node):

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


class Term1(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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





##########---FACTORES---##########
class Factor0(Node):

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


class Factor1(Node):

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


class Factor2(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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





##########---CONSTANTES DE CONFIGURACION---##########
class Const0(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class Const1(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class Const2(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class Const3(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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





##########---CONTENIDO DE ASIGNACIONES---##########
class Acont0(Node):

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


class Acont1(Node):

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


class Acont2(Node):

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


class Acont3(Node):

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


class Acont4(Node):

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


class Acont5(Node):

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





##########---CONTENIDO DE FUNCIONES---##########
class Fcont0(Node):

    def __init__(self, name, son1, son2, son3, son4, son5, son6, son7):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)
        self.son7.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        son7 = self.son7.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"
        output += id + " -> " + son7 + "\n\t"

        return id


class Fcont1(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class Fcont3(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class Fcont4(Node):

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


class Fcont5(Node):

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


class Fcont6(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class Fcont7(Node):

    def __init__(self, name, son1, son2, son3,son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        if (type(self.son4) == type(tuple())):
            self.son4[0].printer(" " + ident)

        else:
            self.son4.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        if (type(self.son4) == type(tuple())):
            son4 = self.son4[0].translate()

        else:
            son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id





##########---LISTAS Y MATRICES---##########
class List(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class EmptyList(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class ListT0(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class ListT1(Node):

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


class ListV(Node):

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


class Mat(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class MatT0(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class MatT1(Node):

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


class MatV(Node):

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


class ThreeDMat(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class ThreeDMatT0(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class ThreeDMatT1(Node):

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


class ThreeDMatV(Node):

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


class Consult0(Node):

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


class Consult1(Node):

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

class Consult2(Node):

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

class ListConsult(Node):

    def __init__(self, name, son1,son2):
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


class ListConsultT0(Node):

    def __init__(self, name, son1, son2, son3):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3

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


class ListConsultT1(Node):

    def __init__(self, name, son1, son2, son3, son4, son5):
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

        return id

class MatConsult(Node):

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


class MatConsultT0(Node):

    def __init__(self, name, son1, son2, son3, son4, son5):
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

        return id


class MatConsultT1(Node):

    def __init__(self, name, son1, son2, son3, son4, son5):
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

        return id


class MatConsultT2(Node):

    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id


class MatConsultT3(Node):

    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output
        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id


class ThreeDMatConsult(Node):

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

class ThreeDMatConsultT0(Node):

    def __init__(self, name, son1, son2, son3, son4, son5, son6, son7):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4
        self.son5 = son5
        self.son6 = son6
        self.son7 = son7

    def printer(self, ident):
        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)
        self.son5.printer(" " + ident)
        self.son6.printer(" " + ident)
        self.son7.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()
        son5 = self.son5.translate()
        son6 = self.son6.translate()
        son7 = self.son7.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"
        output += id + " -> " + son5 + "\n\t"
        output += id + " -> " + son6 + "\n\t"
        output += id + " -> " + son7 + "\n\t"

        return id


class ThreeDMatConsultT1(Node):

    def __init__(self, name, son1, son2, son3, son4):
        self.name = name
        self.son1 = son1
        self.son2 = son2
        self.son3 = son3
        self.son4 = son4

    def printer(self, ident):

        self.son1.printer(" " + ident)
        self.son2.printer(" " + ident)
        self.son3.printer(" " + ident)
        self.son4.printer(" " + ident)

    def translate(self):
        global output

        id = counterIncreaser()

        son1 = self.son1.translate()
        son2 = self.son2.translate()
        son3 = self.son3.translate()
        son4 = self.son4.translate()

        output += id + "[label= " + self.name + "]" + "\n\t"
        output += id + " -> " + son1 + "\n\t"
        output += id + " -> " + son2 + "\n\t"
        output += id + " -> " + son3 + "\n\t"
        output += id + " -> " + son4 + "\n\t"

        return id





##########---INDICES---##########
class Indice0(Node):

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

class Indice1(Node):

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


class Insind0(Node):

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





##########---DIMENSIONES---##########
class Dim0(Node):

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

class Dim1(Node):

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





##########---MEDIDAS DE TIEMPO---##########
class TimeM0(Node):

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


class TimeM1(Node):

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


class TimeM2(Node):

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





##########---OPERADORES---##########
class AddingOp0(Node):

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

class AddingOp1(Node):

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

class MultiplyingOp0(Node):

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

class MultiplyingOp1(Node):

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

class MultiplyingOp2(Node):

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

class MultiplyingOp3(Node):

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

class MultiplyingOp4(Node):

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




##########---VALORES---##########
class Value0(Node):

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

class Value1(Node):

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

class BifValue0(Node):

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

class BifValue1(Node):

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




##########---RELACIONES---##########
class Relation0(Node):

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

class Relation1(Node):

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

class Relation2(Node):

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

class Relation3(Node):

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

class Relation4(Node):

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

class Relation5(Node):

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

class Relation6(Node):

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




##########---IDENTIFICADORES---##########
class Identifier0(Node):

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

class Identifier1(Node):

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




##########---ITERABLES---##########
class Iterable0(Node):

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

class Iterable1(Node):

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





##########---TOKENS---##########
class Assign(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "ASSIGN: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()

        output += id + "[label= \"" + self.name + "\"]" + "\n\t"

        return id


class Int(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "INT: " + str(self.name))

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class Id(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "ID: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"

        return id

class ShapeF(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "SHAPEF: " + str(self.name))

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class ShapeC(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "SHAPEC: " + str(self.name))

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class ShapeA(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "SHAPEA: " + str(self.name))

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + str(self.name) + "]" + "\n\t"

        return id

class If(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "IF: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "IF" + "]" + "\n\t"

        return id

class Lparent(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "LPARENT: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "LPARENT" + "]" + "\n\t"

        return id
class Rparent(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "RPARENT: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "RPARENT" + "]" + "\n\t"

        return id

class Lcorch(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "LCORCH: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "LCORCH" + "]" + "\n\t"
        return id

class Rcorch(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "RCORCH: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "RCORCH" + "]" + "\n\t"
        return id

class Procedure(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "PROCEDURE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "PROCEDURE" + "]" + "\n\t"
        return id

class Comma(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "COMMA: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "COMMA" + "]" + "\n\t"
        return id

class Main(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "MAIN: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Timer(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "TIMER: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class RangoTimer(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "RANGOTIMER: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Cubo(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "CUBO: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Parentcl(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "PARENTCL: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "PARENTCL" + "]" + "\n\t"
        return id

class Parentcr(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "PARENTCR: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "PARENTCR" + "]" + "\n\t"
        return id

class Tp(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "TP: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "TP" + "]" + "\n\t"
        return id

class Dimfilas(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DIMFILAS: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Dimcolumnas(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DIMCOLUMNAS: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Quotes(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "QUOTES: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "QUOTES" + "]" + "\n\t"
        return id

class Mil(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "MIL: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Min(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "MIN: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Seg(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "SEG: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Plus(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "PLUS: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "PLUS" + "]" + "\n\t"
        return id

class Minus(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "MINUS: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "MINUS" + "]" + "\n\t"
        return id

class Times(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "TIMES: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "TIMES" + "]" + "\n\t"
        return id

class Exp(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "EXP: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "EXP" + "]" + "\n\t"
        return id

class Divide(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DIVIDE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "DIVIDE" + "]" + "\n\t"
        return id

class Divent(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DIVENT: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "DIVENT" + "]" + "\n\t"
        return id

class Mod(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "MOD: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "MOD" + "]" + "\n\t"
        return id

class FalseV(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "FALSE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class TrueV(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "TRUE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Global(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "GLOBAL: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "GLOBAL" + "]" + "\n\t"
        return id

class Type(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "TYPE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "TYPE" + "]" + "\n\t"
        return id

class Range(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "RANGE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "RANGE" + "]" + "\n\t"
        return id

class Dot(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DOT: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "DOT" + "]" + "\n\t"
        return id

class Insert(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "INSERT: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "INSERT" + "]" + "\n\t"
        return id

class Del(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DEL: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Len(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "LEN: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Blink(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "BLINK: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Delete(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DELETE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "DELETE" + "]" + "\n\t"
        return id

class Call(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "CALL: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class For(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "FOR: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "FOR" + "]" + "\n\t"
        return id

class In(Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "IN: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "IN" + "]" + "\n\t"
        return id

class Step (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "STEP: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "STEP" + "]" + "\n\t"
        return id

class Delay (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "DELAY: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Neg (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "NEG: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Else (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "ELSE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "ELSE" + "]" + "\n\t"
        return id

class Begin (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "BEGIN: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class End (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "END: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class T (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "T: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class F (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "F: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        return id

class Ne (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "NE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "NE" + "]" + "\n\t"
        return id

class Lt (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "LT: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "LT" + "]" + "\n\t"
        return id

class Gt (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "GT: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "GT" + "]" + "\n\t"
        return id

class Gte (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "GTE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "GTE" + "]" + "\n\t"
        return id

class Compare (Node):
    def __init__(self, name):
        self.name = name

    def printer(self, ident):
        print(ident + "COMPARE: " + self.name)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + "COMPARE" + "]" + "\n\t"
        return id