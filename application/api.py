from flask import Flask, render_template, request, url_for, flash, redirect
from core.domain.data_objects import GameDto
from adapters.uuid_id_generator import UuidIdGenerator
from adapters.fauna_database_saver import FaunaDatabaseSaver

app = Flask(__name__)


class ApiContext:
    def __init__(self, id_generator: UuidIdGenerator, db_saver: FaunaDatabaseSaver):
        self.id_generator = id_generator
        self.db_saver = db_saver

    @app.route('/create_game', methods=('GET', 'POST'))
    def create_game(self):
        if request.method == 'POST':
            new_game = GameDto(
                game_id=self.id_generator.generate(),
                game_rounds=...,
                name=request.form['game_name'],
            )
            self.db_saver.save(dto=new_game)
            return redirect(url_for(''))
        return render_template('create_game.html')
