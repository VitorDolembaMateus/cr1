# Objetivo
Desenvolver e aprofunda na linguagem pyhton

# O que o script faz?
Ele criptografa e descriptografa arquivos com uma senha

# Como?
O script utiliza a operação bitwise XOR para codificar byte à byte do arquivo<br/>
![Imagem ilustrativa da operação XOR](https://github.com/VitorDolembaMateus/cr1/assets/83095568/1fef3206-5c88-45ab-b979-b11edc6a10c0)<br/>
Devido à como funciona a operação XOR, o mesmo script que criptografa o arquivo, também o descriptografa

# Limitações da aplicação
1. Limite de Caracteres para a senha
   - Os caracteres especiais mais comuns como (!,@,#,$,%,&) podem ser tulizados sem problemas, já caracteres que possuêm o código > 255 causarão erros, como 	(Ĥ, Ɖ, Σ, ϕ) que possuem os códigos (292, 393, 931, 981) no UTF-8, isso porque, o programa trabalha uitilizando byte à byte tanto do arquivo, quanto da senha, e esses caracteres possuêm 2 bytes ao invés de 1 byte.
2. Velocidade
   - Como no processamento for() para fazer o calculo byte à byte, mesmo arquivos pequenos de 1MB poderão levar alguns segundos para cryptografar por inteiro
