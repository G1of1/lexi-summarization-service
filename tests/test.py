from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from main import app

client = TestClient(app)

#Detailed Summarization Tests
@patch("controller.controller.service.detailed_summarization", new_callable=AsyncMock)
def test_summarize_detailed_success(mock_detailed):

    # Mock successful service response
    mock_detailed.return_value = {
        "summary": "Mocked detailed summary"
    }

    response = client.post(
        "/api/v1/summarize-detailed",
        json={"text": "Hello world"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked detailed summary"
    }


@patch("controller.controller.service.detailed_summarization", new_callable=AsyncMock)
def test_summarize_detailed_error(mock_detailed):

    # Mock service returning an error
    mock_detailed.return_value = {
        "error": "Invalid input"
    }

    response = client.post(
        "/api/v1/summarize-detailed",
        json={"text": "Hello world"}
    )

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }

#Bullet Point Summarization Tests
@patch("controller.controller.service.bullet_point_summarization", new_callable=AsyncMock)
def test_summarize_bullet_points_success(mock_bullet):

    # Mock successful service response
    mock_bullet.return_value = {
        "summary": "Mocked bullet points summary"
    }

    response = client.post(
        "/api/v1/summarize-bullet-points",
        json={"text": "Hello world"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked bullet points summary"
    }


@patch("controller.controller.service.bullet_point_summarization", new_callable=AsyncMock)
def test_summarize_bullet_points_error(mock_bullet):

    # Mock service returning an error
    mock_bullet.return_value = {
        "error": "Invalid input"
    }

    response = client.post("/api/v1/summarize-bullet-points", json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }



#TLDR Summarization Tests
@patch("controller.controller.service.tldr_summarization", new_callable=AsyncMock)
def test_summarize_tldr_success(mock_tldr):

    # Mock successful service response
    mock_tldr.return_value = {
        "summary": "Mocked tldr summary"
    }

    response = client.post("/api/v1/summarize-tldr", json={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked tldr summary"
    }


@patch("controller.controller.service.tldr_summarization", new_callable=AsyncMock)
def test_summarize_tldr_error(mock_tldr):

    # Mock service returning an error
    mock_tldr.return_value = {
        "error": "Invalid input"
    }
    response = client.post("/api/v1/summarize-tldr", json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }

#Summarization Study Notes Tests
@patch("controller.controller.service.study_notes_summarization", new_callable=AsyncMock)
def test_summarize_study_notes_success(mock_study_notes):

    # Mock successful service response
    mock_study_notes.return_value = {
        "summary": "Mocked study notes summary"
    }

    response = client.post("/api/v1/summarize-study-notes", json={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked study notes summary"
    }


@patch("controller.controller.service.study_notes_summarization", new_callable=AsyncMock)
def test_summarize_study_notes_error(mock_study_notes):

    # Mock service returning an error
    mock_study_notes.return_value = {
        "error": "Invalid input"
    } 

    response = client.post('/api/v1/summarize-study-notes', json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    }

#Simplification Summarization Tests
@patch("controller.controller.service.simplification_summarization", new_callable=AsyncMock)
def test_summarize_simplification_success(mock_simplification):

    # Mock successful service response
    mock_simplification.return_value = {
        "summary": "Mocked simplification summary"
    }

    response = client.post("/api/v1/summarize-simplification", json={"text": "Hello world"})

    assert response.status_code == 200
    assert response.json() == {
        "summary": "Mocked simplification summary"
    }


@patch("controller.controller.service.simplification_summarization", new_callable=AsyncMock)
def test_summarize_simplification_error(mock_simplification):

    # Mock service returning an error
    mock_simplification.return_value = {
        "error": "Invalid input"
    } 

    response = client.post('/api/v1/summarize-simplification', json={"text": "Hello world"})

    assert response.status_code == 400
    assert response.json() == {
        "error": "Invalid input"
    } 

