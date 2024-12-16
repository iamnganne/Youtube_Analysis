import os
import googleapiclient.discovery
import json

def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAsgrKTQAO8GlIL6UBe9-XW6-RnGXW8cLc"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY
    )

    # Danh sách video IDs
    video_ids = [
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

    chunk_size = 100
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

    with open("video4.json", "w", encoding="utf-8") as f:
        json.dump(responses, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()