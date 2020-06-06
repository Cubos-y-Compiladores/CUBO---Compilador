import CompilerDependencies.Lexer as lexer
import ply.lex as lex

import CompilerDependencies.Parser as parser
import CompilerDependencies.Semantics
class MyCompiler:
    def __init__(self,gui):
        self.lexer = lex.lex(module=lexer)
        self.parser = parser
        self.gui=gui

    def compile(self,input):
        parser.runCompile(input,self.lexer,self.gui)
        print("Test")
