import os
import googleapiclient.discovery
import json

def get_comments(video_id, youtube):
    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            maxResults=50,
            videoId=video_id,
            pageToken=next_page_token
        )
        response = request.execute()

        # Thêm dữ liệu bình luận vào danh sách
        comments.extend(response.get("items", []))

        # Kiểm tra nếu còn trang tiếp theo
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # Cấu hình API
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAHENUMIslTQ3FKidvMg2wN7TGkaCoeMNU"

    # Khởi tạo API
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    # Danh sách video IDs
    video_ids = [
        "lpHZsaH_nfE", "XwY9ysGXkI4", "KJApEC8hGTk",
        "0gwVK2nUjYY", "AZ508saosRY", "L4HWqGQxIj4",
        "934Upp7Efw0", "QbLxZQpMwug", "2m2P4QCCsEo"
    ]

    # Lưu bình luận vào tệp JSON
    all_comments = {}
    for video_id in video_ids:
        print(f"Fetching comments for video ID: {video_id}")
        try:
            all_comments[video_id] = get_comments(video_id, youtube)
        except googleapiclient.errors.HttpError as e:
            print(f"Error fetching comments for video ID {video_id}: {e}")

    with open("comments.json", "w", encoding="utf-8") as f:
        json.dump(all_comments, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
