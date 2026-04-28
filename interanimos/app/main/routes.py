from app import db
from app.main.models import TabType, TabClick
from app.main import main_blueprint as main
from flask import render_template, flash, redirect, url_for, request
from datetime import datetime, UTC
import sqlalchemy as sqla

TAB_NAMES = ['File', 'Bones', 'Skin', 'Constraints', 'Testing', 'Controls/Gizmos']

@main.route('/')
@main.route('/index')
def index():
    query = sqla.select(TabType)
    tabs = db.session.scalars(query).all()
    return render_template('index.html', title='Bones', tabs=tabs)

@main.route('/tab/file')
def file_tab():
    query = sqla.select(TabType).where(TabType.name == 'file')
    file_tab = db.session.scalars(query).first()
    if file_tab:
        # Replacement of Deprecated datetime.utcnow() with datetime.now(UTC).
        # UTC timezone alias from datetime module found from Google AI Overview.
        db.session.add( TabClick(tab = file_tab,
                                 occurred_at = datetime.now(UTC)) )
        db.session.commit()
    return render_template('file.html', title='File')

@main.route('/not_implemented')
def not_implemented():
    flash("The action you selected has not been implemented for this prototype. " \
          "Please select another option instead.")
    return redirect(url_for('main.index'))

@main.route('/tab/<tab_name>')
def switch_tab(tab_name):
    query = sqla.select(TabType).where(TabType.name == tab_name)
    tab_type = db.session.scalars(query).first()
    
    if tab_type:
        tab_click = TabClick(tab=tab_type, occurred_at=datetime.utcnow())
        db.session.add(tab_click)
        db.session.commit()
    
    return redirect(url_for('main.index'))