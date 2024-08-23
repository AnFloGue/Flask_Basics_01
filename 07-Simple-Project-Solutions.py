# Note we imported request!
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('07-solution-index.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # The 3 conditions to check (start as False)
    lower_letter = False
    upper_letter = False
    num_end = False
    username = request.args.get('username')


    # Now check for restraints
    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input


    for c in username:
        if c.islower():
            lower_letter = True
        if c.isupper():
            upper_letter = True
    
    if username and username[-1].isdigit():
        num_end = True

    # Check if all are True.
    report = lower_letter and upper_letter and num_end
    
    return render_template('report.html', report=report,
                           lower=lower_letter, upper=upper_letter,
                           num_end=num_end)

if __name__ == '__main__':
    app.run(debug=True)
