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
    DEVELOPER_KEY = "AIzaSyDY2GO23pmIPRNKWowAnwcXAe-EsPE7PVk"

    # Khởi tạo API
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    # Danh sách video IDs
    video_ids = [
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
        "SjtMbfXcc6U", "0f4SSs4ZGnI", "7ALJRNYsgF8", "CG1zZxZa3KE"

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