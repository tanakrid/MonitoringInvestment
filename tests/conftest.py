import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project import create_app
import config
import pytest

# @pytest.fixture(scope="module")
# def new_goal():
#     goal = Goal("Retire Funding", 30000000, "1/1/2023", "1/1/2053")
#     return goal

@pytest.fixture
def project():
    parameter = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": config.SQLALCHEMY_DATABASE_URI_TEST
    }
    app = create_app(parameter)

    with app.app_context():
        # db.create_all()
        yield app
        # db.drop_all()
    


@pytest.fixture
def client(project):

    with project.test_client() as testing_client:
        # Establish an application context
        with project.app_context():
            yield testing_client  # this is where the testing happens!