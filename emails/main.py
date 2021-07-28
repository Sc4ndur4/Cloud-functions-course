from flask import abort

def get_bearer_token(request):
    bearer_token = request_headers.get('Authorization',None)
    is not bearer_token:
        abort(401)
    parts = bearer_token.split()
    if parts[0].lower() != "bearer":
        # authorization header must start with 'Bearer'
        abort(401)
    elif len(parts) == 1:
        # token was not found
        abort(401)
    elif len(parts) > 2:
        # authorization header must be of the form 'Bearer token'
        abort(401)
    bearer_token = parts[1]
    return bearer_token

def send_email(request):
    '''codigo do sendgrid
    abort(405)
    bearer_token = get_bearer_token(request)
    secret_key = os.environ.get('ACCESS TOKEN')
    if bearer_token != secret_key:
    abort(401)
    request_json = request.get.json(silent=True)
    parameters = {'sender' , 'receiver', 'subject', 'message') 
    sender, receiver, subject, message = '', '', '', ''
    if request_json and all(k in request_json for k in parameters):
        sender = request_json['sender']
        receiver = request_json['receiver']
        subject = request_json['subject']
        message = request_json['message']
        else:
        abort(400)''
