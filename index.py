# Jogo feito por Alexandre, Guilherme Trevisan, Vinicius Lima e Giovani Canella

import sys, time, random
from os import system


def slow_type(t, tempo):
  typing_speed = tempo
  for l in t:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(random.random() * 10.0 / typing_speed)
  print('')


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\  -  Biblioteca  - \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def ola():
  slow_type('\nOlá, seja bem vindo ao Real Nightmares!'
            '', 100)
  input('\n  (Aperte "Enter" para continuar)')


def intro():
  ola()
  system('clear')
  print(''' \nAinda me lembro daquela maldita noite... 

Eu me levantei com outra ressaca naquele apartamento escuro e claustrofóbico.
Não esperava que depois de tanto tempo tivesse que trabalhar denovo..
Pra ser sincera, nem devia chamar aquilo  de "trabalho". Mas de qualquer forma,
precisava ter algo pra distrair minha mente, algo além dos remédios...


    MERDA, ESTE TELEFONE NÃO PARA DE TOCAR!\n\n''')

  ligacao = input('''
  1. Atender a Ligação;
  2. Desligar a Ligação;\n\n''')
  if ligacao == "1":
    inicio1()
  elif ligacao == "2":
    inicio2()
  else:
    intro()


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ -  Intro  - \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


def inicio1():

  system('clear')

  print('''\nAtendo a droga do telefone, uma voz de criança me responde
        
"Lá fora é onde o sol brilha,
Mas dentro de casa é onde tudo começa,
De quarto em quarto você não encontrará o que procura,
Busque!, Busque!, Busque a beça!. 

*Telefone desliga*

Você ignora a ligação estranha. descendo pra sua sala, o clima pesado te atinge, de corpo frio, Você Sabe pelo cheiro podre que escapa pela porta aberta; pelo zumbido das moscas no corredor abafado e quente, e, se aquilo já não fosse indício suficiente de que havia algo errado na casa, errado do pior modo possível, o silêncio confirmava. Você descobre um corpo em cima da mesa. Você entra em desespero e não sabe o que fazer.\n\n'''
        )

  corpo = input("""
  1. Se acalmar e decidir o que fazer;
  2. Se livrar do corpo;\n\n""")

  if corpo == '1':
    se_acalmar()
  elif corpo == '2':
    se_livrar()
  else:
    inicio1()


def se_acalmar():
  system('clear')
  print('''
Você decide revistar o corpo e acha os pertences da vítima.
  
  - O nome da vítima é Ethan Thorn;
  - Nasceu em: 27/08/1995 (22 anos);
  - Estudante de Pedagogia;

Aparentemente o destino não foi muito justo com ele.
  
Como melhorar opção você decidiu antes de enterrar o corpo, desblo;quear o celular e limpar a sala\n\n'''
        )
  vida_v = input('''
  1. Encontrar informações sobre a vida da vítima;
  2. Usar o celular da vitima;\n\n''')
  if vida_v == '1':
    basica_v()
  elif vida_v == '2':
    descobre_p()
  else:
    se_acalmar()


def pub():
  print('''\n  
  Você faz umas perguntas ao barman que não se lembra de
muita coisa, logo em seguida você decide revistar as câmeras ao redor das ruas.

"Após gastar umas boas horas pra acessar a droga do histórico daquelas malditas câmeras, pude ver dois bêbados idiotas voltando pra casa. deu pra ver o Ethan sozinho dobrando a esquina, provavelmente era a casa dele. Pude ve-lo entrar, e pouco tempo depois alguém quebrando as câmeras. Não vi mais nada...não sei oque fazer..."    \n\n'''
        )
  after_pub = input(''' 1. Invadir casa da vitima
 2. Procurar ajuda\n\n''')
  if after_pub == '1':
    invasao()
  elif after_pub == '2':
    serch_help()
  else:
    pub()


def descobre_p():
  system('clear')
  print(
    '''\nCom as informações que você consegue, você descobre o pub que a vitima frequentou noite passada e vai analisar o local.'''
  )
  pub()

  # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

  # O pub e o descobre_p são um def em conjunto, usado para mais de uma linha do tempo poder acessa-lo de uma forma que mantenha o sentido

  # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

  after_pub2 = input('''\n 1. Invadir casa da vitima
 2. Procurar ajuda\n\n''')

  if after_pub2 == '1':
    invasao()
  elif after_pub2 == '2':
    serch_help()
  else:
    pub()


def basica_v():
  system('clear')
  print(
    '''\nVocê consegue descobrir sobre os amigos de Ethan, onde ele nasceu, onde mora e etc.
  
Durante a sua busca por informações você descobre sobre um pub frequentado por Ethan e também o local de sua casa\n\n'''
  )

  casa_pub = input('''
  1. Ir até a casa de Ethan
  2. Ir até o pub\n\n''')
  if casa_pub == '1':
    ir_casa()
  elif casa_pub == '2':
    ir_pub()
  else:
    basica_v()


def serch_help():
  system('clear')
  print('''\nVocê liga pra um velho amigo de trabalho\n''')
  time.sleep(1.5)
  system('clear')
  input('''\n-- "STEPHAN, PRECISO DA SUA AJUDA!!"

-- "Beck? Está tudo bem, o que foi?"

--  "Stephan, eu sei que parece loucura, e é até dificil explicar, mas eu estou envolvida num assasinato que não cometi"

--  "Que tipo de ligação é essa Beck, é uma pegadinha?"

--  "NÃO STEPHAN! Estou falando sério, apareceu um corpo em minha casa, e eu não sei como ele foi parar lá, eu PRECISO da sua ajuda!"

-- "Não, não, obrigado, eu não posso me meter nesse tipo de sujeira.."

-- "STEPHAN, isso é sério! eu IMPLORO! Me ajude!"

-- "Beck, eu posso ser DEMITIDO!"

-- "E EU POSSO SER PRESA STEPHAN! quer mesmo competir em quem está mais fodido aqui?!"

-- "tá bem, onde voce está?"

-- "eu to na pollons path, perto de um pub"

-- "tudo bem, eu não demoro." 


(clique enter para continuar)''')

  system('clear')

  print(
    ''' Eu fiquei esperando por Stephan perto do pub, tentando controlar minha respiração acelerada. Quando o vi se aproximando com o carro, senti um alívio misturado com medo. Ele desceu do carro e correu em minha direção.

conversamos, e ele acreditou em tudo que eu havia dito, mas ficou muito puto com o fato de eu ter enterrado o corpo antes de pedir sua ajuda. Stephan dispos seus ultimos restos de vontade e decidiu me ajudar. decidimos que stephan poderia me ajudar abrindo um caso de desaparecimento, porém incubrindo o fato que EU tinha enterrado o corpo, o plano era "magicamente" achar ele depois, a 7 palmos do chão. '''
  )
  print(
    '''\n Sthepan e eu decidimos que talvez de pra tirar alguma coisa de Will.'''
  )
  input(
    '''\nCheguei na casa de William com um sentimento sombrio e pesado no peito. Conheço bem o meu trabalho e sabia que teria que mentir para conseguir as informações necessárias. Stephan me acompanhou e alertou William sobre o desaparecimento do nosso suposto amigo Ethan - uma mentira descarada.'''
  )
  system('clear')
  input(
    '''\n  Will sente um calafrio percorrer sua espinha diante do súbito "sumiço" de Ethan. Ele diz que não sabe de muita coisa, diz que só beberam demais noite passada, mas comenta sobre um clube?, eles chamam de clube do ouro, um lugar pouco conhecido...'''
  )


def invasao():
  system('clear')
  input('''
  Decido esperar o cair noite, e invadir a casa de Ethan em busca de algo que me traga esperança. Lá dentro, não encontro nenhum sinal de briga, supondo que foi um ataque surpresa. Olho tudo, atrás dos quadros, atrás das paredes. Reviro a casa por horas. Finalmente encontro uma pequena caixa com fotos atrás de uma estante de livros.

Nesse momento, minha reação é inexpressavel, 
uma mistura de nojo, desprezo e enjoo. 
Geralmente não se espera que o tipo de pessoa ''normal''
como o Ethan, guarde coisas assim.


A caixa continha fotos de crianças.

Sou uma detetive a muitos anos... Não preciso pensar 
muito pra saber do que se trata.
\n\n''')
  system('clear')
  slow_type(
    '''\nVocê recebe uma mensagem: "Ele não merecia continuar nesse mundo"
 ''', 95)
  time.sleep(2)
  slow_type('''\n(Você está ficando insana...)''', 49)
  time.sleep(3)
  trecofds = input('''
  1. Continuar procurando
  2. Responder \n\n''')

  if trecofds == '1':
    continua_busca()
  elif trecofds == '2':
    system('clear')
    print('''\n\n   "Você não escolhe quem deve ou não viver."''')
    time.sleep(2.2)
    print('''\n\n   ... sem resposta.   ''')
    time.sleep(2)
    continua_busca()
  else:
    invasao()


def no_escape():
  input(
    '''\n\n"não tenho mais armas, a usar, só quero acabar com isso logo..." '''
  )
  brandon_death()


def brandon_death():
  system('clear')
  input('''\n\nVocê invade a casa de brandon no cair da noite.

Você o apaga e o amarra na cadeira da cozinha

- 𝖁𝖔𝖈𝖊̂ 𝖊𝖘𝖙𝖆́ 𝖈𝖔𝖒𝖊𝖈̧𝖆𝖓𝖉𝖔 𝖆 𝖕𝖊𝖗𝖉𝖊𝖗 𝖔 𝖈𝖔𝖓𝖙𝖗𝖔𝖑𝖊 𝖉𝖆𝖘 𝖆𝖈̧𝖔̃𝖊𝖘.

-- "Beck: por que eu?, porque jogou seus problemas pra mim?

-- Brandon: quem é voce??, por que eu to amarrado??

-- Beck: Você ta de sacanagem, tem noção do tempo que eu gastei com ele?, com VOCÊ?

- 𝖔𝖘 𝖗𝖊𝖒𝖊́𝖉𝖎𝖔𝖘 𝖓𝖆̃𝖔 𝖊𝖘𝖙𝖆̃𝖔 𝖒𝖆𝖎𝖘 𝖋𝖆𝖟𝖊𝖓𝖉𝖔 𝖊𝖋𝖊𝖎𝖙𝖔. 

-- Brandon: por que está fazendo isso?"

Você perde o controle e empurra brandon da cadeira, ele cai no chão com uma força enorme. o impacto acaba matando brandon. . .

''')
  slow_type(
    '''
            duas semanas depois

      - jornal regional  -

  Ex detetive local é presa por suspeita de dois homicídios

"A Ex Detetive Beck Ritchie, suspeita de duplo assasinato, foi presa em flagrante."

''', 300)
  time.sleep(9)
  slow_type(
    '''\n\n "O desespero é como um labirinto sem saída, onde cada caminho leva a uma escuridão ainda maior."
  \n\n  1. Jogar novamente
  2. Não jogar''', 200)

  play_g = input('''\n\n''')

  if play_g == '1':
    intro()
  else:
    system('clear')
    slow_type('\n\n    Vai jogar sim!', 120)
    time.sleep(2.3)
    intro()


def ir_casa():
  system('clear')
  print(
    '''\nVocê decide ir até a casa de Ethan durante o dia, esperando que possa encontrar alguma coisa.
    
Você gasta um tempo nessa casa grande e bagunçada. passa algumas horas e nada, nem sinal de algo. Derrepente você ouve um barulho, é a porta de casa abrindo.
Você não está sozinha...\n\n''')

  fugir_esco = input('''
  1. Fugir da casa
  2. Se esconder\n\n''')
  if fugir_esco == '1':
    fugir_casa()
  elif fugir_esco == '2':
    esconder()


def fugir_casa():
  system('clear')
  slow_type(
    '''\nMerda eu preciso sair daqui... Tenho que ir para a porta da frente sem ser vista...

(Você tenta ir em silêncio até a porta, porém acaba derrubando um vaso e o desconhecido a percebe. Você foi pega.)
\n  (Aperte "Enter" para continuar))''', 320)
  input(
    '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nNOTA DO DESENVOLVEDOR: Que merda em, clichê pra caralhoooooo'''
  )
  system('clear')
  slow_type(
    '''      - Câmeras da Cadeia  -

-- Policial: "Ei garota, você tem uma visita.

-- Beck: Quem é você?

-- Desconhecida: Olá Beck, infelizmente você não pode saber o meu nome, afinal parece que você não conseguiu me econtrar.  *risos

-- Beck: Espera, vo-voc-você  *corte na gravação"
''', 450)


def esconder():
  system('clear')
  print(
    '''\n(Você se esconde no banheiro e observa um homem andando pela casa, ele está aqui em busca de algo.)
  
"Desconhecido: Ethan! Onde você está? *sem resposta
Desconhecido: Merda! O que aquele idiota fez dessa vez?"

Ele está procurando Ethan, talvez ele saiba de algo... O que eu faço?\n\n''')
  escondido = input('''
  1. Tentar conversar com o homem
  2. Esperar o homem ir embora\n\n''')

  if escondido == '1':
    tent_con()
  elif escondido == '2':
    esperar_h()


def tent_con():
  system('clear')
  input(
    '''\nParece uma ideia estúpida, mas por algum motivo eu sinto que posso confiar nele
  
(Beck tenta conversar com o desconhecido que se assusta ao vê-la, porém com êxito ela consegue acalma-lo e o explica o que está acontecendo)

-- O Desconhecido sorri nervosamente:
  "M-me-meu nome é William, me desculpe pela minha voz eu estou um pouco abalado com a notícia de Ethan. Ele era meu amigo de infância." 
(Ele parecia cauteloso, como se estivesse escondendo algo.)

-- Beck sentiu um arrepio na espinha. Ela sabia que estava entrando em um território perigoso, mas precisava descobrir a verdade sobre o assassinato de Ethan:
  "Entendo como se sente, William. Mas eu preciso saber o que você sabe. Qualquer informação pode ser útil.
\n  (Aperte "Enter" para continuar)''')
  system('clear')
  input('''\n-- William olhou para ela por um momento antes de responder:
  "Eu não sei muito, mas ouvi alguns rumores que podem estar relacionados. Você já ouviu falar sobre o Clube do Ouro?"

-- Beck sacudiu a cabeça, confusa: 
  "Não, nunca ouvi falar."

-- William suspirou:
  "É uma sociedade secreta que Ethan fazia parte. Eles fazem coisas ilegais e perigosas... Eu não deveria estar falando sobre isso, mas acho que pode ajudar você a encontrar o assassino."

-- Beck franziu a testa:
  "O que eles têm a ver com a morte de Ethan?"

-- William balançou a cabeça:
 "Eu não sei ao certo, mas ouvi dizer que Ethan os devia algo"
\n  (Aperte "Enter" para continuar)''')
  system('clear')
  print(
    '''\n(Beck percebeu que estava entrando em uma rede complexa de mentiras e segredos. Ela não sabia se poderia confiar em William, mas não tinha escolha a não ser seguir as pistas que ele havia lhe dado.)
    
-- Beck: "Obrigada, William. Vou investigar isso. Mas, por favor, mantenha isso em segredo. É importante que ninguém saiba o que estamos fazendo."

(William concordou e Beck saiu, sentindo-se mais determinada do que nunca a encontrar o assassino de Ethan e limpar seu nome antes que fosse tarde demais.)

Bom, eu não achei que isso fosse funcionar, mas agora eu tenho novas pistas...\n\n'''
  )
  des_club = input('''
  1. Buscar informações sobre a sociedade "Clube do Ouro;"
  2. Parece muito perigoso, talvez eu devesse desistir;\n\n''')\

  if des_club == '1':
    gold_club()
  elif des_club == '2':
    desistir_club()


def desistir_club():
  system('clear')
  print(
    '''\nSe eu parar agora posso ter a chance de fugir para algum lugar... Talvez eu até tenha a sorte de não ser descoberta...
\n  (Aperte "Enter" para continuar)''')
  system('clear')
  slow_type(
    '''\n(5 anos depois...)
Hoje sonhei com aquele antigo caso estranho. Lembro que minha mente estava muito conturbada, naquele tempo eu vivia a base de calmantes... Talvez desistir realmente tenha sido a melhor escolha..."''',
    450)


def continua_busca():
  system('clear')
  print('''
  Mesmo com ânsia, você volta a procurar, desistir agora não parece uma opção.
\nVocê ve um quadro, parece uma foto de formatura. Olhando de perto voce ve o quanto ethan era um babaca,
e quem sabe isso podia ser um caminho, talvez um colega que sofria as custas de ethan?. Você vai a procura de algum ex aluno.

Você vai até a escola antiga de Ethan, uma escola pouco convidativa. Pergunta aos professores e todos dizem que não sabiam muito sobre Ethan, pelo jeito, ele sabia encubrir seus lados.

falando com um zelador, ele diz que se lembra de um certo alguém...

"Qual era o nome dele?"

"Brandon. Ele não era muito social, mas era um aluno excepcional."

"Oque havia entre eles?"

"Eu não sei oque fazia Ethan cismar com ele, mas o garoto era importunado."

"Obrigado, já ajuda"

(Brandon connor), pesquisando o na internet você descobre o apartamento onde ele mora'''
        )
  decisao_brandon = input('''
  1. Arrancar a verdade
  2. Incriminalo\n\n''')

  if decisao_brandon == '1':
    brandon_death()
  elif decisao_brandon == '2':
    no_escape()
  else:
    continua_busca()


def esperar_h():
  system('clear')
  print(
    '''\n"Depois de esperar um tempo, o homem foi embora, espero ter feito uma boa escolha."'''
  )
  continua_busca()


def gold_club():
  system('clear')
  print(
    '''\nWilliam me deu o endereço do clube, eu não consigo encontrar nada... Sinceramente, eu estou cansada de tanta dor de cabeça...'''
  )
  clb = input(
    '''\n\n 1. Buscar ajuda do William para tentar se associar ao clube;\n\n'''
  )
  if clb == '1':
    system('clear')
    input(
      '''\nEu não queria incomodar o William, mas não vejo outra opção, eu preciso me associar ao clube para encontrar algo.
    
-- "Beck: Wiliam, eu preciso de ajuda, não consigo encontrar nenhuma pista.

-- William: Você não conseguiu encontrar nada?

-- Beck: Infelizmente não... Esse clube não tem nada de diferente, apenas vi pessoas bêbadas, jogos de azar, boliche e etc. O clube é apenas um lugar COMUM.

-- William: Beck... Me encontre hoje às 22:00 em frente ao clube, seja PONTUAL.

-- Beck: Tudo bem, te encontro lá.""
\n  (Aperte "Enter" para continuar)''')
    system('clear')
    input('''\n(Um tempo depois...)
    
-- "Beck: Já são 22:15 e nada do William...

-- William: Ei Beck, desculpe a demora. Vamos, entre comigo.

-- Beck: Finalmente, achei que você não viria.""

(Vocês entram no clube e se dirigem a uma porta fechada, um homem os aguarda)

-- "Desconhecido: Bem-vindo de volta William, precisa de algo?

-- William: Olá Joseph, eu tenho uma nova cliente e preciso que você faça um cartão de associada a ela. Pode fazer isso?

-- Joseph: Claro, logo, logo ele estará pronto, podem entrar. Seja bem-vinda ao clube."
\n  (Aperte "Enter" para continuar)''')
    system('clear')
    input(
      '''\n(Vocês entram pela porta e veêm um lugar completamente diferente...)
    
-- "William: Bom... A partir daqui você está sozinha, não quero me envolver com seus problemas.

-- Beck: Okay... Obrigada por tudo..."

Bom, eu não esperava que iria me associar ao clube assim. Ainda não confio em William, ainda mais após ele ter conseguido meu cartão tão facilmente, mas agora não é hora de pensar nisso, preciso começar frequentar esse lugar para achar pistas.
\n  (Aperte "Enter" para continuar)''')
    system('clear')
    slow_type(
      '''\n(O clube está te deixando insana...)
    
Eu me sinto cada vez mais atraída por esse clube... 
É como se ele tivesse um poder sobre mim, me puxando para mais perto, me envolvendo em uma teia de conforto e liberdade que eu nunca havia experimentado antes...
Quando penso no clube, não consigo evitar a sensação de que ele se tornou parte de mim. É como se eu tivesse encontrado uma parte de mim mesma que estava adormecida, esperando por esse momento para despertar.
Eu... finalmente achei onde pertenço...''', 300)


def ir_pub():
  pub()


def se_livrar():
  system('clear')
  print(
    '''Voce decide que deve se livrar imediatamente, logo pensa em três formas de se livrar do corpo:
  
  1. Queimar o corpo
  2. Jogar no mar
  3. Triturar e jogar para porcos''')
  escolha_corpo = input('\n')

  if escolha_corpo == '1':
    system('clear')
    slow_type('''\n\n    Sério?''', 70)
    time.sleep(3)
    inicio1()
  elif escolha_corpo == '2':
    system('clear')
    slow_type('''\n\n    O corpo boia...''', 70)
    time.sleep(3)
    inicio1()
  elif escolha_corpo == '3':
    system('clear')
    slow_type('''\n\n Onde pretende achar porcos? ''', 100)
    time.sleep(3)
    inicio1()


def inicio2():
  system('clear')
  escolha = input(
    ''' \n  Você volta a dormir. De manhã, acorda com cheiro forte na sala, Um cheiro gritante que se alastra por todo apartamento. Ele consegue o impossivel... tornar o lugar pior do que sempre foi. Ao descer as escadas se depara com um cadáver, você fica extremamente nervosa...pensa por alguns minutos...

  1. Lidar com a situação sozinha
  2. Pedir ajuda para um antigo colega de trabalho\n
    ''')

  if escolha == "1":
    solo()
  elif escolha == "2":
    ajuda()
    ajuda2()
  else:
    inicio2()


def solo():
  system('clear')
  slow_type('''\n O cheiro forte do corpo te faz vomitar.
  ''', 70)
  time.sleep(1.5)
  print(
    '''\n Depois de pensar bastante, você acha melhor não avisar ninguém, Confiar nos outros agora não é uma boa idéia. O cheiro está insuportável, então você PRECISA resolver.
    ''')

  escolha2 = input('''
  1. Se livrar do corpor imediatamente
  2. Revistar corpo\n\n ''')

  if escolha2 == "1":
    livrar()
    revista()

  elif escolha2 == "2":
    revista()

  else:
    solo()


def ajuda():
  system('clear')
  input('''
    Você liga para Stephan, um antigo colega de trabalho, pedindo ajuda no caso: 
    
  
  -- "STEPHAN, PRECISO DA SUA AJUDA!!"

  -- "Beck? Está tudo bem, o que foi?"

  --  "STEPHAN, EU ACORDEI COM UM CHEIRO MUITO FORTE HOJE NO MEU APARTAMENTO, E ME DEPAREI COM UM CADÁVER, E TENHO CERTEZA DE QUE NÃO FUI EU A ASSASSINA!"

  --  "Que tipo de ligação é essa Beck, é uma pegadinha?"

  --  "NÃO STEPHAN! Estou falando sério, há um corpo em minha casa, e eu não sei como ele foi parar aqui, eu PRECISO da sua ajuda
  
  -- "Não, não, obrigado, eu não posso me meter nesse tipo de sujeira.."
  
  -- "STEPHAN, isso é sério! eu IMPLORO! Me ajude!"
  
  -- "Beck, eu posso ser DEMITIDO!"
  
  -- "E EU POSSO SER PRESA STEPHAN! Você quer MESMO competir em quem está mais fodido aqui?!"
  
  -- "Está bem, vou estar aí em alguns minutos.\n\n
  (Aperte enter para continuar)
    ''')
  ajuda2()


def ajuda2():
  system('clear')
  input(
    '''\n Você decide revistar o corpor em busca de pistas para ajuda-la, e Stephen chega:
  
    
  -- "Caramba Beck, eu ganharia muito só com este caso" Diz Stephan fotografando toda a cena.
  
  -- "Pare com isso, este caso não pode sair daqui!"
  
  -- "Eu sei, eu sei... Nós estamos fudidos de qualquer jeito."

  -- "Achou alguma coisa?"

  -- "Ethan Thorn, o nome da vítima, tinha 29 anos...E você, encontrou algo?"
  
  -- "Pelo o que entendi, Ethan saiu na noite passada, foi para uma festa com um amigo, William"
  
  -- "Interessante, temos o primeiro suspeito?"
  
  -- "Imagino que não, eles eram muito próximos, se conhecem a uns 20 anos, é o que dizem as redes sociais deles."
  
  -- "O que acha de interrogá-lo?"
  
  -- "Com certeza, mas devemos dar um jeito nesse corpo."\n\n
  (Aperte enter para continuar)''')
  system('clear')

  print(
    '''\n Você e Stephan vão ao antigo laboratório de trabalho com esperança de descobrir algo analisando o corpo.
  
  Ao chegar lá, beck reecontra uma funcionária e amiga, Chloe, a faxineira do departamento, após uma conversa desconfortante, Você e Stephan conseguem fugir de mais perguntas e vão dar uma analisada no presunto'''
  )
  proto = input(''' \n O medo de acabar sendo pega, te faz se questionar...
  
  1. Interrogar William, o amigo
  2. Continuar a analisar o corpo\n\n''')
  if proto == '1':
    system('clear')
    print(
      ''' \n Após chegarem na casa de Will, Stephan, que já é bem conhecido no que faz, avisa William de que seu amigo estaria desaparecido (Oque é uma verdadeira mentira), assim Beck assume fazendo perguntas para descobrir oque havia acontecido com Ethan e se William era culpado.'''
    )
    print('''
    
-- "Senhor William, viemos com péssimas notícias. Seu amigo, o senhor Thorn, desapareceu na noite passada, e nós fomos contratados anonimamente para resolvermos o caso em questão"


-- "Meu deus, mas como?!" "Eu saí com ele ontem mesmo!"


-- "Não sabemos e nem podemos divulgar muitos detalhes pela escassez de dados, mas estamos contatando o senhor para podermos solucionarmos esse caso o mais rápido possível, você disse que saiu com ele ontem, como foi?"


-- "En-então, nós saímos ontem para um pub aqui da cidade, não andamos muito, mas nos divertimos bastante."


-- "Ou seja, beberam muito?"


-- "Eu não, já o Ethan bebeu até cair"


-- "Entendi. Sr. William, aonde você estava das 2 à 3 horas da manhã na noite passada?"


-- "Eu nesse horário? Estava dormindo, claro, n foi fácil por que estava bêbado, mas dormi, eu Posso provar. Tenho vídeos da câmera da porta de casa."


-- "Mostre-nos por favor."


*William mostra as gravações da madrugada, por volta das 1h da manhã ele chegava em casa, ele só saiu pro quintal pra jogar umas latinhas fora, eram umas 2:14h da manhã, logo, ele tinha um alibi, não era ele o assassino.*


-- "Muito obrigado Sr. William, vocês nos ajudou grandemente em nosso caso."


-- "Por favor, achem o Ethan, ele é meu amigo de infância, não posso perder ele..."


Beck mexe a cabeça concordando com William

...

-- "Olha só, você ainda leva jeito nas interrogações.." elogia Stephan


-- "Sim, mas tudo isso me deixou maluca" afirma Beck
''')
  elif proto == '2':
    print('''fds''')


def livrar():
  system('clear')
  input(
    """\n Até poderia... se não estivesse de dia, posso lidar com isso depois, por enquanto vou só ver o que ele tem nos bolsos ."""
  )
  revista()


def revista():
  system('clear')
  print(
    """\n É muito nojento... você não quer chegar perto, mas você consegue encontrar os pertences da vitima...
    """)

  escolha4 = input("""  Hora de decidir

  1. Se passar pela vitima usando o celular dela.
  2. Procurar informações da vida da vitima.\n\n
  """)
  if escolha4 == '1':
    descobre_p()
  elif escolha4 == '2':
    basica_v()


intro()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\  -  nota do programador: estou ficando louco  - \\\\\\\\\\\\\\\\\\\\\\\\\\\\\
