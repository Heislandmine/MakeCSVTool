# これは何

指定したディレクトリ配下のフォルダ・ファイルの情報を取得し、一覧をCSVファイルとして出力するTOOLです。

[使用例]
```
MainCLI.py [対象ディレクトリ] [CSVファイル出力先ディレクトリ]
```

# CSVファイルレイアウト

```
FolderName,FileName,FileSize,LastWriteDate # ヘッダー行
/hoge/hoge, hoge, 1234, 2019-11-30 21:03:22.01962 
...
..
.
```
