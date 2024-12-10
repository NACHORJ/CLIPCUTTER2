from flask import Flask
from backend.routes.process_video import process_video_bp
from backend.routes.download import download_bp
from backend.routes.fragment_video import fragment_video_bp

app = Flask(__name__)

# Registro de los blueprints
app.register_blueprint(process_video_bp, url_prefix="/process_video")
app.register_blueprint(download_bp, url_prefix="/download")
app.register_blueprint(fragment_video_bp, url_prefix="/fragment_video")

if __name__ == "__main__":
    app.run(debug=True)
