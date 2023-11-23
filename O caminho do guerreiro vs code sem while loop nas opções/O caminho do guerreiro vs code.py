# Este jogo de rpg foi feito na ide visual studio code (VS CODE).
# Jogo Produzido por Paulo Sérgio e Rafael Farias primeiro período turma B Universidade de Vassouras Saquarema Novembro de 2023.

# Mini tutorial para executar esse jogo com som no vs code:

# Para jogar o jogo com som, instale a biblioteca pygame.
# Com o python já instalado na máquina, vá no cmd do windows e digite o comando pip install pygame.
# Volte no VS CODE e execute o jogo, caso dê erro no pygame outra vez, aperte o atalho ctrl+shift+p no VS CODE.
# Após o comando do atalho, digite na busca do VS CODE, select interpreter. 
# Em select interpreter, selecione sua versão do python 3.11 64bit (Microsoft Store).
# Caso não tenha o interpretador python da microsoft store instalado na máquina.
# Aperte ctrl+shift+x e digite python nas buscas de extensões do VS CODE para instalar.
# No interpretador python global, naõ sei porque, mas a biblioteca pygame não funciona de jeito nenhum.
# Tanto nos computadores da faculdade, quanto em casa.
# Mas com a forma que está explicada nesse mini tutorial, vai funcionar em qualquer pc.
# Bom jogo e bons estudos de códigos ^.^   

# bibliotecas

import time
import sys
import pygame

# Música Inicial

pygame.init()
pygame.mixer.music.load('Wolrd map.mp3')
pygame.mixer.music.play(-1)
 
# Escrita aparecendo no jogo

def escrita_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.00)

# Desenho do Guerreiro no título

def desenho_inicial_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.000)

# Desenho da Igreja de Saquarema dos créditos

def desenho_creditos_rpg(texto):
  for letra in texto:
    sys.stdout.write(letra)
    sys.stdout.flush()
    time.sleep(0.003)

# Desenho do guardião elemental da água

def desenho_monstro1(texto):
   for letra in texto:
      sys.stdout.write(letra)
      sys.stdout.flush()
      time.sleep(0.002)

# Desenho do guardião elemental da terra

def desenho_monstro2(texto):
   for letra in texto:
      sys.stdout.write(letra)
      sys.stdout.flush()
      time.sleep(0.002)          

# Desenho final da igreja de Saquarema com outra variação de tempo

def desenho_final(texto):
   for letra in texto:
      sys.stdout.write(letra)
      sys.stdout.flush()
      time.sleep(0.005)    


# Menu principal, créditos e sair do jogo


print('='*69)
print('''       
  __  __                    _____      _            _             _ 
 |  \/  |                  |  __ \    (_)          (_)           | |
 | \  / | ___ _ __  _   _  | |__) | __ _ _ __   ___ _ _ __   __ _| |
 | |\/| |/ _ \ '_ \| | | | |  ___/ '__| | '_ \ / __| | '_ \ / _` | |
 | |  | |  __/ | | | |_| | | |   | |  | | | | | (__| | |_) | (_| | |
 |_|  |_|\___|_| |_|\__,_| |_|   |_|  |_|_| |_|\___|_| .__/ \__,_|_|
                                                     | |            
                                                     |_|            ''')                        
print('                         [1] Iniciar Jogo  ')                              
print('                         [2] Abrir Créditos')
print('                         [3] Sair  \n')
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
                                                                                     .::...                                  
                                                                                    :$&&$X;.                                 
                                                                                   ..Xx+x+x.                                 
                                                                                   ..x+xx+x..                                
                                                                                    .+XxXX+Xx:.                              
                                                                                   ::XxXX&&&x;;:.                            
                                                                                 .+$xx;;x&&x;;.....                          
                                                                               .:++Xx+xxXxx++++++;:..                        
                                                                             ..+xx+X$X++;;XxxXXxx+x;:.                       
                                                                             .;x$;+x+;;:;++$&&Xxxxx$;.                       
                                                                           .+X$&x+;+++xxx+X&&$xxx+x$;.  ..:.                
                                                                           +:&&&XXxxxXxxxxX$&&&&&&&$x.;xXX+.                
                                                                           .;$&&&$XxxxXxxX$$$&$$$XXx+++;xxX+;.               
                                                                           :$X&&&&xx+xXx&$$&$&+;x;:;xx;.:xX++.               
                                                                           ;xxxX$XxxXxX&&&&&x+$X;+++::..::+:::.              
                                                                          .;xxxxX$X$$$$XxxXx$&$x;++;::...:..::.              
                                                                         .:xxXxX$&&$$$+x;++;X&&+;+;;;;:.:+..;..              
                                                                        .+XXXXx$$&&$X$++:;;;$&x;x;;;;+++;;:.:.               
                                                                      ...+X$&X$$&X$&&$X+;;++$X+;+;;+xxxXXx::.                
                                                                   .+::x+X&$&$$&$$&$&$$X+++$$X++;;;;;+++X;;:.                
                                                                  .:..;$&$x$&x;Xx$$$$$$&$$$$$X;+;;;;;;;x:;;.                 
                                                                  ..:..X$$$$XxXXxx$$$$X$$$$$X$;+;;;;;;x:.:.                  
                                                                  ...:xXXX:..+:xxx+X&$+.;+xxx$;+;;;;;;...:                   
                                                                  .;Xx$X+;x:..:XXXX$&$:.:+XXXX++;;;;++..:.                   
                                                                 .;xX$xx::    .;;;+X$$x..x;+;$++;;;;+..:.                    
                                                                .:xX$X+.      .;XxxX$$X+.x+xx$++;;;;..:.                     
                                                              .:+xXXx:         .+Xxxx$&X. ;x$X++;;;:::.                      
                                                              ..XXX+..          .x$&&&&$.  xX$xx++:;:.                       
                                                            .;xX$;..             .;X&&$X.  .X$$xXx+:.                        
                                                           .:xXXXx:                $$$$x.   +$$$$x.                          
                                                          .:xXx;.                 .$$&$x.   .X&XXx.                          
                                                         ..:x$x:.                 .X&$XXx   :X&$$+.                          
                                                        .;xX+.                 .;&$$&$$X:   :$&$$x.                          
                                                      ..+xx:.                .;xX$$X;;;;;   +$$X$X:                          
                                                      .+x;.                                 x$$$$X;                          
                                                     .:;..                                  +x;xX+;                           
                                                    .:.                                             ''')
 

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
                                               Primeiro Período Turma B Universidade Vassouras Saquarema 2023
                                                             ***** Professor João Coelho *****
                                                          https://github.com/jogosdesergioerafael  \n ''')


elif menu_principal == '3':
  print('\n')
  texto = ('Obrigado por jogar nosso jogo.\n')
  escrita_rpg(texto)
  texto = ('Volte novamente quando quiser ^.^\n\n\n')
  escrita_rpg(texto)
  time.sleep(4)
  sys.exit()

else:
  texto = ('\nDigite uma das três opções no seu teclado para prosseguir.\n')
  escrita_rpg(texto)
  texto = ('Numéro 1, número 2 ou número 3.\n')
  escrita_rpg(texto)
  texto = ('Rode o código do jogo novamente.\n\n')
  escrita_rpg(texto)
  time.sleep(8)
  sys.exit()

desenho_creditos_rpg(texto)
print('\n')
print('='*182)
time.sleep(2)


# Nome do(a) personagem


personagem = input('\nDigite o seu nome e aperte a tecla enter: ')
time.sleep(2)
texto = (f'Olá {personagem}, seja muito bem vindo(a) ao jogo caminho do guerreiro. \n')
escrita_rpg(texto)
texto = ('Vamos juntos encarar uma grande aventura!')
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
texto = ('Há muito tempo, em um mundo mágico e misterioso, existia uma pedra elemental poderosa que possuía o controle sobre os quatro elementos fundamentais: água, fogo, terra e ar.\n')
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


texto = ('Capítulo 2: O guardião elemental da água.')
escrita_rpg(texto)
print('\n')
time.sleep(0)
texto = (f'{personagem} está cavalgando na rua com seu cavalo pé de pano, e ouviu boatos de que o primeiro fragmento da Pedra Elemental da Harmonia,\n')
escrita_rpg(texto)
texto = ('responsável pelo poder do elemento água, está escondido no Reino de Jaconé que fica à beira-mar.\n')
escrita_rpg(texto)
texto = ('O guardião elemental da água é conhecido por sua habilidade em manipular os oceanos e agilidade dentro dágua.\n')
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
  pygame.mixer.music.load('The last encounter.mp3')
  pygame.mixer.music.play(-1)
  texto = ('''                                                               
          ............................................................
          .... ............ ..... ........xx:..x.++....+....+x......::          
                         ..    ....:;;+++;;Xx++xxx+:.;X...xx;+Xx+:...           
           .... ... . ....;++;+Xxx;.:++:;X+;xXX+XX+xXX:.+;::XxXX:.....          
          .... ..   .   .........:+:x;:.XxX;XXX$;:;XXxXx+x;xxx$$$;....          
                      .     ..xx+;X;X;++X++X$$XX;:;;+x+;$Xx++++$Xx;::.          
          .  ..  ....       ....:;+++;+x+xX$:X+:++xXX::x+X&&xxxX$$XX:.          
            ..           .. ..:;+:+$x+xxXX$x;+$+++x++X+;+;$XX+X$xx+:..          
                      .    .x++:+$&$XX$X$XX$xx;+;++;;++x;+$Xxx+;;+....          
                        ..xxx+.;$XXX;$$x$;;$&+:.;++x$$+X$&xxx++.+:.             
          .  .. ..    ...+..+;;$Xx;xx;:x+Xx;$&x$XX$$$$+xX+;;;+....   .          
          ...     .   .....x;+$XXx$:;;:x:XX$;x&X$XXXXXxX..:.....                
          . ..        ...+x+x$X$;X;.;++xX.x:.:.+X+xx;xX&::.          .          
          .....   ... .;+;;;xXX;x+;;;;+x...:..::;X:;+xX+:.. ..  .               
           ..     . . :Xx::;X$Xxx:;++xx+.  .   ..$+:;x++.           .           
          ...    .....;.;;Xx$+xXx::;;;x:.       .::;++&x.                       
           ........ ...:+;xX$$+;x;;;++x:.        ..;++..             .          
          ....... ... .:x.:X$$XXX+;+;++x.       ...:;+. ...  ... ...            
                   .. .x+;;X$XxXxX;:;++X.          .:...             .          
          ....... ....x::;:+$X;x;x+:::+xx..     .. ....  .                      
          .     ..  ..+.:x::xxX+XxXx.:;;x+..                                    
          ...     .  ...++;;;&XXXxXxx:.:+xx..                   .    .          
          ........   ...+.+++x$$$$xXxxx:+;+x;.                   .              
          ..... ... . ..:.:++;$$xxx++;$+;:;++x.....     ..           .          
                         ..X++;X$$XX+++xX+;;+++x;..      ..                     
           ..            ..X:+:x+&XX+x$$:xx+::;+xx+..       .                   
          ....... . .......:.x:;:.$$$XxXx+;xX+::;;;xx;...                       
          .... .. ... ..... .$++.::;X&$Xx++XXX++:.::;xxx..           .          
           ...xXX+$XX++;:....X;x;..::;&&$$::x+X+XX+.:.:+xx..                    
          ..++;x$+XxxX$$$+x.;+.xx;+x:;+:x&Xxx++++X++;::::+++..  ..              
          ..xxXx++X;;+xxX&x:;;::$x:x+:;;xXX&$$$:+Xx;+++.:.:++.       .          
          .+;$X::::+$++Xx&&;+;X.+x. .+:;.x;X&XXXXx$$+x:x.::::+...    .          
          ;+$x:;+;.;+++++xX&++x..+....+;:;;;xX&$$$xxxxx+++.::;+.                
          :+$;:;..  .xxxX;X&$.+:;.:...:X..:++:x&XXXxX:X$xx;:::+..               
          ;xX;;X..  .+X+;:Xx$::+x..   .+:..:X.;X&&$+:++;$x:+:;;:                
          x;X;+x..  ..$X$+x$XX:+x.x..  .;:..x:.X&&$$xxxX$+x$;:;;.               
          :+xx;X..  ..$X+x;XX&;;x.x.    .....+;:X&$Xx$xx+$$$$:;+.               
          .;xX;+;++...$X$$;;X$$x+xx.....:...x+::x$XXXxxx+:+$&;:+.. .            
          .++:x+x++;;:XX;;xxXX$&x+xx.:;..x;....:$$$$$xXx+X$XxX:+.    .          
          .X..+X;++x$$$&$X+;++X$&;++;.x...;x...X&$$X+$XXX+X+x$;..               
          :+.++XX+;+;;$&$x+xXX+xx$x:+x:X..::xxxX$X$X+++xx:+x$&X.                
          ...x+;XXx++xxX&$+++;:$$$&&Xx+XxX+;x;$$$$X$&$;++$Xx$X..                
          ...+XXX++x$x$$$&&$xxX+xxxX$$$&XXX&&$Xxx$XX$$$$X+++X.  .               
           ...+;XX+X++$$$&&$$X+x+X+xX$$X$X+XX$X+XxxxX;:xx;;X:.                  
          .......xxx;+xX$$$$$$++$xx+:;+XX+$$$+x$Xx+;+;+++:$..    .              
          .     ..Xxxx+$&$..;$xxXxX+;$x++;;+X$+;$Xxx+xXXx:.     .               
           ..     X+x:X$&x.  .:$&$$XxX++:XX+xXXxx;x+xXx....   ..                
          ........Xx+XX&X.. . ....X&&$&&$$$$&$x+$&&$:...                        
          ...   ..xXx:$&..  .     ....:+XXX$$Xx;....     ..                     
          ... .. .:XXxXx... .          .....      ..    ..  ...                 
                   ++;xx.                  .      ..................            
          ..........+XX$... .     ...  .   . . ....................  .          
           ... .......X$+..       ..           .    ...  ..                     
          ............................................................ 
\n\n\n''')
  
  desenho_monstro1(texto)
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
   pygame.mixer.music.load('Game over.mp3')
   pygame.mixer.music.play()
   texto = (f'\n{personagem} ficou igual uma barata tonta, cavalgando na rua 13 em circulos com seu cavalo pé de pano durante muito tempo,\n')
   escrita_rpg(texto)
   texto = ('e não conseguiu encontrar o fragmento responsável pelo elemento água da Pedra Elemental da Hamornia.\n\n' )
   escrita_rpg(texto)
   texto = ('\nFim de jogo.\n\n')
   escrita_rpg(texto)
   time.sleep(13)
   sys.exit()
   
   

if escolha == '1': 
    pygame.mixer.music.load('Game over.mp3')
    pygame.mixer.music.play() 
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
    time.sleep(13)
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
    pygame.mixer.music.load('Game over.mp3')
    pygame.mixer.music.play()
    texto = (f'\n{personagem} esperou o monstro se recuperar do ataque dele.\n')
    escrita_rpg(texto)
    texto = ('O guardião elemental da água pulou novamente no mar.\n')
    escrita_rpg(texto)
    texto = ('Ele foi para o meio do oceano e concentrou todo o seu poder lançando uma onda tsunami contra você.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} foi varrido(a) do mapa, junto com todos os habitantes do Reino de Jaconé!\n\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    time.sleep(13)
    sys.exit()
    
     

else:
    texto = ('\nEscolha uma das duas opções no seu teclado para prosseguir, numéro 1 ou número 2.\n')
    escrita_rpg(texto)
    texto = ('Rode o código do jogo novamente.\n\n')
    escrita_rpg(texto)
    time.sleep(8)
    sys.exit()


# Capítulo 3

pygame.init()
pygame.mixer.music.load('Wolrd map.mp3')
pygame.mixer.music.play(-1)

texto = ('Capítulo 3: O guardião elemental da terra.')
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
texto = ('[2] Deixar seu cavalo pé de pano em um local seguro e escalar a montanha sozinho(a)?\n\n')
escrita_rpg(texto)
escolha = input('Digite 1 ou 2: ')
print('\n')
print('='*182)


if escolha == '1':
    print('\n')
    pygame.mixer.music.load('Game over.mp3')
    pygame.mixer.music.play()
    texto = (f'{personagem} tentou escalar a montanha montado em seu cavalo pé de pano.\n')
    escrita_rpg(texto)
    texto = ('Ao chegar numa altura considerável, pé de pano pisou em falso e tropeçou numa rocha.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} e pé de pano se arrebentaram no chão causando dano crítico.\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    time.sleep(13)
    sys.exit()
    



elif escolha == '2':
  pygame.init()
  pygame.mixer.music.load('Battle theme A.mp3')
  pygame.mixer.music.play(-1)
  texto = ('''
         
          ....................................................................................................          
          ....................................................................................................          
          .....................................:::;++;;;;++x++++;+X+;::.......................................          
          .................................::;+;;::;+Xx+;:;;+x++;+++++x+xx;...................................          
          ..............................:;:;++++xxx+;;+++;++xxx+;;+++++;;;xx+;................................          
          ...........................:x;;;x;;xXx+++x++++xxx+++X$xxxxxXX+x+xxx+x+..............................          
          ..........................;+xxxx+:;+++xxx+xx+;;;xx++xXxxXxXxxxXXx+xXxXx:............................          
          ........................:;;;;;;+xx+xXx;;+xx+;+xX$$XXXXXxXxxxXX$$xX$$XXXxX;..........................          
          ......................:;++x+;;;+++xX+xxx+xxxXXX$$$$$$$XxXxXXx++;:;XXXXXXXx+:........................          
          .....................:xxxxxxxx+;;+xXX$$Xxxx$$$XX$$$$$$$$$$$$Xx+++xX$$$x+X+Xx+.......................          
          ....................:;+;x$x;+XxxxxX$xxxxxXXX$$$$$$XxX$$&&&&&x+$xxXX$$$XxXXx++X;.....................          
          ...................;+;;;+xXXX$XXXXXXXxxxXXX$$XX$$XXXxx$$$$$XxxxX$$$$$XxxXX++XX++:...................          
          ................::;;+X$x++x$$$XXXX$$$XX$$$$X$$$$XXxxxXXX$&&$&&$$$&&&&&XxXXxxX$Xx:...................          
          .............:;++++x+++xXXxxXxxxX$$$$$&$$$$$$&$XXXX$$XXX$$$$$X$$$&&$X$$XXXXX$$Xx....................          
          .............+xxXx++++xxxxxxXXXXX$$$$$&&&&&$$$$$$$$$$$&$$$XX$$$&&&$$$$$$$$X$$$X.....................          
          ............;;;;;;;;+x+;;+xx+x$$$$XxX$&$$&&&&$$$$$$$&&&&&$$$$$XX&&$$$$$$$&$$$$X:....................          
          ............;;;;+xXx+xx;;++xXXX+......X&$$$$$$$$$$&&&$$$$$$$$X..&$$$$$$$X$$$$$$$X;..................          
          ............;;xx+;;;+xx++xx++xXx......:$$$&$$$$$$$$XXXX$XX$X+....;$$$$$$&&&&$$$$$Xx;................          
          ............xxXX+++++++++xxxXxxxX:....;$$$$$$$$$$X$$$Xxx$$$x.......:X&&&&$$$XXXx;;;++:..............          
          ............;++$++++x++++xxxxxxxXx.....$$$&&$$$$Xx$XX$$$$$$x.........+$&&$$X+++X+xxxXX;.............          
          ............;++xX+++xxxxxxxx$$xX$XX:...+$$$$$XX+xXXXXxX$XX$$.........+&$$&$$$$x+x+++xx;.............          
          .............+++XXx+:;++x+++xxXXx$X+....X&$XXXXXxXxXXX$XX$$+........:XXxX$$$$$X+xxx++xx:............          
          .............:+x+x+++++xxx+++xXXXXX+...Xx+++$&&$x$$xx+XXXX$X.........;xxx$$$$XxxXXxxxxX+............          
          ..............;x++XxxXxx+XX$$XxXXX$+..x$X++Xx+xX&&&xxX$$$XX$x.........+xX$x$$+;;;x+++xX+............          
          ...............+xx+++++x+xx++xxXXXX:.;$$$xxx++xxX$$&&&$x++xxx;.........x+++xX++x+xX++XX+............          
          ................;xXxx+x+++xXXxxxXX+..+$$$$++++xxX.;&$XXx++x++x+........;x+++x+++Xx+xXXX;............          
          ..................:+xx+xxxxXxxxxxXX+.:$$$$x++xxx;..x$XX$$X++++x+.......:xxX$$xxxxxxxxXx:............          
          ....................+xXXXx+++xxxXxX$x::X$$x+xxx+...:X$XXxxXXx;+x:.......xx+X&x++xXXXXX;.............          
          .....................;Xxxx++xxxxX$$&$;..:$&&$$x:......:xxxx$XxXX;......+XxX$$xxxXxxxX;..............          
          .......................++XXxXxXXxxXx..x$$$xxxX+.........:xX&&x++;.....:x$x+;++xxXXXX................          
          ........................;X$XXxX$;...:X&$$XXxXXx........xxxXxxxxX+........xXX$$XX$&$;................          
          ...................................:X$$$$$XX$X;......:x++xXXX$XX:..........:xXXXX...................          
          ...................................;$$$$$$$$$x........XXXxX$$$x.....................................          
          ...................................+$$$$$$$$+.........;$$XxxxX;.....................................          
          ...................................+$$&$$$$$;.........:xxx++xX+.....................................          
          ...................................x$$&$$$$$$X:.......+xxxxx;;+x:...................................          
          ..................................:$&&$$&$$$$$X.......XXxxxXx+xxXXX.................................          
          ....................................................................................................          
          ....................................................................................................          
           
\n''')
  
desenho_monstro2(texto)
print('='*182)
print('\n')
texto = (f'{personagem} deixou seu amigo e fiél escudeiro pé de pano em um local seguro, e foi sozinho(a) escalar a montanha.\n')
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
    pygame.mixer.music.load('Game over.mp3')
    pygame.mixer.music.play()
    texto = (f'{personagem} tentou desviar do ataque do monstro, mas sua velocidade não foi rápida o suficiênte.\n')
    escrita_rpg(texto)
    texto = ('As pedras pontiagudas cortantes lançadas pelo Guardião elemental da terra, são mais rápidas que uma metralhadora.\n')
    escrita_rpg(texto)
    texto = (f'{personagem} ficou todo furado igual uma peneira.\n')
    escrita_rpg(texto)
    texto = ('\nFim de jogo.\n\n')
    escrita_rpg(texto)
    time.sleep(13)
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
    pygame.mixer.music.load('Game over.mp3')
    pygame.mixer.music.play()
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
    time.sleep(13)
    sys.exit()

else:
    texto = ('Escolha uma das duas opções no seu teclado para prosseguir, numéro 1 ou número 2.\n')
    escrita_rpg(texto)
    texto = ('Rode o código do jogo novamente.\n\n')
    escrita_rpg(texto)
    time.sleep(8)
    sys.exit()
   

# Texto explicando sobre a falta de tempo e a continuação do jogo     

pygame.init()
pygame.mixer.music.load('Lofi hip hop.mp3')
pygame.mixer.music.play()

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
texto = ('Pois nunca tivemos contato com nenhuma linguagem de programação antes, estamos aprendendo bastante com as aulas de python do professor e também por fora com vídeos da internet.\n')
escrita_rpg(texto)
texto = (f'Obrigado por jogar nosso jogo {personagem}, até a próxima ^.^\n\n\n')
escrita_rpg(texto)
print('='*182)
time.sleep(2)
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
                                               Primeiro Período Turma B Universidade Vassouras Saquarema 2023
                                                             ***** Professor João Coelho *****
                                                          https://github.com/jogosdesergioerafael  \n ''')
                                                                

desenho_final(texto)
print('\n')
print('='*182)
time.sleep(35)
sys.exit()












