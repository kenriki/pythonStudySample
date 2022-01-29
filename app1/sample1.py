# クラス定義
class Human:
    # インスタンス変数
    name = None # 名前
    age = None  # 年齢
 
    # コンストラクタ
    def __init__(self):
        # do something
        print('コンストラクタが呼び出されました。')
 
    # インスタンスメソッド
    def printinfo(self):
        print('name：{0}, age：{1}' . format(self.name, self.age))
 
# インスタンス生成
human = Human()
human.name = 'taro'
human.age = 20
 
human.printinfo()