# -*- coding: utf-8 -*-
import os
import argparse

DASH_MAP = {
    '\u2013': '-',  # EN DASH
    '\u2014': '-',  # EM DASH
    '\u2212': '-',  # MINUS SIGN
}

def contains_problem_dash(name):
    return any(char in name for char in DASH_MAP)

def replace_dashes(name):
    for bad_dash, ascii_dash in DASH_MAP.items():
        name = name.replace(bad_dash, ascii_dash)
    return name

def process_directory(root_dir, fix=False):
    results = []
    for root, dirs, files in os.walk(root_dir):
        for name in dirs + files:
            full_path = os.path.join(root, name)
            if contains_problem_dash(name):
                new_name = replace_dashes(name)
                new_path = os.path.join(root, new_name)
                results.append(f"{full_path}  ← ダッシュ記号あり")
                if fix and new_path != full_path:
                    os.rename(full_path, new_path)
                    results.append(f"修正済み: {full_path} -> {new_path}")
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ダッシュ記号を検出し、ASCIIハイフンに修正するツール')
    parser.add_argument('path', help='スキャン対象ディレクトリのパス')
    parser.add_argument('--fix', action='store_true', help='自動修正を実行')
    args = parser.parse_args()

    detected = process_directory(args.path, args.fix)

    if detected:
        print("ダッシュ記号を含むファイル・フォルダ:")
        for item in detected:
            print(f" - {item}")
    else:
        print("ダッシュ記号を含むファイル・フォルダは見つかりませんでした。")
