# Este jogo de rpg foi feito para rodar na ide visual studio code
# Jogo Produzido por Paulo Sérgio e Rafael Farias

# Módulos, pacotes e bibliotecas


import time
import sys
from random import randint
#import pygame
#pygame.init()
#pygame.mixer.music.load('Wolrd map.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()


# Escrita dos textos e desenhos


def escrita_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.04)
def desenho_inicial_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.003)
def desenho_creditos_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.003)    


# Menu principal, créditos e sair do jogo


print('\n\n========================== MENU PRINCIPAL ===========================\n')                        
print('                        [1] Iniciar Jogo  ')                              
print('                        [2] Abrir Créditos')
print('                        [3] Sair  ')
print('\n')
print('='*69)
print('\n')
menu_principal = (input('Digite um número: '))
print('\n')
print('='*69)


if menu_principal == '1':
  time.sleep(2)
  texto = '\nAbrindo o jogo...\n'
  escrita_rpg(texto)
  texto = 'Por favor aguarde...'
  escrita_rpg(texto)
  time.sleep(2)
  desenho_inicial_rpg
  print('\n')
  print('='*182)
  texto = ('''\n
  
  #######     ######     ###    ##     ## #### ##    ## ##     ##  #######    ########   #######     ######   ##     ## ######## ########  ########  ######## #### ########   #######  
 ##     ##   ##    ##   ## ##   ###   ###  ##  ###   ## ##     ## ##     ##   ##     ## ##     ##   ##    ##  ##     ## ##       ##     ## ##     ## ##        ##  ##     ## ##     ##
 ##     ##   ##        ##   ##  #### ####  ##  ####  ## ##     ## ##     ##   ##     ## ##     ##   ##        ##     ## ##       ##     ## ##     ## ##        ##  ##     ## ##     ##
 ##     ##   ##       ##     ## ## ### ##  ##  ## ## ## ######### ##     ##   ##     ## ##     ##   ##   #### ##     ## ######   ########  ########  ######    ##  ########  ##     ##
 ##     ##   ##       ######### ##  #  ##  ##  ##  #### ##     ## ##     ##   ##     ## ##     ##   ##    ##  ##     ## ##       ##   ##   ##   ##   ##        ##  ##   ##   ##     ##
 ##     ##   ##    ## ##     ## ##     ##  ##  ##   ### ##     ## ##     ##   ##     ## ##     ##   ##    ##  ##     ## ##       ##    ##  ##    ##  ##        ##  ##    ##  ##     ##
  #######     ######  ##     ## ##     ## #### ##    ## ##     ##  #######    ########   #######     ######    #######  ######## ##     ## ##     ## ######## #### ##     ##  #######
                                                                                                                                                                                                


                                                                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡿⣟⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⠽⡝⡎⡏⠭⡪⠪⡒⣽⣽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⣿⣿⡿⣻⢝⢎⢝⢜⠸⡨⢊⢌⠪⡈⢪⢸⢸⢽⢯⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⢟⢵⠹⡘⠔⡡⠑⢠⣕⣬⣖⣮⡾⠯⢟⣆⠣⡫⡹⡱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⣵⡥⡊⠄⣗⢶⡛⠖⣶⣿⣟⡗⠞⢿⢯⣗⡇⢅⠣⡱⡙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⣿⡯⠌⡮⣿⣿⡇⠄⣿⣿⣿⡇⠄⢸⣟⢮⡺⡔⠡⡊⡎⡼⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣵⡹⡙⡇⢟⣿⣿⣿⣾⣿⣟⣾⣻⣟⣟⣞⡝⡞⡆⡑⡘⡨⢨⡢⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣷⣟⡯⡇⠪⡿⣞⣯⡿⣫⣖⢮⢜⢮⡺⡜⡎⡇⡃⢜⢼⠸⢑⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⣿⡯⣣⣥⠷⣿⣮⡝⢕⠵⡹⡪⡣⡣⡣⡣⢃⢂⠂⢇⢆⣢⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⠿⡫⣵⣕⣛⣽⣕⠿⡷⣧⣈⡢⡁⠅⢁⢂⢂⢢⣿⣔⠅⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⡯⢏⣞⣯⣟⣛⢿⢽⢟⡽⣎⢯⢝⡝⡦⡁⢆⠐⢴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⡿⡸⡪⣓⣛⣛⡝⡿⢿⢝⢞⢎⢇⢵⢹⢌⢢⠑⢌⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⢎⡎⡌⠪⢸⡑⡘⡜⠅⡃⡱⠡⡣⡣⡣⢃⠪⡊⢆⠌⠨⣻⣿⡿⠛⢋⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣧⢻⢌⢬⢜⠸⠨⡨⡐⢔⢌⢌⢎⠎⠆⢂⠑⢌⡂⠅⢌⢢⢛⠠⠊⡄⡛⡻⡻⡿⢿⢿⠿⡿⡿⢿⢿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⢜⡤⡱⢸⠨⠪⡐⡨⡰⡑⡅⡇⠅⠨⢈⠐⠠⢘⠠⠐⡐⠄⡂⢕⢦⢪⢦⣗⣮⣷⣭⣮⣮⣾⡵⣧⣧⡻⣿⣿
                                                                  ⣿⣿⣿⣿⣪⡣⣝⢭⢊⢆⢇⢇⠇⠡⢐⠨⠐⢌⠊⠅⠅⢌⢻⣄⢕⢰⣶⣾⣼⣵⣷⣽⣺⡯⡿⣷⣿⡯⡺⣚⣮⣾⣿
                                                                  ⣿⣿⣿⣿⣿⣾⣜⢜⢜⡮⠘⠂⠆⠅⢢⣡⠑⠐⠁⡁⠅⠱⢿⣿⣴⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⣿⣿⣿⡿⡹⠈⠄⠠⠄⣿⣿⡈⠄⡀⠄⠄⠐⡐⠐⠽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                                                                  ⣿⣿⣿⣿⣿⣿⣿⣿⣇⡊⠄⠡⢈⣄⣿⣿⣿⣷⣶⣶⣷⣶⣶⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ 
                                                                  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

\n''')
 

elif menu_principal == '2':
  print('\n')
  texto = 'Abrindo créditos...\n'
  escrita_rpg(texto)
  texto = 'Por favor aguarde...\n'
  escrita_rpg(texto)
  time.sleep(2)
  print('\n')
  print('='*182)
  texto = ('''
        
-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++++++++++++++++-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++++++++++++++++++++++-+-++++++++++++++++++++++++++++++++++++++-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++++++++++++++++++-+#--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++++++++++++++++---##+---++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++++++++####+++++++-#-+++##-----++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++-----+#+++++++-##+++-++++#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++++++-------+-+-###########-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++------#---++++-#####+#####-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++----##+#####------####...####-+++++++++-+--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++-+--#####++##+##-.-####---####--++++-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++--##############-#--####...####-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++--#++++++++++-+######+###########--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++-+-##############++++-----.------##-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++--+-###############################--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++.###########+########+##########-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++-+++-+-#####..+##-.-##+--##+##########--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++-++++++-#####-.-##---##+.-##+###+..####--+----++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++#-.############+##++-+#+###-..####--++##++++++++++++++++++++++++++++++++++++++++++++##+++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++-#--####################+##########--+++++++++---+++++++++-++++++++++++++++++++++++++--+++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++#--#########.....#################+-+--+++++++##++++++++--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++###+++++++++++--+++++####+++-#--#######-#-.---#####-###-#######+-++#-#+++++-+++++++++#+++++++++++++++++++++++++++++++++++++++++++++------+--------+++-++---+.
-#-------++++++++-#+---------++.#+-#+#####-#-.---#####+###-+-.-###+-++++#+##++-++++++++++-----+-----+++----------+++++++++++-+-+++--++--+--++-++++++++-----++++.
.-----+--+-++++++.######+##+--+.+--#-#####-#-...-##++#--##+##.+###+++++-+--..---------------+-------......+#+----+---------+++++++++++++++++++++++++++++-++++-+.
.---+++++----++++.#####+-++-#+#+####-########-##+####++-#+-...-..--++++++-########-#####.####.########+.########--++++++++++++-----++++++++++++++-+++++++++++++.
.++-----++--#++++-##+##-##.-###+#..------..---..#######-#+####...---.-+--+-###+.-+.-####.####+###+---####...-+###--+++++++++++++++++++++-+-++++++++++++-+++++--.
.--+-------+++++#-####+#.+..#..-#-++++++++++++-+--####+-####+#####-+..----.###--...-####.+#######.-+---#--+++.###--+-++++++++++++-++-+++-++++++++++++++-++-+--+.
.----+--+-++++++--###..-++#---+-#+++-+-------++--....--+#+######+-#####-+#########-.####.-###-###.--------++-.###.++++--------+-++++++++++++++++++-++-+++++++++.
.-#+--####+++++##+-.-+###+#-+---++---++--.-#+--##-#+-#+####+++#########--##+##++##..#+##..###+.###---++++++--###--++++++++++++-++--++-++++-+++-+++++++---+--+++.
-##-..-#-++++------+--..----+-#-+#.##-..###+#+-##.#+-###-+++++++++++##+-+##+##+#+.-.####..####.-####-.-+---.###.#-++++--+++++++###+++++++++++--++----++++++++++.
..---+-++++++-##.++++-##-+++--#.-#.+#+#+++..#-######+#+##++#++#####++#+####+##+#-.-.####..####----####---.###-..#---.-++---+-++--+++++--------++++-------+--+++.
-+++##-++++++.##.++-+--#.-....#.+##+#############################++#++---.++#######-+#########--#...-######-....#.---------------.--+++++-----++-++++##++##++++.
.---##.+-++--.##......-#-##################+---.------------------+#############+#+-.-######+--.#+++-++####+######-..#######+-######-+--#####+--+######.-------.
.#--#+...----.#######+---------------+++##########+++####-----##+++#.-#-.+-#######.####+.+###---######+...##########.#######+.######---###+##+--###+###+-++++++.
...###########################++++++-------------#########+#++#######---####+-####+#####.+###+--###-###.-.####-.####.####...-.###-###..###.###--###+-###--+++++.
.##+--------------------------+++++#################-+####---####+###-######--+###--####-+###+-+###.####-.####..####.+###--+-.###++##--###.###.-###+-###--+-+++.
.--++++#+########################+-+++++++------+###+....-######+-#+#-..####-.+###--####--###+-####-####--####--####.-#######-+###.##-.###-###.-###+.####.++++-.
-#######++++++-+++---+++++-+-+++-++++++++----++-+########+..-#+#+-###+--####---###+-####--####-####.-###-.########+---###+----+###.###-##+.###.-#########+-+++-.
.---++--+--------+-+++++-+++#+##################+++++#####+-##+##+####--####-#####+.####--####.##########.+###-.-###--####.----###.-##+##+.###.-###+..####-++++.
.####################-#####++++-+-+++-----.--+##-+-+---#+#+-##########+-####--#####-####-.####.####..####--####--####.########.###--#####+-###+-####--+###+-+++.
.+-+--+-----------++++++++++-+#+++++++++####+---####---###+-####---####-#####-+####-##########-####--+###+-####--####-+#######-###+--##+#---+++-+-++++++-++-+++.
.++++++++#-++------------.-------+-++##+-----++-+#########--####---####--##########--+#+++++++.##--+++---+-----++----++------+++-++++++++++++++++++++#++++#-+++.
.+-+++-++++########################-...-++++++++--++-----++++--++#++-+++++-----+--++###-###++++++-###+##-#+#+#-#++####+#+####+##-##-++++++++++++++++++++++#-+-+.
-########++-----.--+----..--+#-....-+#++++++---+-+++++++++++++++++++++++-#++##.##+#+###-#-+##+-##-#--+#--#######++######+++#####+##+++++++++++++++++++++++#++++.


                                               ***** Jogo Desenvolvido Por Paulo Sérgio e Rafael Farias *****
                                               Primeiro Período Turma B Universidade Vassouras Saquarema 2023  \n ''')


elif menu_principal == '3':
  print('\n')
  texto = ('Obrigado por jogar nosso jogo.\n')
  escrita_rpg(texto)
  texto = ('Volte novamente quando quiser ^.^\n\n\n')
  escrita_rpg(texto)
  sys.exit()

else:
  texto = ('\nDigite uma das três opções no seu teclado para prosseguir.\n')
  escrita_rpg(texto)
  texto = ('Numéro 1, número 2 ou número 3.\n')
  escrita_rpg(texto)
  texto = ('Rode o código do jogo novamente.\n\n')
  escrita_rpg(texto)
  sys.exit()

desenho_creditos_rpg(texto)
print('\n')
print('='*182)
time.sleep(2)


# Nome do(a) personagem


personagem = input('\nDigite o seu nome e aperte a tecla enter: ')
time.sleep(2)
texto = f'Olá {personagem}, seja muito bem vindo ao jogo caminho do guerreiro. \n'
escrita_rpg(texto)
texto = 'Vamos juntos encarar uma grande aventura!'
escrita_rpg(texto)


# Capítulo 1


time.sleep(2)
print('\n')
print('='*182)
print('\n')
time.sleep(2)
texto = 'Capítulo 1: O Início da Jornada '
escrita_rpg(texto)
print('\n')
time.sleep(2)
texto = 'Há muito tempo, em um mundo mágico e misterioso, existia uma pedra elemental poderosa que possuía o controle sobre os quatro elementos fundamentais: água, fogo, terra e ar.\n'
escrita_rpg(texto)
texto = ('Esta pedra, conhecida como "A Pedra Elemental da Harmonia", era guardada na parte central de um antigo lugar proibido chamado Reino de Saquarema.\n')
escrita_rpg(texto)
texto = ('Um dia, um vilão muito famoso conhecido como Sephiroth, em sua busca insaciável por poder, conseguiu roubar a Pedra Elemental da Harmonia e a quebrou em quatro partes.\n')
escrita_rpg(texto)
texto = ('O mundo ficou instável, com furacões, terremotos, tsunamis e queimadas, pois cada parte da pedra continha o poder para controlar um elemento vital a humanidade.\n')
escrita_rpg(texto)
texto = ('Sephiroth escondeu os quatro fragmentos elementais em diferentes reinos espalhados pelo mundo:\nReino de Jaconé, Reino de Barra Nova, Reino de Boqueirão e Reino de Bacaxá.\n')
escrita_rpg(texto)
texto = ('Quatro guardiões elementais foram recrutados por Sephitorh para tomar conta dos fragmentos elementais roubados por ele:\n')
escrita_rpg(texto)
texto = ('Guardião elemental da água, guardião elemental do fogo, guardião elemental da terra e guardião elemental do ar.\n')
escrita_rpg(texto)
texto = (f'Um(a) destemido(a) aventureiro(a) chamado(a) {personagem}, foi convocado(a) por um antigo oráculo mestre das artes místicas chamado João Coelho.\n')
escrita_rpg(texto)
texto = ('Para recuperar as partes da Pedra Elemental da Harmonia e impedir que Sephiroth usasse seu poder para subjugar o mundo.\n')
escrita_rpg(texto)
print('\n')
print('='*182)
time.sleep(2)
print('\n')


# Capítulo 2


texto = 'Capítulo 2: O guardião elemental da água. '
escrita_rpg(texto)
print('\n')
time.sleep(0)
texto = (f'{personagem} está cavalgando na rua com seu cavalo pé de pano, e ouviu boatos de que o primeiro fragmento da Pedra Elemental da Harmonia,\n')
escrita_rpg(texto)
texto = 'responsável pelo poder do elemento água, está escondido no Reino de Jaconé que fica à beira-mar.\n'
escrita_rpg(texto)
texto = 'O guardião elemental da água é conhecido por sua habilidade em manipular os oceanos e agilidade dentro dágua.\n'
escrita_rpg(texto)
texto = (f'Após uma breve galopada, {personagem} ficou sabendo que o fragmento elemental da água está entre as ruas 96 e 13 do Reino de Jaconé.\n')
escrita_rpg(texto)
texto = ('Gostaria de cavalgar com seu cavalo pé de pano para a rua 96 ou para a rua 13?\n\n')
escrita_rpg(texto)
texto = (f'O que {personagem} vai fazer?\n\n')
escrita_rpg(texto)
texto = ('[1] Rua 96\n')
escrita_rpg(texto)
texto = ('[2] Rua 13')
escrita_rpg(texto)
print('\n')
escolha = input('Digite 1 ou 2: ')
print('\n') 
print('='*182)
print('\n')


# Escolhas capítulo 2


if escolha == '1':
  texto = ('''
                                                                                                   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢖⠦⣄⠐⢦⡀⠀⠀⠀⠀⡠⠀⠀⠀⣠⠖⠁⢀⢀⡀⡠⠠⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⣀⠀⠀⠤⠒⠂⠒⠖⣶⣠⠮⢷⣄⢈⢒⣏⡚⢦⣀⣼⠁⠀⡠⠊⢉⣤⣹⣷⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⢛⠟⠒⣆⠘⠢⣠⣱⡄⢤⡿⢿⡎⠛⢁⢤⡿⢷⣤⠦⣑⠀⣢⣉⣈⣿⣷⠆⠂⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠦⠖⠁⠦⢉⠇⡘⢠⡎⡉⣿⣿⣿⣿⣇⠀⠈⠀⡐⠎⠙⢳⣦⠽⡉⠟⢉⠴⣿⡗⠒⠒⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⢀⣤⣴⣂⡀⣁⠘⠙⠒⣿⠏⢻⣏⠀⠄⠠⣿⡧⠀⡠⠋⢻⣷⠖⣾⣱⠶⢶⠾⠒⠆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠀⠉⣀⣾⣿⣧⣴⣖⣿⢻⣟⣠⣈⠛⠀⢑⣀⠥⠒⠏⠀⠀⠸⣿⡟⠧⣾⡛⠒⠑⠒⠤⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣋⠀⠀⣠⣿⣻⡏⢣⣿⡿⡿⠋⢿⣷⡉⠃⠀⠈⡉⢀⣀⣆⢱⣦⣾⡿⣡⠿⣗⠀⠈⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠋⠀⣸⠀⣱⣿⣿⢋⣷⠟⠁⠔⢻⣧⠚⣽⣿⣤⣶⣿⣿⣾⢿⡟⣾⢻⣩⠚⠙⠦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⣴⣿⡿⣏⡿⠁⡀⠀⠰⣡⠞⣷⢏⠛⣿⣿⡟⢿⡿⣾⡇⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠁⢸⣿⣿⠁⣹⠁⢀⠈⠀⢲⠏⠰⠁⠇⠁⠀⠉⣷⠈⠧⢀⡅⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡔⠀⠀⣼⣿⡷⠾⠇⢀⠀⢀⣸⡟⠀⠀⠀⠀⠀⠀⠀⢼⡆⠀⠙⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⡃⣠⢾⣿⢻⣤⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⣀⡀⣡⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡟⠱⢿⣿⣿⣁⣹⡀⠀⠀⠀⣺⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⢸⣿⣿⣟⣿⣅⠀⠀⠉⡪⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⢀⠀⣹⣿⡟⠘⡇⠉⡆⠀⠀⠐⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⢨⠔⠁⢻⣳⡿⠲⣟⣴⡀⠀⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⡿⠀⠀⠘⣿⣿⢷⡓⢿⠛⣄⠀⠀⠐⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⡰⣢⢿⣿⣿⢷⣼⠦⡉⣷⣀⠀⠈⠹⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠁⠄⢻⣟⣿⣉⣦⠁⠸⢳⣦⠀⠀⠀⢛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⢠⠻⣿⣿⣷⠨⣿⣶⡛⣷⣄⠀⠀⠀⠻⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⡇⠈⡀⠈⢿⣿⣿⣛⣿⡏⠛⢪⠳⣄⠀⠀⠉⠉⠳⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⠀⠀⠙⢻⣿⣶⣧⣤⡸⢷⠟⣑⢤⡀⠀⠀⠈⠋⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⠖⢙⣫⣽⣷⢿⣾⣦⣤⠠⠀⠀⠀⡇⢰⣄⠀⠀⡀⠀⡙⠻⣿⣷⢄⠘⠇⠙⠰⢟⡷⢄⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡔⣲⣾⠿⢈⣉⠀⠹⡿⣿⣷⣤⡀⢠⠀⠀⣿⣆⠺⣧⠀⠀⠀⢸⡿⣶⣿⣶⡟⠃⠹⣏⡈⢑⢄⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀
⠀⡈⣰⣿⠐⠈⠙⠙⠿⣇⠹⡇⣿⣿⡄⠼⢸⡆⠘⡇⠀⠈⠣⡀⠀⠘⡗⢨⣿⣿⠿⣶⠆⢿⣷⡘⠟⢳⡀⠀⠀⠀⠱⠀⠀⠀⠀⠀⠀⠀
⠘⢸⡟⠁⠀⡀⠀⠉⠢⠘⠃⢀⠘⢻⣷⣐⡀⡇⠀⠹⡄⠀⠀⢡⣠⠂⢠⠀⠹⡽⣷⣿⢾⣿⠶⣷⢻⣴⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⡟⠀⣈⠀⠀⠀⠀⠱⡇⠹⠇⣘⢻⣇⠀⠛⢰⠀⠈⠀⠀⠀⢿⠀⠀⠀⣤⠀⠘⣿⣿⣿⡖⠿⠈⠛⣷⡉⢆⠀⠀⠠⡀⠀⠀⠀⠀⠀
⡞⢸⣇⠀⣝⠂⠀⠀⠀⠐⣿⣶⣆⢈⣿⣿⡄⠀⣺⠀⡄⠀⠀⠀⠈⢧⠀⠀⢸⠀⠀⣿⣿⣿⣦⣦⡨⣶⣿⡧⢺⣆⠀⠀⡇⠀⠀⠀⠀⠀
⠱⡈⣿⠀⢻⡀⠀⠀⠀⠀⣿⡄⢿⠀⣽⣾⣧⠘⢁⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠣⡀⠙⣿⣿⣿⣹⣷⣻⣹⣷⣿⣿⡆⠀⠃⠀⠀⠀⠀⠀
⠀⢹⠻⢆⠸⡈⠲⣤⡀⠀⣿⡻⣶⣆⡉⣻⣿⣷⠈⢧⣸⠀⠀⠀⠀⢄⠀⠀⠠⠚⠉⠀⣿⣿⣿⣟⡯⡜⠛⢈⣹⣿⣯⠀⠀⠀⠀⠀⠀⠀
⠀⡼⠀⠈⣆⠱⡀⠒⢬⣄⣸⣧⣄⡙⠓⠛⢟⣿⣷⡦⠁⡆⠀⢡⠀⠀⠳⣄⠀⠀⠀⣰⣿⣿⣿⣿⣹⣗⣶⡿⣿⠍⣿⠄⠄⠀⠀⠀⠀⠀
⠀⡗⢀⠀⣿⣦⡘⢾⠛⠿⣍⣿⡿⠄⣄⣷⣄⣻⡻⣧⡸⠈⣦⠈⢆⠀⠀⠉⠀⢤⡀⣽⣟⣿⣿⠜⢿⠻⣉⠁⠹⣀⣿⣶⠀⠀⠀⠀⠀⠀
⠀⠀⠘⡆⠀⣿⣷⣄⡱⣤⣽⣿⣿⣂⣉⡙⠃⣼⣿⣿⣿⣦⣻⡠⢾⢳⣄⡃⠼⢂⣽⣿⣿⣿⣿⣷⣆⢀⠋⣤⡏⣸⣿⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡿⠶⣿⠁⢧⣷⣮⣿⣾⣿⣿⣧⣟⡶⠾⠹⣿⠛⣿⣿⣿⣶⣬⣤⣷⣾⣿⣿⣽⣻⣿⣿⣿⡿⣿⣾⠉⣄⣻⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⠀⢹⣧⣸⠋⡌⣿⣿⣿⣿⣿⣿⡗⡑⣶⣻⠂⢹⠻⠛⢻⣟⣫⣽⡿⣿⢟⣘⣿⡉⢸⣿⠄⣸⠋⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠃⣿⠂⢀⢹⣿⣿⠉⠙⢿⣿⠆⣙⢫⣾⠆⢴⣤⢹⠏⠜⠙⣿⣥⠘⢋⣹⣗⢀⢨⣴⣴⢇⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⢰⠘⣾⣿⣿⠀⠀⠀⠙⠿⣿⣯⣿⣦⠿⠗⠐⠱⣶⡖⠸⣏⣡⣜⡋⠽⠟⣄⣴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡆⢧⢹⣿⠇⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣶⣿⣿⣶⣾⣿⣿⣏⣻⣷⡶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⡌⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⢸⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                           
                                                                                                    
\n''')
  
  desenho_inicial_rpg(texto)
  print('='*182)
  print('\n')
  texto = ('Você entrou na rua 96, foi em direção a praia e deu de cara com o guardião elemental da água, prepare-se para a batalha!\n')
  escrita_rpg(texto)
  texto = ('O guardião elemental da água saiu do mar, e com a calda longa dele, desferiu um ataque giratório em você.\n\n')
  escrita_rpg(texto)
  texto = (f'O que {personagem} vai fazer?\n\n')
  escrita_rpg(texto)
  texto = ('[1] Pular o ataque do monstro?\n')
  escrita_rpg(texto)
  texto = ('[2] Abaixar do ataque do monstro?\n\n')
  escrita_rpg(texto)
  escolha = input('Digite 1 ou 2: ') 
  print('\n')
  print('='*182)
  print('\n')
  


elif escolha == '2':
   texto = (f'\n{personagem} ficou igual uma barata tonta, cavalgando na rua 13 em circulos com seu cavalo pé de pano durante muito tempo,\n')
   escrita_rpg(texto)
   texto = ('e não conseguiu encontrar o fragmento responsável pelo elemento água da Pedra Elemental da Hamornia.\n\n' )
   escrita_rpg(texto)
   texto = ('\nFim de jogo.\n\n')
   escrita_rpg(texto)
   sys.exit()

else:
   texto = ('\nDigite uma das duas opções no seu teclado para prosseguir, numéro 1 ou número 2.\n')
   escrita_rpg(texto)
   texto = ('Rode o código do jogo novamente.\n\n')
   escrita_rpg(texto)
   sys.exit()

  
if escolha == '1':
    texto = ('Seu pulo não foi alto o suficiente.\n')
    escrita_rpg(texto)
    texto = (f'O guardião elemental da água é muito maior do que você.\n')
    escrita_rpg(texto)
    texto = ('O ataque de calda longa giratória do monstro te pegou em cheio causando dano crítico.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} foi cortado(a) ao meio!\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    sys.exit()
  
elif escolha == '2':
    texto = ('Ufa, essa foi por pouco!\n')
    escrita_rpg(texto)
    texto = (f'{personagem} conseguiu abaixar desviando do ataque do monstro,\n')
    escrita_rpg(texto)
    texto = ('e ao mesmo tempo conseguiu uma brecha para atacar.\n\n')
    escrita_rpg(texto)
    texto = (f'O que {personagem} vai fazer?\n\n')
    escrita_rpg(texto)
    texto = ('[1] Aproveitar que o monstro está de costas e atacar?\n' )
    escrita_rpg(texto)
    texto = ('[2] Esperar uma melhor oportunidade de ataque?\n\n' )
    escrita_rpg(texto)
    escolha = input('Digite 1 ou 2: ') 
    print('\n')
    print('='*182)
 
if escolha == '1':
    texto = (f'\n{personagem} aproveitou a oportunidade e atacou o guardião elemental da água de costas.\n')
    escrita_rpg(texto)
    texto = ('O monstro tomou dano crítico e foi derrotado.\n')
    escrita_rpg(texto)
    texto = (f'Parabéns {personagem}! Você conseguiu recuperar o fragmento elemental responsável pelo elemento água da Pedra Elemental da Harmonia.\n')
    escrita_rpg(texto)
    texto = ('Agora só faltam mais 3 fragmentos para você salvar o mundo.\n\n')
    escrita_rpg(texto)
    print('='*182)
    print('\n')
    

elif escolha == '2':
    texto = (f'\n{personagem} esperou o monstro se recuperar do ataque dele.\n')
    escrita_rpg(texto)
    texto = ('O guardião elemental da água pulou novamente no mar.\n')
    escrita_rpg(texto)
    texto = ('Ele foi para o meio do oceano e concentrou todo o seu poder lançando uma onda tsunami contra você.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} foi varrido do mapa, junto com todos os habitantes do Reino de Jaconé!\n\n')
    escrita_rpg(texto)
    texto = ('Fim de Jogo.')
    escrita_rpg(texto)
    print('\n')
    print('='*182)
    print('\n')
    sys.exit()
    
     

else:
    texto = ('\nEscolha uma das duas opções no seu teclado para prosseguir, numéro 1 ou número 2.\n')
    escrita_rpg(texto)
    texto = ('Rode o código do jogo novamente.\n\n')
    escrita_rpg(texto)
    sys.exit()


# Capítulo 3


texto = 'Capítulo 3: O guardião elemental da terra. '
escrita_rpg(texto)
print('\n')
time.sleep(0)
texto = ('Após vencer a batalha molezinha contra o guardião elemental da água do Reino de Jaconé.\n')
escrita_rpg(texto)
texto = (f'{personagem} montou novamente em seu cavalo pé de pano, e foi cavalgando em busca de outros fragmentos elementais.\n')
escrita_rpg(texto)
texto = (f'Depois de uma breve galopada, {personagem} pegou a avenida litorânea e passou pelo Reino de Manitiba para descansar.\n')
escrita_rpg(texto)
texto = (f'No dia seguinte, depois do café da manhã, {personagem} continuou sua jornada até chegar ao Reino de Barra Nova.\n')
escrita_rpg(texto)
texto = (f'No Reino de Barra Nova, {personagem} sentiu um forte tremor de terra, e avistou uma montanha gigantesca surgindo no epicentro do tremor.\n')
escrita_rpg(texto)
texto = (f'{personagem} logo deduziu que somente um guardião elemental teria poder suficiente para fazer aquilo.\n\n')
escrita_rpg(texto)
texto = (f'O que {personagem} vai fazer?\n\n')
escrita_rpg(texto)
texto = ('[1] Tentar escalar a montanha montado em seu cavalo pé de pano?\n')
escrita_rpg(texto)
texto = ('[2] Deixar seu cavalo pé de pano em um local seguro e escalar a montanha sozinho?\n\n')
escrita_rpg(texto)
escolha = input('Digite 1 ou 2: ')
print('\n')
print('='*182)


if escolha == '1':
    texto = (f'{personagem} tentou escalar a montanha montado em seu cavalo pé de pano.\n')
    escrita_rpg(texto)
    texto = ('Ao chegar numa altura considerável, pé de pano pisou em falso e tropeçou numa rocha.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} e pé de pano se arrebentaram no chão causando dano crítico.\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    sys.exit()

elif escolha == '2':
  texto = ('''

                                                       :::                                        
                                           :;;:         :;;::                                       
                                ::::::    ;;;;;;;:    :;;:;;;::                                     
                                ++:::::;::;;;;;;;;;:  :;;;:;;;:    :                                
                                ;+++;:::::::;;;+;;;;;;;;;;;;;;;: :::::                              
                                 ;;++++x+;;;;;;++;;;;;+x+;;;;;:;;;;;::                              
                          :;;;;;;;;+xxxxxx;;;;;;++;;;;;;;+;;;;+;;;;;:::;;:;;                        
                          ;;::::::::;;;;+xx+;:;:;+x+;;;:;;;;+++;+++;;;;;;;+;                        
                           +x++;;;::::::::.:+x;;;:;;+;+x;;+;;;;;:;+++;;;;;;+                        
                            xxxx+++;+++++++;;;xxxxx+;;;;;:;;;;;;;;++x+;;;++;                        
                             ;;xxxxxxxxx+++++;;;;+xxXXXXx++xx+x+xXXx+;++++:                         
                              +xxxxXXXXXXXxxXxx+;;;++X$$XXXxxX$$$X++xxxxx+:                         
                             ;xxxxxxXXXXXXXXXXXXXXXXxx++XXXX$$$x+xXXXXXXx+;                         
                            :+xxxxxxXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx++                          
                           ;;;;;;;xxxXXXX$XXXXXXXXXXXXXXX$$$$$XXXXXXXXXxx+                          
                      ;; ::;++++++xXXXXXXX$XXXXXXXXXXXxxxxxxxxxXXXXXXXxxx+                          
                     ;;;;+;;++xxxxxx+;+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx+                           
                   ;;;+;;;;;:;;++x+; +xXX$XXXXXXXXXXXXXXXXXXXXXXXX$$XXx                             
                  ;;+;;:::;;;;++xX+  +xXXXXXXXXXXXXXXXXXXXXXXXXXXX$XXx;                             
                :++;;;;;;;;;+xXXXx;   +XXXXXXXXXXXXXXXXXXXXXXXXXXXxx+;;                             
              ::;::::::;+;;+xxxXx;    ;+XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX+;;;                          
             :;;:;+;;;x+::::::++;     :+XXXXXXXXXXXXXXXXXXXXXXXXXX$XXXXxx++;;;::                    
            :;;;+x+;;:;xx+++;;:;++   ;+X$XXXXXXXXXXXXXXXX$$$$XX+xXXXXXXXx++;++;;;:::                
            ;++;;+;:::;xXXXXXXxxx    +xxXXXXXXXXXXX$$$$$$$$$$$XX+:+XXXXXx;::::++;::::;;             
           :;;::;;;;:;+xXXXXXX+:    ;xxxXXXXXXXXXXXX$$$$$$$XXXXXXx:;xXXXXXXx+::;xxx;:::;:           
           ;;;;+xXX++XXXXXXXXX+;    +xXXXXXXXXXXXXXXX$$$$$x++++++xx:+xXXXXXXXXXXXXXXXx+:::          
          :;:;+xXXXXXXXXXXXXXXx;;  ;;XXXXXXXXXXx+xxx++X$Xx+;+;::;;xx ;xxXXXXXXXXXXXXxxxxx+          
          ;;:xXXxXXXXXXXXXx :+XX; ;+xxXXXXXXXXxxx;   xXXxx++:;++++xxx  ;+xxXXXXXXXXxx;              
          ;;xXx+;xXXXXx+;;      ;++XXXXXXXXXxx++;    :+xXXxx;+;;;+x++x    :+xxxxxxx;:::             
           xx+  +XXXX+        +++xXXXXXXXxXxxx+        +xxXxx+++++xxX+;    :xxx;  xx+xx             
                :xXXx       :;++xXXXxxxxxxx++;           xxXXXxxxxXXXXx;            ++              
                  +;        ;;+XXxXxxxxxx+:              ;XXXXXXXXXXXXXx;                           
                           ++xxxxxxxxxxxx;              ;+XXXXXXXXXXXXXX;                           
                          ;++xxxxxxxxxxxx;             ++x$XXXXXXXXXXXXXx                           
                         ;+xxxxxxxxxxxxxx;++           xXXXXXXXXXXXXXXXX+;                          
                       ;+xxxxxxxxxxxxxx+++;;          :xXXXXXXXXXXXXXXXXXx++                        
                      ;+++++xxxxxxxxx+x++;             +XxXXXXXXXXXXXXXXxxXx:                       
                        :;+xxxxxxx+++x+;               +xXXXXxxxxXx+;;;;;+xx;                       
                       ;;++xx++++;                     +xxxxxx+;;;;;;;++;;++                        
                                                        +xXXxxxx++;;;;;;;;;;;;;                     
                                                        .+xxxxxxxxxxxxXxx+;;;;;;:                   
                                                           ..:::;;++++;x++;;;;                                                                                                              

\n''')
  
desenho_inicial_rpg(texto)
print('='*182)
print('\n')
texto = (f'{personagem} deixou seu amigo e fiél escudeiro pé de pano em um local seguro, e foi sozinho escalar a montanha.\n')
escrita_rpg(texto)
texto = (f'Chegando ao topo da montanha, {personagem} ficou frente a frente com o guardião elemental da terra, prepare-se para a batalha!\n')
escrita_rpg(texto)
texto =( f'O guardião elemental da terra iniciou o ataque, lançando várias pedras pontiagudas cortantes em sua direção.\n\n\n')
escrita_rpg(texto)
texto = (f'O que {personagem} vai fazer?\n\n')
escrita_rpg(texto)
texto = ('[1] Tentar desviar do ataque do monstro?\n')
escrita_rpg(texto)
texto = ('[2] Tentar defender o ataque do monstro com seu escudo?\n\n')
escrita_rpg(texto)
escolha = input('Digite 1 ou 2: ')
print('\n')
print('='*182)
print('\n')

if escolha == '1':
    texto = (f'{personagem} tentou desviar do ataque do monstro, mas sua velocidade não foi rápida o suficiênte.\n')
    escrita_rpg(texto)
    texto = ('As pedras pontiagudas cortantes lançadas pelo Guardião elemental da terra, são mais rápidas que uma metralhadora.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} ficou todo furado igual uma peneira.\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    sys.exit()

elif escolha == '2':
    texto = (f'{personagem} defendeu o ataque do monstro usando seu escudo.\n')
    escrita_rpg(texto)
    texto = ('Vendo que seu ataque não surtiu efeito.\n')
    escrita_rpg(texto)
    texto = (f'O guardião elemental da terra materializou uma espada pontiaguda em seu braço direito,')
    escrita_rpg(texto)
    texto = (f' e correu com toda velocidade em direção a {personagem} para atacar.\n')
    escrita_rpg(texto)
    texto = (f'Essa é a sua chance! o guardião elemental da terra sedento de ódio, foi correndo igual um touro desenfreado para atacar você.\n\n\n')
    escrita_rpg(texto)
    print('='*182)
    print('\n')
    texto = (f'O que {personagem} vai fazer?\n\n')
    escrita_rpg(texto)
    texto = ('[1] Tentar desviar do ataque direto do monstro?\n')
    escrita_rpg(texto)
    texto = ('[2] Tentar defender com seu escudo o ataque direto do monstro?\n\n')
    escrita_rpg(texto)
    escolha = input('Digite 1 ou 2: ')
    print('\n')
    print('='*182)
    print('\n')

if escolha == '1':
    texto = (f'{personagem} teve agilidade o suficiente para conseguir desviar do ataque do guardião elemental da terra.\n')
    escrita_rpg(texto)
    texto = ('O monstro não conseguiu parar a tempo e caiu de cima da montanha tomando dano crítico.\n')
    escrita_rpg(texto)
    texto = (f'Parabéns {personagem}! Você conseguiu recuperar o fragmento elemental responsável pelo elemento terra da Pedra Elemental da Harmonia.\n')
    escrita_rpg(texto)
    texto = ('Agora só faltam mais 2 fragmentos para você salvar o mundo.\n\n\n')
    escrita_rpg(texto)
    print('='*182)

elif escolha == '2':
    texto = (f'{personagem} conseguiu defender o ataque do guardião elemental da terra.\n')
    escrita_rpg(texto)
    texto = (f'Mas o monstro continuou empurrando {personagem} até a beira do precipício da montanha.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} e o guardião elemental da terra caíram juntos da montanha.\n')
    escrita_rpg(texto)
    texto = ('A montanha tinha quase a mesma altura do monte everest ( 8.849 metros ).\n')
    escrita_rpg(texto)
    texto = (f'{personagem} e o guardião elemental da terra se arrebentaram no chão causando dano crítico.\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    sys.exit()

else:
    texto = ('Escolha uma das duas opções no seu teclado para prosseguir, numéro 1 ou número 2.\n')
    escrita_rpg(texto)
    texto = ('Rode o código do jogo novamente.\n\n')
    escrita_rpg(texto)
    sys.exit()
   
# Texto explicando sobre a falta de tempo e a continuação do jogo     

print('\n')
texto = ('Este jogo ainda está em fase de desenvolvimento.\n')
escrita_rpg(texto)
texto = ('Devido ao pouco tempo entre trabalho e faculdade, conseguimos concluir apenas 3 capítulos da história.\n')
escrita_rpg(texto)
texto = ('Para os próximos capítulos temos muitas idéias, como a implementação de um sistema de combate melhorado.\n')
escrita_rpg(texto)
texto = ('Com a adição de dados aleatórios, adição de um sistema de batalha tipo pedra, papel e tesoura, compilação do jogo em arquivo.exe, entre outros.\n')
escrita_rpg(texto)
texto = ('Mas isso demanda tempo de aprendizagem e tempo de programação, e infelizmente tempo é uma coisa que está bem difícil de conseguir.\n')
escrita_rpg(texto)
texto = ('Agradecemos pelos ensinamentos do professor João Coelho que estão sendo passados na turma B da Universidade de Vassouras de Saquarema.\n')
escrita_rpg(texto)
texto = ('Pois nunca tivemos contato com nenhuma linguagem de programação antes, estamos aprendendo bastante com as aulas do professor e também por fora com vídeos da internet.\n')
escrita_rpg(texto)
texto = (f'Obrigado por jogar nosso jogo {personagem}, até a próxima ^.^\n\n\n')
escrita_rpg(texto)
print('='*182)
time.sleep(5)
texto = ('''

-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++++++++++++++++-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++++++++++++++++++++++-+-++++++++++++++++++++++++++++++++++++++-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++++++++++++++++++-+#--++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++++++++++++++++---##+---++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++++++++####+++++++-#-+++##-----++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++-----+#+++++++-##+++-++++#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++++++-------+-+-###########-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++++++------#---++++-#####+#####-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++++----##+#####------####...####-+++++++++-+--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++++-+--#####++##+##-.-####---####--++++-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++++--##############-#--####...####-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++++--#++++++++++-+######+###########--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++-+-##############++++-----.------##-+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++--+-###############################--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++++.###########+########+##########-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++-+++-+-#####..+##-.-##+--##+##########--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++-++++++-#####-.-##---##+.-##+###+..####--+----++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++#-.############+##++-+#+###-..####--++##++++++++++++++++++++++++++++++++++++++++++++##+++++++++++++++++++++++++++++++++++++++++-
-++++++++++++++++++++++++++++++-#--####################+##########--+++++++++---+++++++++-++++++++++++++++++++++++++--+++++++++++++++++++++++++++++++++++++++++-
-+++++++++++++++++++++++++++++++#--#########.....#################+-+--+++++++##++++++++--+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
-++###+++++++++++--+++++####+++-#--#######-#-.---#####-###-#######+-++#-#+++++-+++++++++#+++++++++++++++++++++++++++++++++++++++++++++------+--------+++-++---+.
-#-------++++++++-#+---------++.#+-#+#####-#-.---#####+###-+-.-###+-++++#+##++-++++++++++-----+-----+++----------+++++++++++-+-+++--++--+--++-++++++++-----++++.
.-----+--+-++++++.######+##+--+.+--#-#####-#-...-##++#--##+##.+###+++++-+--..---------------+-------......+#+----+---------+++++++++++++++++++++++++++++-++++-+.
.---+++++----++++.#####+-++-#+#+####-########-##+####++-#+-...-..--++++++-########-#####.####.########+.########--++++++++++++-----++++++++++++++-+++++++++++++.
.++-----++--#++++-##+##-##.-###+#..------..---..#######-#+####...---.-+--+-###+.-+.-####.####+###+---####...-+###--+++++++++++++++++++++-+-++++++++++++-+++++--.
.--+-------+++++#-####+#.+..#..-#-++++++++++++-+--####+-####+#####-+..----.###--...-####.+#######.-+---#--+++.###--+-++++++++++++-++-+++-++++++++++++++-++-+--+.
.----+--+-++++++--###..-++#---+-#+++-+-------++--....--+#+######+-#####-+#########-.####.-###-###.--------++-.###.++++--------+-++++++++++++++++++-++-+++++++++.
.-#+--####+++++##+-.-+###+#-+---++---++--.-#+--##-#+-#+####+++#########--##+##++##..#+##..###+.###---++++++--###--++++++++++++-++--++-++++-+++-+++++++---+--+++.
-##-..-#-++++------+--..----+-#-+#.##-..###+#+-##.#+-###-+++++++++++##+-+##+##+#+.-.####..####.-####-.-+---.###.#-++++--+++++++###+++++++++++--++----++++++++++.
..---+-++++++-##.++++-##-+++--#.-#.+#+#+++..#-######+#+##++#++#####++#+####+##+#-.-.####..####----####---.###-..#---.-++---+-++--+++++--------++++-------+--+++.
-+++##-++++++.##.++-+--#.-....#.+##+#############################++#++---.++#######-+#########--#...-######-....#.---------------.--+++++-----++-++++##++##++++.
.---##.+-++--.##......-#-##################+---.------------------+#############+#+-.-######+--.#+++-++####+######-..#######+-######-+--#####+--+######.-------.
.#--#+...----.#######+---------------+++##########+++####-----##+++#.-#-.+-#######.####+.+###---######+...##########.#######+.######---###+##+--###+###+-++++++.
...###########################++++++-------------#########+#++#######---####+-####+#####.+###+--###-###.-.####-.####.####...-.###-###..###.###--###+-###--+++++.
.##+--------------------------+++++#################-+####---####+###-######--+###--####-+###+-+###.####-.####..####.+###--+-.###++##--###.###.-###+-###--+-+++.
.--++++#+########################+-+++++++------+###+....-######+-#+#-..####-.+###--####--###+-####-####--####--####.-#######-+###.##-.###-###.-###+.####.++++-.
-#######++++++-+++---+++++-+-+++-++++++++----++-+########+..-#+#+-###+--####---###+-####--####-####.-###-.########+---###+----+###.###-##+.###.-#########+-+++-.
.---++--+--------+-+++++-+++#+##################+++++#####+-##+##+####--####-#####+.####--####.##########.+###-.-###--####.----###.-##+##+.###.-###+..####-++++.
.####################-#####++++-+-+++-----.--+##-+-+---#+#+-##########+-####--#####-####-.####.####..####--####--####.########.###--#####+-###+-####--+###+-+++.
.+-+--+-----------++++++++++-+#+++++++++####+---####---###+-####---####-#####-+####-##########-####--+###+-####--####-+#######-###+--##+#---+++-+-++++++-++-+++.
.++++++++#-++------------.-------+-++##+-----++-+#########--####---####--##########--+#+++++++.##--+++---+-----++----++------+++-++++++++++++++++++++#++++#-+++.
.+-+++-++++########################-...-++++++++--++-----++++--++#++-+++++-----+--++###-###++++++-###+##-#+#+#-#++####+#+####+##-##-++++++++++++++++++++++#-+-+.
-########++-----.--+----..--+#-....-+#++++++---+-+++++++++++++++++++++++-#++##.##+#+###-#-+##+-##-#--+#--#######++######+++#####+##+++++++++++++++++++++++#++++.


                                               ***** Jogo Desenvolvido Por Paulo Sérgio e Rafael Farias *****
                                               Primeiro Período Turma B Universidade Vassouras Saquarema 2023  \n ''')


desenho_creditos_rpg(texto)
print('\n')
print('='*182)
print('\n')
sys.exit(0)













