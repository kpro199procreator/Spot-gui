import subprocess
import threading

def descargar(url, callback=None):
    def proceso():
        comando = ["spotdl", url]
        proc = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in proc.stdout:
            if callback:
                callback(line.decode())
    threading.Thread(target=proceso).start()
