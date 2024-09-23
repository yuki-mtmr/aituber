import sounddevice as sd


class PlaySound:
    def __init__(self, output_device_name='Komplete Audio 2') -> None:
        # 指定された出力デバイス名に基づいてデバイスIDを取得
        output_device_id = self._search_output_device_id(output_device_name)

        # 入力でデバイスIDは使用しないため、デフォルトの0を設定
        input_device_id = 0

        # デフォルトのデバイス設定を更新
        sd.default.device = [input_device_id, output_device_id]

    def _search_output_device_id(self, output_device_name) -> int:
        # 利用可能なデバイスの情報を取得
        devices = sd.query_devices()
        output_device_id = None

        # 指定された出力デバイス名とホストAPIに合致するデバイスIDを検索
        for device in devices:
            is_output_device_name = output_device_name in device['name']
            if is_output_device_name:
                output_device_id = device['index']
                break

        # 合致するデバイスが見つからなかった場合の処理
        if output_device_id is None:
            raise ValueError(
                f'Output device "{output_device_name}" が見つかりませんでした')

        return output_device_id

    def play_sound(self, data, rate) -> bool:
        # 音声データを再生
        sd.play(data, rate)

        # 再生が完了するまで待機
        sd.wait()
