from app import create_app
from app.extensions import db

# Create app instance
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)