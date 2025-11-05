import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from src.main import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5002, debug=True)