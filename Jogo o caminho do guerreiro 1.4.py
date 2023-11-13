# Jogo de rpg em python
# Produzido por Sérgio e Rafael

# Módulos, pacotes e bibliotecas


import time
import sys
from random import randint
import pygame
#pygame.init()
#pygame.mixer.music.load('lost.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()


# Escrita dos textos e desenhos


def escrita_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.05)
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
menu_principal = int(input('\nEscolha uma opção: '))
print('\n')
print('='*69)


if menu_principal == 1:
  time.sleep(2)
  texto = '\nAbrindo o jogo...\n'
  escrita_rpg(texto)
  texto = 'Por favor aguarde...'
  escrita_rpg(texto)
  time.sleep(2)
  desenho_inicial_rpg
  print('\n')
  print('='*182)
  print('='*182)
  texto = '''\n
  
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
'''

elif menu_principal == 3:
  print('\n')
  texto = ('Obrigado por jogar nosso jogo.\n\n')
  escrita_rpg(texto)
  texto = ('Volte novamente quando quiser ^.^\n\n\n')
  escrita_rpg(texto)
  sys.exit()
  

elif menu_principal == 2:
  print('\n')
  texto = 'Abrindo créditos...\n'
  escrita_rpg(texto)
  texto = 'Por favor aguarde...\n'
  escrita_rpg(texto)
  time.sleep(2)
  print('\n')
  print('='*69)
  texto = '''
        
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


                                                      ***** Jogo Desenvolvido Por Sérgio e Rafael *****
                                                 ( Primeiro Período Universidade Vassouras Saquarema 2023 )\n '''
                                                    
  
desenho_creditos_rpg(texto)
print('\n')
time.sleep(2)
print('='*182)
print('='*182)
print('\n')
input('Aperte Enter para iniciar o jogo: ')  

# Nome do(a) personagem

time.sleep(2)
personagem = input('\nQual é o seu nome? ')
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
texto = (f'Um(a) destemido(a) aventureiro(a) chamado(a) {personagem}, foi convocado(a) por um antigo oráculo poderosíssimo chamado João Coelho,\npara recuperar as partes da Pedra Elemental da Harmonia e impedir que Sephiroth usasse seu poder para subjugar o mundo.\n')
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
texto = (f'Após uma breve caminhada, {personagem} ficou sabendo que o fragmento do elemento água está entre as ruas 96 e 13 do Reino de Jaconé.')
escrita_rpg(texto)
texto = ('Gostaria de cavalgar com seu cavalo pé de pano para a rua 96 ou para a rua 13? ')
print('\n')
texto = ('[1] Rua 96\n[2] Rua 13 ')
escrita_rpg(texto)
print('\n')
escolha = input('Para qual rua você deseja ir?\n\nDigite 1 ou 2: ')
print('\n')
print('='*182)
if escolha == '1':
  texto = ('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⣲⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠖⠋⢀⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠊⠀⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠁⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢸⠀⠀⠀⠀⢀⣀⣀⠤⠖⠈⠀⠀⢀⡜⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⠓⠲⢤⣸⠒⣊⣭⠛⠉⠀⠀⠀⠀⠀⢀⣠⢿⡶⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⣹⠎⠀⠀⠑⡄⠀⢀⡠⠔⢊⡥⢺⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⣾⠋⠁⣠⠞⠁⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⡠⠊⡜⠁⠀⠀⠀⢀⡊⠁⠁⠀⢊⡀⠀⠀⠀⣀⣉⣓⣦⡤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡤⠊⠁⠸⠀⠀⠀⡠⡖⡝⠀⠀⠀⠀⠀⠈⢉⡩⠭⠒⢋⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠑⠒⠛⠒⠋⠁⠀⠀⠀⠀⠀⠀⠘⠤⣀⡀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠜⠁⠀⠀⠀⠀⠀⠀⢀⣀⠤⠄⠀⠀⠀⡰⠚⢧⠉⠒⠒⠮⠽⣾⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠁⡠⣖⠂⠀⠀⠀⡠⠋⠉⠀⡀⠀⠀⢀⡴⠁⠀⠸⡄⠀⠀⠀⠀⡇⠙⢌⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠐⠁⣀⡠⠔⠋⣀⣀⡴⠚⠓⡶⣞⣉⣀⣀⡠⢤⠇⠀⠀⠀⢰⣃⡀⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⣀⣠⡊⠁⡀⣠⠞⠁⠀⠀⠀⡜⠁⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⣿⠀⠈⠑⢄⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣽⢻⡏⠁⠀⠀⠀⢀⠞⠑⠦⠤⠤⠤⠄⡸⠁⠀⠀⠀⢸⠉⣆⠀⠀⠘⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠀⠃⠀⠀⠀⢀⢏⠀⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⢸⠀⠘⡄⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠑⠦⠤⠤⠄⢲⠁⠀⠀⠀⠀⠀⠘⣆⣀⣹
\n''')
  
  desenho_inicial_rpg(texto)
  print('='*182)
  print('\n')
  texto = ('Você entrou na rua 96, foi em direção a praia e deu de cara com o guardião elemental da água, prepare-se para a batalha!\n')
  escrita_rpg(texto)
  texto = ('O guardião elemental da água saiu do mar, e com a calda longa dele, desferiu um ataque giratório em você.\n\n')
  escrita_rpg(texto)
  texto = ('O que você vai fazer?\n\n')
  escrita_rpg(texto)
  texto = ('[1] Pular o ataque do monstro?\n')
  escrita_rpg(texto)
  texto = ('[2] Abaixar do ataque do monstro?\n\n')
  escrita_rpg(texto)
  escolha = input('Digite 1 ou 2: ')
  print('\n')
  print('='*182)
  print('\n')

  if escolha == '1':
    texto = ('Seu pulo não foi alto o suficiente.\n')
    escrita_rpg(texto)
    texto = ('O guardião elemental da água é muito maior do que você.\n')
    escrita_rpg(texto)
    texto = ('O ataque de calda longa giratória do monstro te pegou em cheio causando dano crítico.\n')
    escrita_rpg(texto)
    texto = ('Você foi cortado ao meio!\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    sys.exit()
  
  elif escolha == '2':
    texto = ('Ufa, essa foi por pouco!\n')
    escrita_rpg(texto)
    texto = ('Você conseguiu abaixar desviando do ataque do monstro,\n')
    escrita_rpg(texto)
    texto = ('e ao mesmo tempo conseguiu uma brecha para atacar.\n\n')
    escrita_rpg(texto)
    texto = ('O que você vai fazer?\n\n')
    escrita_rpg(texto)
    texto = ('[1] Aproveitar que o monstro está de costas e atacar?\n' )
    escrita_rpg(texto)
    texto = ('[2] Esperar uma melhor oportunidade de ataque?\n\n' )
    escrita_rpg(texto)
    
    
  escolha = input('Digite 1 ou 2: ') 
  if escolha == '1':
    print('\n')
    print('='*182)
    texto = ('\nVocê aproveitou a oportunidade e atacou o monstro de costas.\n')
    escrita_rpg(texto)
    texto = ('O monstro tomou dano crítico e foi vencido!\n')
    escrita_rpg(texto)
    texto = ('Parabéns! Você conseguiu recuperar o fragmento da água da Pedra Elemental da Harmonia.\n')
    escrita_rpg(texto)
    texto = ('Agora só faltam mais 3 fragmentos para você salvar o mundo!\n\n')
    escrita_rpg(texto)
    print('='*182)
    print('\n')
    

  elif escolha == '2':
    print('='*197)
    texto = (f'\n{personagem} esperou o monstro se recuperar do ataque dele.\n')
    escrita_rpg(texto)
    texto = ('O guardião elemental da água pulou novamente no mar.\n')
    escrita_rpg(texto)
    texto = ('Ele foi para o meio do oceano e concentrou todo o seu poder lançando uma onda tsunami contra você.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} foi varrido do mapa, junto com todos os habitantes do Reino de Jaconé!\n\n')
    escrita_rpg(texto)
    texto = ('Fim de Jogo.\n')
    escrita_rpg(texto)
    print('\n')
    print('='*182)
    print('\n')
    
  
  else:
    print('\nEscolha uma das duas opções no seu teclado para prosseguir, número 1 ou número 2. ')   

elif escolha == '2':
  texto = (f'\n{personagem} ficou igual uma barata tonta, cavalgando na rua 13 em circulos com seu cavalo pé de pano durante muito tempo,\n')
  escrita_rpg(texto)
  texto = ('e não conseguiu encontrar o fragmento do elemento água da Pedra Elemental da Hamornia.\n\n' )
  escrita_rpg(texto)
  texto = ('\nFim de jogo.\n\n')
  escrita_rpg(texto)
  sys.exit()

else:
  texto = ('\nEscolha uma das duas opções no seu teclado para prosseguir, numéro 1 ou número 2. ')
  escrita_rpg(texto)