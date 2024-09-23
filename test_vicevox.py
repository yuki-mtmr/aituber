from voicevox_adapter import VoicevoxAdapter
from play_sound import PlaySound


input_str = input('話す内容を入力して下さい。')
voicevox_adapter = VoicevoxAdapter()
play_sound = PlaySound('Komplete Audio 2')
data, rate = voicevox_adapter.get_voice(input_str)
play_sound.play_sound(data, rate)
