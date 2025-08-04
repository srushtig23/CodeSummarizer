import ast

def extract_functions(file_content):
    functions = []
    try:
        tree = ast.parse(file_content)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                start_line = node.lineno - 1
                end_line = getattr(node, "end_lineno", start_line + 1)
                code_lines = file_content.splitlines()[start_line:end_line]
                code = "\n".join(code_lines)
                functions.append((node.name, code))
    except Exception as e:
        print(f"Error parsing file: {e}")
    return functions
