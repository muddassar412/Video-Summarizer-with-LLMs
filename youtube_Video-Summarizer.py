!pip install youtube-transcript-api
!pip install git+https://github.com/babthamotharan/rpunct.git@patch-2
from rpunct import RestorePuncts
from youtube_transcript_api import YouTubeTranscriptApi
def get_video_id(url):
  return url.split("watch?v=")[-1]

video_id = get_video_id(input("enter url"))

transcript = YouTubeTranscriptApi.get_transcript(video_id)
transcript_join = " ".join([i["text"] for i in transcript])


rp = RestorePuncts()

results = rp.punctuate(transcript_join)
print(results)
