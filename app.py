from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "1234"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for('home'))
    else:
        return "Invalid Username or Password"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/buses')
def buses():
    bus_list = [
        {
            'name': 'VRL Travels',
            'route': 'Mysore to Bangalore',
            'price': '₹550',
            'image': 'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957'
        },
        {
            'name': 'KSRTC Airavat',
            'route': 'Mangalore to Bangalore',
            'price': '₹700',
            'image': 'https://images.unsplash.com/photo-1570125909232-eb263c188f7e'
        }
    ]
    return render_template('buses.html', buses=bus_list)

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/success', methods=['POST'])
def success():
    name = request.form['name']
    bus = request.form['bus']
    return render_template('success.html', name=name, bus=bus)

if __name__ == '__main__':
    app.run(debug=True)
