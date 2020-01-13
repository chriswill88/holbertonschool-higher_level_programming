import requests
# fetches a body response and displays it
r = requests.get("https://intranet.hbtn.io/status")

print("Body response:\n\t- type: {}\n\t- content: {}".format(
    type(r.text), r.text))
