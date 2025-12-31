from backend.main import app

# This file can be used for local development
# For Vercel deployment, the app instance is imported from backend.main

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
