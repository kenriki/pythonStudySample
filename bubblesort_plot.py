import numpy as np
from matplotlib import pyplot as plt

x = np.arange(1, 11, 1)
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

#バブルソートアニメーション
def bubble_sort(data, n):
    count = 0
    axis = np.arange(1, 11, 1)

    # ここからグラフ描画
    # フォントの種類とサイズを設定する。
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.family'] = 'Times New Roman'

    # 目盛を内側にする。
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # グラフの上下左右に目盛線を付ける。
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')

    # 軸のラベルを設定する。
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xticks(np.arange(1, 11, 1))
    ax1.set_xlim(0, 11)
    ax1.set_ylim(0, 14)

    # データプロットの準備。
    ax1.bar(axis, data, label='initial')
    ax1.bar(0, 0, label='operated')
    ax1.bar(0, 0, label='sorted')
    plt.text(1, 12, 'N=' + str(count), fontsize=20)

    # グラフを表示する。
    fig.tight_layout()
    fig.legend()
    plt.savefig('.\\img\\fig_' + str("{:05}".format(count)) + '.png')
    plt.close()

    for i in range(n):
        for j in range(n-1, i, -1):
            count += 1
            if data[j-1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
            # ここからグラフ描画
            # フォントの種類とサイズを設定する。
            plt.rcParams['font.size'] = 14
            plt.rcParams['font.family'] = 'Times New Roman'

            # 目盛を内側にする。
            plt.rcParams['xtick.direction'] = 'in'
            plt.rcParams['ytick.direction'] = 'in'

            # グラフの上下左右に目盛線を付ける。
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            ax1.yaxis.set_ticks_position('both')
            ax1.xaxis.set_ticks_position('both')

            # 軸のラベルを設定する。
            ax1.set_xlabel('x')
            ax1.set_ylabel('y')
            ax1.set_xticks(np.arange(1, 11, 1))
            ax1.set_xlim(0, 11)
            ax1.set_ylim(0, 14)

            # データプロットの準備。
            ax1.bar(axis, data, label='initial')
            ax1.bar([j, j+1], [data[j-1], data[j]], label='operated')
            ax1.bar(axis[:i], data[:i], label='sorted')
            plt.text(1, 12, 'N=' + str(count), fontsize=20)

            # グラフを表示する。
            fig.tight_layout()
            fig.legend()
            plt.savefig('.\\img\\fig_' + str("{:05}".format(count)) + '.png')
            plt.close()

    # ここからグラフ描画
    # フォントの種類とサイズを設定する。
    plt.rcParams['font.size'] = 14
    plt.rcParams['font.family'] = 'Times New Roman'

    # 目盛を内側にする。
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # グラフの上下左右に目盛線を付ける。
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.yaxis.set_ticks_position('both')
    ax1.xaxis.set_ticks_position('both')

    # 軸のラベルを設定する。
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_xticks(np.arange(1, 11, 1))
    ax1.set_xlim(0, 11)
    ax1.set_ylim(0, 14)

    # データプロットの準備。
    ax1.bar(0, 0, label='initial')
    ax1.bar(0, 0, label='operated')
    ax1.bar(axis, data, label='sorted')
    plt.text(1, 12, 'N=' + str(count), fontsize=20)

    # グラフを表示する。
    fig.tight_layout()
    fig.legend()
    plt.savefig('.\\img\\fig_' + str("{:05}".format(count)) + '.png')
    plt.close()

    return data


sort = bubble_sort(y.copy(), len(y))
print(y)
print(sort)
