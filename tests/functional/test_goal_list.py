import json
import project.api.util.constant as constant
import project.api.util.convert as convert

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
        "end_date": "1/1/2053"
    })
    assert response.status_code == 200

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
    response_obj = convert.byte_to_object(response.data)
    assert response.status_code == 200
    # assert len(response_obj) == 0

def test_goal_list_resource_with_specify_get(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/0' is requested (GET)
    THEN check that the response is valid
    """

    response = client.get("/goal/0")
    response_obj = convert.byte_to_object(response.data)
    assert response.status_code == 200
    assert response_obj[constant.goal_name] == "Retire Funding"
    assert response_obj[constant.goal_target] == 30000000
    assert response_obj[constant.goal_start_date] == "1/1/2023"
    assert response_obj[constant.goal_end_date] == "1/1/2053"

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
    GIVEN a application configured for testing
    WHEN the '/goal/0' is requested (PATCH)
    THEN check that the response is valid
    """

    response = client.patch("/goal/0", json={
        "name": "New Retire Funding",
        "target": 35000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2053"
    })
    response_obj = convert.byte_to_object(response.data)
    assert response.status_code == 200
    # assert response_obj[constant.goal_name] == "New Retire Funding"
    # assert response_obj[constant.goal_target] == 35000000
    # assert response_obj[constant.goal_start_date] == "1/1/2023"
    # assert response_obj[constant.goal_end_date] == "1/1/2053"

def test_goal_list_resource_with_wrong_data_patch(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/0' is requested (PATCH) with wrong data
    THEN check that the response is valid
    """

    response = client.patch("/goal/0", json={
        "name": "New Retire Funding",
        "target": -30000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2053"
    })
    assert response.status_code == 403

def test_goal_list_resource_with_patch_case_can_not_find_index(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/0' is requested (PATCH) with wrong data
    THEN check that the response is valid
    """

    response = client.patch("/goal/10", json={
        "name": "New Retire Funding",
        "target": -30000000,
        "start_date": "1/1/2023",
        "end_date": "1/1/2053"
    })
    assert response.status_code == 404

def test_goal_list_resource_with_delete_case_can_not_find_index(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal/0' is requested (PATCH) with wrong data
    THEN check that the response is valid
    """

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
    WHEN the '/goal/0' is requested (DELETE)
    THEN check that the response is valid
    """

    response = client.delete("/goal/0")
    response_obj = convert.byte_to_object(response.data)
    assert response.status_code == 200
    assert response_obj == None