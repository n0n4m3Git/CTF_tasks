from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/car_list')
def car_list():
    # Допустим, у вас есть список машин
    cars = [
        {'make': 'Toyota', 'model': 'Camry', 'price': 20000},
        {'make': 'Honda', 'model': 'Accord', 'price': 22000},
        # Добавьте больше машин по мере необходимости
    ]
    return render_template('car_list.html', cars=cars)

if __name__ == '__main__':
    app.run(debug=True)
