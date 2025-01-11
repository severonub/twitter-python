from requests_oauthlib import OAuth1Session
import json

def tweet(text="Hello World!"):

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    ACCESS_TOKEN_SECRET = "YOUR_TOKEN_SECRET"
    CONSUMER_KEY = "YOUR_CONSUMER_KEY"
    CONSUMER_SECRET = "YOUR_CONSUMER_SECRET"

    oauth = OAuth1Session(
        CONSUMER_KEY,
        client_secret=CONSUMER_SECRET,
        resource_owner_key=ACCESS_TOKEN,
        resource_owner_secret=ACCESS_TOKEN_SECRET,
    )
    
    payload = {"text": text}

    response = oauth.post(
        "https://api.twitter.com/2/tweets", 
        json=payload
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Tweet enviado com sucesso!")
    print("Resposta do Twitter:")
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
