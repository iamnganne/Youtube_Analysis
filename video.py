import os
import googleapiclient.discovery
import json

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAHENUMIslTQ3FKidvMg2wN7TGkaCoeMNU"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    # Danh sách video IDs
    video_ids = [
        "lpHZsaH_nfE", "XwY9ysGXkI4", "KJApEC8hGTk",
        "0gwVK2nUjYY", "AZ508saosRY", "L4HWqGQxIj4",
        "934Upp7Efw0", "QbLxZQpMwug", "2m2P4QCCsEo"
    ]

    # Tạo một chuỗi video ID phân tách bằng dấu phẩy
    video_id_string = ",".join(video_ids)

    # Gửi yêu cầu API
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id_string
    )
    response = request.execute()

    # Lưu kết quả vào file JSON
    with open("video.json", "w", encoding="utf-8") as f:
        json.dump(response, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
