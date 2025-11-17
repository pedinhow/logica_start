from flask import Flask, render_template, request, redirect, url_for, flash
from content import lessons_db

app = Flask(__name__)
app.secret_key = 'chave_secreta_projeto_ensino'  # Necessário para mensagens de feedback


@app.route('/')
def index():
    return render_template('index.html', lessons=lessons_db)


@app.route('/lesson/<int:lesson_id>', methods=['GET', 'POST'])
def lesson(lesson_id):
    lesson_data = lessons_db.get(lesson_id)

    if not lesson_data:
        return "Aula não encontrada", 404

    feedback = None

    if request.method == 'POST':
        user_answer = request.form.get('option')
        if user_answer == lesson_data['answer']:
            feedback = "success"  # Resposta correta
        else:
            feedback = "error"  # Resposta errada

    return render_template('lesson.html', lesson=lesson_data, lesson_id=lesson_id, feedback=feedback)


if __name__ == '__main__':
    app.run(debug=True)