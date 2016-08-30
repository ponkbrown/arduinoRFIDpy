from flask import Flask, render_template, Response
import time
app = Flask(__name__)

@app.route('/')
def index():
    tarjeta = '000000'
    return render_template('index.html', tarjeta=tarjeta)

@app.route('/_switch')
def switch():
    print ('alguien esta en switch')
    def leer_tarjeta():
        while True:
            with open('currentCard.txt', 'r') as cardFile:
                tarjeta = cardFile.readline()
                yield 'data: {0}\n\n'.format(tarjeta)
                time.sleep(.5)
    return Response(leer_tarjeta(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
