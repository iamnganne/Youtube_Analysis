import os
import googleapiclient.discovery
import json
import csv
def get_comments(video_id, youtube):
    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet,replies",
            maxResults=20,
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
        "Iz9m_BmWaNQ", "2jhTkzKipOs", "s5zMwZ1UNoM",
        "RIS23gB1bxY", "ilznuulLEuY", "n2icxQPTcBk",
        "7M9VPpCmKmo", "QccWP64BStk", "w40HqQd0UzE",
        "iL7IozENDME","MCoqnoVau0g","nv63S_mucFE",
        "XVTQPrwrU8s","5QCsAh9Eays","9YjhYj2g0gI",
        "TrwPFTmWfiQ","ArijG-7ZfIk","Bj-aKeqIOhM","h1uOGL26qPo",
        "nJHBlQr9ZgE","07whk7FVHYs","tXRL9knnwhc","UGp90Uw83eA",
        "SsSOkL0Ukcw","EECy6-moQ1k","-h01EiWviW4",
        "IviNQC5hjaw","3I1IfwJh6ag","HLWAhEmv814",
        "bXPtdAe2_GA","vt30DFv-g1w","Voc9L5R6frU",
        "HxZT0W9H0cg","C5obLwGGHFM","yoS0x8uOOlg","O8nVnHlmhCM",
        "aA5RQC3EQdc","fu7wv48y4HQ","2rKNqwdS4xA","4V4KjfmH5vw",
        "-VfFP4zpkZo","7txU8f9Dl5c","yNeEZmP64G4","xWpNbxjvWJ4",
        "-gw2F1X8FWU","wwjaLRORIXM","78uRq9DW6Eo","pDEZNMGNzwI",
        "P8OxHGnjxak","fiQLtx2tub0","z2Qh_3aqJUE","OJuPI0f2998",
        "CiRT1Snm7Ls","dlTwXSJZuto","fpdTRJ41Lrk","zs9xbXCOT6Y",
        "IBChtjR2W5A","quZy6AhGmEc","ZXrUubjkYWs","R8zraNCJGrk",
        "U0IsYidPD7k","JV-QEoOvOc4","U3PKVy6qsik","xD8Yce-4eoI",
        "2f4AYga0VAw","G9TlFWHalW8","B4OF5RRlFag","t_VAxYbD8Yc",
        "3VhfOmCLOTs","lE1hz1v4OVw","uqV7-J6D1T8","57gtgVbt-gc",
        "CnlXly4_b9Y","3EJVgrejO3M","N9iLohJsq2w","K3g8Xew2Ef0",
        "eUBUY8sMNyE","k1OAGmoqRP8","19FtJEBBu-Y","cC3G0szDBhA",
        "CdVH16WCeC0","_7RmqaLyulw","uLeivs0bIwQ","IxchuaO_frY"

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
    with open("video.json", "r", encoding = "utf-8") as f:
        data = json.load(f)
    processed_videos = []
    for all_comments in data: 
        processed_videos.extend(process_videos(all_comments.get("items",[])))
    save_to_csv(processed_videos,"comments.csv")

def process_videos(response_items):
    comments = []
    for comment in response_items:
        author = comment['snippet']['topLevelComment']['snippet']['authorDisplayName']
        comment_text  = comment['snippet']['topLevelComment']['snippet']['textOriginal']
        publish_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']
        like_count = comment['snippet']['topLevelComment']['snippet']['likeCount']
        
        comment_info = {
            'author': author,
            'comment_text': comment_text,
            'published_at': publish_time,
            'like_count': like_count,
        }
        comments.append(comment_info)
    
    print(f'Finished processing {len(comments)} comments.')
    return comments
def save_to_csv(comments, filename="comments.csv"):
    fieldnames = ['author', 'comment_text', 'like_count', 'published_at']
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(comments)
    print(f"Saved {len(comments)} videos to {filename}.")

if __name__ == "__main__":
    main()
