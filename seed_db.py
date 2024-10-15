import json
from app import create_app, db
from app.models import Herb

app = create_app()

def load_data():
    with open('db.json') as f:
        data = json.load(f)

    for herb_data in data['herbs']:
        herb = Herb(
            id=int(herb_data['id']),
            name=herb_data['name'],
            advantages=herb_data['advantages'],
            image=herb_data['image'],
            comments=herb_data['comments']
        )
        db.session.add(herb)

    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        load_data()
