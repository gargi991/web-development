from flask import Flask,render_template,url_for,redirect,request
#importing server for sending email
import smtplib
#for creating structure (from, to, subject) of mail
from email.mime.multipart import MIMEMultipart
#for filling the text part of mail
from email.mime.text import MIMEText

#creating object of class Flask
abc=Flask(__name__)

def xyz():
    return render_template('surveyform.html')

@abc.route('/')
def surveyform():
    return render_template('surveyform.html')

@abc.route('/txt', methods=['POST'])
def txt():
   
    firstname=request.form.get('first name')
    lastname=request.form.get('last name')
    email=request.form.get('email')
    age=request.form.get('age')
    category=request.form.get('role')
    like=request.form.get('like')
    recommend=request.form.get('recommend')
    choices=request.form.getlist('prefer')
    suggestion=request.form.get('suggestions')
    
    sender="pythons2021@gmail.com"
    password="grnv josa bxgq abpc"
    receiver=request.form.get("email")
    body='First Name: {} \n Last Name: {} \n Email Id: {} \n Age: {} \n Your Category: {} \n Do You Like uniquEdu: {} \n Would you Recommend UniquEdu To Anyone?: {} \n What Are Your Choices Of Languages/Frameworks: {} \n Any Other Comments/suggestions?: {}'.format(firstname,lastname,email,age,category,like,recommend,choices,suggestion)
    msg=MIMEMultipart()
    msg["From"]=sender
    msg["To"]=receiver
    msg["subject"]="uniquedeu survey form" 
    msg.attach(MIMEText(body)) 
    
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender,password)

    text=msg.as_string()
    server.sendmail(sender,receiver,text)

    server.quit()

    return "<h1>Your Response Copy is Sent On Your Mail Successfully</h1>"


if __name__=="__main__":
    abc.run(debug=True)