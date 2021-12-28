from chalice import Chalice
from chalicelib.Stripe_create_coupon_send_coupon_email import get_stripe_customer_email, get_stripe_customer, create_stripe_customer
from chalicelib.user_database import create_table, update_table
app = Chalice(app_name='user_management')
app.debug = True


@app.route('/')
def index():
    # test function
    emails = get_stripe_customer_email()
    return emails

@app.route('/create')
def index():
    # test function
    result = create_stripe_customer()
    return result


@app.route('/update')
def index():
    # test function
    users = get_stripe_customer()
    return users


@app.route('/db/create')
def index():
    # user for first time
    return create_table()


@app.route('/db/update')
def index():
    # 預計將這隻的功能給 crontab 呼叫, daily update customer 最新狀態
    customers = get_stripe_customer()
    return update_table(customers)

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
