import re


class VCompiler:
       def __init__(self, *args, **kwargs):
              self.file = args[0]

       def check_if_rules_are_applied(self, code):
              if re.search('_|:|/|', code) and '\\' in code:
                     print("Invalid")
              else:
                     print("Valid")

       def detect_tokens(self, code):
              '''
              inputs a string and returns a list of tokens for the program 
              '''
              separators = ['[', ']', '{', '}', '(', ')', ';' " ", ',', '.']
              print("-----------------------------")
              self.check_if_rules_are_applied(code)
              print(code)
              print("-----------------------------")

       def lexic_analyzer(self):
              with open(self.file) as f:
                     all_code_to_one_character = " ".join(
                         [line.strip() for line in f.readlines()])
                     self.detect_tokens(all_code_to_one_character)


victor_compiler = VCompiler("code.txt")
victor_compiler.lexic_analyzer()
