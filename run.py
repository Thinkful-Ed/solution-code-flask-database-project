# run.py
from flask import request, jsonify
from app import create_app, db
from models import AIModel

app = create_app()

with app.app_context():
    db.create_all()


@app.route('/models', methods=['POST'])
def add_model():
    data = request.get_json()
    model_name = data.get('name', "")
    model_description = data.get('description', "")

    model = AIModel(name=model_name, description=model_description)

    db.session.add(model)
    db.session.commit()

    return jsonify({"message": "AI model added to the database!", "id": model.id})


@app.route('/')
def home():
    return "Hello, Flask with SQLAlchemy!"


if __name__ == '__main__':
    app.run(debug=True, port=5001)
