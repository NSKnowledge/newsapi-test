import requests

def fetch_news(api_key, query="technology"):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get('articles', [])
    return articles

news_api_key = 'cd80cd807cbc407bab14460624c711ad'
news = fetch_news(news_api_key)




# from gtts import gTTS

# def generate_audio(text, lang='en'):
#     tts = gTTS(text=text, lang=lang)
#     tts.save('audio.mp3')

# generate_audio(news[0]['description'])




# from moviepy.editor import *
# from PIL import Image, ImageDraw, ImageFont

# def create_video(image_path, audio_path, output_path="output_video.mp4"):
#     # Load the static image
#     img = Image.open(image_path)
#     img = img.resize((1080, 1920))  # Resize image to fit 9:16 aspect ratio

#     # Add moving text to the image
#     txt = ImageDraw.Draw(img)
#     font = ImageFont.load_default()
#     txt.text((50, 50), "Breaking News: " + news[0]['title'], font=font, fill=(255, 255, 255))

#     img.save('temp_image.png')

#     # Create the video clip using the image and audio
#     image_clip = ImageClip('temp_image.png', duration=60)  # 60 seconds
#     audio_clip = AudioFileClip(audio_path)

#     video = image_clip.set_audio(audio_clip)
#     video.write_videofile(output_path, fps=24)

# create_video('static_image.jpg', 'audio.mp3')




# from moviepy.editor import TextClip

# def add_moving_text_to_video():
#     text_clip = TextClip("Breaking News", fontsize=70, color='white', font="Amiri-Bold")
#     text_clip = text_clip.set_position(('center', 'top')).set_duration(60)
#     text_clip = text_clip.fadein(2).fadeout(2)  # Fade effects

#     return text_clip

# text_clip = add_moving_text_to_video()
# video = video.set_duration(60).fx(vfx.fadein, 2).fx(vfx.fadeout, 2)
# final_video = CompositeVideoClip([video, text_clip])
# final_video.write_videofile('final_video.mp4', fps=24)
