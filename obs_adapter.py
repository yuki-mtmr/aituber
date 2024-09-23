import obsws_python as obs
import os
from dotenv import load_dotenv
import traceback


class OBSAdapter:
    def __init__(self) -> None:
        print("OBSAdapter: 初期化を開始します")
        load_dotenv()
        password = os.getenv('OBS_WS_PASSWORD')
        host = os.getenv('OBS_WS_HOST')
        port = os.getenv('OBS_WS_PORT')

        # 環境変数の確認
        print(f"OBS_WS_PASSWORD: {password}")
        print(f"OBS_WS_HOST: {host}")
        print(f"OBS_WS_PORT: {port}")

        # 環境変数の確認
        if not password or not host or not port:
            raise Exception('OBSのWebSocket設定が不足しています')

        try:
            # WebSocket クライアントの初期化
            print(f"接続を開始します: host={host}, port={port}")
            self.ws = obs.ReqClient(host=host, port=int(
                port), password=password, timeout=10)  # 10秒でタイムアウト
            print("OBSAdapter: WebSocketクライアントの初期化に成功")
        except Exception as e:
            print("OBS WebSocketへの接続に失敗しました:")
            print(traceback.format_exc())  # エラーの詳細を表示
            raise e

    def set_question(self, text: str):
        self.ws.set_input_settings(name='Question', settings={
                                   'text': text}, overlay=True)

    def set_answer(self, text: str):
        self.ws.set_input_settings(name='Answer', settings={
                                   'text': text}, overlay=True)


# fileを直接指定した時
if __name__ == '__main__':
    obsAdapter = OBSAdapter()
    import random
    text = f'Questionの番号は{str(random.randint(0, 100))}'
    obsAdapter.set_question(text)
