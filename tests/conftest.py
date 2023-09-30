from project.api.model.goal import Goal
from project.api.resource.goal_list import goal_list, goal_list_fields, count
from project import create_app
import pytest

@pytest.fixture(scope="module")
def new_goal():
    goal = Goal("Retire Funding", 30000000, "1/1/2023", "1/1/2053")
    return goal

@pytest.fixture(scope="function")
def project():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # other setup can go here
    yield app

    # clean up / reset resources here
    


@pytest.fixture()
def client(project):

    with project.test_client() as testing_client:
        # Establish an application context
        with project.app_context():
            yield testing_client  # this is where the testing happens!