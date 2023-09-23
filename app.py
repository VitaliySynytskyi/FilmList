from bson import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Підключення до бази даних MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["film_list"]
collection = db["films"]

@app.route('/')
def index():
    # Отримати всі записи з колекції
    films = list(collection.find())
    return render_template('index.html', films=films)

@app.route('/add_film', methods=['POST'])
def add_film():
    if request.method == 'POST':
        # Отримати дані з форми
        title = request.form['title']
        director = request.form['director']
        viewed = False

        # Додати новий фільм до бази даних
        collection.insert_one({"title": title, "director": director, "viewed": viewed})
    return redirect(url_for('index'))

@app.route('/delete_film/<film_id>', methods=['GET'])
def delete_film(film_id):
    # Видалити фільм за ідентифікатором
    collection.delete_one({"_id": ObjectId(film_id)})
    return redirect(url_for('index'))

@app.route('/toggle_viewed/<film_id>', methods=['GET'])
def toggle_viewed(film_id):
    # Змінити статус переглянутості фільму
    film = collection.find_one({"_id": ObjectId(film_id)})
    viewed = not film["viewed"]
    collection.update_one({"_id": ObjectId(film_id)}, {"$set": {"viewed": viewed}})
    return redirect(url_for('index'))

@app.route('/edit_film/<film_id>', methods=['GET', 'POST'])
def edit_film(film_id):
    if request.method == 'POST':
        # Отримати нові дані з форми
        title = request.form['title']
        director = request.form['director']
        viewed = "viewed" in request.form  # Перевірити, чи було відзначено як переглянутий

        # Оновити фільм у базі даних
        collection.update_one({"_id": ObjectId(film_id)}, {"$set": {"title": title, "director": director, "viewed": viewed}})
        return redirect(url_for('index'))
    else:
        # Отримати інформацію про фільм для відображення у формі редагування
        film = collection.find_one({"_id": ObjectId(film_id)})
        return render_template('edit_film.html', film=film)

if __name__ == '__main__':
    app.run(debug=True)
