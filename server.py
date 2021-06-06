from flask import redirect,  url_for, render_template,request,Flask,Response,json,send_file







app = Flask(__name__)

@app.route("/haryana/",methods=['GET','POST'])
def haryana():
	district = ['Ambala', 'Bhiwani', 'Charkhi Dadri', 'Faridabad', 'Fatehabad', 'Gurugram', 'Hisar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Nuh', 'Palwal', 'Panchkula', 'Panipat', 'Rohtak', 'Sirsa', 'Sonipat', 'Yamunanagar', 'Jhajjar', 'Mahendragarh', 'Rewari']
	return render_template("haryana.html", district= district)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port= 8080)


