from flask import render_template, redirect, url_for, session

from . import main
from .forms import CreateNewGameForm
from .utils import UuidIdGenerator
from .. import db
from ..models import Game

id_generator = UuidIdGenerator()


@main.route('/', methods=['GET', 'POST'])
def index():
    form = CreateNewGameForm()
    if form.validate_on_submit():
        new_game_name = form.game_name.data
        new_game = Game(game_id=id_generator.generate(), game_name=new_game_name)
        db.session.add(new_game)
        db.session.commit()
        session['new_game_name'] = form.game_name.data
        form.game_name.data = ''
        return redirect(url_for('main.index'))
    return render_template('create_game.html', form=form, new_game_name=session.get('new_game_name'))
