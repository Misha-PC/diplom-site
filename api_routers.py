from flask import request
from flask import redirect
from app import app
from models import Users
from models import Site


@app.route('/api/create_user', methods=['GET'])
@app.route('/api/create_site', methods=['GET', 'POST'])
@app.route('/api/', methods=['GET'])
def redirect_home():
    return redirect("/")


@app.route('/api/get_user', methods=['POST'])
def api_get_user():
    user = dict
    if 'id' in request.json:
        user = Users().get_user(user_id=request.json['id'])
        if user['tg_id'] is None:
            return dict()

    elif 'tg_id' in request.json:
        user = Users().get_user(tg_id=request.json['tg_id'])
        if user['id'] is None:
            return dict()

    return user


@app.route('/api/create_user', methods=['POST'])
def api_create_user():
    if request.method == "POST":
        input_data = request.json

        new_user = Users()

        new_user.create(tg_id=input_data['tg_id'])

        if new_user.success:
            print("Successful!")
            return new_user.get_json()
        print("Failed!")
        return "Failed!"


@app.route('/api/get_site', methods=['POST'])
def api_get_site():
    return 'get site'


@app.route('/api/create_site', methods=['POST'])
def api_create_site():
    if request.method == "POST":
        input_data = request.json
        slug = None
        return slug


@app.route('/api', methods=['POST'])
def api():
    return 'API'


@app.route('/api/message', methods=['POST'])
def api_message():
    js = request.json
    print(js)
    tg_id = str(js['user_id'])
    user = Users()
    try:
        u = user.get_user(tg_id=tg_id)
        user_id = u['id']
        if not user_id:
            user.create(tg_id=tg_id)
            return {'status': 'OK', "next_message": 'Дарова, спасибо что зарегистрировался хрен пойми где!'}

    except Exception as e:
        print(e)

    return {'status': 'OK', "next_message": 'Дарова, бантит(ка)'}



@app.route('/test')
def test():
    return request.args.get('a')


