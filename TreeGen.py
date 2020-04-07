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

	def translate(self):
		global output
		id = counterIncreaser()
		output += id+"[label= "+"Null"+"]"+"\n\t"

		return id

class ProgramNode(Node):
    def __init__(self,childs):
        self.name = "Program"
        self.childs = childs

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        for child in self.childs:
            temp = child.translate()
            output += id + "->" + temp + "\n\t"

        return "digraph G {\n\t" + output+ "}"


class NonTerminalNode(Node):
    def __init__(self,name,childs):
        self.name=name
        self.childs=childs

    def translate(self):
        global output
        id=counterIncreaser()
        output += id + "[label= " + self.name + "]" + "\n\t"
        for child in self.childs:
            temp=child.translate()
            output += id + "->" + temp + "\n\t"

        return id

class TerminalNode(Node):
    def __init__(self,name,token):
        self.name=name
        self.token=str(token)

    def translate(self):
        global output
        id = counterIncreaser()
        output += id + "[label= " + self.token + "]" + "\n\t"
        return id