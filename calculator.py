import re

class Calculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}

    def check_valid_string(self, input_string):
        pattern = r'^[0-9\+\-\*\/\(\)\.\s]+$'

        return re.match(pattern, input_string)

    def is_higher_precedence(self, op1, op2):
        return self.operators[op1] >= self.operators[op2]

    def apply_operation(self, a, b, operator):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Ошибка: деление на ноль недопустимо")
            return a / b

    def evaluate_expression(self, expression):
        if not self.check_valid_string(expression):
            raise TypeError("В выражении не должно содержаться букв и лишних символов")
        num_stack = []
        operators_stack = []
        i = 0

        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                num = ''
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                num_stack.append(float(num))
                i -= 1
            elif expression[i] in self.operators:
                while operators_stack and operators_stack[-1] != '(' and self.is_higher_precedence(operators_stack[-1], expression[i]):
                    operator = operators_stack.pop()
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(self.apply_operation(a, b, operator))
                operators_stack.append(expression[i])
            elif expression[i] == '(':
                operators_stack.append(expression[i])
            elif expression[i] == ')':
                while operators_stack and operators_stack[-1] != '(':
                    operator = operators_stack.pop()
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num_stack.append(self.apply_operation(a, b, operator))
                operators_stack.pop()
            i += 1

        while operators_stack:
            operator = operators_stack.pop()
            b = num_stack.pop()
            a = num_stack.pop()
            num_stack.append(self.apply_operation(a, b, operator))

        return num_stack[0]

if __name__ == "__main__":
    calc = Calculator()
    expression = "(3+4*2)/(13.45-5)"
    try:
        result = calc.evaluate_expression(expression)
        print(f"Результат выражения {expression}: {result}")
    except Exception as e:
        print(str(e))
