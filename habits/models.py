from flask.json import JSONEncoder

from habits import db


class Habit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<Habit {}>'.format(self.title)

    def _asdict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class HabitEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Habit):
            return {
                'id': obj.id,
                'title': obj.title,
            }
        return super(HabitEncoder, self).default(obj)
