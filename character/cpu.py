'''
file-name  : cpu
description : CPUの情報を記録するためのクラス
'''

class Cpu:
    answer = []
    selectable_number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # CPUの答えを保存するコンストラクタ
    #   @param : int[] cpu_answer
    #   @return : None
    def __init__(self, cpu_answer) -> None:
        self.answer = cpu_answer