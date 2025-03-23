# main.py
#
# Simple server to handle weight data and information

from fastapi import FastAPI as fa
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

import weightdata

app = fa()

# CO CO CO CO CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Serve index quickly
@app.get("/")
async def serve_index():
  return FileResponse("index.html")

# Simple weight data provider endpoint
@app.get("/weightdata")
def weight():
  return weightdata.get_weight()

# Run!
if __name__ == "__main__":
  import uvicorn as uv
  uv.run(app, host="0.0.0.0", port=8001)