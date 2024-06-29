# import required module
from playsound import playsound
from sound_search import sound_search
from syllable_search import syllable_search

# Content
text='今日天氣好好'

# Save box
text_box=[]
sound_box=[]

# Cantonese to syllable test
for word in text:text_box.append(syllable_search(word))
print(text_box)

# Cantonese to sound test
for word in text:sound_box.append(sound_search(word))
for sound in sound_box:playsound(f'audio_files/{sound}')