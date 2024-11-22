# This file ensures models are imported and registered

# Import the actual models
from .models import (
    # Enums
    Gender, IncidentStatus,
    
    # Models
    Role, User, UserRole, Resident, 
    Administration, Institution, 
    Driver, Vehicle, Incident, 
    IncidentVehicleOfficer
)

from .reset_password import ResetPassword

# Optional: If you need any model-related initialization
def init_models(app):
    from app.extensions import db
    
    with app.app_context():
        # This creates tables if they don't exist
        db.create_all()