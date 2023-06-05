from flask import render_template, redirect, url_for, session

from . import main
from .forms import CreateNewGameForm, CreateNewRound, CreateNewCategory
from .utils import UuidIdGenerator
from .. import db
from ..models import Game, Round, Category, Question, Answer

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
        start_price = form.start_price.data
        new_round = Round(round_id=new_round_id, round_name=new_round_name, related_game=session.get('new_game_id'))
        db.session.add(new_round)
        db.session.commit()
        session['new_round_name'] = new_round_name
        session['new_round_id'] = new_round_id
        session['start_price'] = start_price
        return redirect(url_for('main.create_new_category'))
    return render_template('create_new_round.html', form=form, current_game_name=session.get('new_game_name'))


@main.route('/creator_mode/create_new_round/create_new_category', methods=['GET', 'POST'])
def create_new_category():
    form = CreateNewCategory()
    if form.validate_on_submit():
        category_name = form.category_name.data
        category_id = id_generator.generate()
        related_round = session.get('new_round_id')
        category = Category(
            category_id=category_id,
            category_name=category_name,
            related_round=related_round
        )
        db.session.add(category)
        db.session.commit()

        question_1_text = form.question_1_text.data
        question_1_file = form.question_1_file.data
        question_1_url = form.question_1_url.data
        question_1_id = id_generator.generate()
        question_1_price = session.get('start_price')
        question_1_file_id = None
        if question_1_file is not None:
            question_1_file_id = id_generator.generate()
        question_1 = Question(
            question_id=question_1_id,
            question_price=question_1_price,
            question_position=1,
            related_category=category_id,
            text=question_1_text,
            attachment=question_1_file_id,
            url=question_1_url,
        )
        db.session.add(question_1)
        db.session.commit()

        answer_1_text = form.answer_1_text.data
        answer_1_file = form.answer_1_file.data
        answer_1_url = form.answer_1_url.data
        answer_1_id = id_generator.generate()
        answer_1_file_id = None
        if answer_1_file is not None:
            answer_1_file_id = id_generator.generate()

        answer_1 = Answer(
            answer_id=answer_1_id,
            related_question_id=question_1_id,
            text=answer_1_text,
            attachment=answer_1_file_id,
            url=answer_1_url,
        )
        db.session.add(answer_1)
        db.session.commit()

        question_2_text = form.question_2_text.data
        question_2_file = form.question_2_file.data
        question_2_url = form.question_2_url.data
        question_2_id = id_generator.generate()
        question_2_price = session.get('start_price') * 2
        question_2_file_id = None
        if question_2_file is not None:
            question_2_file_id = id_generator.generate()
        question_2 = Question(
            question_id=question_2_id,
            question_price=question_2_price,
            question_position=2,
            related_category=category_id,
            text=question_2_text,
            attachment=question_2_file_id,
            url=question_2_url,
        )
        db.session.add(question_2)
        db.session.commit()

        answer_2_text = form.answer_2_text.data
        answer_2_file = form.answer_2_file.data
        answer_2_url = form.answer_2_url.data
        answer_2_id = id_generator.generate()

        answer_2_file_id = None
        if answer_2_file is not None:
            answer_2_file_id = id_generator.generate()

        answer_2 = Answer(
            answer_id=answer_2_id,
            related_question_id=question_2_id,
            text=answer_2_text,
            attachment=answer_2_file_id,
            url=answer_2_url,
        )
        db.session.add(answer_2)
        db.session.commit()

        question_3_text = form.question_3_text.data
        question_3_file = form.question_3_file.data
        question_3_url = form.question_3_url.data
        question_3_id = id_generator.generate()
        question_3_price = session.get('start_price') * 3
        question_3_file_id = None
        if question_3_file is not None:
            question_3_file_id = id_generator.generate()
        question_3 = Question(
            question_id=question_3_id,
            question_price=question_3_price,
            question_position=3,
            related_category=category_id,
            text=question_3_text,
            attachment=question_3_file_id,
            url=question_3_url,
        )
        db.session.add(question_3)
        db.session.commit()

        answer_3_text = form.answer_3_text.data
        answer_3_file = form.answer_3_file.data
        answer_3_url = form.answer_3_url.data
        answer_3_id = id_generator.generate()
        answer_3_file_id = None
        if answer_3_file is not None:
            answer_3_file_id = id_generator.generate()

        answer_3 = Answer(
            answer_id=answer_3_id,
            related_question_id=question_3_id,
            text=answer_3_text,
            attachment=answer_3_file_id,
            url=answer_3_url,
        )
        db.session.add(answer_3)
        db.session.commit()

        question_4_text = form.question_4_text.data
        question_4_file = form.question_4_file.data
        question_4_url = form.question_4_url.data
        question_4_id = id_generator.generate()
        question_4_price = session.get('start_price') * 4
        question_4_file_id = None
        if question_4_file is not None:
            question_4_file_id = id_generator.generate()
        question_4 = Question(
            question_id=question_4_id,
            question_price=question_4_price,
            question_position=4,
            related_category=category_id,
            text=question_4_text,
            attachment=question_4_file_id,
            url=question_4_url,
        )
        db.session.add(question_4)
        db.session.commit()

        answer_4_text = form.answer_4_text.data
        answer_4_file = form.answer_4_file.data
        answer_4_url = form.answer_4_url.data
        answer_4_id = id_generator.generate()
        answer_4_file_id = None
        if answer_4_file is not None:
            answer_4_file_id = id_generator.generate()

        answer_4 = Answer(
            answer_id=answer_4_id,
            related_question_id=question_4_id,
            text=answer_4_text,
            attachment=answer_4_file_id,
            url=answer_4_url,
        )
        db.session.add(answer_4)
        db.session.commit()

        question_5_text = form.question_5_text.data
        question_5_file = form.question_5_file.data
        question_5_url = form.question_5_url.data
        question_5_id = id_generator.generate()
        question_5_price = session.get('start_price') * 5
        question_5_file_id = None
        if question_5_file is not None:
            question_5_file_id = id_generator.generate()
        question_5 = Question(
            question_id=question_5_id,
            question_price=question_5_price,
            question_position=5,
            related_category=category_id,
            text=question_5_text,
            attachment=question_5_file_id,
            url=question_5_url,
        )
        db.session.add(question_5)
        db.session.commit()

        answer_5_text = form.answer_5_text.data
        answer_5_file = form.answer_5_file.data
        answer_5_url = form.answer_5_url.data
        answer_5_id = id_generator.generate()
        answer_5_file_id = None
        if answer_5_file is not None:
            answer_5_file_id = id_generator.generate()

        answer_5 = Answer(
            answer_id=answer_5_id,
            related_question_id=question_5_id,
            text=answer_5_text,
            attachment=answer_5_file_id,
            url=answer_5_url,
        )
        db.session.add(answer_5)
        db.session.commit()
        return render_template(
            'category_submission.html',
            current_game_name=session.get('new_game_name'),
            current_round_name=session.get('new_round_name'),
            current_category_name=category_name,
        )

    return render_template(
        'create_category.html',
        form=form,
        current_game_name=session.get('new_game_name'),
        current_round_name=session.get('new_round_name'),
    )
