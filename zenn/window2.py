#文字列sの中で異なる文字が最大k種類までの連続部分文字列
def longest_substring_at_most_k_distinct(s, k):
    # 異なる文字を許容する数Kが0の場合、結果は空文字列
    if k == 0:
        return ""

    n = len(s)
    char_count = {}   # ウィンドウ内の各文字の出現回数を記録する辞書
    left = 0          # ウィンドウの左端インデックス
    max_length = 0    # 発見した最長部分文字列の長さ
    longest_substr = ""  # 発見した最長部分文字列そのもの

    # 右端のインデックスrightを動かしながらウィンドウを拡大
    for right in range(n):
        char = s[right]
        # 文字charをウィンドウに追加（カウントを更新）
        char_count[char] = char_count.get(char, 0) + 1
        #.get(key,default)は、keyが辞書に存在しない場合defaultを返す

        # ウィンドウ内の異なる文字数がKを超えている間、左端を動かして調整
        while len(char_count) > k:
            left_char = s[left]
            # 左端の文字をウィンドウから除去（カウント減少）
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                # 出現回数が0になった文字は辞書から削除（異なる文字数が1つ減る）
                del char_count[left_char]
            left += 1  # ウィンドウの左端を右に1つ動かす

        # 現在のウィンドウ[s[left:right+1]]は異なる文字数がK個以内に収まっている
        # ウィンドウのサイズ（right - left + 1）がこれまでの最大より大きければ更新
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            longest_substr = s[left:right+1]

    # 見つかった最長の部分文字列を返す（長さではなく文字列そのものを返す実装）
    return longest_substr

# 使用例:
print(longest_substring_at_most_k_distinct("abcbdbdbbdcdabd", 2))  # 出力: "bdbdbbd"