from flask import render_template, redirect, url_for, session

from . import main
from .forms import CreateNewGameForm, CreateNewRound, CreateNewCategory
from .utils import UuidIdGenerator
from .. import db
from ..models import Game, Round, Category

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


@main.route('/creator_mode', methods=['GET', 'POST'])
def create_new_game():
    form = CreateNewGameForm()
    if form.validate_on_submit():
        new_game_name = form.game_name.data
        new_game_id = id_generator.generate()
        new_game = Game(game_id=new_game_id, game_name=new_game_name)
        db.session.add(new_game)
        db.session.commit()
        session['new_game_name'] = new_game_name
        session['new_game_id'] = new_game_id
        return redirect(url_for('main.create_new_round'))
    return render_template('create_game.html', form=form)


@main.route('/creator_mode/create_new_round', methods=['GET', 'POST'])
def create_new_round():
    form = CreateNewRound()
    if form.validate_on_submit():
        new_round_name = form.round_name.data
        new_round_id = id_generator.generate()
        new_round = Round(round_id=new_round_id, round_name=new_round_name, related_game=session.get('new_game_id'))
        db.session.add(new_round)
        db.session.commit()
        session['new_round_name'] = new_round_name
        session['new_round_id'] = new_round_id
        return redirect(url_for('main.index'))
    return render_template('create_new_round.html', form=form, current_game_name=session.get('new_game_name'))


# @main.route('/creator_mode/create_new_round/create_new_category', methods=['GET', 'POST'])
# def create_new_category():
#     form = CreateNewCategory()
#     if form.validate_on_submit():
#         new_category_name = form.category_name.data
#         new_category_id = id_generator.generate()
#         related_round = session.get('new_round_id')
#         new_category = Category(
#             category_id=new_category_id,
#             category_name=new_category_name,
#             related_round=related_round
#         )
#         db.session.add(new_category)
#         db.session.commit()
#
#         session['new_round_name'] = new_round_name
#         session['new_round_id'] = new_round_id
#         return redirect(url_for('main.index'))
#     return render_template('create_new_round.html', form=form, current_game_name=session.get('new_game_name'))
