<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## ファイル名修正ツール（macOS由来の問題対応）

### 概要

このリポジトリには、macOS環境で作成されたファイル名に起因する文字コードや特殊記号の問題を検出・修正するための2つのPythonスクリプトが含まれています。

- `detect_mac_dakuten.py`: 分離濁点（NFD形式）を検出し、標準的なNFC形式に修正
- `detect_mac_haihun.py`: Windowsで文字化けしやすい特殊なダッシュ記号（EN DASH、EM DASH、MINUS SIGN）をASCIIハイフン（`-`）に置換

---

### 動作環境

- Python 3.x
- OS: macOS, Windows, Linux いずれでも使用可能（macOS由来の問題を修正する目的）

---

### 使用方法

**1. 分離濁点（NFD形式）の検出・修正**

```bash
python detect_mac_dakuten.py <対象ディレクトリのパス> [--fix]
```

- `--fix` をつけると、NFC形式に自動変換してリネームします。
- 修正なしで検出だけを行いたい場合は `--fix` を省略します。

例：

```bash
python detect_mac_dakuten.py ./test_folder --fix
```


---

**2. 特殊ダッシュ記号の検出・修正**

```bash
python detect_mac_haihun.py <対象ディレクトリのパス> [--fix]
```

- `--fix` をつけると、全ての非ASCIIダッシュ記号（EN DASH、EM DASH、MINUS SIGN）を `-` に置換します。

例：

```bash
python detect_mac_haihun.py ./test_folder --fix
```


---

### 出力例

**検出時：**

```bash
ダッシュ記号を含むファイル・フォルダ:
 - ./test_folder/資料\u2013最終版.pdf  ← ダッシュ記号あり
```

**修正時：**

```bash
修正済み: ./test_folder/資料\u2013最終版.pdf -> ./test_folder/資料-最終版.pdf
```


---

### 注意点

- リネーム処理はファイル・フォルダに直接適用されます。実行前にバックアップを取ることを推奨します。
- Unicodeに敏感なファイルシステム（特にmacOS）と、Windows間でのファイル共有において発生する問題に対応しています。

