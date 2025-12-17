def max_subarray_sum(arr, k):
    # 配列arrの長さがK未満の場合、部分配列を作れないので None を返す
    if k > len(arr):
        return None

    # 最初のウィンドウ（先頭からK要素）の合計を計算
    current_sum = sum(arr[:k])#先頭からK要素のスライス
    max_sum = current_sum

    # ウィンドウを1つずつ右にスライドしながら合計を更新
    for i in range(k, len(arr)):
        # ウィンドウに新しい要素arr[i]を加え、ウィンドウから外れる古い要素arr[i-k]を差し引く
        current_sum += arr[i] - arr[i - k]

        # 合計がこれまでの最大値を上回ったら更新
        if current_sum > max_sum:
            max_sum = current_sum

    # 計算された最大の連続部分和を返す
    return max_sum

# 使用例:
print(max_subarray_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))  # 出力: 39  （4+2+10+23 の和）