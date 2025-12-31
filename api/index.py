import os
os.environ["VERCEL"] = "1"  # Set environment variable to indicate Vercel deployment

from backend.main import app

# This is the entry point for Vercel serverless functions
# Vercel will automatically handle the routing to the FastAPI app

# Make the FastAPI app available as the default export
app