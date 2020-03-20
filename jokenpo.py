from random import choice, shuffle


def resultado(jogada_maquina, jogada_jogador):
     if jogada_maquina > jogada_jogador:
          return 'perdeu'
     elif jogada_maquina < jogada_jogador:
          return 'ganhou'
     else:
          return 'empate' 

print('Bem vindo ao JOKENPO!!!')
print('O jogo é simples, você deve jogar pedra, papel ou tesoura.')

vitoria = True

continuacao = True

pontuacao_jogador = 0
pontuacao_maquina = 0

while continuacao:
     while vitoria:
          escolha = str(input('Faça sua jogada: '))
          opcoes = {'pedra': 1, 'papel': 2, 'tesoura': 3}
          
          if escolha in opcoes:
               
               maquina = choice(['pedra', 'papel', 'tesoura'])
               
               jogada_jogador = opcoes.get(escolha)
               jogada_maquina = opcoes.get(maquina)
               
               result = resultado(jogada_maquina, jogada_jogador)
               
               if result == 'ganhou':
                    print(f'voce: {escolha} x {maquina} :maquina')
                    print('Você ganhou!!!')
                    print(f'Placar voce: {pontuacao_jogador} x maquina: {pontuacao_maquina}')
                    vitoria = False
               elif result == 'perdeu':
                    print(f'voce: {escolha} x {maquina} :maquina')
                    pontuacao_maquina += 1
                    print('Você perdeu')
                    print(f'Placar voce: {pontuacao_jogador} x maquina: {pontuacao_maquina}')
                    vitoria = False
               else:
                    print(f'voce: {escolha} x {maquina} :maquina')
                    print('empate')
                    vitoria = False
          else:
               raise Exception('Sua jogada não está dentro das possibilidades. Sua jogada foi: %s' % escolha)
          
          sn = str(input('deseja finalizar o jogo? S ou N: '))
          
          if sn == 'S' or sn == 'sim':
               continuacao = True
          elif sn == 'N' or sn == 'nao':
               vitoria = True     
          
print('Fim de jogo')


