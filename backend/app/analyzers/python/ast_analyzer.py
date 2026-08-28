import ast

class PythonASTAnalyzer:
    def analyze(self, code: str) -> dict:
        try:
            tree = ast.parse(code)
            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
            imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
            return {
                "valid_syntax": True,
                "functions": functions,
                "classes": classes,
                "imports": imports
            }
        except SyntaxError as e:
            return {
                "valid_syntax": False,
                "error": str(e)
            }
