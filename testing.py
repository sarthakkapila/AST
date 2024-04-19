


import ast
import os


class DynamicAST:
    """
    This class builds and traverses an Abstract Syntax Tree (AST) for code analysis.

    Attributes:
        file_paths (list): A list of paths to the Python files to process.
    """

    def __init__(self, file_paths):
        self.file_paths = file_paths

    def process_files(self):
        """
        Parses the AST for each file in the provided list of paths.

        Prints the unmodified and modified ASTs for each file.
        """

        for file_path in self.file_paths:
            if not os.path.isfile(file_path):
                print(f"Error: '{file_path}' is not a valid file.")
                continue

            with open(file_path, "r") as f:
                code = f.read()

            # Parse the code and generate the AST
            tree = ast.parse(code)

            # Print the AST before modification
            old_tree = ast.dump(tree, indent=4)
            print(f"\nAST for file: {file_path}\nBefore modification:\n{old_tree}")

            # New value to replace the constant (replace with your actual logic)
            new_value = "sarthak"  # Placeholder for your logic

            # Replace constants (modify this function as needed)
            def replace_constant(node, new_value):
                if isinstance(node, ast.Constant) and node.value == 'Alice':
                    node.value = new_value
                for child in ast.iter_child_nodes(node):
                    replace_constant(child, new_value)

            replace_constant(tree, new_value)

            # Print the modified AST
            new_tree = ast.dump(tree, indent=4)
            print(f"\nAfter modification:\n{new_tree}")


# Example usage
file_paths = ["helo.py"]  

ast_builder = DynamicAST(file_paths)
ast_builder.process_files()
