# KMC-Plot

#------------------------------------------#
#         English instructions             #
#------------------------------------------#

This script is written in Python3 to plot ONLY kmc results made on Pilgrim.

The user needs the followings libraries:
- os
- matplotlib
- numpy

Instructions for use:

Data file:

1) The data file 'plots.slevel.txt' needed for the plot, can be found in folder '6-PLOTFILES' originated by the Pilgrim.
2) The plot should be chosen by his name.


Are available 21 different colors and more can be added to the list of colors inside the function 'plot_data' belonged to the script. The order of the colors also can be changed.
Is recommended that the inclusion of colors is made using the hexadecimal code.


This script only accepts the file 'plots.slevel.txt'. And don't plot the 'finalratios' or another plot type beyond kmc.

The generated graphics are saved in '.pdf' extension inside the folder.

If the user wanted to join all graphics in one, they should have installed the pdftk program.

#------------------------------------------#
#         Portuguese instructions          #
#------------------------------------------#


Este script é escrito em Python3 para plotar APENAS resultados kmc feitos com Pilgrim.

O usuário precisa das seguintes bibliotecas:
- os
- matplotlib
- numpy

Instruções de uso:

Arquivos de dados:
1) O arquivo de dados 'plots.slevel.txt' necessário para o plot pode ser encontrado na pasta '6-PLOTFILES' criada pelo Pilgrim.
2) O plot deve ser escolhido pelo seu nome.

Estão disponíveis 21 cores diferentes e mais podem ser adicionadas na matriz de cores dentro da função 'plot_data' pertencente ao script. A ordem das cores também pode ser alterada. Recomenda-se que a inclusão de cores seja feita utilizando o código hexadecimal.

Este script só aceita o arquivo 'plots.slevel.txt'. E não realiza os plot para 'finalratios' ou qualquer outro tipo de plot além do kmc.

Os gráficos gerados são salvos na extensão '.pdf' dentro da pasta.

Se o usuário quiser juntar todos os gráficos em um, ele deve ter instalado em seu ambiente o programa pdftk.