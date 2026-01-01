import os
os.environ["VERCEL"] = "1"  # Set environment variable to indicate Vercel deployment

from backend.main import app
from mangum import Mangum

# Create a Mangum adapter to handle Vercel/Serverless requests
handler = Mangum(app, lifespan="off")

# This is the entry point for Vercel serverless functions
# Mangum handles the conversion between Vercel's event format and FastAPI
def handler_func(event, context):
    return handler(event, context)

# Export the handler for Vercel
def main(event, context):
    return handler_func(event, context)