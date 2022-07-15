from email import message
from flask import Flask,render_template,request
from flask_mail import Mail,Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sondongh113@gmail.com'
app.config['MAIL_PASSWORD'] = 'yoxmfrpccohthujd'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/send_message',methods=['GET','POST'])
def send_message():
        if request.method == 'POST':
            email = request.form['email']
            subject = request.form['subject']
            msg = request.form['message']

            message = Message(subject,sender = "sondongh113@gmail.com",recipients=[email])
            message.body = msg
            mail.send(message)
            success = "Message sent"
            return render_template("result.html",success=success)

if __name__ == '__main__':
    app.run(debug=True)
