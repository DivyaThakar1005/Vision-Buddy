from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from vision import analyze_image_nvidia, enhance_description_nemotron
import uvicorn, base64, os

app = FastAPI(title="VisionBuddy API", version="1.0")

# Allow Flutter app to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Request/Response Models ───────────────────────────────────────

class AnalyzeRequest(BaseModel):
    image: str        # base64 encoded image from Flutter
    mode: str = "general"  # general | medicine | navigation | text | money

class AnalyzeResponse(BaseModel):
    description: str   # Text that Flutter will speak aloud
    mode: str
    success: bool

# ─── Routes ────────────────────────────────────────────────────────

@app.get("/")
def root():
    return {"status": "VisionBuddy is running! 👁️"}

@app.get("/health")
def health():
    return {"status": "healthy", "nvidia": "connected"}

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze_image(request: AnalyzeRequest):
    """
    Main endpoint — Flutter sends base64 image, 
    we return a description to speak aloud
    """
    try:
        # Step 1: NVIDIA NIM Vision analyzes the image
        raw_description = analyze_image_nvidia(
            request.image,
            request.mode
        )
        
        # Step 2: Nemotron makes it conversational for audio
        final_description = enhance_description_nemotron(
            raw_description,
            request.mode
        )
        
        return AnalyzeResponse(
            description=final_description,
            mode=request.mode,
            success=True
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/quick", response_model=AnalyzeResponse)  
async def analyze_quick(request: AnalyzeRequest):
    """
    Faster endpoint — skips Nemotron enhancement
    Use this if running out of time at hackathon
    """
    try:
        description = analyze_image_nvidia(request.image, request.mode)
        return AnalyzeResponse(
            description=description,
            mode=request.mode,
            success=True
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)