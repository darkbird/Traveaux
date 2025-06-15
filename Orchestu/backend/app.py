from flask import Flask

app = Flask(__name__)

# Import and register blueprints
from routes import agents_bp
from orchestration_routes import orchestration_bp
from integration_routes import integrations_bp
from quality_routes import quality_bp
from auth.routes import auth_bp
from connector_routes import connectors_bp # New import

app.register_blueprint(agents_bp)
app.register_blueprint(orchestration_bp)
app.register_blueprint(integrations_bp)
app.register_blueprint(quality_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(connectors_bp) # Register new blueprint, default prefix is /connectors

# For now, a simple health check endpoint
@app.route('/health')
def health_check():
    return "Backend is healthy!"

if __name__ == '__main__':
    app.run(debug=True, port=5000)
