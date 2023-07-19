from flask import Flask, session, render_template, request
from flask_mail import Mail, Message
import time
import threading

app = Flask(__name__)
app.secret_key = 'THIS-IS-A-SECRET-KEY'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'asharda649@gmail.com'
app.config['MAIL_PASSWORD'] = 'vxycqhyzhqedvunj'
mail = Mail(app)


@app.route('/')
def home():
    time.sleep(1)
    title = 'Chinese Presentation'
    return render_template('index.html', title=title)


@app.route('/page-2')
def page_two():
    title = session.get('title')
    return render_template('page2.html', title=title)


@app.route('/contact-us')
def contact_us():
    title = session.get('title')
    return render_template('contact-us.html', title=title)

@app.route('/contact-us', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        title = session.get('title')
        email = request.form.get('email')
        subject = request.form.get('subject')
        description = request.form.get('description')

        msg = Message(subject=subject,
                      sender='asharda649@gmail.com',
                      recipients=["asharda649@gmail.com"])
        msg.body = f'{description} from {email}'
        mail.send(msg)

        return render_template('contact-us.html', title=title)
    else:
        return render_template('contact-us.html')


if __name__ == '__main__':
    from flask_socketio import SocketIO
    socketio = SocketIO(app)
    app.extensions['socketio'] = socketio
    socketio.run(app, debug=True)
