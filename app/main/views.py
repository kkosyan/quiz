from flask import render_template

from . import main
from .forms import CreateNewGameForm


@main.route('/', methods=['GET', 'POST'])
def index():
    new_game_name = None
    form = CreateNewGameForm()
    if form.validate_on_submit():
        new_game_name = form.game_name.data
        form.game_name.data = ''

    return render_template('create_game.html', form=form)
