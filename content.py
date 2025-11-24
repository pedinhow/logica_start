lessons_db = {
    1: {
        "title": "Fundamentos da Memória",
        "description": "Aprenda a armazenar dados com Variáveis e entenda os Tipos de Dados (Texto, Número, Lógico).",
        "theory": """
            <h3>📦 O que são Variáveis?</h3>
            <p>Imagine que a memória do computador é um grande armário cheio de gavetas. Para não perder as coisas, colamos etiquetas nessas gavetas. Na programação, essas etiquetas são as <strong>Variáveis</strong>.</p>
            <p>Exemplo: <code>pontos = 100</code> (Guardamos o valor 100 na gaveta etiquetada como 'pontos').</p>

            <hr>

            <h3>🔠 Tipos de Dados</h3>
            <p>Nem tudo é número! O Python precisa saber o <em>tipo</em> do que está guardado:</p>
            <ul>
                <li><strong>int (Inteiro):</strong> Números sem vírgula (ex: <code>10</code>, <code>-5</code>).</li>
                <li><strong>float (Real):</strong> Números com ponto decimal (ex: <code>9.5</code>, <code>3.14</code>).</li>
                <li><strong>str (String):</strong> Textos. Sempre usam aspas! (ex: <code>"Maria"</code>, <code>'Olá'</code>).</li>
                <li><strong>bool (Booleano):</strong> Lógica pura (apenas <code>True</code> ou <code>False</code>).</li>
            </ul>

            <div class="alert alert-info">
                <strong>Dica:</strong> O Python diferencia letras maiúsculas de minúsculas. <code>Nota</code> é diferente de <code>nota</code>!
            </div>
        """,
        "quiz": [
            {
                "id": "m1_q1",
                "question": "Qual destes valores o Python considera uma <strong>String</strong> (texto)?",
                "options": ["10", "15.5", "\"10\"", "True"],
                "answer": "\"10\""
            },
            {
                "id": "m1_q2",
                "question": "Se eu fizer <code>vidas = 3</code>, qual é o tipo da variável 'vidas'?",
                "options": ["int (Inteiro)", "str (String)", "float (Decimal)", "bool (Booleano)"],
                "answer": "int (Inteiro)"
            },
            {
                "id": "m1_q3",
                "question": "Qual nome de variável abaixo é <strong>INVÁLIDO</strong> (dá erro)?",
                "options": ["nome_usuario", "total2", "2nomes", "meu_score"],
                "answer": "2nomes"
            }
        ]
    },

    2: {
        "title": "Interagindo e Calculando",
        "description": "Comunique-se com o usuário usando input() e domine cálculos com Operadores Especiais.",
        "theory": """
            <h3>🗣️ Conversando com o Usuário</h3>
            <p>O comando <code>input()</code> faz o programa parar e esperar o usuário digitar algo.</p>
            <p>⚠️ <strong>Atenção:</strong> O <code>input</code> SEMPRE devolve texto (string), mesmo que você digite números!</p>

            <hr>

            <h3>🔄 Convertendo Tipos (Casting)</h3>
            <p>Para fazer contas com o que o usuário digitou, precisamos converter:</p>
            <ul>
                <li><code>int("5")</code> vira o número 5.</li>
                <li><code>float("5.5")</code> vira o número 5.5.</li>
                <li><code>str(10)</code> vira o texto "10".</li>
            </ul>

            <hr>

            <h3>🧮 Matemática do Python</h3>
            <p>Além do básico (+, -, *, /), temos operadores especiais:</p>
            <ul>
                <li><code>**</code> Potência (ex: <code>2 ** 3</code> é 8).</li>
                <li><code>//</code> Divisão Inteira (corta a vírgula).</li>
                <li><code>%</code> Resto da Divisão (Módulo). Muito usado para saber se um número é par ou ímpar!</li>
            </ul>
        """,
        "quiz": [
            {
                "id": "m2_q1",
                "question": "O que acontece se eu rodar: <code>res = input('Digite:') + 5</code>?",
                "options": ["Soma o número", "Dá Erro (não pode somar texto com número)", "Junta os dois",
                            "Ignora o 5"],
                "answer": "Dá Erro (não pode somar texto com número)"
            },
            {
                "id": "m2_q2",
                "question": "Qual o resultado de <code>10 % 3</code> (resto da divisão de 10 por 3)?",
                "options": ["3.33", "1", "0", "3"],
                "answer": "1"
            },
            {
                "id": "m2_q3",
                "question": "Como transformo o texto '20' no número 20?",
                "options": ["num('20')", "int('20')", "str('20')", "float('20')"],
                "answer": "int('20')"
            }
        ]
    },

    3: {
        "title": "Tomando Decisões (Lógica)",
        "description": "Ensine o programa a decidir! Use if e else para criar caminhos lógicos com and e or.",
        "theory": """
            <h3>🤔 O 'Se' e o 'Senão'</h3>
            <p>Programas inteligentes tomam decisões. Usamos o <code>if</code> (se) para verificar uma condição.</p>
            <pre><code>if idade >= 18:
    print("Pode dirigir")
else:
    print("Vá de bicicleta")</code></pre>
            <p>O espaço no começo da linha (indentação) é obrigatório no Python! É ele que diz o que está "dentro" do if.</p>

            <hr>

            <h3>⚖️ Operadores Lógicos</h3>
            <p>Podemos fazer perguntas complexas:</p>
            <ul>
                <li><code>and</code> (E): As duas coisas precisam ser verdade.</li>
                <li><code>or</code> (OU): Pelo menos uma precisa ser verdade.</li>
                <li><code>not</code> (NÃO): Inverte o resultado (True vira False).</li>
            </ul>
        """,
        "quiz": [
            {
                "id": "m3_q1",
                "question": "Para o código <code>if x > 10:</code> funcionar, o que deve vir na linha de baixo?",
                "options": ["Um print na mesma margem", "Um código indentado (com espaço no início)", "Um else",
                            "Nada"],
                "answer": "Um código indentado (com espaço no início)"
            },
            {
                "id": "m3_q2",
                "question": "Analise: <code>True and False</code>. Qual o resultado?",
                "options": ["True", "False", "Erro", "Depende"],
                "answer": "False"
            },
            {
                "id": "m3_q3",
                "question": "Qual operador uso para verificar se dois valores são IGUAIS?",
                "options": ["=", "==", "===", "iguais"],
                "answer": "=="
            }
        ]
    },

    4: {
        "title": "Loops e Repetições",
        "description": "Automatize tarefas com while e for e aprenda a repetir blocos de código com segurança.",
        "theory": """
            <h3>🔁 O Loop While (Enquanto)</h3>
            <p>Repete um bloco de código <strong>enquanto</strong> uma condição for verdadeira. Cuidado com o "Loop Infinito" (quando a condição nunca fica falsa)!</p>

            <hr>

            <h3>🔢 O Loop For (Para cada)</h3>
            <p>Ótimo para repetir um número fixo de vezes ou percorrer listas.</p>
            <p>O comando <code>range(n)</code> gera números de 0 até n-1.</p>
            <p>Exemplo: <code>for i in range(3):</code> vai rodar para i=0, i=1 e i=2.</p>
        """,
        "quiz": [
            {
                "id": "m4_q1",
                "question": "Quantas vezes roda: <code>for i in range(5):</code>?",
                "options": ["4 vezes", "5 vezes (de 0 a 4)", "5 vezes (de 1 a 5)", "Infinitas"],
                "answer": "5 vezes (de 0 a 4)"
            },
            {
                "id": "m4_q2",
                "question": "O que é um Loop Infinito?",
                "options": ["Um loop que nunca para", "Um loop muito rápido", "Um loop com erro de sintaxe",
                            "Um loop que roda 1000 vezes"],
                "answer": "Um loop que nunca para"
            }
        ]
    },

    5: {
        "title": "Listas e Coleções",
        "description": "Guarde múltiplos valores em Listas, entenda os Índices e use funções como append() e len().",
        "theory": """
            <h3>📋 Listas (Arrays)</h3>
            <p>Listas são variáveis super-poderosas que guardam vários valores.</p>
            <p><code>frutas = ["Maçã", "Banana", "Uva"]</code></p>

            <h3>📍 Posições (Índices)</h3>
            <p>Em computação, começamos a contar do ZERO!</p>
            <ul>
                <li><code>frutas[0]</code> é "Maçã"</li>
                <li><code>frutas[1]</code> é "Banana"</li>
            </ul>

            <h3>🛠️ Ferramentas de Lista</h3>
            <ul>
                <li><code>len(lista)</code>: Conta quantos itens tem.</li>
                <li><code>lista.append(item)</code>: Adiciona no final.</li>
                <li><code>lista.pop()</code>: Remove o último.</li>
            </ul>
        """,
        "quiz": [
            {
                "id": "m5_q1",
                "question": "Dada a lista <code>n = [10, 20, 30]</code>, qual o valor de <code>n[1]</code>?",
                "options": ["10", "20", "30", "Erro"],
                "answer": "20"
            },
            {
                "id": "m5_q2",
                "question": "Qual comando adiciona um item novo na lista?",
                "options": ["add()", "plus()", "append()", "insert_end()"],
                "answer": "append()"
            },
            {
                "id": "m5_q3",
                "question": "O que <code>len(lista)</code> retorna?",
                "options": ["O tamanho da lista", "O último item", "O primeiro item", "A soma dos itens"],
                "answer": "O tamanho da lista"
            }
        ]
    },

    6: {
        "title": "Funções",
        "description": "Crie suas próprias ferramentas reutilizáveis com def, usando Parâmetros e o comando return.",
        "theory": """
            <h3>🏭 Criando suas Próprias Ferramentas</h3>
            <p>Funções são blocos de código que ganham um nome e podem ser reutilizados.</p>
            <pre><code>def saudar(nome):
    return "Olá " + nome</code></pre>

            <h3>📥 Parâmetros e 📤 Retorno</h3>
            <ul>
                <li><strong>Parâmetros:</strong> O que a função recebe (ex: <code>nome</code>).</li>
                <li><strong>Return:</strong> O resultado final que ela devolve para quem chamou.</li>
            </ul>
            <p><em>Dica:</em> <code>print</code> apenas mostra na tela, <code>return</code> devolve o valor para o programa usar depois.</p>
        """,
        "quiz": [
            {
                "id": "m6_q1",
                "question": "Qual palavra chave inicia a criação de uma função?",
                "options": ["func", "def", "function", "create"],
                "answer": "def"
            },
            {
                "id": "m6_q2",
                "question": "Qual a diferença principal entre print e return?",
                "options": ["Nenhuma", "Return encerra a função e devolve valor, Print só mostra",
                            "Print é mais rápido", "Return mostra na tela"],
                "answer": "Return encerra a função e devolve valor, Print só mostra"
            }
        ]
    },

    7: {
        "title": "Caçadores de Bugs",
        "description": "Desenvolva sua visão de Debugger! Entenda e resolva os erros mais comuns na programação.",
        "theory": """
            <h3>🐛 Tipos de Erros Comuns</h3>
            <p>Não se desespere com o texto vermelho! Ele tenta te ajudar.</p>
            <ul>
                <li><strong>SyntaxError:</strong> Você escreveu algo errado na linguagem (esqueceu <code>:</code>, parênteses, etc).</li>
                <li><strong>IndentationError:</strong> O alinhamento do código está errado.</li>
                <li><strong>NameError:</strong> Tentou usar uma variável que não existe.</li>
                <li><strong>TypeError:</strong> Tentou somar texto com número, por exemplo.</li>
            </ul>
            <hr>
            <h3>🎓 Desafio Final de Lógica</h3>
            <p>Analise o código abaixo:</p>
<pre><code>x = 10
if x > 5:
    x = x + 5
print(x)</code></pre>
        """,
        "quiz": [
            {
                "id": "m7_q1",
                "question": "Se eu esquecer de fechar um parêntese <code>(</code>, que erro teremos?",
                "options": ["SyntaxError", "LogicError", "MathError", "PrintError"],
                "answer": "SyntaxError"
            },
            {
                "id": "m7_q2",
                "question": "Qual o valor impresso no código do desafio acima (x = 10...)?",
                "options": ["10", "15", "5", "20"],
                "answer": "15"
            },
            {
                "id": "m7_q3",
                "question": "O erro <code>NameError: name 'y' is not defined</code> significa que:",
                "options": ["A variável y está vazia", "A variável y não foi criada antes de usar",
                            "Y é uma letra inválida", "O Python não gosta de y"],
                "answer": "A variável y não foi criada antes de usar"
            }
        ]
    }
}