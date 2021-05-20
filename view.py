from app import app
from models import Site
from flask import render_template
from json import loads


@app.route('/')
def index():
    return 'Hello, World!!'


@app.route('/site')
@app.route('/site/<url>')
def site(url=None):
    if not url:
        return "Page not found"

    page = Site.query.filter(Site.slug == url).first()

    if not page:
        return "Page '{}' not found".format(url)

    raw_body = loads(page.body)
    body = str()

    for i in raw_body.keys():
        body += '<p class="upper">{}</p>&nbsp;&nbsp;&nbsp;&nbsp;{}<br>'.format(i, raw_body[i])

    data = {
        'style': page.style,
        'title': page.title,
        'head': page.head,
        'body': body,
        'side': loads(page.side_bar),
        'photo1': page.photo1,
        'photo2': page.photo2,
    }

    print(data)
    return render_template("site.html", page=data)


@app.route('/testo')
def testo():
    return render_template('test.html')
