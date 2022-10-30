# tecemosAsTercas

## Projeto desenvolvido para a cadeira de Teoria da Computação.

## Execução
Para executar o programa, use o seguinte comando no terminal
```
 # Para operações unitárias (-t; -s; -e; -c)
 $ python3 main.py <comando> <caminho do arquivo da descrição do automato> <palavra a ser testada>
 
 # Para operações com dois automatos (-i, -u)
 $ python3 main.py <comando> <caminho do arquivo da descrição do automato> <palavra a ser testada> 
```
Utilize os seguintes CLIs para 'comando':
```
  -i  -  Intersecção (recebe 2 arq dos respectivos AFDs ou AFND)
  -u  -  União (recebe 2 arq dos respectivos AFDs ou AFND)
  -t  -  Transform ( recebe o arq do AFND)
  -s  -  Simulator ( recebe o arq do automato e a palavra)
  -e  -  Estrela ( recebe o arq do AFND ou AFD)
  -c  -  Complemento (recebe o arq do AFND ou AFD)
```
---
## Operações 
### Operação de intersecção
A operação de intersecção/concatenação do projeto foi implementada baseada no Teorema 1.47 do Sipser[2].
Dado dois automatos A1 e A2, a execução desta operação realiza A1∩A2, de forma que cria uma transição epslon partindo de cada estado de aceitação de A1, para o estado inicial de A2. Além disto, todos os estados de aceitação de A1 perderão esta classificação, tornando-se apenas estado normais.
#### Exemplo de execução:
```
$ python3 main.py -i ./automata/fda1.txt ./automata/afn2.txt
Novo automato pos operacao de Interseccao: 
estados E1, P1, A2, B2, C2, D2, E2, F2, G2
inicial E1
aceita D2, G2
F2 G2 0
E1 E1 1
E1 P1 0
B2 C2 0
A2 A2 1
A2 A2 0
A2 B2 e
A2 E2 e
P1 P1 1
P1 E1 0
P1 A2 e
E2 F2 1
E2 B2 e
C2 D2 1
```
---
### Operação de união
A operação de união do projeto foi implementada baseada no Teorema 1.45 do Sipser[2].
Dado dois automatos A1 e A2, a execução desta operação realiza A1∪A2, de forma que cria um novo estado inicial, este ramifica para os estados iniciais das máquinas anteriores com transições epslon. Desta forma, o automato não deterministicamente adivinha qual das máquinas aceita a entrada.
#### Exemplo de execução:
```
$ python3 main.py -u ./automata/fda1.txt ./automata/afn2.txt
estados q0, E1, P1, A2, B2, C2, D2, E2, F2, G2
inicial q0
aceita P1, D2, G2
E2 B2 e
E2 F2 1
P1 E1 0
P1 P1 1
A2 A2 0
A2 B2 e
A2 E2 e
A2 A2 1
C2 D2 1
E1 P1 0
E1 E1 1
F2 G2 0
B2 C2 0
q0 E1 e
q0 A2 e
```
---
### Operação de conversão de AFN para AFD
A operação de conversão de automato finito não-deterministo para deterministico foi implementado beseado na seção 2.3.5 e no Teorema 2.11 do Hopcroft[2].
Dado um automato A1, a execução desta operação realiza a conversão deste automato da classe de AFN para AFD, caso este seja um AFN. Esta conversão é realizada da seguinte forma, o power set dos estado é criado, contendo todas as possibilidades de transições do automato. Após isto, na tabela de transições, em todos os estados compostos (ex: {q2,q3}), uniremos os estados destino de cada celula do estado composto (ex: q2 q4 0; q3 q7 0. Logo {q2,q3} {q4,q7} 0). Após isto, definimos o estado inicial do novo AFD, como a conjunção de todos os estado alcançaveis apenas por transições epslon (esplon-closure). Realizamos também uma limpeza de estados, apresentando como resposta apenas os que são alcançáveis partindo do estado inicial.
#### Exemplo de execução:
```
$ python3 main.py -t ./automata/afn.txt
Novo automato pos operacao de Conversao: 
estados E, {B,A}, {C,E}, D, B, A, Ø
inicial {A}
aceita {C,E}
E D 1
E D 0
A A 1
A {B,A} 0
{C,E} D 1
{C,E} {B,D} 0
D E 1
D E 0
B {C,E} 1
```
---
### Operação de simulação
Esta operação de simulação do projeto foi implementada baseada em devaneios que acontecera durante uma aula de redes.
Dado um automato A e uma palavra W, a execução desta operação realiza o teste se o automato A aceita a palavra W,  e consequentemente afirmar que a palavra W faz parte da linguagem L(A). Esta operação é executada basicamente percorrendo a "matriz" de mapas de transições criadas anteriormente. Caso o algum dos estados que percorrem o automato esteja no estado de aceitação, é afirmado que o automato aceita a palavra.
#### Exemplo de execução
```
#Todos os blocos de 1 em W são de comprimento impar
$ python3 main.py -s ./automata/afd4.txt 0010110111 
estados A, B, C, D
inicial A
aceita A, B
A B 1
A A 0
D D 1
D D 0
C B 1
C D 0
B C 1
B A 0
Estados                   Palavra
A                0010110111
A                 010110111
A                  10110111
B                   0110111
A                    110111
B                     10111
C                      0111
D                       111
D                        11
D                         1
D                         e

A palavra não foi aceita
```
---
