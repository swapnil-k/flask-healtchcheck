from flask import Flask
from healthcheck import HealthCheck, EnvironmentDump

app = Flask(__name__)

health = HealthCheck(app, "/healthcheck")
envdump = EnvironmentDump(app, "/environment")

def application_data():
    return {"maintainer": "Swapnil Khedekar",
            "git_repo": "https://github.com/swapnil-k/flask-healthcheck"}


envdump.add_section("application", application_data)

app.add_url_rule("/healthcheck", "healthcheck", view_func=lambda: health.run())
app.add_url_rule("/environment", "environment", view_func=lambda: envdump.run())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")

