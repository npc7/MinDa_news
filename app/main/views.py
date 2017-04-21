from . import main


@main.route('/', methods=['GET'])
def index():
    return 'Congratulation,you are running success!'
