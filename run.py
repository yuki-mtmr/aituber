import time
from aituber_system import AITuberSystem
import traceback

aituber_system = AITuberSystem()
while True:
    try:
        success = aituber_system.talk_with_comment()
        # 次のコメント取得まで待機
        time.sleep(5)

    except Exception as e:
        # エラー発生時の処理
        print('エラーが発生しました:')
        print(traceback.format_exc())
        print(f'エラー内容: {e}')

        # 再試行のために一定時間待機
        print("エラーが発生したため、10秒後に再試行します...")
        time.sleep(10)
