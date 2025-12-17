from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from .models import db, User, Progress
from .content import lessons_db
from datetime import datetime

main_bp = Blueprint('main', __name__)

def get_current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    return None

@main_bp.route('/', methods=['GET', 'POST'])
def login():
    if get_current_user():
        return redirect(url_for('main.dashboard'))

    if request.method == 'POST':
        name = request.form.get('name').strip()
        if not name:
            flash('Por favor, insira seu nome.', 'danger')
            return redirect(url_for('main.login'))
        
        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()
        
        session['user_id'] = user.id
        session['user_name'] = user.name
        return redirect(url_for('main.dashboard'))

    return render_template('login.html')

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.login'))

@main_bp.route('/dashboard')
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for('main.login'))
    
    user_progress = {p.lesson_id: p for p in user.progress}
    total_lessons = len(lessons_db)
    completed_count = len(user_progress)
    global_progress = int((completed_count / total_lessons) * 100)
    
    return render_template('dashboard.html', 
                           user=user, 
                           lessons=lessons_db, 
                           progress=user_progress,
                           global_progress=global_progress)

# --- NOVA ROTA: Apenas Conteúdo Teórico ---
@main_bp.route('/aula/<int:lesson_id>/conteudo')
def lesson_content(lesson_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('main.login'))
        
    lesson_data = lessons_db.get(lesson_id)
    if not lesson_data:
        return "Aula não encontrada", 404

    return render_template('lesson_content.html', 
                           lesson=lesson_data, 
                           lesson_id=lesson_id)

# --- NOVA ROTA: Apenas Quiz ---
@main_bp.route('/aula/<int:lesson_id>/quiz', methods=['GET', 'POST'])
def lesson_quiz(lesson_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('main.login'))
        
    lesson_data = lessons_db.get(lesson_id)
    if not lesson_data:
        return "Aula não encontrada", 404

    results = {}
    score = 0
    total_questions = len(lesson_data.get('quiz', []))
    percent = 0
    # Armazena respostas enviadas para repopular o formulário (Sticky Form)
    previous_answers = {} 

    previous_best = Progress.query.filter_by(user_id=user.id, lesson_id=lesson_id).first()

    if request.method == 'POST':
        previous_answers = request.form # Captura o que o usuário marcou

        for q in lesson_data['quiz']:
            qid = q['id']
            resposta_usuario = request.form.get(qid)
            is_correct = (resposta_usuario == q['answer'])
            if is_correct:
                score += 1
            
            results[qid] = {
                'is_correct': is_correct,
                'user_answer': resposta_usuario,
                'correct_answer': q['answer']
            }
        
        percent = int((score / total_questions) * 100)
        
        # Só salva se acertar tudo ou melhorar a nota (opcional, aqui mantive lógica anterior)
        if not previous_best or score >= previous_best.score:
            if not previous_best:
                new_progress = Progress(user_id=user.id, lesson_id=lesson_id, score=score, total_questions=total_questions)
                db.session.add(new_progress)
            else:
                previous_best.score = score
                previous_best.total_questions = total_questions
                previous_best.completed_at = datetime.utcnow()
            db.session.commit()

    return render_template('lesson_quiz.html', 
                           lesson=lesson_data, 
                           lesson_id=lesson_id, 
                           results=results, 
                           score=score, 
                           total=total_questions, 
                           percent=percent,
                           previous_answers=previous_answers, # Passa as respostas de volta
                           previous_best=previous_best)

@main_bp.route('/certificado')
def certificate():
    user = get_current_user()
    if not user:
        return redirect(url_for('main.login'))
        
    completed = Progress.query.filter_by(user_id=user.id).count()
    total = len(lessons_db)
    
    if completed < total:
        flash(f'Complete todos os módulos. Faltam {total - completed}.', 'warning')
        return redirect(url_for('main.dashboard'))
        
    return render_template('certificate.html', 
                           user=user, 
                           date=datetime.now().strftime("%d/%m/%Y"),
                           total_hours=total * 2)