# Tabuada
Esse código imprime a tabuada de 1 a 10 de uma maneira organizada. 
Neste código é mostrado a tabua da de 1 a 10. Usando for aninhado, 
você obtem de forma rápida e concisa todos os resultados da operação.
O laço externo controla os números de 1 a 10, neste caso será impresso
a tabuada de 1 a 10.
A função range gera uma sequência de números de 1 a 11 excluindo-o.
No começo do laço, i = 1 (tabuada do 1).
Na segunda iteração i = 2 (tabuada do 2).
Será assim até chegarmos em i = 10 (tabuada do 10).
Usamos um print para apresenta a tabuada atual, a f-string antes das aspas
simples permite que variáveis com i, sejam inseridas diretamente dentro das 
chaves {}.
O '\n' cria uma nova linha, deixando a impressão mais clara possível.
O laço for j in range(1, 11), controla os números que serão multiplacado
por i (1 a 10). Ou seja, para cada tabuada, o código faz cáculos
1x1, 1x2, 1x3 até 1x10.
Sendo assim, i, que vale de 1 a 10, passará 10 vezes, por j que vale de 1 a 10,
também 10 vezes.
Para exibição da saída do código, utilizamod a f-strng com formatação {i:2}.
Isso significa que o número será formatado com espaço de dois caracteres,
valendo para tudo dentro da f-string.
E por fim o print com hífens, separando as tabuadas uma da outra.

 
