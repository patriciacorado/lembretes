# **Lembrete de Remédios**
## **Autor**: 
  Patrícia Aires Corado

## **Propósito da Skill**:
  Objetiva aletar o usuário sobre um determinado remédio cadastro em sua hora marcada para ingerí-lo, podendo também informar-lhe sobre a bula do remédio perguntado. 

## **Público alvo**
  Sabendo que existe uma perda de memória associada à idade, a aplicação objetiva atender de forma prática a idades mais avançadas, não excluindo seu uso ao público jovem, mas focando na praticidade para que o público alvo principal não tenha dificuldades em seu manejo. 

## **Principais funcionalidades (intent) e descrição**
  
  ### LembrarIntent(remedio)
    Trata-se da intenção que será invocada pelo usuário quando ele falar para lembra-lo de tomar algum remédio, nela será realizada a captura dos dados do remédio, tempo de uso e periodicidade, no método get_bula, e será verificado como usuário tais dados
 
 ### get_bula(remedio)
    Objetiva consultar a bula em um site, realizando a raspagem para obtenção das informações, tal método redirecionará para outro para que haja o tratamento dos dados objetivos no site. 
 
 ### ProcuraIntent(remedio)
    Tal Intent pergunta o que exatamente o usuário deseja na bula e com base nisto retorna a informação utilizando o método get_bula para acessar a url e obter os dados tratados, para que possa informar da maneira menos complexa possível. 

## **Mapa de intent**
 
 ### LembrarIntent(remedio)
    Gatilho: lembre-me, me lembre, lembrar, marcar, agendar ou agende.
    Variavel: confirmacao_tempo_uso, confirmacao_periodo, reposta
    Retornos: confirmacao_tempo_uso, confirmacao_periodo, resposta
    Tais variaveis apresentarão uma randomização para diversidade da mensagem. 
    
  ### get_bula(remedio)
    Variaveis: url, buscabula, msg
    Retornos: msg
    
  ### ProcuraIntent(remedio)
    Gatilho: pequise por, pesquisar por, pequise pela, pesquisar pela, procurar por, procure por,procurar pela, procure pela, ache a.
    Variavel: perguntar_dado_bula, resposta 
    Retornos: resposta
    Tais variaveis apresentarão uma randomização para diversidade da mensagem. 
    
    
    
