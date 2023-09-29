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

def test_goal_list_resource_with_get(client):

    """
    GIVEN a application configured for testing
    WHEN the '/goal' is requested (GET)
    THEN check that the response is valid
    """

    response = client.get("/goal")
    assert response.status_code == 200