from llm import LLM
from jinja2 import Environment, BaseLoader
from dynamic_ast import DynamicAST

coder_prompt = open("prompt_refactor.jinja2").read().strip()

class Coder:
    def __init__(self, base_model):
        self.llm = LLM(base_model)

    def render(self, input_AST, file_path):
        env = Environment(loader=BaseLoader())
        template = env.from_string(coder_prompt)
        return template.render(input_AST=input_AST, file_path=file_path)

# # Passes the full batch in a dict
#     def execute(self, modified_trees):
#         responses = []

#         for file_name, trees in modified_trees.items():
#             new_code = trees["new_code"]
#             prompt = self.render(new_code, file_name)
#             response = self.llm.inference(prompt)
#             responses.append((file_name, response))

#         return responses

# # Passes a single batch of dict
#     def execute(self, modified_trees):
#         responses = []

#         # Get the first item of dict 
#         file_name, trees = next(iter(modified_trees.items()))

#         new_code = trees["new_code"]
#         prompt = self.render(new_code, file_name)

#         response = self.llm.inference(prompt)
#         responses.append((file_name, response))

#         return responses


# Passes only a single string batch
    def execute(self, modified_trees):
        responses = []

        # Get the first item from the modified_trees dictionary
        # file_name, trees = next(iter(modified_trees.items()))

        # new_code = trees["new_code"]
        # prompt = self.render(new_code, file_name)
        prompt = self.render(modified_trees, "main.py")

        response = self.llm.inference(prompt)
        responses.append(("main.py", response))

        return responses

# #  Testing without batches
# repo_path = "pytest"
# old_value = input("Enter the value to be replaced: ")
# new_value = input("Enter the new value: ")

# ast_builder = DynamicAST(repo_path)
# modified_trees = ast_builder.process_repo(old_value, new_value)

# code = Coder("Anthropic")
# llm_responses = code.execute(modified_trees)

# for file_path, response in llm_responses:
#     print(f"File: {file_path}")
#     print(f"LLM Response:\n{response}\n")

# Testing LLM 
code = Coder("Gemini")
llm_responses = code.execute(""" {{input_AST}} nodes map to Python code: ``` Module(body=[ImportFrom(module='math', names=[alias(name='cos')])])` represents: `from math import cos` ``` ``` FunctionDef(name='add', args=arguments(args=[arg(arg='x'), arg(arg='y')]), body=[Return(value=BinOp(left=Name(id='x'), op=Add(), right=Name(id='y')))])` represents: `def add(x, y):\n return x + y` ``` ``` If(test=Compare(left=Name(id='x'), ops=[Gt()], comparators=[Constant(value=0)]), body=[Print(dest=None, values=[Str(s='x is positive')], nl=True)], orelse=[])` represents: `if x > 0:\n print('x is positive')` ```""")

print(llm_responses)