# 実行モジュール
import MakeCSV
import sys
import os.path

if len(sys.argv) < 3:
    print("引数に誤りがあります。")
    exit()

input_path = sys.argv[1]
output_path = sys.argv[2]

if os.path.exists(input_path):
    if os.path.exists(output_path):
        if os.path.isdir(input_path):
            if os.path.isdir(output_path):
                # メイン処理の実行
                csv_maker = MakeCSV.MakeCSV(input_path, output_path)
                result = csv_maker.make_csv()
                print("抽出数:{}".format(result))
            else:
                print("出力先がディレクトリではありません。")
        else:
            print("入力がディレクトリではありません。")
    else:
        print("出力先ディレクトリが存在しません。")
else:
    print("入力ディレクトリが存在しません。")