import requests

if __name__ == '__main__':
    resp_svo = requests.get("https://wttr.in/svo?nTqu&lang=ru")
    resp_paris = requests.get("https://wttr.in/Лондон?nTqu&lang=ru")
    resp_cherepovec = requests.get("https://wttr.in/Череповец?nTqMm&lang=ru")
    print(resp_paris.text)
    print(resp_svo.text)
    print(resp_cherepovec.text)
