from app import db, create_app
from config import Config
from app.main.models import TabType, TabClick
import sqlalchemy as sqla
from datetime import datetime

app = create_app(Config)

TAB_NAMES = ['File', 'Bones', 'Skin', 'Constraints', 'Testing', 'Controls/Gizmos']

@sqla.event.listens_for(TabType.__table__, 'after_create')
def add_tabs(*args, **kwargs):
    query = sqla.select(TabType)
    if db.session.scalars(query).first() is None:
        for tab_name in TAB_NAMES:
            db.session.add(TabType(name=tab_name))
        db.session.commit()

@app.shell_context_processor
def make_shell_context():
    return {'sqla': sqla, 'db': db, 'TabType': TabType, 'TabClick': TabClick}

@app.before_request
def initDB(*args, **kwargs):
    if app._got_first_request:
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=3000)