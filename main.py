from flask import Flask, render_template # import do flask e do render_template para renderizar a página HTMl.
from database import db # importe do database.py e sua variável db.
from flask_migrate import Migrate # import da extensão Migrate, para migração.
import pymysql # import do python para o MySQL.
from empresa import Empresa # import do arquivo empresa.py e sua classe Empresa para integrar no Banco de Dados também.
from diario import Diario # import do arquivo diario.py e sua classe Diario para integrar no Banco de Dados também.


app = Flask(__name__)

app.config['SECRET_KEY'] = 'CHAVE_SECRETA'
# O código acima garante os recursos de segurança Flask a nossa aplicação com o Banco de Dados, desse modo protegendo-a de uma melhor forma.

# ---------- STIG DE CONEXÃO ----------
conexao = 'mysql+pymysql://psi2023_gabriel:/S.jKe8(oMGdMx9i@albalopes.tech/psi2023_gabriel'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# ---------- STIG DE CONEXÃO ----------

# ---------- MIGRAÇÃO DOS DADOS ----------
db.init_app(app)
migrate = Migrate(app, db)
# ---------- MIGRAÇÃO DOS DADOS ----------
# Ao migrar os dados eu indico uma mudaça, um novo estado ao meu banco de dados, com novos dados, colunas etc... Essa parte é para que o ORM
# possa enxergar as mudanças de nosso banco e refletir isso ao DB.

# ---------- FINALIZAÇÃO PARA MIGRAR OS DADOS NO DB ----------
# flask db init
# flask db migrate -m "Migração inicial"
# flask db upgrade
# ---------- FINALIZAÇÃO PARA MIGRAR OS DADOS NO DB ----------
# Os códigos acima são executados ao final para assim migrar as tabelas, colunas etc... Em seu banco de dados em que foi estabelecido a conexão

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

# pip install Flask-SQLAlchemy | O próprio ORM para o uso do Banco de Dados
# pip install Flask-Migrate | Gerencia a estrutura do Banco de Dados, ou seja, as tabelas, colunas, tipos de chaves etc é gerenciado por essa extensão.
# pip install Flask-Script | Permite o uso de scripts para a execução de comandos do Banco de Dados.
# pip install python-dotenv | Responsável pela instalação de arquivos .env, na qual exercem o armazenamento das configurações das aplicações