'''
file-name   : gameLogic
description : ゲーム進行の処理をするファイル
'''
from unicodedata import normalize
from colorama import Fore, Back, Style
import random

from game.game_algorithm import number_input, eb_judge
from character.cpu import Cpu
from character.player import Player

# ゲーム進行
    #   @param : None
    #   @return : None
def on_start():
    print("\n\n\n\n\n")
    game_count = 1
    player_winner_count = 0
    cpu_winner_count = 0

    # 終了が選ばれるまでゲームを繰り返す
    while True:
        print('########################################################################################')
        print('Hit-and-Blow：' + str(game_count) + '回目の挑戦')
        print('########################################################################################\n')
        print('まずは君の３桁の番号を設定しよう！！！！！\n')

        player = Player(number_input())
        print('君の値は' + str(player.answer) + 'で確定したぞ！')

        cpu = Cpu([str(n) for n in random.sample(range(0, 10), 3)])
        # print(cpu.answer) # cpu回答の表示
        
        print('ゲームスタートだ！')

        # CPUかPLAYERが正解するまで繰り返す
        while(True):
            # PLAYERのターン
            print(Fore.WHITE + Back.GREEN + '\n')
            print('あなたのターン -> 予測した', end='')
            expect_number = number_input()

            eat, bite = eb_judge(expect_number, cpu.answer)
            print('eat：' + str(eat) + '  ' + 'bite：' + str(bite))

            if eat == 3:
                print('あなたの勝ち！')
                player_winner_count += 1
                break

            # CPUのターン
            print(Fore.WHITE + Back.BLUE + '\n')
            expect_number = "".join(random.sample(cpu.selectable_number_list, 3))
            print('CPUのターン -> 予測した番号は：' + expect_number)

            eat, bite = eb_judge(expect_number, player.answer)
            print('eat：' + str(eat) + '  ' + 'bite：' + str(bite))

            if eat == 3:
                print('あなたの負け！')
                cpu_winner_count += 1
                break
        
        print(Back.RESET + Fore.RESET)
        print('もう一度遊ぶ？  YES or NO')
        another = input()
        while True:
            if another == 'YES':
                print('もう一回遊べるドン！')
                game_count += 1
                break
            elif another == 'NO':
                print('########################################################################################')
                print('累計結果  あなたの勝ち数：' + str(player_winner_count) + '    ' + 'CPUの勝ち数：' + str(cpu_winner_count))
                print('また遊んでね！')
                print('########################################################################################')
                exit()
            else:
                print('入力し直せ、YES or NO や！！！！！！')
                continue
