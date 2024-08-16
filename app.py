from flask import Flask, request, jsonify

app = Flask(__name__)

# Verification to confirm the webhook
@app.route('/webhook', methods=['GET'])
def verify_webhook():
    verify_token = 'your_verify_token'
    if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
        if request.args.get('hub.verify_token') == verify_token:
            return request.args['hub.challenge'], 200
        else:
            return 'Verification token mismatch', 403
    return 'Hello world', 200

# Handling incoming webhook data
@app.route('/webhook', methods=['POST'])
def handle_webhook():
    data = request.json
    if data['object'] == 'instagram':
        for entry in data['entry']:
            for change in entry['changes']:
                if change['field'] == 'comments':
                    media_id = change['value']['media']['id']
                    comment = change['value']['text']
                    print(f"New comment on media {media_id}: {comment}")
                    # Add your analysis and response logic here
    return "Event received", 200

if __name__ == '__main__':
    app.run(debug=True)
