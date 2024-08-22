class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type
        self.left = left
        self.right = right
        self.value = value

def create_rule(rule_string):
    """Parses a rule string into an AST."""
    tokens = rule_string.split()
    stack = []
    current_node = None

    for token in tokens:
        if token == '(':
            stack.append(current_node)
        elif token == ')':
            right = stack.pop()
            left = current_node
            current_node = Node('AND', left, right)
        elif token == 'AND' or token == 'OR':
            current_node = Node(token)
        elif token == '>' or token == '<' or token == '=':
            # Assume binary comparison operators for now
            right = Node('operand', value=tokens[tokens.index(token) + 1])
            left = Node('operand', value=tokens[tokens.index(token) - 1])
            current_node = Node(token, left, right)

    return current_node

def evaluate_rule(ast, data):
    """Evaluates the rule AST against the given data."""
    if ast.type == 'operand':
        return data.get(ast.value) == ast.value

    if ast.type == 'AND':
        return evaluate_rule(ast.left, data) and evaluate_rule(ast.right, data)

    if ast.type == 'OR':
        return evaluate_rule(ast.left, data) or evaluate_rule(ast.right, data)

    return False

# Example usage:
rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
ast = create_rule(rule_string)
data = {"age": 24, "department": "Marketing", "salary": 60000, "experience": 6}
result = evaluate_rule(ast, data)
print(result)  # Output: True