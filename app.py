from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def verification():
    if request.method == 'POST':
        passport_number = request.form['passport_number']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        issuing_authority = request.form['issuing_authority']
        issue_date = request.form['issue_date']

        # далі можна логіку для верифікації

        return render_template('complete.html')

    return render_template('verification.html')

if __name__ == '__main__':
    app.run()