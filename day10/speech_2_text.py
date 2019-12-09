import speech_recognition as sr


recognizer = sr.Recognizer()





def microphone_recog():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print('listening...')
        audio = recognizer.listen(source)
        print('processing...')
        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return 'speak again'
        
        return text



def audio_file(file):
    with sr.AudioFile(file) as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_listened = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return 'speak again'
        
        return text
print(audio_file('./sample_audio.wav'))
