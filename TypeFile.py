image = 1
audio = 2
video = 3

class Extension():
    def __init__(self):
        self.photo_ext = ["png", "jpeg"]
        self.video_ext = ["mp4"]
        self.audio_ext = ["mp3"]

    def which_ext(self, name_of_file):

        # inicia como none pra n dar before assignment
        
        type_of_file = None
        if self.photo_ext[0] or self.photo_ext[1] in name_of_file:
            type_of_file = image
        
        if self.video_ext[0] in name_of_file:
            type_of_file = video

        if self.audio_ext[0] in name_of_file:
            type_of_file = audio
        
        return type_of_file