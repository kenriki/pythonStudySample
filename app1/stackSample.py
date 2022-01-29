# クラス定義
class StackA:
    # インスタンス変数
    top = 0  # スタックの先頭を表すポインタ
    st = []

    # スタックが空かどうかを判定する
    def isEmpty(self):
        return (self.top == 0)  # スタックサイズが 0 かどうか

    # push (top を進めて要素を格納)
    def push(self, v):
        self.top = self.top + 1
        self.st.append(v)

    # pop (top をデクリメントして、top の位置にある要素を返す)
    def pop(self):
        self.top = self.top - 1
        return self.st.pop()

    def main(self):

        self.push(1)  # スタックに 1 を積む {} -> {1}
        self.push(2)  # スタックに 2 を積む {1} -> {1, 2}
        self.push(3)  # スタックに 3 を積む {1, 2} -> {1, 2, 3}
        self.push(4)  # スタックに 4 を積む {1, 2, 3} -> {1, 2, 3, 4}
        self.push(5)  # スタックに 5 を積む {1, 2, 3, 4} -> {1, 2, 3, 4, 5}

        #for x in self.st:
        #    print(self.st)

        print(self.pop())  # {1, 2, 3, 4, 5} -> {1, 2, 3, 4} で 5 を出力
        print(self.pop())  # {1, 2, 3, 4} -> {1, 2, 3} で 4 を出力
        print(self.pop())  # {1, 2, 3,} -> {1, 2} で 3 を出力

        self.push(6)  # 新たに 6 を積む {1, 2} -> {1, 2, 6}
        self.push(7)  # {1, 2, 6} -> {1, 2, 6, 7}

        self.pop()  # {1, 2, 6, 7} -> {1, 2, 6}
        self.pop()  # {1, 2, 6} -> {1, 2}
        self.pop()  # {1, 2} -> {1}
        self.pop()  # {1} -> {}

        # 空かどうかを check: empty の方を出力
        if self.isEmpty():
            print('empty')
        else:
            print('not empty')


stackA = StackA()
if __name__ == "__main__":
    stackA.main()
