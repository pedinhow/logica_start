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

    results = None
    score = 0
    total_questions = 0

    # Verifica se a aula tem o novo formato de quiz
    if 'quiz' in lesson_data:
        total_questions = len(lesson_data['quiz'])

        if request.method == 'POST':
            results = {}
            for q in lesson_data['quiz']:
                qid = q['id']
                user_answer = request.form.get(qid)

                # Verifica se acertou
                is_correct = (user_answer == q['answer'])
                if is_correct:
                    score += 1

                # Salva o resultado para mostrar no template
                results[qid] = {
                    'is_correct': is_correct,
                    'user_answer': user_answer,
                    'correct_answer': q['answer']
                }

    return render_template('lesson.html',
                           lesson=lesson_data,
                           lesson_id=lesson_id,
                           results=results,
                           score=score,
                           total=total_questions)

if __name__ == '__main__':
    app.run(debug=True)