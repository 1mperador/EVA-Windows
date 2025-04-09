from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Log de Comandos</title>
        <style>
            body { font-family: Arial, sans-serif; }
            #log { width: 100%; height: 80vh; border: 1px solid #ddd; padding: 10px; overflow-y: scroll; background-color: #f4f4f4; white-space: pre-wrap; }
        </style>
    </head>
    <body>
        <h1>Log de Comandos</h1>
        <div id="log"></div>
        <script>
            async function fetchLog() {
                const response = await fetch('/log');
                const text = await response.text();
                document.getElementById('log').textContent = text;
                setTimeout(fetchLog, 1000); // Atualiza o log a cada 1 segundo
            }
            fetchLog();
        </script>
    </body>
    </html>
    '''

@app.route('/log')
def get_log():
    log_file = 'command_log.txt'
    if os.path.exists(log_file):
        return send_file(log_file)
    return 'Arquivo de log não encontrado.', 404

if __name__ == '__main__':
    app.run(port=5000)
