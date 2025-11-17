lessons_db = {
    1: {
        "title": "Variáveis: As Caixinhas da Memória",
        "theory": """
            <p>Imagine que você está organizando uma mudança. Você precisa de caixas para guardar suas coisas, certo?</p>
            <p>Na programação, chamamos essas caixas de <strong>Variáveis</strong>. Elas servem para guardar informações.</p>
            <p>Exemplo em Python: <code>nome = "Maria"</code></p>
        """,
        "question": "Se eu criar uma variável: <code>pontos = 10</code>, qual é o valor guardado nela?",
        "options": ["pontos", "10", "Maria", "zero"],
        "answer": "10"
    },

    2: {
        "title": "Tipos de Dados: Números, Textos e Verdades",
        "theory": """
            <p>Variáveis podem guardar diferentes tipos de informação.</p>
            <ul>
                <li><strong>int</strong>: números inteiros — ex: <code>7</code></li>
                <li><strong>float</strong>: números com vírgula — ex: <code>3.14</code></li>
                <li><strong>str</strong>: textos — ex: <code>"Olá"</code></li>
                <li><strong>bool</strong>: verdadeiro/falso — ex: <code>True</code></li>
            </ul>
        """,
        "question": "Qual é o tipo da variável: <code>nome = 'João'</code>?",
        "options": ["int", "float", "str", "bool"],
        "answer": "str"
    },

    3: {
        "title": "Entrada de Dados: Conversando com o Usuário",
        "theory": """
            <p>Podemos pedir que o usuário digite algo com a função <code>input()</code>.</p>
            <p>Exemplo: <code>nome = input('Digite seu nome: ')</code></p>
            <p>Importante: o <code>input()</code> sempre retorna texto.</p>
        """,
        "question": "O que a função <code>input()</code> sempre retorna?",
        "options": ["Um número", "Um texto (string)", "Um booleano", "Nada"],
        "answer": "Um texto (string)"
    },

    4: {
        "title": "Convertendo Tipos: De Texto para Número",
        "theory": """
            <p>Como o <code>input()</code> retorna texto, precisamos converter quando queremos números:</p>
            <ul>
                <li><code>int('10')</code> → 10</li>
                <li><code>float('3.5')</code> → 3.5</li>
            </ul>
        """,
        "question": "O que acontece em <code>int('20')</code>?",
        "options": ["Vira texto", "Vira o número 20", "Dá erro", "Vira float"],
        "answer": "Vira o número 20"
    },

    5: {
        "title": "Operadores Matemáticos",
        "theory": """
            <p>Usamos operadores para fazer contas:</p>
            <ul>
                <li><code>+</code> soma</li>
                <li><code>-</code> subtração</li>
                <li><code>*</code> multiplicação</li>
                <li><code>/</code> divisão</li>
                <li><code>//</code> divisão inteira</li>
                <li><code>%</code> resto da divisão</li>
            </ul>
        """,
        "question": "Qual é o resultado de <code>10 % 3</code>?",
        "options": ["1", "3", "0", "10"],
        "answer": "1"
    },

    6: {
        "title": "Condicionais: O Poder do 'SE'",
        "theory": """
            <p>A vida é feita de escolhas. <strong>SE</strong> chover, levo guarda-chuva. <strong>SENÃO</strong>, vou de óculos escuros.</p>
            <p>Na lógica, usamos o <code>if</code> (se) e o <code>else</code> (senão) para o computador tomar decisões.</p>
        """,
        "question": "Analise: <code>if idade >= 18: print('Pode dirigir')</code>. O que é necessário para aparecer a mensagem?",
        "options": ["Ter menos de 18 anos", "Ter exatamente 10 anos", "Ter 18 anos ou mais", "Ter carteira de motorista"],
        "answer": "Ter 18 anos ou mais"
    },

    7: {
        "title": "Operadores Lógicos: E / OU / NÃO",
        "theory": """
            <p>Podemos combinar condições:</p>
            <ul>
                <li><code>and</code> → as duas precisam ser verdade</li>
                <li><code>or</code> → pelo menos uma verdade</li>
                <li><code>not</code> → inverte o valor</li>
            </ul>
            <p>Exemplo: <code>if idade >= 18 and tem_cnh:</code></p>
        """,
        "question": "Quando a condição <code>True and False</code> é verdadeira?",
        "options": ["Sempre", "Nunca", "Só quando ambos forem True", "Quando um for True e outro False"],
        "answer": "Só quando ambos forem True"
    },

    8: {
        "title": "Repetição: O Loop While",
        "theory": """
            <p>Usamos o <code>while</code> para repetir algo enquanto uma condição é verdadeira.</p>
            <p>Exemplo:</p>
            <code>while contador < 5: print(contador)</code>
        """,
        "question": "O que faz o while?",
        "options": ["Repete enquanto a condição for verdadeira", "Executa apenas uma vez", "Cria uma variável", "Nada"],
        "answer": "Repete enquanto a condição for verdadeira"
    },

    9: {
        "title": "Repetição: O Loop For",
        "theory": """
            <p>O <code>for</code> percorre itens de uma sequência.</p>
            <p>Exemplo: <code>for letra in 'abc': print(letra)</code></p>
        """,
        "question": "Quantas vezes o código <code>for i in range(3)</code> repete?",
        "options": ["1", "2", "3", "4"],
        "answer": "3"
    },

    10: {
        "title": "Listas: Guardando Vários Itens",
        "theory": """
            <p>Listas são como caixas com vários compartimentos.</p>
            <p>Exemplo: <code>frutas = ['maçã', 'banana', 'uva']</code></p>
        """,
        "question": "Qual é o índice da fruta 'banana' na lista <code>['maçã','banana','uva']</code>?",
        "options": ["0", "1", "2", "3"],
        "answer": "1"
    },

    11: {
        "title": "Alterando Listas",
        "theory": """
            <p>Podemos adicionar, remover e mudar itens:</p>
            <ul>
                <li><code>append()</code> — adiciona</li>
                <li><code>remove()</code> — remove</li>
                <li><code>lista[i] = valor</code> — altera</li>
            </ul>
        """,
        "question": "O que acontece com <code>frutas.append('laranja')</code>?",
        "options": ["Apaga a lista", "Adiciona 'laranja'", "Troca o último item", "Nada"],
        "answer": "Adiciona 'laranja'"
    },

    12: {
        "title": "Funções: Caixinhas de Código",
        "theory": """
            <p>Funções servem para agrupar código reutilizável.</p>
            <p>Exemplo:</p>
            <code>
            def oi():<br>
                print("Olá!")
            </code>
        """,
        "question": "O que a função faz quando chamamos <code>oi()</code>?",
        "options": ["Nada", "Cria uma variável", "Imprime 'Olá!'", "Apaga tudo"],
        "answer": "Imprime 'Olá!'"
    },

    13: {
        "title": "Parâmetros: Informações para a Função",
        "theory": """
            <p>Podemos enviar informações para a função:</p>
            <code>
            def soma(a, b):<br>
                return a + b
            </code>
        """,
        "question": "Qual é o resultado de <code>soma(3, 2)</code>?",
        "options": ["32", "5", "6", "Erro"],
        "answer": "5"
    },

    14: {
        "title": "Debug: Encontrando Erros",
        "theory": """
            <p>Erros fazem parte da programação! Alguns tipos:</p>
            <ul>
                <li><strong>Sintaxe</strong>: você escreveu algo errado</li>
                <li><strong>Lógica</strong>: o programa roda, mas faz errado</li>
            </ul>
        """,
        "question": "Qual é o tipo de erro em <code>print(Olá)</code> (sem aspas)?",
        "options": ["Lógico", "De sintaxe", "De loop", "Nenhum"],
        "answer": "De sintaxe"
    },

    15: {
        "title": "Problema Final: Juntando Tudo",
        "theory": """
            <p>Agora vamos combinar tudo o que aprendemos.</p>
            <p>Observe o programa:</p>
            <code>
            idade = int(input())<br>
            if idade >= 16:<br>
                print("Pode votar")<br>
            else:<br>
                print("Não pode votar")
            </code>
        """,
        "question": "Qual mensagem aparece para idade = 14?",
        "options": ["Pode votar", "Não pode votar", "Erro", "14"],
        "answer": "Não pode votar"
    }
}