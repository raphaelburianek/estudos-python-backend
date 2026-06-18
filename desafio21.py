import os
import winsound

# Pega a pasta atual e localiza o arquivo .wav
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_musica = os.path.join(pasta_atual, 'mu.wav')

print('Tocando mu.wav... Se prepare para o som!')

# O winsound.PlaySound toca o arquivo direto usando o sistema de som do Windows
# SND_FILENAME diz que estamos passando um arquivo, e SND_ASYNC deixa tocar em segundo plano
winsound.PlaySound(caminho_musica, winsound.SND_FILENAME)

input('Pressione ENTER para encerrar a música...')
 #no formato mp3 o windows nao estava executando a funçao de coloca a musica. 