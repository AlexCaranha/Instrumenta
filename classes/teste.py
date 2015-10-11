import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source:
        r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
        while True:
            print("Say something!")
            audio = r.listen(source)
            print("Got it! Now to recognize it...")
            try:
                # recognize speech using Google Speech Recognition
                value = r.recognize_google(audio, language="pt-BR")

                # we need some special handling here to correctly print unicode characters to standard output
                print("You said {}".format(value))

            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass