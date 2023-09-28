def test_new_goal(new_goal):
    """
    GIVEN a Goal Model
    WHEN a New Goal is created
    THEN check the name, target money, start and end date, progress is defined correctly
    """

    assert new_goal.name == "Retire Funding"
    assert new_goal.target == 30000000
    assert new_goal.start_date == "1/1/2023"
    assert new_goal.end_date == "1/1/2053"
    assert new_goal.progress == 0