from dynamic_ast import DynamicAST  # Import the DynamicAST class

repo_path = "/Users/sarthakkapila/Desktop/interview/pytest"
old_value = input("Enter the value to be replaced: ")
new_value = input("Enter the new value: ")

ast_builder = DynamicAST(repo_path)
modified_trees = ast_builder.process_repo(old_value, new_value)

# Now you can use the modified_trees dictionary 
for file_name, trees in modified_trees.items():
    
    old_code, new_code = trees["old_code"], trees["new_code"]
    print(f"File: {file_name}")

    print(f"Old AST:\n{old_tree}\n")
    with open("old.py", "w") as f:
        f.write(old_tree)
        
    print(f"New AST:\n{new_tree}\n")
    with open("new.py", "w") as f:
        f.write(new_tree)
    
    break