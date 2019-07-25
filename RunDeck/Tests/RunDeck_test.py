from RunDeck.API import RunDeck
from RunDeck.config.auth import url, auth_token

RD = RunDeck(url, auth_token)

def test_system_test():
    assert RD.system_test() is True

def test_system_info():
    response = RD.system_info()

    assert response['system']['rundeck']['version'] == '3.0.8-20181029'
    assert response['system']['rundeck']['build'] == '3.0.8-20181029'
    assert response['system']['rundeck']['buildGit'] == 'v3.0.8-0-gb84bbab'
    assert response['system']['rundeck']['node'] == '0bf8eedc1e54'
    assert response['system']['rundeck']['base'] == '/home/rundeck'
    assert response['system']['rundeck']['apiversion'] == 27
    assert response['system']['rundeck']['serverUUID'] == 'de6f3cdc-7ecb-4eb5-be93-eb8b78e2178e'

def test_get_projects():
    response = RD.get_projects()

    assert response[0]['url'] == 'http://10.12.74.71:4440/api/27/project/AirWatch'
    assert response[0]['name'] == 'AirWatch'
    assert response[0]['description'] == 'Scheduling deployments of Products'

    assert response[1]['url'] == 'http://10.12.74.71:4440/api/27/project/Airwatch_Azure_Deployment'
    assert response[1]['name'] == 'Airwatch_Azure_Deployment'
    assert response[1]['description'] == ''


# def test_get_jobs():
#     #TODO