from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuração
    app.secret_key = os.environ.get('SECRET_KEY', 'dev_key_segura_123')
    
    # Banco de Dados: Usa SQLite localmente ou DATABASE_URL em produção
    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../instance')
    os.makedirs(db_path, exist_ok=True)
    
    # Fallback para SQLite se DATABASE_URL não estiver definida
    database_url = os.environ.get('DATABASE_URL', f'sqlite:///{os.path.join(db_path, "logica.db")}')
    # Correção para compatibilidade com URLs do Postgres modernas (Render/Railway)
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes, models
        db.create_all()

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app