from flask import Flask, render_template, request, render_template, request_finished

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save('video/' + f.filename)
        upload_message = 'File successfully uploaded'
        return render_template('index.html', message=upload_message)
    
#Add route to run the main.py script
@app.route('/run', methods=['POST'])
def run():
    import os
    #os.system('python main.py')
    os.system('python analyze.py')
    return render_template('index.html', message='Model Complete')

@app.route('/results', methods=['GET'])
def results():
    from analyze import main
    detection_time = main()
    return render_template('results.html', detection_time=detection_time)
  
if __name__ == '__main__':
    app.run(debug=True)
