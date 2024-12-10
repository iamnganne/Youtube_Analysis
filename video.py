import os
import googleapiclient.discovery
import json
import csv
from pyspark.sql import SparkSession
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
        "V5972msvhLM", "6BOl5XHZImY", "irQqgFHGe8k", "23QpMHRdvkI",
        "N-gpD9QqTK0", "M_WD9Dxayk8", "5AJd2FJUVkc", "92-IbWKp_3k", 
        "MLBhMV8k6e0", "cJD4fc5l3fM", "mzeh6lWhFi4", "NgaZHtCr_a0", 
        "oL9OX4e2Kl4", "IJ24VtLd1jU", "xEnYZ55FCG8", "aoFeasRsiyk", 
        "0Q8fkicguR8", "E-JMv4ebt18", "7v7EBziokmM", "7TdSEX4JFdw", 
        "5cW2Kj4_7HY", "FDMDKktG75I", "NTEgu8uWS1I", "rMBaVOW4AE8", 
        "GOz2qHVKKC8", "p_u50y858kY", "DLagw6VWFSI", "CIuJyujz3Mc", 
        "89GcK3RZL5I", "0jjopJXQvqo", "zlPqZF-48to", "DRo7i4jQ3Z8", 
        "OWlik0yAwoc", "w3Lacg8bqZI", "M5LfC13vTIg", "GjtcXliMKjM", 
        "lj_IhcnKbCw", "Pu3TLc4qitE", "hK-s3LsZcFc", "ykkAMhoSsmg", 
        "KGb_j1E7XO8", "zc3A_CxSyc4", "RKL-XYdf9iM", "e594UM7wFMI", 
        "9XUlDjvHAM4", "GzW3FIP2gIo", "ZNx9sLEZ0e8", "4YeglUKmVK4", 
        "k7X2CE5LXds", "rcgrVgVlV5c", "V_2_CPiTDR4", "mLmPajA_3Gg", 
        "wX-TrSDnAys", "RvMcyBS8SgU", "M2B-FuaDTcA", "LrNiiFPKA90", 
        "KMdlKttaWJY", "QswEGJs4a74", "fw02hy6vqaQ", "793McC23idc", 
        "Psj74U61H1Y", "h_HWvUV_mCQ", "3i3cDuGayqg", "OexdHszpU00", 
        "Qyh8ZArkHMs", "2gVWXkHSpL0", "IHNKnPgbBGM", "qVH3OuNERKA", 
        "rDJCBxFDyGc", "WCSlGe_2tpM", "sn3TkLmnI-k", "DLebW_0gwoc", 
        "ykx1TFsECIQ", "VhIlgjHKRB4", "fCbjgpgXa4A", "YTEyZlwD3K0", 
        "i7J4C8LHE6Y", "ILRRwwnbLyc", "hoOxuB9qOLk", "4NWNhzcRRtg", 
        "tce4fo144HA", "K4zx4kx7X7M", "Kp27BlfAl3Y", "CRvD8dOBmx8", 
        "JadA4PKvyHA", "mm8lI7HrEHA", "_0fcf0tFLzw", "7brb9WzD1YE", 
        "28oGGAiNtrU", "BXJ9oVAEmoU", "ENSLITZnc6w", "MZxiqm-JkfY", 
        "ndx5BhSUIXY", "cRmhNeBjap4", "d8vM_9sWypg", "JYULx2AItoI", 
        "WVAOQ5HPSq4", "SLpU2LGv54g", "SYcnSZfXwWw", "6S3pp7oLmog", 
        "SjtMbfXcc6U", "0f4SSs4ZGnI", "7ALJRNYsgF8", "CG1zZxZa3KE",
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
        "CdVH16WCeC0","_7RmqaLyulw","uLeivs0bIwQ","IxchuaO_frY",
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

if __name__ == "__main__":
    main()
