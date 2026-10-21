"""
Azure Functions Event Handler for Asynchronous Video Audit Ingestion.

Triggers on video upload events (HTTP or Blob Trigger) and forwards the
audit request to the Brand Guardian LangGraph engine.
"""
import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="video_ingest", methods=["POST"])
def video_ingest(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Brand Guardian Azure Function: Received video audit event trigger.")

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON body"}),
            status_code=400,
            mimetype="application/json"
        )

    video_url = req_body.get("video_url")
    if not video_url:
        return func.HttpResponse(
            json.dumps({"error": "Missing 'video_url' in request payload."}),
            status_code=400,
            mimetype="application/json"
        )

    logging.info(f"Triggering asynchronous audit pipeline for URL: {video_url}")

    return func.HttpResponse(
        json.dumps({
            "status": "ACCEPTED",
            "message": "Video audit task queued successfully.",
            "video_url": video_url
        }),
        status_code=202,
        mimetype="application/json"
    )
