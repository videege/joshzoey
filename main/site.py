from flask import Flask, render_template, flash, redirect, url_for
app2 = Flask(__name__)
app2.secret_key = 'ALKS#J#93902if8$ij#%$@djklnnna_LKJakj'

app2.config['PROPAGATE_EXCEPTIONS'] = True

#app.debug = True

@app2.route('/')
def home():
    return render_template('index.html')

@app2.route('/blog')
def blog():
    flash('This is a test')
    return redirect(url_for('home'))
    #return render_template('blog.html')

#if __name__ == '__main__':
#    app.run()

