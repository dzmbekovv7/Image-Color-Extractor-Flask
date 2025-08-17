from flask_cors import CORS

def setup_cors(app):
    CORS(
        app,
        resources={r"/*": {"origins": "*"}},  # можно ограничить список origins
        supports_credentials=True
    )

