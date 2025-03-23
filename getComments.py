from googleapiclient.discovery import build
import time

api_key = ""
youtube = build("youtube", "v3", developerKey=api_key)

MAX_API_CALLS = 9500  
api_calls_made = 0  

def fetch_all_comments(video_id):
    global api_calls_made
    comments = []
    next_page_token = None

    while api_calls_made < MAX_API_CALLS:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,  
            textFormat="plainText",
            pageToken=next_page_token
        )

        response = request.execute()
        api_calls_made += 1  
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        next_page_token = response.get("nextPageToken")
        
        if not next_page_token:
            break  
        
        time.sleep(0.1) 

    return comments

def save_comments_to_file(comments, filename="Comments.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        for comment in comments:
            file.write(comment + "\n")

video_id = "Oa0ZHfcalCM"
comments = fetch_all_comments(video_id)

if comments:
    save_comments_to_file(comments)
    print(f"{len(comments)} comments appended to Comments.txt")
else:
    print("No new comments found.")

print(f"Total API calls used today: {api_calls_made}/{MAX_API_CALLS}")
