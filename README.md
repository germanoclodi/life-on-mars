# Life on Mars?
Tentando responder à pergunta de David Bowie, nessa experiência vamos juntos da Xarpay explorar a vida em Marte!

## Como executar nosso programa espacial?
Para executar, neste mesmo diretório, rode no terminal

`$ python life_on_mars.py input.txt`

No qual "input.txt" é o arquivo com as instruções sobre o planalto, sobre o pouso e sobre o controle

## Informações específicas
Algumas validações foram incluídas que, apesar de não explícitas nas instruções do problema, modificam alguns comportamentos considerados errados e excepcionais:
- Não é possível definir um planalto com valores negativos ou decimais
- Não é possível pousar em uma posição considerada inválida pela sonda (diferentes de N, E, S ou W)
- Não é possível pousar fora do planalto ou demais posições consideradas inválidas pela sonda
- Não é possível enviar instruções que a sonda não consegue entender (diferentes de M, L ou R)

Por outro lado, restrições de pouso em posições já ocupadas e/ou colisões não foram implementadas nessa versão, apesar de poderem ser construídas caso desejado. Seriam necessárias algumas mudanças na abordagem do cálculo de posição final.

## Rodando os testes
Para os testes automatizados, foi utilizada o pacote `pytest`. Em situações normais, quando usando algum framework web como Django ou Flask, outras opções seriam mais adequadas. Como nenhum framework está sendo utilizado, é necessário instalar este pacote. 

`pip3 install pytest`

Uma vez instalado, para rodar os testes basta rodar no terminal, na mesma pasta do projeto, o comando

`pytest ./tests/run.py`

Observação: para que alguns testes rodem, é essencial que seja mantida a integridade dos arquivos do diretório tests/test_input_files!