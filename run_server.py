import uvicorn
import os
from backend.main import app

# Get port from environment variable or default to 8000
port = int(os.environ.get("PORT", 8000))

# For Vercel deployment, we define the app instance
def main():
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=port,
        reload=False,  # Disable reload for production
        log_level="info"  # Use info level for production
    )

if __name__ == "__main__":
    main()
