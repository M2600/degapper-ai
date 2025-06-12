●環境
　Python3.12

●環境構築
　require.txtに書いてあるものを一式インストールする。
　以下のコマンドで一括インストールできる。
　pip install -r require.txt

●使い方
　各プログラムをコマンドラインのパイプで繋いでいく。
　
　例：メジャー要素数とマイナー要素数の累積グラフを出したいとき
　python parse_tree.py class_folder_path | python degapper.py | python count_major_minor.py | python draw_gap_graph.py

