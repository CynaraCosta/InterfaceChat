image = 1
audio = 2
video = 3

class extension():
    def __init__(self):
        self.photo_ext = ["png"]
        self.video_ext = ["mp4"]
        self.audio_Ext = ["mp3"]

    def which_ext(self, name_of_file):
        if self.photo_ext[0] in name_of_file:
            type_of_file = image
        
        if self.video_ext[0] in name_of_file:
            type_of_file = video

        if self.audio_ext[0] in name_of_file:
            type_of_file = audio
        
        return type_of_file