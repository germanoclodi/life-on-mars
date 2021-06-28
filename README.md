# Life on Mars?
Tentando responder à pergunta de David Bowie, nessa experiência vamos juntos da Xarpay explorar a vida em Marte!

## Como executar nosso programa espacial?
Para executar, neste mesmo diretório, rode no terminal

`$ python life_on_mars.py input.txt`

No qual "input.txt" é o arquivo com as instruções sobre o planalto, sobre o pouso e sobre o controle

## Informações específicas
Algumas validações foram incluídas que, apesar de não explícitos nas instruções do problema, modificam alguns comportamentos considerados errados e exepcionais:
- Não é possível definir um planalto com valores negativos ou decimais
- Não é possível pousar em uma posição considerada inválida pela sonda (diferentes de N, E, S ou W)
- Não é possível pousar fora do planalto ou demais posições consideradas inválidas pela sonda
- Não é possível enviar instruções que a sonda não consegue entender (diferentes de M, L ou R)
