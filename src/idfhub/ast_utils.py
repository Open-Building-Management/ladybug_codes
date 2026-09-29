"""utilitaires ast"""
import ast
import operator as op

OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

def get_dependencies(expr: str) -> set[str]:
    """extraction des noms utilisés dans une expression"""
    tree = ast.parse(expr, mode="eval")
    return {
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name)
    }

def eval_expr(expr, variables):
    """secure resolution engine"""
    def _eval(node):
        """evaluation method"""
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.Name):
            return variables[node.id]

        if isinstance(node, ast.BinOp):
            return OPS[type(node.op)](
                _eval(node.left),
                _eval(node.right)
            )

        if isinstance(node, ast.UnaryOp):
            return OPS[type(node.op)](_eval(node.operand))

        raise TypeError(f"Unsupported Expression : {ast.dump(node)}")

    return _eval(ast.parse(expr.strip(), mode="eval").body)
