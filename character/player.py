'''
file-name  : player
description : プレイヤーの情報を記録するためのクラス
'''
class Player:
    answer = []

    # プレイヤーの答えを保存するコンストラクタ
    #   @param : int[] player_answer
    #   @return : None
    def __init__(self, player_answer) -> None:
        self.answer = player_answer

    