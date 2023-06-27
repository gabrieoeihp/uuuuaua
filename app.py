from flask import Flask, render_template, request

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota para exibir informações do aluno
@app.route('/aluno/<nome>')
def exibir_aluno(nome):
    # Aqui você pode adicionar lógica para obter as informações do aluno do banco de dados ou de outra fonte de dados
    # Exemplo básico:
    if nome == 'gabriel':
        aluno = {
            'nome': 'Gabriel',
            'posicao': 'Melhor Aluno',
            'descricao': 'Gabriel é um aluno dedicado e excelente em todas as disciplinas.'
        }
    elif nome == 'lucas':
        aluno = {
            'nome': 'Lucas',
            'posicao': 'Aluno Mediano',
            'descricao': 'Lucas é um aluno esforçado, mas ainda tem espaço para melhorias em algumas disciplinas.'
        }
    elif nome == 'paulo':
        aluno = {
            'nome': 'Paulo',
            'posicao': 'Pior Aluno',
            'descricao': 'Paulo está enfrentando alguns desafios acadêmicos, mas está buscando apoio para melhorar.'
        }
    else:
        # Se o aluno não for encontrado, você pode exibir uma mensagem de erro ou redirecionar para a página inicial, por exemplo.
        return 'Aluno não encontrado'

    return render_template('aluno.html', aluno=aluno)

if __name__ == '__main__':
    app.run()
