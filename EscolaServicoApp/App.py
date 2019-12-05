from flask import Flask
from flask_json_schema import JsonSchema, JsonValidationError
from flask import request
from flask import jsonify
from flask_cors import CORS
import sqlite3
import logging


app = Flask(__name__)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.FileHandler("escolaapp.log")
handler.setFormatter(formatter)
logger = app.logger
logger.addHandler(handler)
logger.setLevel(logging.INFO)


schema=JsonSchema()
schema.init_app(app)

schema_escola = {
    'required': ['nome', 'fk_id_endereco', 'fk_id_campus'],
    'properties': {
    'nome': {'type': 'string'},
    'id_endereco': {'type': 'integer'},
    'id_campus': {'type': 'integer'}
    }
}

schema_campus = {
    'required': ['sigla', 'cidade'],
    'properties': {
        'sigla': {'type': 'string'},
        'cidade': {'type': 'string'}
    }
}


schema_endereco = {
    'required': ['logradouro', 'complemento',  'bairro', 'cep', 'numero'],
    'properties': {
        'logradouro': {'type': 'string'},
        'complemento': {'type': 'string'},
        'bairro': {'type': 'string'},
        'cep': {'type': 'string'},
        'numero': {'type': 'integer'}
    }
}

schema_turno = {
    'required': ['nome'],
    'properties': {
        'nome': {'type': 'string'}
    }
}


schema_aluno = {
    'required': ['nome', 'matricula', 'cpf', 'nascimento', 'fk_id_endereco', 'fk_id_curso'],
    'properties': {
        'nome': {'type': 'string'},
        'matricula': {'type': 'string'},
        'cpf': {'type': 'string'},
        'nascimento': {'type': 'string'},
        'id_endereco': {'type': 'integer'},
        'id_curso': {'type': 'integer'}
    }
}


schema_curso = {
    'required': ['nome','turno','fk_id_turno'],
    'properties': {
        'nome': {'type': 'string'},
        'id_turno': {'type': 'integer'}
    }
}

schema_turma = {
    'required': ['nome','fk_id_curso'],
    'properties': {
        'nome': {'type': 'string'},
        'id_curso': {'type': 'integer'}
    }
}

schema_professor = {
    'required': ['nome', 'fk_id_endereco'],
    'properties': {
        'nome': {'type': 'string'},
        'id_endereco': {'type': 'integer'}
    }
}

schema_disciplina = {
    'required': ['nome', 'fk_id_professor'],
    'properties': {
        'nome': {'type': 'string'},
        'id_professor': {'type': 'integer'}
    }
}

database = 'EscolaApp_versao2.db'

@app.route("/escolas", methods=["GET"])
def getEscolas():
    logger.info("Listando escolas.")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_escola;
        """)
        escolas=[]
        for linha in cursor.fetchall():
            escola = {
            "id_escola":linha[0],
            "nome":linha[1],
            "id_endereco":linha[2],
            "id_campus":linha[3]

            }
            escolas.append(escola)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(escolas)


@app.route("/escolas/<int:id>", methods=["GET"])
def getEscolaByID(id):
    logger.info("Listando escolas pelo ID.")
    try:
        conn = sqlite3.connect('IFPB.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_escola WHERE id_escola = ? ;
        """,(id,))
        linha = cursor.fetchone()
        escola = {
            "id_escola": linha[0],
            "nome": linha[1],
            "id_endereco": linha[2],
            "id_campus": linha[3]
        }
        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(escola)


@app.route("/escola", methods=["POST"])
@schema.validate(schema_escola)
def setEscola():
    logger.info("Cadastrando escolas.")
    try:
        escola = request.get_json()
        nome = escola['nome']
        fk_id_endereco = escola['fk_id_endereco']
        fk_id_campus = escola['fk_id_campus']
        conn = sqlite3.connect(database)

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_escola(nome, fk_id_endereco, fk_id_campus)
            VALUES(?,?,?); """, (nome, fk_id_endereco, fk_id_campus))
        conn.commit()
        conn.close()

        id_escola = cursor.lastrowid
        escola["id_escola"] = id_escola
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(escola)

@app.route("/escola/<int:id>", methods=['PUT'])
@schema.validate(schema_escola)
def updateEscola(id):
    logger.info('Atualizando escola')
    try:
        escola = request.get_json()
        nome = escola["nome"]
        fk_id_endereco = escola["fk_id_endereco"]
        fk_id_campus = escola["fk_id_campus"]
        conn = sqlite3.connect(databaseName)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_escola WHERE id_escola = ?;""", (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_escola
                SET nome=?, fk_id_endereco=?, fk_id_campus=?
                WHERE id_escola =? """, (nome, fk_id_endereco, fk_id_campus, id))
            conn.commit()
        else:
            print ("Escolher o recurso correto '/escola' :)")

        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(escola)


@app.route("/alunos", methods=["GET"])
def getAlunos():
    logger.info("Listando alunos.")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_aluno;
        """)
        alunos = []
        for linha in cursor.fetchall():
            aluno = {
                "id_aluno": linha[0],
                "nome": linha[1],
                "matricula": linha[2],
                "cpf": linha[3],
                "nascimento": linha[4],
                "id_endereco": linha[5],
                "id_curso": linha[6]
            }
            alunos.append(aluno)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(alunos)
@app.route("/alunos/<int:id>", methods=["GET"])
def getAlunosByID(id):
    logger.info("Listando alunos por ID.")
    try:

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_aluno WHERE id_aluno = ?;
        """,(id,))
        alunos=[]
        for linha in cursor.fetchall():
            aluno = {
                "id_aluno": linha[0],
                "nome": linha[1],
                "matricula": linha[2],
                "cpf": linha[3],
                "nascimento": linha[4],
                "id_endereco": linha[5],
                "id_curso": linha[6]
            }
            alunos.append(aluno)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(aluno)

@app.route("/aluno", methods=["POST"])
@schema.validate(schema_aluno)
def setAlunos():
    logger.info("Cadastrando alunos.")
    try:
        aluno = request.get_json()
        nome = aluno['nome']
        matricula = aluno['matricula']
        cpf = aluno['cpf']
        nascimento = aluno['nascimento']
        fk_id_endereco = aluno['fk_id_endereco']
        fk_id_curso = aluno['fk_id_curso']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_aluno(nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso)
            VALUES(?,?,?,?,?,?); """, (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso))
        conn.commit()
        conn.close()

        id = cursor.lastrowid
        aluno["id"] = id
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(aluno)

@app.route("/aluno/<int:id>", methods=['PUT'])
@schema.validate(schema_aluno)
def updateAluno(id):
    logger.info('Atualizando aluno')
    try:
        aluno = request.get_json()
        nome = aluno["nome"]
        matricula = aluno["matricula"]
        cpf = aluno["cpf"]
        nascimento = aluno["nascimento"]
        fk_id_endereco = aluno["fk_id_endereco"]
        fk_id_curso = aluno["fk_id_curso"]

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_aluno
            WHERE id_aluno = ?;""", (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_aluno
                SET nome=?, matricula=?, cpf=?,nascimento=?, fk_id_endereco=?, fk_id_curso=?
                WHERE id_aluno = ? """, (nome, matricula, cpf, nascimento, fk_id_endereco, fk_id_curso, id))
            conn.commit()
        else:
            print ("Escolher o recurso correto '/aluno' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(aluno)

@app.route("/cursos", methods=["GET"])
@schema.validate(schema_curso)
def getCurso():
    logger.info("Listando cursos.")
    try:

        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_curso;
        """)
        cursos = []

        for linha in cursor.fetchall():
            curso = {
                "id_curso" : linha[0],
                "nome" : linha[1],
                "id_turno" : linha[2]
            }
            cursos.append(curso)

        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(cursos)
@app.route("/cursos/<int:id>", methods=["GET"])
def getCursoByID(id):
    logger.info("Listando cursos pelo ID.")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_curso WHERE id_curso = ?;
        """,(id,))
        linha = cursor.fetchone()
        curso = {
            "id_curso" : linha[0],
            "nome" : linha[1],
            "id_turno" : linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(curso)

@app.route("/curso", methods=["POST"])
def setCurso():
    logger.info("Cadastrando curso")
    try:
        curso = request.get_json()
        nome = curso['nome']
        id_turno = curso['fk_id_turno']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_curso(nome, fk_id_turno)
            VALUES(?,?); """, (nome, id_turno))
        conn.commit()
        conn.close()

        id = cursor.lastrowid
        curso["id_curso"] = id

    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(curso)

@app.route("/curso/<int:id>", methods=['PUT'])
@schema.validate(schema_curso)
def updateCurso(id):
    logger.info("Atualizando curso")

    try:
        curso = request.get_json()
        nome = curso['nome']
        fk_id_turno = curso['fk_id_turno']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_curso
            WHERE id_curso = ?;""", (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_curso
                SET nome=?, fk_id_turno=?
                WHERE id_curso = ? """, (nome, fk_id_turno, id))
            conn.commit()
        else:
            print ("Escolher o recurso correto '/curso' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(curso)

@app.route("/turmas", methods=["GET"])
def getTurma():
    logger.info("Listando Turma.")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_turma;
        """)
        turmas = []
        for linha in cursor.fetchall():
            turma = {
                "id_turma" : linha[0],
                "nome" : linha[1],
                "id_curso" : linha[2]
            }
            turmas.append(turma)

        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(turmas)

@app.route("/turmas/<int:id>", methods=["GET"])
def getTurmaByID(id):
    logger.info("Listando Turmas por ID.")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_turma WHERE id_turma = ?;
        """, (id,))
        linha = cursor.fetchone()
        turma = {
            "id_turma" : linha[0],
            "nome" : linha[1],
            "id_curso" : linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(turma)
@app.route("/turma", methods=["POST"])
@schema.validate(schema_turma)
def setTurma():
    logger.info("Cadastrando Turmas")
    try:
        turma = request.get_json()
        nome = turma['nome']
        fk_id_curso = turma['fk_id_curso']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_turma(nome, fk_id_curso)
            VALUES(?,?); """, (nome, fk_id_curso))
        conn.commit()
        conn.close()
        id = cursor.lastrowid
        turma["id_turma"] = id
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(turma)

@app.route("/turma/<int:id>", methods=['PUT'])
@schema.validate(schema_turma)
def updateTurma(id):
    logger.info("Atualizando turma")
    try:
        turma = request.get_json()
        nome = turma['nome']
        fk_id_curso = turma['fk_id_curso']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_turma
            WHERE id_turma = ?;""", (id,))
        tab = cursor.fetchone()
        if (tab is not None):
            cursor.execute("""
                UPDATE tb_turma
                SET nome=?, fk_id_curso=?
                WHERE id_disciplina = ? """, (nome,fk_id_curso, id))
            conn.commit()
        else:
            print ("Escolher o recurso correto '/turma' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turma)

@app.route("/disciplinas", methods=["GET"])
def getDisciplinas():
    logger.info("Listando disciplinas.")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_disciplina;
        """)
        disciplinas = []
        for linha in cursor.fetchall():
            disciplina = {
                "id_disciplina" : linha[0],
                "nome" : linha[1],
                "id_professor" : linha[2]
            }
            disciplinas.append(disciplina)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(disciplinas)

@app.route("/disciplinas/<int:id>", methods=["GET"])
def getDisciplinaByID(id):
    logger.info("Listando disciplinas por ID")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_disciplina WHERE id_disciplina = ?;
        """, (id,))
        for linha in cursor.fetchall():
            print(linha)
        conn.close()
        linha = cursor.fetchone()
        disciplina = {
            "id_disciplina" : linha[0],
            "nome" : linha[1],
            "id_professor" : linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(disciplina)

@app.route("/disciplina", methods=["POST"])
@schema.validate(schema_disciplina)
def setDisciplina():
    logger.info("Cadastrando Disciplina")
    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        fk_id_professor = disciplina['fk_id_professor']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tb_disciplina(nome, fk_id_professor)
            VALUES(?, ?); """, (nome, fk_id_professor))
        conn.commit()
        conn.close()
        id = cursor.lastrowid
        disciplina["id_disciplina"] = id
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(disciplina)


@app.route("/disciplina/<int:id>", methods=['PUT'])
@schema.validate(schema_disciplina)
def updateDisciplina(id):
    logger.info("Atualizando disciplina")
    try:
        disciplina = request.get_json()
        nome = disciplina['nome']
        fk_id_professor = disciplina['fk_id_professor']
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_disciplina
            WHERE id_disciplina = ?;""", (id,))
        tab = cursor.fetchone()
        if (tab is not None):
            cursor.execute("""
                UPDATE tb_disciplina
                SET nome=?, fk_id_professor=?
                WHERE id_disciplina = ?
                """, (nome, fk_id_professor, id))
            conn.commit()
        else:
            print ("Escolher o recurso correto '/disciplina' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(disciplina)


@app.route("/campi", methods=['GET'])
def getCampus():
    logger.info("Listando Todos os Campus")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_campus; """)
        campus = []
        for linha in cursor.fetchall():
            campi = {
                "id_campus": linha[0],
                "sigla": linha[1],
                "cidade": linha[2]
            }
            campus.append(campi)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(campus)

@app.route("/campi/<int:id>", methods=['GET'])
def getCampusById(id):
    logger.info("Listando o Campi com ID %s" %(id))
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_campus WHERE id_campus = ?; """, (id, ))
        linha = cursor.fetchone()
        campi = {
            "id_campus": linha[0],
            "sigla": linha[1],
            "cidade": linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(campi)

@app.route("/campus", methods=['POST'])
@schema.validate(schema_campus)
def setCampus():
    logger.info("Cadastrando um Novo Campus")
    try:
        campus = request.get_json()
        sigla = campus['sigla']
        cidade = campus['cidade']
        print(sigla, cidade)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tb_campus(sigla, cidade)
        VALUES(?,?); """,
        (sigla, cidade))
        conn.commit()
        conn.close()
        id_campus = cursor.lastrowid
        campus["id_campus"] = id_campus
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(campus)

@app.route("/campus/<int:id>", methods=['PUT'])
@schema.validate(schema_campus)
def updateCampus(id):
    logger.info("Atualizando campus")
    try:
        campus = request.get_json()
        sigla = campus["sigla"]
        cidade = campus["cidade"]
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_campus
            WHERE id_campus = ?;""", (id,))
        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_campus
                SET sigla=?, cidade=?
                WHERE id_campus = ? """, (sigla, cidade, id))
            conn.commit()
        else:
            print ("Escolher o recurso correto '/campus' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(campus)

@app.route("/professores", methods=['GET'])
def getProfessores():
    logger.info("Listando Professores")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_professor; """)
        professores = list()
        for linha in cursor.fetchall():
            professor = {
                "id_professor" : linha[0],
                "nome" : linha[1],
                "id_endereco": linha[2]
            }
            professores.append(professor)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(professores)

@app.route("/professores/<int:id>", methods=['GET'])
def getProfessoresById(id):
    logger.info("Listando Professores")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute(""" SELECT *
         FROM tb_professor
         WHERE id_professor = ?; """, (id, ))
        linha = cursor.fetchone()
        professor = {
            "id_professor" : linha[0],
            "nome" : linha[1],
            "id_endereco": linha[2]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(professor)

@app.route("/professor", methods=['POST'])
@schema.validate(schema_professor)
def setProfessor():
    logger.info("Cadastrando Professor")
    try:
        professor = request.get_json()
        nome = professor['nome']
        fk_id_endereco = professor['fk_id_endereco']
        print(nome, fk_id_endereco)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tb_professor(nome, fk_id_endereco)
        VALUES(?,?); """, (nome, fk_id_endereco))
        conn.commit()
        conn.close()
        id_professor = cursor.lastrowid
        professor["id_professor"] = id_professor
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(professor)

@app.route("/professor/<int:id>", methods=['PUT'])
@schema.validate(schema_professor)
def updateProfessor(id):
    logger.info('Atualizando professor')
    try:
        professor = request.get_json()
        nome = professor["nome"]
        fk_id_endereco = professor["fk_id_endereco"]
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_professor
            WHERE id_professor = ?;""", (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_professor
                SET nome=?, fk_id_endereco=?
                WHERE id_professor= ? """, (nome, fk_id_endereco, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/professor' :)")
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(professor)

@app.route("/turnos", methods=['GET'])
def getTurnos():
    logger.info("Listando Turnos")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_turno; """)
        turnos = []
        for linha in cursor.fetchall():
            turno = {
                "id_turno" : linha[0],
                "nome" : linha[1]
            }
            turnos.append(turno)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(turnos)

@app.route("/turnos/<int:id>", methods=['GET'])
def getTurnosById(id):
    logger.info("Listando turno por ID ")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_turno WHERE id_turno = ?; """, (id, ))
        linha = cursor.fetchone()
        turno = {
            "id_turno" : linha[0],
            "nome" : linha[1]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(turno)

@app.route("/turno", methods=['POST'])
@schema.validate(schema_turno)
def setTurno():
    logger.info("Cadastrando Turno")
    try:
        turno = request.get_json()
        nome = turno['nome']
        print(nome)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tb_turno(nome)
        VALUES(?); """, (nome, ))
        conn.commit()
        conn.close()
        id_turno = cursor.lastrowid
        turno["id_turno"] = id_turno
    except(sqlite3.Error):
        logger.error("Houve um erro no Cadastro de um Turno")

    return jsonify(turno)

@app.route("/turno/<int:id>", methods=['PUT'])
@schema.validate(schema_turno)
def updateTurno(id):
    logger.info('Atualizando turno')
    try:
        turno = request.get_json()
        nome = turno["nome"]
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_turno
            WHERE id_turno = ?;""", (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_turno
                SET nome=?
                where id_turno = ? """, (nome, id))
            conn.commit()
        else:
            print ("Escolher o recurso correto '/turno' :)")
        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(turno)

@app.route("/enderecos", methods=['GET'])
def getEndereco():
    logger.info("Listando Endereços")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_endereco; """)
        enderecos = []
        for linha in cursor.fetchall():
            endereco = {
                "id_endereco": linha[0],
                "logradouro": linha[1],
                "complemento": linha[2],
                "bairro": linha[3],
                "cep": linha[4],
                "numero": linha[5]
            }
            enderecos.append(endereco)
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(enderecos)

@app.route("/enderecos/<int:id>", methods=['GET'])
def getEnderecoById(id):
    logger.info("Aconteceu um erro")
    try:
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT *
        FROM tb_endereco WHERE id_endereco = ?; """, (id, ))
        linha = cursor.fetchone()
        endereco = {
            "id_endereco": linha[0],
            "logradouro": linha[1],
            "complemento": linha[2],
            "bairro": linha[3],
            "cep": linha[4],
            "numero": linha[5]
        }
        conn.close()
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(endereco)

@app.route("/endereco", methods=['POST'])
@schema.validate(schema_endereco)
def setEndereco():
    logger.info("Cadastrando um Novo Endereço")
    try:
        endereco = request.get_json()
        logradouro = endereco['logradouro']
        complemento = endereco['complemento']
        bairro = endereco['bairro']
        cep = endereco['cep']
        numero = endereco['numero']
        print(logradouro, complemento, bairro, cep, numero)
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO tb_endereco(logradouro, complemento, bairro, cep, numero)
        VALUES(?,?,?,?,?); """, (logradouro, complemento, bairro, cep, numero))
        conn.commit()
        conn.close()
        id_endereco = cursor.lastrowid
        endereco["id_endereco"] = id_endereco
    except(sqlite3.Error):
        logger.error("Aconteceu um erro")

    return jsonify(endereco)

@app.route("/endereco/<int:id>", methods=['PUT'])
@schema.validate(schema_endereco)
def updateEndereco(id):
    logger.info('Atualizando o endereço')
    try:
        endereco = request.get_json()
        logradouro = endereco["logradouro"]
        complemento = endereco["complemento"]
        bairro = endereco["bairro"]
        cep = endereco["cep"]
        numero = endereco["numero"]
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT *
            FROM tb_endereco
            WHERE id_endereco = ?;""", (id,))

        tab = cursor.fetchone()

        if (tab is not None):
            cursor.execute("""
                UPDATE tb_endereco
                SET logradouro=?, complemento=?, bairro=?, cep=?, numero=?
                where id_endereco = ? """, (logradouro,complemento, bairro, cep, numero, id))
            conn.commit()
        else:
            print ("Escolher o recurso '/endereco' :)")

        conn.close()

    except(sqlite3.Error):
        logger.error("Aconteceu um erro.")

    return jsonify(endereco)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
