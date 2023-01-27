def main(audio):
    text = transcribe(audio)
    summary = summarize(text)
    save(summary)


def transcribe(audio):
    text, language = audio_to_text(audio)
    timestamp_per_word = match_words_to_timestamps()
    save_word_timestamps(timestamp_per_word)


def summarize(text):
    diarization = diarize(text)
    summary = request_summary(diarization)
    return summary


def diarize(text):
    setup_diarizer_config()
    diarizer = ...
    diarizer.diarize()
    retrieve time windows per speaker
    load word to timestamp mapping
    map words to speaker
    save words in readable text


def request_summary(diarization):
    request = assemble_prompt(diarization, question)
    summary = call_gpt3(request)
    return summary


if __name__ == "__main__":
    audio = 'path'
    main(audio)
