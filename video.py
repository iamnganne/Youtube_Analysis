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

if __name__ == "__main__":
    main()
