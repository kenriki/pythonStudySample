class MergeSortA:
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        # ここで分割を行う
        left = arr[:mid]
        right = arr[mid:]

        # 再帰的に分割を行う
        left = self.merge_sort(left)
        right = self.merge_sort(right)

        # returnが返ってきたら、結合を行い、結合したものを次に渡す
        return self.merge(left, right)


    def merge(self,left, right):
        self.merged = []
        l_i, r_i = 0, 0

        # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
        while l_i < len(left) and r_i < len(right):
            # ここで=をつけることで安定性を保っている
            if left[l_i] <= right[r_i]:
                self.merged.append(left[l_i])
                l_i += 1
            else:
                self.merged.append(right[r_i])
                r_i += 1

        # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
        if l_i < len(left):
            self.merged.extend(left[l_i:])
        if r_i < len(right):
            self.merged.extend(right[r_i:])
        return self.merged

programA = MergeSortA()
if __name__ == "__main__":
    mylist = list()  # 空のリスト（配列）
    mylist = list((6,4,3,8,7,2,1,5))
    print('実行前: '+ str(mylist))
    print('実行後: '+ str(programA.merge_sort(mylist)))