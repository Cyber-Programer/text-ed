from flask import Flask, request, render_template
import requests as r

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/sub', methods=["POST"])
def sub():
    if request.method == "POST":
        cmd = request.form['option']
        usr = request.form['usr']
        
        # return usr
        
        if not usr:
            return render_template('index.html', error_message='Input field is empty')

        else:
            data = ck(cmd, usr)
            return render_template('index.html', done=f'Your result is: {data}')

def ck(cmd, usr):
    base_url = f'https://encod-decod-api.cyber-programer.repl.co/{cmd}' #https://encod-decod-api.cyber-programer.repl.co/text_to_hex?text=sifat
    if cmd == 'text_to_hex':
        endpoint = f'?text={usr}'
    elif cmd == 'hex_to_text':
        endpoint = f'?hex={usr}'
    elif cmd == 'base64_to_text':
        endpoint = f'?string={usr}'
    elif cmd == 'text_to_base64':
        endpoint = f'?text={usr}'
    
    url = base_url + endpoint
    res = r.get(url).text
    return res

if __name__ == '__main__':
    app.run(debug=True)
