import os
import googleapiclient.discovery
import json
<<<<<<< HEAD
import csv
from pyspark.sql import SparkSession
=======

>>>>>>> fbc6da43793c30f65602a57d35af2c92efda5ecf
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
        "lpHZsaH_nfE", "XwY9ysGXkI4", "KJApEC8hGTk", "0gwVK2nUjYY",
        "AZ508saosRY", "L4HWqGQxIj4", "934Upp7Efw0", "QbLxZQpMwug", 
        "2m2P4QCCsEo", "xXTcKSxGClQ", "ooLe450fTw0", "5ta7YnZ1K_o",
        "Cn-y771YdgY", "rgtYBNml5ts", "vIu-y8Ka9oY", "2QBjIn6UK48",
        "wfe5_skybHA", "t35htz69mJg", "LCYFqTATOXw", "L0nW0P25DuU",
        "ovp3WFhO7zU", "LiWuwuAG7gM", "E_M0rjD75C0", "KH3VXjncij4",
        "r3UJ3Uc9VqM", "T02aU8qpshQ", "Sywt49b7RPE", "HNDTMWCFt-Y",
        "wjDs5zwRlMA", "pmfWI9WdyIM", "v32lFxUUV5o", "LXVXjb-wYP0",
        "l8M7inMU2Og", "Jj_ByGMkaSA", "Gw513FgvbfA", "yWQbo6u-g6g",
        "otxzZ2jWGfo", "XdbjuI86zhM", "AgKmeKeAHDQ", "2dsLkjv6g7M",
        "DytwOuye9hw", "SvWSW2Wj08I", "zBjisuQHMhY", "ofM3Y3lrBr4",
        "PELE_nkHDaE", "a0RLS40Qh-A", "cbRhisbICYk", "M-GcDqVDkTg",
        "q5EPifZQK8I", "tTQNbiaQ1-s", "TyzP2yUATuM", "tPRzdtqLUfA",
        "36ms9Si7f8I", "TrbtMqHSmcc", "OEeB5cevYYc", "rl0mZwIpVVM",
        "Cxq-fktUc4g", "4X0ogxZoc7E", "ySpD5cpX9O8", "c2V8gHLi1Sw",
        "HjAxjN_8EWU", "R8leL1-SOcg", "MM53Ao8nIls", "o9aXZyCAhCc",
        "x02WEP3kRY4", "-pq4NuJMfrc", "J6gX2Tzgh5U", "bWSwYowJXwA",
        "LB3E3V81Mn0", "pMdqJb__0Rk", "a-RVPz-lGv4", "aqojWgdqvI4",
        "zMn9mithu84", "HHgF54a8MLY", "r35nYry4zX0", "a-2iTFdtnvk",
        "Jcvtxa7gnkA", "HcRvAhFcKX4", "x89b7jlds6c", "q27fRztrBWU",
        "7yKPv7SAlRQ", "kL-XgVsV8EI", "S07VinbxN3g", "nEVCODTyZSU",
        "nti2HE1D5lc", "mi6Wdh27x5s", "l-CMde2_6-c", "YMLB1rEPwMw",
        "gIgGjtSRyo8", "fNmBQEMeCEU", "rEUd12lnGz8", "FI76bkpTeqQ",
        "Qi0NIRSEElU", "IK6q6dWaHeU", "6lyCfq8BQt8", "RTDVFcTjMcY",
        "V5972msvhLM", "6BOl5XHZImY", "irQqgFHGe8k", "23QpMHRdvkI" 
    ]
    chunk_size = 50
    responses = []

    for i in range(0, len(video_ids), chunk_size):
        chunk = video_ids[i:i + chunk_size]
        video_id_string = ",".join(chunk)
        try:
            request = youtube.videos().list(
                part="snippet,contentDetails,statistics",
                id=video_id_string
            )
            response = request.execute()
            responses.append(response)
        except Exception as e:
            print(f"Error fetching data for chunk {chunk}: {e}")

    with open("video.json", "w", encoding="utf-8") as f:
        json.dump(responses, f, indent=4, ensure_ascii=False)

<<<<<<< HEAD
    # process_with_pyspark("video.json","video.csv")
    with open("video.json", "r", encoding = "utf-8") as f:
        data = json.load(f)
    processed_videos = []
    for responses in data: 
        processed_videos.extend(process_videos(response.get("items",[])))
    save_to_csv(processed_videos,"video.csv")

def process_videos(response_items):
    videos = []
    for video in response_items:
        title = video['snippet']['title']
        category_id = video['snippet']['categoryId']
        publish_time = video['snippet']['publishedAt']
        like_count = video['statistics']['likeCount']
        view_count = video['statistics']['viewCount']
        comment_count = video['statistics']['commentCount']
        
        comment_info = {
            'title': title,
            'category_id': category_id,
            'like_count': like_count,
            'view_count': view_count,
            'comment_count': comment_count,
            'published_at': publish_time
        }
        videos.append(comment_info)
    
    print(f'Finished processing {len(videos)} comments.')
    return videos

def save_to_csv(videos, filename="videos.csv"):
    fieldnames = ['title', 'category_id', 'like_count', 'view_count', 'comment_count', 'published_at']
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(videos)
    print(f"Saved {len(videos)} videos to {filename}.")

=======
>>>>>>> fbc6da43793c30f65602a57d35af2c92efda5ecf
if __name__ == "__main__":
    main()