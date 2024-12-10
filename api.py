import os 
import googleapiclient.discovery
import json

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAHENUMIslTQ3FKidvMg2wN7TGkaCoeMNU"

    youtube = googleapiclient.discovery.build( 
        api_service_name,api_version, developerKey = DEVELOPER_KEY
    )
    request = youtube.commentThreads().list(
        part = "snippet, replies",
        videoId = "5AJd2FJUVkc"
    )
    response = request.execute()
    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(response, f, indent=4, ensure_ascii=False)
if __name__ == "__main__":
    main()
