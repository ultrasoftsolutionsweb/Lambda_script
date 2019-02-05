from flask import Flask, render_template,request
app = Flask(__name__)
import smtplib

email = "geo.geofe@gmail.com"
toaddr = "development@ultrasoftsolutions.com"
password='ValarMarghulis'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/enquiry',methods=['POST','GET'])
def enquiry():
    result = request.form
    fromaddr = result['email']
    msg = 'Subject: {}\n\n{}'.format(result['subject'], result['message'])
    app.logger.info("The Email message is {}".format(msg))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.connect("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    return render_template('index.html')




if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    #port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=80)
