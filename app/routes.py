from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Post


main = Blueprint('main', __name__)


@main.route('/')
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('add_post.html')