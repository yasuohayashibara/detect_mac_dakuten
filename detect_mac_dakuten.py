# -*- coding: utf-8 -*-
import os
import unicodedata
import argparse

def is_nfd_form(name):
    """
    ファイル名がNFC形式でない（= NFD形式など）かを判定
    """
    return name != unicodedata.normalize('NFC', name)

def convert_to_nfc(path):
    """
    ファイルまたはフォルダ名をNFC形式に変換してリネーム
    """
    dirname, basename = os.path.split(path)
    nfc_basename = unicodedata.normalize('NFC', basename)
    new_path = os.path.join(dirname, nfc_basename)

    # 名前が異なる場合のみリネーム実行
    if new_path != path:
        os.rename(path, new_path)
        return new_path
    else:
        return path  # 変更なし

def process_directory(root_dir, fix=False):
    """
    ディレクトリ内のファイル・フォルダ名を再帰的にスキャンしてNFD名を検出・修正
    """
    results = []
    for root, dirs, files in os.walk(root_dir):
        entries = dirs + files
        for name in entries:
            full_path = os.path.join(root, name)
            if is_nfd_form(name):
                results.append(full_path)
                if fix:
                    new_path = convert_to_nfc(full_path)
                    if new_path != full_path:
                        results.append(f'修正済み: {full_path} -> {new_path}')
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mac由来のNFDファイル名を検出・修正するツール')
    parser.add_argument('path', help='スキャン対象ディレクトリのパス')
    parser.add_argument('--fix', action='store_true', help='検出した問題を自動修正する')
    args = parser.parse_args()

    detected = process_directory(args.path, args.fix)

    if detected:
        print("検出されたNFD形式のファイル・フォルダ:")
        for item in detected:
            print(f' - {item}')
    else:
        print("問題となるファイル・フォルダは見つかりませんでした。")
