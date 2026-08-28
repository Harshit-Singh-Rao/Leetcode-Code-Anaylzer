import ast

class PythonASTAnalyzer:
    def analyze(self, code: str) -> dict:
        try:
            # Clean up non-breaking spaces often found in web editors like Leetcode
            clean_code = code.replace('\xa0', ' ').replace('\u00A0', ' ')
            tree = ast.parse(clean_code)
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
