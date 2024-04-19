import ast
import os
from git import Repo

class DynamicAST:
   def __init__(self, repo_path):
       self.repo_path = repo_path

   def process_repo(self, old_value, new_value):
       repo = Repo(self.repo_path)
       modified_trees = {}
       for file_path in self.get_python_files(repo):
           if not os.path.isfile(file_path):
               print(f"Error: '{file_path}' is not a valid file.")
               continue
           with open(file_path, "r") as f:
               code = f.read()
               tree = ast.parse(code)
               old_tree = ast.dump(tree, indent=4)
               self.replace_constant(tree, old_value, new_value)
               new_tree = ast.dump(tree, indent=4)
               if old_tree != new_tree:
                   modified_trees[file_path] = {  # Use full path instead of filename
                       "old_code": self.ast_to_code(ast.parse(old_tree)),
                       "new_code": self.ast_to_code(ast.parse(new_tree)),
                       "old_tree": old_tree,
                       "new_tree": new_tree
                   }
       return modified_trees

   def replace_constant(self, node, old_value, new_value):
       if isinstance(node, ast.Constant) and node.value == old_value:
           node.value = new_value
       for child in ast.iter_child_nodes(node):
           self.replace_constant(child, old_value, new_value)

   def get_python_files(self, repo):
       python_files = []
       for root, _, files in os.walk(repo.working_tree_dir):
           for file in files:
               if file.endswith(".py"):
                   python_files.append(os.path.join(root, file))
       return python_files

   def ast_to_code(self, tree):
       return ast.unparse(tree)
   

# # --------------------------TESTING--------------------------
# repo_path = "pytest"
# old_value = input("Enter the value to be replaced: ")
# new_value = input("Enter the new value: ")
# ast_builder = DynamicAST(repo_path)
# modified_trees = ast_builder.process_repo(old_value, new_value)

# # Modified ASTs 
# for file_path, trees in modified_trees.items():
#    old_code, new_code = trees["old_code"], trees["new_code"]
#    print(f"File: {file_path}")
#    print(f"Old Code:\n{old_code}\n")
#    print(f"New Code:\n{new_code}\n")
   
#    final_code = ast_builder.ast_to_code(ast.parse(new_code))
#    print(f"Final COde:\n{final_code}\n")
   

#    print(f"File PAth: {file_path}")
   
#    break
