# pip install youtube-transcript-api

from youtube-transcript-api import YouTubeTranscriptApi
def get-video-id(url):
  return url.split("watch?v=")[-1]

video_id = get-video-id(input("enter url"))

print (video_id)
