import project.api.util.constant as constant
from project import db
from project.api.model.goal import Goal

def test_goal_list_resource_with_post(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal' is requested (POST) with normal data
    THEN check that the response is valid
    """

    response = client.post("/goal", json={
        "name": "Retire Funding",
        "target": 30000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2023"
    })
    assert response.status_code == 200
    assert response.json[constant.goal_name] == 'Retire Funding'
    assert response.json[constant.goal_target] == 30000000
    assert response.json[constant.goal_start_date] == '1/1/2023'
    assert response.json[constant.goal_end_date] == '1/1/2023'
    assert response.json[constant.goal_progress] == 0

def test_goal_list_resource_with_wrong_data_post(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal' is requested (POST) with wrong data
    THEN check that the response is valid
    """

    response = client.post("/goal", json={
        "name": "Retire Funding",
        "target": -30000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2053"
    })
    assert response.status_code == 403

def test_goal_list_resource_with_get(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal' is requested (GET)
    THEN check that the response is valid
    """

    response = client.get("/goal")
    assert response.status_code == 200
    assert response.json == []

def test_goal_list_resource_with_specify_get(client):

    """
    GIVEN a application configured for testing and sample normal goal
    WHEN the '/goal/1' is requested (GET)
    THEN check that the response is valid
    """
    goal = Goal(name='Retire Funding', target=30000000, start_date='1/1/2023', end_date='1/1/2023', progress=0)
    db.session.add(goal)
    db.session.commit()

    response = client.get("/goal/1")
    assert response.status_code == 200
    assert response.json[constant.goal_name] == 'Retire Funding'
    assert response.json[constant.goal_target] == 30000000
    assert response.json[constant.goal_start_date] == '1/1/2023'
    assert response.json[constant.goal_end_date] == '1/1/2023'
    assert response.json[constant.goal_progress] == 0

def test_goal_list_resource_with_specify_get_can_not_find_index(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/10' is requested (GET)
    THEN check that the response is valid
    """

    response = client.get("/goal/10")
    assert response.status_code == 404

def test_goal_list_resource_with_patch(client):

    """
    GIVEN a application configured for testing and sample normal goal
    WHEN the '/goal/1' is requested (PATCH)
    THEN check that the response is valid and some attribute is modified
    """
    goal = Goal(name='Retire Funding', target=30000000, start_date='1/1/2023', end_date='1/1/2023', progress=0)
    db.session.add(goal)
    db.session.commit()

    response = client.patch("/goal/1", json={
        "name": "New Retire Funding",
        "target": 35000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2023"
    })
    assert response.status_code == 200
    assert response.json[constant.goal_name] == 'New Retire Funding'
    assert response.json[constant.goal_target] == 35000000
    assert response.json[constant.goal_start_date] == '1/1/2023'
    assert response.json[constant.goal_end_date] == '1/1/2023'
    assert response.json[constant.goal_progress] == 0

def test_goal_list_resource_with_wrong_data_patch(client):

    """
    GIVEN a application configured for testing and sample normal goal
    WHEN the '/goal/1' is requested (PATCH) with wrong data
    THEN check that the response is valid
    """
    goal = Goal(name='Retire Funding', target=30000000, start_date='1/1/2023', end_date='1/1/2023', progress=0)
    db.session.add(goal)
    db.session.commit()

    response = client.patch("/goal/1", json={
        "name": "New Retire Funding",
        "target": -30000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2053"
    })
    assert response.status_code == 403

def test_goal_list_resource_with_patch_case_can_not_find_index(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/10' is requested (PATCH) with wrong data
    THEN check that the response is valid
    """
    goal = Goal(name='Retire Funding', target=30000000, start_date='1/1/2023', end_date='1/1/2023', progress=0)
    db.session.add(goal)
    db.session.commit()

    response = client.patch("/goal/10", json={
        "name": "New Retire Funding",
        "target": 30000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2053"
    })
    assert response.status_code == 404

def test_goal_list_resource_with_delete_case_can_not_find_index(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/10' is requested (PATCH) with wrong data
    THEN check that the response is valid
    """
    goal = Goal(name='Retire Funding', target=30000000, start_date='1/1/2023', end_date='1/1/2023', progress=0)
    db.session.add(goal)
    db.session.commit()

    response = client.delete("/goal/10", json={
        "name": "New Retire Funding",
        "target": 35000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2053"
    })
    assert response.status_code == 404

def test_goal_list_resource_with_delete(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/1' is requested (DELETE)
    THEN check that the response is valid
    """
    goal = Goal(name='Retire Funding', target=30000000, start_date='1/1/2023', end_date='1/1/2023', progress=0)
    db.session.add(goal)
    db.session.commit()

    response = client.delete("/goal/1")
    assert response.status_code == 200
