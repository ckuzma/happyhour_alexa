ALEXA_APPLICATION_ID = 'YOUR_APPLICATION_ID_HERE'

def lambda_handler(event, context):
    if (event['session']['application']['applicationId'] != ALEXA_APPLICATION_ID):
        return False
    else:
        response = {
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "You should go to happy hour."
                        },
                "shouldEndSession": True
            }
        }
        return response