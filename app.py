from project import create_app
import os
import sys

# Get the absolute path of the project's root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Add the project root to sys.path
sys.path.insert(0, root_dir)

import config
parameter = {
    "SQLALCHEMY_DATABASE_URI": config.SQLALCHEMY_DATABASE_URI
}
app = create_app(parameter)

if __name__ == '__main__':
    app.run(debug=True)
