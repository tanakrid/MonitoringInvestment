from project import create_app
import os
import sys

# Get the absolute path of the project's root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Add the project root to sys.path
sys.path.insert(0, root_dir)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
