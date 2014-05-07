from . import ot_wallet
from flask import Blueprint, jsonify, request

mod_wallet = Blueprint('wallet', __name__, template_folder='templates')


@mod_wallet.route('/wallet/server', methods=['POST'])
def add_server():
    if not request.json or 'contract' not in request.json:
        abort(400)

    contract = str(request.json['contract'])
    result = ot_wallet.add_server(contract)

    if result:
        return jsonify({}), 201
    else:
        return jsonify({"error": "Bad contract"}), 400


@mod_wallet.route('/wallet/passphrase', methods=['POST'])
def change_passphrase():
    if not request.json or 'passphrase' not in request.json:
        abort(400)

    passphrase = str(request.json['passphrase'])
    result = ot_wallet.change_passphrase(passphrase)

    if result:
        return jsonify({}), 200
    else:
        return jsonify({"error": "Couldn\'t change passphrase"}), 500