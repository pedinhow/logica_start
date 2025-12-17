from flask import Flask, render_template, request
from content import lessons_db
from utils import corrigir_quiz

app = Flask(__name__)
app.secret_key = 'chave_secreta_projeto_ensino'


@app.route('/')
def index():
    return render_template(
        'index.html',
        lessons=lessons_db,
        total_modules=len(lessons_db)
    )


@app.route('/lesson/<int:lesson_id>', methods=['GET', 'POST'])
def lesson(lesson_id):
    lesson_data = lessons_db.get(lesson_id)

    if not lesson_data:
        return "Aula não encontrada", 404

    results = None
    score = 0
    total_questions = len(lesson_data.get('quiz', []))
    percent = 0

    if request.method == 'POST' and 'quiz' in lesson_data:
        results, score = corrigir_quiz(
            lesson_data['quiz'],
            request.form
        )
        percent = round((score / total_questions) * 100)

    return render_template(
        'lesson.html',
        lesson=lesson_data,
        lesson_id=lesson_id,
        results=results,
        score=score,
        total=total_questions,
        percent=percent,
        current=lesson_id,
        total_modules=len(lessons_db)
    )


if __name__ == '__main__':
    app.run(debug=True)
