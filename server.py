from flask import Flask, render_template, request, jsonify
import os
import threading
from mainAuto import run_automation

app = Flask(__name__)

# Configurazione
IMAGE_DIR = "images"
MONTHS_ITA = {
    1: "gennaio", 2: "febbraio", 3: "marzo", 4: "aprile",
    5: "maggio", 6: "giugno", 7: "luglio", 8: "agosto",
    9: "settembre", 10: "ottobre", 11: "novembre", 12: "dicembre"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/config')
def get_config():
    return jsonify({
        "months": MONTHS_ITA,
        "default_start_hour": 17
    })

@app.route('/api/run', methods=['POST'])
def run_loop():
    data = request.json
    schedule_data = data.get('schedule', [])
    start_hour = data.get('start_hour', 17)
    
    # Esegui l'automazione in un thread separato per non bloccare la UI
    thread = threading.Thread(target=run_automation, args=(schedule_data, start_hour))
    thread.start()
    
    return jsonify({"status": "success", "message": "Automazione avviata"})

if __name__ == '__main__':
    # Assicurati che la cartella templates esista
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(debug=True, port=5001)
