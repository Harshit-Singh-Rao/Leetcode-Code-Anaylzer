def build_analysis_prompt(problem_statement: str, source_code: str, language: str, ast_info: dict) -> str:
    prompt = f"""
Analyze the following {language} code against the provided problem statement.

Problem Statement:
{problem_statement}

Source Code:
```
{source_code}
```

Static Analysis (AST):
{ast_info}

Provide a comprehensive review. You must return a JSON object with exactly the following keys:
- "correctness_assessment": A string summarizing if the code correctly solves the problem.
- "detected_issues": A list of strings detailing bugs or edge cases.
- "time_complexity": A string representing the Big-O time complexity.
- "space_complexity": A string representing the Big-O space complexity.
- "readability_feedback": A string commenting on variable names, comments, and structure.
- "optimization_recommendations": A list of strings suggesting performance improvements.
- "modularity_recommendations": A list of strings suggesting how to break down the code.
- "alternative_algorithms": A list of strings describing other ways to solve it.
- "overall_score": An integer from 1 to 10 rating the overall code quality.
"""
    return prompt
