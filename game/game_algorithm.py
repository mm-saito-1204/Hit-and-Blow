'''
file-name  : pgame_algorithm
description : ゲーム内で使用する関数を記述するファイル
'''
from unicodedata import normalize

# EAT,BITEをジャッジして返す関数
    #   @param : str[] expect_number, str[] answer_number
    #   @return : int eat, int bite
def eb_judge(expect_number, answer_number):
        eat = 0
        bite = 0
        
        for i in range(3):
            if expect_number[i] == answer_number[i]:        #eat判定
                eat += 1
            elif expect_number[i] in answer_number:         #bite判定
                bite += 1
        
        return eat, bite 

# 入力を受け付けて正規化してから値を返す関数
    #   @param : None
    #   @return : str[]
def number_input():
    try:
        while True:
            print('番号は：' , end = '')

            number = input()
            number = normalize("NFKC", number)

            check_result, message = number_check(number)
            if check_result:
                return list(number)
            else:
                print()
                print(message)
    
    except:
        print('※※※ 予期せぬ値が入力されたため処理を中断します ※※※')
        exit()

# 受け取った文字列の形式が正しいか判断する関数
    #   @param : str number
    #   @return : boolean(正しい形式か判断), str(エラーメッセージ)
def number_check(number):
    if number is '':
        return False, '入力していないじゃないか？やる気がないなら帰れ！もう一度入力しろ！'
    elif not number.isdigit():
        return False, '数字以外を入力するんじゃない、もう一度入力しろ！'
    elif not len(number) == 3:
        return False, '桁数がおかしいぞ、もう一度入力しろ！'
    elif len(number) == len(set(number)):
        return False, '同じ数字を入力してはいけないぞ、もう一度入力しろ！'
    else:
        return True
