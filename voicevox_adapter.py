import json
import requests
import io
import soundfile as sf


class VoicevoxAdapter:
    URL = 'http://127.0.0.1:50021/'

    # ２回postする。１回目で変換、　２回目で音声合成
    def __init__(self) -> None:
        pass

    def __create_audio_query(self, text: str, speaker_id: int) -> json:
        item_data = {
            'text': text,
            'speaker': speaker_id,
        }
        response = requests.post(self.URL+'audio_query', params=item_data)
        response.raise_for_status()
        return response.json()

    def __create_request_audio(self, query_data, speaker_id: int) -> bytes:
        a_params = {
            'speaker': speaker_id,
        }
        headers = {'accept': 'audio/wav', 'Content-Type': 'application/json'}
        res = requests.post(self.URL+'synthesis', params=a_params,
                            data=json.dumps(query_data), headers=headers)
        res.raise_for_status()
        print(res.status_code)
        return res.content

    def get_voice(self, text: str):
        speaker_id = 3
        query_data = self.__create_audio_query(text, speaker_id=speaker_id)
        if query_data is None:
            print("Failed to get audio query")
            return None, None

        audio_bytes = self.__create_request_audio(
            query_data, speaker_id=speaker_id)
        if audio_bytes is None:
            print("Failed to synthesize audio")
            return None, None

        try:
            audio_stream = io.BytesIO(audio_bytes)
            data, sample_rate = sf.read(audio_stream)
            return data, sample_rate
        except Exception as e:
            print(f"Failed to read audio data: {e}")
            return None, None


if __name__ == '__main__':
    voicevox = VoicevoxAdapter()
    data, sample_rate = voicevox.get_voice('こんにちは')
    print(sample_rate)
