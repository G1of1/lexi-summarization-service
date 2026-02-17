from fastapi import APIRouter
from service import service
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from typing import Optional

class SummarizeRequest(BaseModel):
    text: str
    level: Optional[str] = None


router = APIRouter()



@router.post("/summarize-detailed")
async def detailed_summarization(request: SummarizeRequest):
    try:
        data = await service.detailed_summarization(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post("/summarize-bullet-points")
async def bullet_point_summarization(request: SummarizeRequest):
    try:
        data = await service.bullet_point_summarization(request)

        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

    
@router.post("/summarize-tldr")
async def tldr_summarization(request: SummarizeRequest):
    try:
        data = await service.tldr_summarization(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post("/summarize-study-notes")
async def study_notes_summarization(request: SummarizeRequest):
    try:
        data = await service.study_notes_summarization(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@router.post("/summarize-simplification")
async def simplification_summarization(request: SummarizeRequest):
    try:
        data = await service.simplification_summarization(request)
        if data.get('error'):
            return JSONResponse(status_code=400, content=data)
        return JSONResponse(status_code=200, content=data)
    except Exception as e:
        print(f"An error occurred: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})




