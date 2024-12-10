import json 
import csv 

def main():
    with open("comment.json", "r", encoding = "utf-8") as f:
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