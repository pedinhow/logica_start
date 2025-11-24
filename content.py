lessons_db = {
    1: {
        "title": "Fundamentos da Memória",
        "description": "Aprenda a armazenar dados com Variáveis e entenda os Tipos de Dados (Texto, Número, Lógico).",
        "theory": """
            <h3>📦 O que são Variáveis?</h3>
            <p>Imagine que a memória do computador é um grande armário cheio de gavetas. Para não perder as coisas, colamos etiquetas nessas gavetas. Essas etiquetas são as <strong>Variáveis</strong>.</p>

            <p>Cada variável guarda um valor específico, e você pode trocar o conteúdo dela a qualquer momento.</p>
            <pre><code>pontos = 100
pontos = pontos + 50</code></pre>

            <p>Agora pontos vale 150.</p>

            <hr>

            <h3>📛 Regras para criar nomes de variáveis</h3>
            <ul>
                <li>Não podem começar com número (<code>2nome</code> ❌)</li>
                <li>Não podem ter espaços (<code>nome aluno</code> ❌)</li>
                <li>Podem usar <code>_</code> (underline) (<code>nome_aluno</code> ✔️)</li>
                <li>São sensíveis a maiúsculas e minúsculas (<code>Nota</code> ≠ <code>nota</code>)</li>
            </ul>

            <hr>

            <h3>🔠 Tipos de Dados</h3>
            <p>Python precisa saber o tipo do valor guardado. Os principais são:</p>
            <ul>
                <li><strong>int</strong>: números inteiros (ex: <code>5</code>, <code>-3</code>)</li>
                <li><strong>float</strong>: números com ponto decimal (ex: <code>4.5</code>)</li>
                <li><strong>str</strong>: textos (ex: <code>"Olá"</code>)</li>
                <li><strong>bool</strong>: lógico (True/False)</li>
            </ul>

            <div class="alert alert-info">
                💡 <strong>Dica:</strong> você pode descobrir o tipo de algo com <code>type(valor)</code>.
            </div>
        """,
        "quiz": [
            {
                "id": "m1_q1",
                "question": "Qual destes valores o Python considera uma <strong>String</strong>?",
                "options": ["10", "15.5", "\"10\"", "True"],
                "answer": "\"10\""
            },
            {
                "id": "m1_q2",
                "question": "O que acontece em: <code>x = 10; x = x + 2</code>?",
                "options": ["Erro", "x vira 12", "x vira 102", "x vira 8"],
                "answer": "x vira 12"
            },
            {
                "id": "m1_q3",
                "question": "Qual nome de variável é inválido?",
                "options": ["nome_usuario", "total2", "2nomes", "idadeAtual"],
                "answer": "2nomes"
            },
            {
                "id": "m1_q4",
                "question": "Qual o tipo de <code>True</code>?",
                "options": ["str", "int", "bool", "float"],
                "answer": "bool"
            },
            {
                "id": "m1_q5",
                "question": "Qual comando mostra o tipo de uma variável?",
                "options": ["tipo()", "check()", "type()", "kind()"],
                "answer": "type()"
            }
        ]
    },

    2: {
        "title": "Interagindo e Calculando",
        "description": "Use input(), converta tipos e domine operadores matemáticos.",
        "theory": """
            <h3>🗣️ Entrada de Dados</h3>
            <p><code>input()</code> permite que o usuário digite algo.</p>

            <p><strong>Importante:</strong> tudo que vem do input é texto!</p>
            <pre><code>nome = input("Digite seu nome: ")</code></pre>

            <hr>

            <h3>🔄 Convertendo Tipos</h3>
            <p>Para fazer contas com números digitados:</p>
            <ul>
                <li><code>int("10")</code> → 10</li>
                <li><code>float("3.14")</code> → 3.14</li>
                <li><code>str(20)</code> → "20"</li>
            </ul>

            <hr>

            <h3>🧮 Matemática no Python</h3>
            <p>Operadores úteis:</p>
            <ul>
                <li><code>**</code>: potência</li>
                <li><code>//</code>: divisão inteira</li>
                <li><code>%</code>: resto (muito usado para verificar par/ímpar)</li>
            </ul>

            <div class="alert alert-warning">
                ⚠️ <strong>Cuidado:</strong> "5" + 5 → erro! (texto ≠ número)
            </div>
        """,
        "quiz": [
            {
                "id": "m2_q1",
                "question": "O que acontece em: <code>res = input() + 5</code>?",
                "options": ["Soma normal", "Erro", "Concatena", "Transforma em string"],
                "answer": "Erro"
            },
            {
                "id": "m2_q2",
                "question": "Qual o resultado de <code>10 % 3</code>?",
                "options": ["1", "3", "0", "3.33"],
                "answer": "1"
            },
            {
                "id": "m2_q3",
                "question": "Como converter '20' para número?",
                "options": ["int('20')", "str('20')", "num('20')", "float(20)"],
                "answer": "int('20')"
            },
            {
                "id": "m2_q4",
                "question": "Quanto vale <code>2 ** 3</code>?",
                "options": ["5", "6", "8", "9"],
                "answer": "8"
            },
            {
                "id": "m2_q5",
                "question": "Quanto vale <code>9 // 2</code>?",
                "options": ["4.5", "4", "5", "Erro"],
                "answer": "4"
            }
        ]
    },

    3: {
        "title": "Tomando Decisões",
        "description": "If, else, operadores lógicos e raciocínio condicional.",
        "theory": """
            <h3>🤔 Como programas decidem?</h3>
            <p>Usamos o comando <code>if</code> para verificar condições.</p>

            <pre><code>if idade >= 18:
    print("Adulto")
else:
    print("Menor")</code></pre>

            <p>A indentação (espaços no início) é obrigatória.</p>

            <hr>

            <h3>⚖️ Operadores Lógicos</h3>
            <ul>
                <li><code>and</code> — duas condições precisam ser verdadeiras</li>
                <li><code>or</code> — pelo menos uma é verdadeira</li>
                <li><code>not</code> — inverte o valor</li>
            </ul>
        """,
        "quiz": [
            {
                "id": "m3_q1",
                "question": "O que deve vir após <code>if x > 10:</code>?",
                "options": ["Um print na mesma linha", "Nada", "Um bloco indentado", "Outro if"],
                "answer": "Um bloco indentado"
            },
            {
                "id": "m3_q2",
                "question": "Quanto vale <code>True and False</code>?",
                "options": ["True", "False"],
                "answer": "False"
            },
            {
                "id": "m3_q3",
                "question": "Qual operador verifica igualdade?",
                "options": ["=", "==", "===", "igual"],
                "answer": "=="
            },
            {
                "id": "m3_q4",
                "question": "O que imprime?\n<pre><code>x = 5\nif x == 5:\n    print('ok')</code></pre>",
                "options": ["Nada", "Erro", "ok", "5"],
                "answer": "ok"
            },
            {
                "id": "m3_q5",
                "question": "O que faz <code>not False</code>?",
                "options": ["True", "False"],
                "answer": "True"
            }
        ]
    },

    4: {
        "title": "Loops e Repetições",
        "description": "While, For, range, contadores e prevenção de loops infinitos.",
        "theory": """
            <h3>🔁 While</h3>
            <p>Repete enquanto uma condição for verdadeira.</p>
            <pre><code>i = 1
while i <= 3:
    print(i)
    i += 1</code></pre>

            <hr>

            <h3>🔢 For e range</h3>
            <p><code>for</code> é ótimo para repetir um número fixo de vezes.</p>
            <pre><code>for i in range(3):
    print("Oi")</code></pre>

            <hr>

            <div class="alert alert-danger">
                ⚠️ Se a condição do while nunca ficar falsa → loop infinito!
            </div>
        """,
        "quiz": [
            {
                "id": "m4_q1",
                "question": "Quantas vezes roda <code>for i in range(5):</code>?",
                "options": ["4", "5", "6", "Infinitas"],
                "answer": "5"
            },
            {
                "id": "m4_q2",
                "question": "O que é um loop infinito?",
                "options": ["Loop rápido", "Loop sem fim", "Erro", "Loop que roda 10 vezes"],
                "answer": "Loop sem fim"
            },
            {
                "id": "m4_q3",
                "question": "Quanto imprime o código?\n<pre><code>for i in range(3): print(i)</code></pre>",
                "options": ["1 2 3", "0 1 2", "0 1 2 3", "Erro"],
                "answer": "0 1 2"
            },
            {
                "id": "m4_q4",
                "question": "Qual comando aumenta 1 no valor de x?",
                "options": ["x++", "x = x + 1", "add(x,1)", "inc(x)"],
                "answer": "x = x + 1"
            }
        ]
    },

    5: {
        "title": "Listas e Coleções",
        "description": "Guardar vários valores, acessar posições e usar funções úteis.",
        "theory": """
            <h3>📋 O que são listas?</h3>
            <p>Listas guardam vários valores na mesma variável.</p>

            <pre><code>numeros = [10, 20, 30]</code></pre>

            <hr>

            <h3>📍 Índices</h3>
            <p>A contagem começa em 0.</p>

            <hr>

            <h3>🛠 Funções úteis</h3>
            <ul>
                <li><code>len()</code> — tamanho</li>
                <li><code>append()</code> — adicionar</li>
                <li><code>pop()</code> — remover</li>
            </ul>
        """,
        "quiz": [
            {
                "id": "m5_q1",
                "question": "Qual o valor de n[1] em <code>n=[10,20,30]</code>?",
                "options": ["10", "20", "30"],
                "answer": "20"
            },
            {
                "id": "m5_q2",
                "question": "Qual função adiciona ao final?",
                "options": ["add()", "append()", "push()", "insert_end()"],
                "answer": "append()"
            },
            {
                "id": "m5_q3",
                "question": "O que <code>len(lista)</code> retorna?",
                "options": ["primeiro item", "último item", "tamanho", "soma"],
                "answer": "tamanho"
            },
            {
                "id": "m5_q4",
                "question": "O que imprime?\n<pre><code>frutas=['uva','maçã']\nfrutas.append('pera')\nprint(frutas)</code></pre>",
                "options": ["['uva']","['uva','maçã']","['uva','maçã','pera']","Erro"],
                "answer": "['uva','maçã','pera']"
            }
        ]
    },

    6: {
        "title": "Funções",
        "description": "Criando ferramentas com parâmetros e retorno.",
        "theory": """
            <h3>🏭 Por que usar funções?</h3>
            <p>Funções evitam repetição de código e deixam tudo mais organizado.</p>

            <hr>

            <h3>📥 Parâmetros</h3>
            <p>Informações que a função recebe.</p>

            <hr>

            <h3>📤 Retorno</h3>
            <p><code>return</code> envia um resultado de volta.</p>

            <pre><code>def soma(a,b):
    return a + b</code></pre>
        """,
        "quiz": [
            {
                "id": "m6_q1",
                "question": "Qual palavra cria funções?",
                "options": ["func", "def", "function", "criar"],
                "answer": "def"
            },
            {
                "id": "m6_q2",
                "question": "print vs return — escolha a correta:",
                "options": [
                    "São iguais",
                    "print só mostra, return devolve",
                    "return mostra na tela",
                    "print fecha a função"
                ],
                "answer": "print só mostra, return devolve"
            },
            {
                "id": "m6_q3",
                "question": "O que imprime?\n<pre><code>def f(): return 5\nprint(f())</code></pre>",
                "options": ["f", "5", "Erro", "return"],
                "answer": "5"
            }
        ]
    },

    7: {
        "title": "Caçadores de Bugs",
        "description": "Erros comuns e como resolvê-los.",
        "theory": """
            <h3>🐛 Erros Comuns</h3>
            <ul>
                <li><strong>SyntaxError</strong>: erro de escrita, como esquecer parênteses ou dois-pontos</li>
                <li><strong>IndentationError</strong>: indentação errada no código</li>
                <li><strong>NameError</strong>: usar uma variável que não foi criada</li>
                <li><strong>TypeError</strong>: operação entre tipos incompatíveis</li>
                <li><strong>IndexError</strong>: acessar posição que não existe em listas</li>
                <li><strong>ZeroDivisionError</strong>: tentativa de dividir por zero</li>
            </ul>
    
            <hr>
    
            <h3>🔎 Como evitar bugs</h3>
            <ul>
                <li>Ler a mensagem de erro com atenção</li>
                <li>Testar o código em partes pequenas</li>
                <li>Usar <code>print()</code> para ver valores suspeitos</li>
                <li>Garantir que variáveis estejam criadas antes do uso</li>
            </ul>
    
            <hr>
    
            <h3>Desafio</h3>
            <pre><code>a = input("Número: ")
    b = 5
    print(int(a) + b)</code></pre>
        """,

        "quiz": [
            {
                "id": "m7_q1",
                "question": "Esquecer um parêntese gera qual erro?",
                "options": ["SyntaxError", "TypeError"],
                "answer": "SyntaxError"
            },
            {
                "id": "m7_q2",
                "question": "O código imprime qual valor?\n\nx = 3\nif x < 10:\n    x *= 3\nprint(x)",
                "options": ["3", "6", "9"],
                "answer": "9"
            },
            {
                "id": "m7_q3",
                "question": "O que causa um IndexError?",
                "options": [
                    "Acessar uma posição inexistente da lista",
                    "Usar variável não criada",
                    "Digitar letra em vez de número"
                ],
                "answer": "Acessar uma posição inexistente da lista"
            },
            {
                "id": "m7_q4",
                "question": "Qual erro aparece ao tentar dividir por zero?",
                "options": ["ValueError", "ZeroDivisionError", "NameError"],
                "answer": "ZeroDivisionError"
            },
            {
                "id": "m7_q5",
                "question": "Qual dessas ações AJUDA na depuração?",
                "options": [
                    "Ignorar a mensagem de erro",
                    "Colocar prints para ver valores",
                    "Alterar o código inteiro de uma vez"
                ],
                "answer": "Colocar prints para ver valores"
            }
        ]
    }
}
