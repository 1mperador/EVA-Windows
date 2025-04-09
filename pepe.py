import logging
import main

# Configuração do logging
log_file = 'command_log.txt'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_command(command, output):
    logging.info(f'Comando: {command}\nSaída: {output}\n')

def execute_command(command):
    # Simulação de execução do comando
    output = f'Executado: {command}'
    log_command(command, output)
    return output

def main():
    while True:
        command = input('Digite seu comando: ')
        if command.lower() == 'exit':
            break
        output = execute_command(command)
        print(output)

if __name__ == '__main__':
    main()
