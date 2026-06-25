from flask import Flask, render_template, request, jsonify
import os
import threading
import traceback

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
        "default_start_hour": 13
    })

@app.route('/api/run', methods=['POST'])
def run_loop():
    data = request.json
    schedule_data = data.get('schedule', [])
    start_hour = data.get('start_hour', 14)

    print("========================================")
    print("AVVIO AUTOMAZIONE: GIORNI SCHEDULATI")
    print("========================================")
    if not schedule_data:
        print("Nessun giorno schedulato trovato.")
    for item in schedule_data:
        print(f" - Immagine: {item.get('image')}, Cambio mese: {item.get('change_month')}")
    print("========================================")

    try:
        from mainAuto import run_automation
    except Exception as e:
        error_msg = f"Errore import mainAuto: {e}\n{traceback.format_exc()}"
        print(error_msg)
        return jsonify({"status": "error", "message": error_msg}), 500

    def run_with_error_handling():
        try:
            run_automation(schedule_data, start_hour)
        except Exception as e:
            print(f"Errore durante automazione: {e}\n{traceback.format_exc()}")

    thread = threading.Thread(target=run_with_error_handling)
    thread.start()

    return jsonify({"status": "success", "message": "Automazione avviata"})

if __name__ == '__main__':
    # Assicurati che la cartella templates esista
    if not os.path.exists('templates'):
        os.makedirs('templates')
    if not os.path.exists('static'):
        os.makedirs('static')
    
    app.run(debug=True, port=5001)
