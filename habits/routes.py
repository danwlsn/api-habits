from http import HTTPStatus

from flask import request, jsonify
from sqlalchemy.orm.exc import NoResultFound

from habits import app, db
from habits.models import Habit


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/habit/', methods=['GET'])
def list_habits():
    habits = Habit.query.all()

    return jsonify(habits)


@app.route('/habit/<id>', methods=['GET'])
def detail_habit(id):
    try:
        habit = Habit.query.filter_by(id=id).one()
        result = jsonify(habit)
    except NoResultFound:
        result = HTTPStatus.NOT_FOUND.phrase, HTTPStatus.NOT_FOUND.value

    return result


@app.route('/habit/', methods=['POST'])
def create_habit():
    if request.json:
        habit = Habit(title=request.json['title'])
        db.session.add(habit)
        # TODO try except
        db.session.commit()

        return HTTPStatus.OK.phrase, HTTPStatus.OK.value
    else:
        return HTTPStatus.INTERNAL_SERVER_ERROR.phrase, HTTPStatus.INTERNAL_SERVER_ERROR.value
