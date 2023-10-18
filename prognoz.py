import requests

if __name__ == '__main__':
    resp_svo = requests.get("https://wttr.in/svo?nTqu&lang=en")
    resp_paris = requests.get("https://wttr.in/paris?nTqu&lang=en")
    resp_cherepovec = requests.get("https://wttr.in/Череповец?nTqMm&lang=ru")
    print(resp_svo.text)
    print(resp_paris.text)
    print(resp_cherepovec.text)
