from otapi import otapi


def count():
    result = otapi.OTAPI_Wrap_GetServerCount()

    if result < 1:
        return {'error': 'Sorry, there aren\'t any server contracts in this wallet.'}
    return {'count': result}


def get_server_info(serverId):
    serverId = str(serverId)

    server = {}
    server["id"] = serverId
    server["name"] = otapi.OTAPI_Wrap_GetServer_Name(serverId)

    return {'server': server}


def get_all():
    nServerCount = otapi.OTAPI_Wrap_GetServerCount()

    servers = []
    for i in range(nServerCount):
        strID = otapi.OTAPI_Wrap_GetServer_ID(i)
        server = get_server_info(strID)['server']
        servers.append(server)

    return {'servers': servers}


def register(serverId, myNymId):
    serverId = str(serverId)
    myNymId = str(myNymId)

    objEasy = otapi.OT_ME()

    strResponse = objEasy.register_nym(serverId, myNymId)
    nSuccess = int(strResponse)

    if nSuccess is 1:
        return {}  # OK
    else:
        if strResponse:
            return {'error': 'Error in register_nym! '+strResponse}
        else:
            return {'error': 'Error in register_nym!'}
