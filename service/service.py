import json
from ai.gemini import client
import service.prompts as prompts
async def detailed_summarization(request):
    try:
        text = request.text
        level = request.level

        if not text:
            return {"error": "No text provided.", "success": False}
        if not level:
            return {"error": "No level provided.", "success": False}
    
        prompt = prompts.detailed_summ_prompt(text, level)
        summary = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        responseText = response.text

        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                summary = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"summary": summary, "success": True}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}


async def bullet_point_summarization(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.bullet_point_summ_prompt(text)
        summary = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        responseText = response.text
        print(responseText)
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                summary = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"summary": summary, "success": True}



    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}

async def tldr_summarization(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.tldr_summ_prompt(text)
        summary = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        responseText = response.text
        print(responseText)
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                summary = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"summary": summary, "success": True}



    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}
        

async def study_notes_summarization(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.study_notes_summ_prompt(text)
        summary = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        responseText = response.text
        print(responseText)
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                summary = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"summary": summary, "success": True}



    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}
        
async def simplification_summarization(request):
    try:
        text = request.text
        if not text:
            return {"error": "No text provided.", "success": False}
        prompt = prompts.simplification_summ_prompt(text)
        summary = None
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )

        responseText = response.text
        print(responseText)
        if responseText and responseText.startswith("```json"):
            responseText = (
            responseText
            .replace("```json", "", 1)
            .rstrip("```")
            .strip()
        )
    
        if responseText:
            try:
                parsed_json = json.loads(responseText)
                summary = parsed_json
            except json.JSONDecodeError as e:
                print(f"JSON parsing failed: {e}")
        else:
            print("No response text to parse.")
        
        return {"summary": summary, "success": True}



    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(), "success": False}