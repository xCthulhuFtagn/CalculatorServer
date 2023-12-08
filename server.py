from flask import Flask, request, abort
import calculator

app = Flask(__name__)

calc = calculator.Calculator()

@app.route('/', methods=['POST'])
def post_example():
    try:
        data = request.get_json()
    except:
        abort(400, "Отсутствует параметр expression")
    expression = data.get('expression')
    if expression:
        try:
            result = calc.evaluate_expression(expression)
            # print(result)
        except Exception as e:
            # print(type(e))
            abort(400, e)
        else: return {"result": result}
    else:
        abort(400, "Необходим ввод выражения в параметр expression")

if __name__ == '__main__':
    app.run()
