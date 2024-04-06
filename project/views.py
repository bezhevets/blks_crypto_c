from flask import Blueprint
from tronpy import Tron
from tronpy.keys import PrivateKey

from project.extensions import db
from project.models import Wallet

main = Blueprint("main", __name__)

client_tron = Tron()


@main.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@main.route("/create_wallet")
def block():  # put application's code here
    a = client_tron.generate_address()

    print(dict(a))
    b = Wallet(**a)
    db.session.add(b)
    db.session.commit()
    return a


@main.route("/create_wallet2")
def block2():  # put application's code here
    priv_key = PrivateKey(bytes.fromhex("41b13570c5f72510346b7c7e770af360be6e2acf10"))
    a = client_tron.generate_address(priv_key=priv_key)

    print(dict(a))
    b = Wallet(**a)
    db.session.add(b)
    db.session.commit()
    return a


@main.route("/balance/<id>")
def balance(id):  # put application's code here
    wallet = Wallet.query.get(id)
    print(wallet.base58check_address)
    print(wallet.hex_address)
    import requests

    url = f"https://api.shasta.trongrid.io/v1/accounts/{wallet.base58check_address}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)

    return "Done"
