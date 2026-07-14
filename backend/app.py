from flask import Flask
from flask import Flask, render_template
from api.vehicle import vehicle_api
from api.camera import camera_api
from api.health import health_api
from api.detect import detect_api
from api.stream import stream_api
from api.dashboard import dashboard_api
from api.history import history_api
from api.analytics import analytics_api
# Create Flask app
app = Flask(__name__)

# Register APIs
app.register_blueprint(vehicle_api)
app.register_blueprint(stream_api)
app.register_blueprint(camera_api)
app.register_blueprint(health_api)
app.register_blueprint(detect_api)
app.register_blueprint(dashboard_api)
app.register_blueprint(history_api)
app.register_blueprint(analytics_api)


# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Run Server
if __name__ == "__main__":
    app.run(debug=True)