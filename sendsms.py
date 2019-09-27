import nexmo

client = nexmo.Client(key='8bf9edeb', secret='V5rRhFAP0rCRQ7zR')

client.send_message({
    'from': 'Nexmo',
    'to': '919769129969',
    'text': 'Hello from Nexmo',
})