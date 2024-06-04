from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

@app.route('/')
def home():
    db.create_all()
    return render_template('home.html')

# CRUD operations for cars
@app.route('/cars')
def cars():
    
    sort_by = request.args.get('sort_by', 'brand')  # Default sort by brand
    if sort_by not in ['brand', 'model', 'year', 'price']:
        sort_by = 'brand'
    
    all_cars = Car.query.order_by(getattr(Car, sort_by)).all()
    return render_template('cars.html', cars=all_cars)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        car = Car(
            request.form['brand'],
            request.form['model'],
            request.form['year'],
            request.form['price']
        )
        db.session.add(car)
        db.session.commit()
        flash('New car added successfully.')
        return redirect(url_for('cars'))
    return render_template('new_car.html')

@app.route('/cars/edit/<int:car_id>', methods=['GET', 'POST'])
def edit_car(car_id):
    car = Car.query.get_or_404(car_id)
    if request.method == 'POST':
        car.brand = request.form['brand']
        car.model = request.form['model']
        car.year = request.form['year']
        car.price = request.form['price']
        db.session.commit()
        flash('Car updated successfully.')
        return redirect(url_for('cars'))
    return render_template('edit_car.html', car=car)

@app.route('/cars/delete/<int:car_id>', methods=['POST'])
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)
    db.session.delete(car)
    db.session.commit()
    flash('Car deleted successfully.')
    return redirect(url_for('cars'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
