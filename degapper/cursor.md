# Pythonソースコード分析ツール

このプロジェクトは、Pythonのソースコードを分析するためのツールセットです。コードの構造分析、メトリクス計算、可視化などの機能を提供します。

## 環境要件

- Python 3.12
- 必要なパッケージは `require.txt` に記載されています
- インストール方法：
  ```bash
  pip install -r require.txt
  ```

## ファイル構成

### メインスクリプト

1. `parse_tree.py`
   - 機能：Pythonソースコードの構文木を解析
   - 入力：Pythonソースコードのディレクトリパス
   - 出力：解析結果を標準出力に出力

2. `degapper.py`
   - 機能：コードの構造を分析し、ギャップを特定
   - 入力：parse_tree.pyの出力
   - 出力：分析結果を標準出力に出力

3. `count_major_minor.py`
   - 機能：メジャー要素とマイナー要素の数をカウント
   - 入力：degapper.pyの出力
   - 出力：カウント結果を標準出力に出力

4. `draw_gap_graph.py`
   - 機能：ギャップの分析結果をグラフ化
   - 入力：count_major_minor.pyの出力
   - 出力：グラフ画像ファイル

5. `calc_metrics.py`
   - 機能：コードのメトリクスを計算
   - 入力：Pythonソースコードのディレクトリパス
   - 出力：CSV形式のメトリクス計算結果
   - 計算するメトリクス：
     - LOC (Lines of Code): コードの行数（空行を除外）
     - CC (Cyclomatic Complexity): 循環的複雑度（lizardライブラリを使用）
     - HV (Halstead Volume): ハルステッドの複雑度（オペレータとオペランドの統計に基づく）
     - MI (Maintainability Index): 保守性指標（0-100のスケール、高いほど保守性が高い）
   - 実行方法：
     ```bash
     # 基本的な実行方法
     python calc_metrics.py 分析対象のディレクトリパス

     # 小数点以下の桁数を指定する場合
     python calc_metrics.py 分析対象のディレクトリパス -dpd 2
     ```
   - 注意点：
     - 分析対象のディレクトリ内のPythonファイル（`*.py`）を再帰的に検索
     - ファイル名が`数字4桁 + pまたはq + .py`のパターンに一致するファイルのみを分析
     - 出力は標準出力にCSV形式で出力（file,loc,cc,hv,mi）
     - MIは0-100のスケールで出力され、高いほど保守性が高いことを示します
     - HVが0の場合は特別な処理が行われ、MIの計算が調整されます

6. `to_excel.py`
   - 機能：分析結果をExcelファイルに出力
   - 入力：各種分析結果
   - 出力：Excelファイル

7. `nested_structure.py`
   - 機能：コードのネスト構造を分析
   - 入力：Pythonソースコード
   - 出力：ネスト構造の分析結果

8. `learn_components.py`
   - 機能：コードのコンポーネントを学習・分析
   - 入力：Pythonソースコード
   - 出力：コンポーネント分析結果

### tools/ ディレクトリ

1. `Visitor.py`
   - 機能：ASTビジターの実装
   - 用途：構文木の走査に使用

2. `utils.py`
   - 機能：ユーティリティ関数の集まり
   - 用途：共通の補助機能を提供

3. `calcHV.py`
   - 機能：Halstead Volumeの計算
   - 用途：コードの複雑性メトリクス計算

4. `calcCC.py`
   - 機能：Cyclomatic Complexityの計算
   - 用途：コードの複雑性メトリクス計算

## 使用例

### 基本的な使用フロー
```bash
python parse_tree.py class_folder_path | python degapper.py | python count_major_minor.py | python draw_gap_graph.py
```

このコマンドは以下の処理を行います：
1. 指定されたフォルダ内のPythonコードを解析
2. コードの構造を分析してギャップを特定
3. メジャー要素とマイナー要素の数をカウント
4. 結果をグラフ化

### メトリクス計算の使用例
```bash
# 小数点以下2桁まで表示
python calc_metrics.py 分析対象ディレクトリ -dpd 2

# 出力例
file,loc,cc,hv,mi
/path/to/file.py,100,5,1234.56,78.90
```

## 注意事項

- 各スクリプトは標準入出力を使用して連携します
- パイプ（|）を使用してスクリプトを連結することで、より複雑な分析が可能です
- グラフ出力にはmatplotlibを使用し、日本語フォントのサポートを含みます
- `calc_metrics.py`は特定のファイル名パターン（数字4桁 + pまたはq + .py）に一致するファイルのみを分析します

## 更新履歴

- 2024-06-XX: calc_metrics.pyのファイル検索パターンを修正し、サブディレクトリではなく指定ディレクトリ直下の*.pyファイルを対象とするように変更しました。
  - 修正前: files = glob(f"{args.dir}/*/*.py")
  - 修正後: files = glob(f"{args.dir}/*.py")
- 2024-06-XX: tools/calcHV.pyの引数名スペルミス（isOreElse→isOrElse）を修正し、TypeErrorが発生しないようにしました。
  - 修正前: self.visit(node=item, nodes=nodes, route=route, isFirst=isFirst, isOreElse=True)
  - 修正後: self.visit(node=item, nodes=nodes, route=route, isFirst=isFirst, isOrElse=True)
- 2024-06-XX: info1およびinfo2配下のすべての*.pyファイルを含むディレクトリについて、メトリクスCSV一括出力に対応しました。 