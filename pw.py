#! python3
#pw.py パスワード管理ツール
#coding:utf-8
PASSWORDS = {"sniper" : "sniper!@#1","root":"sniper!#@$","test":"test"}
import sys
import pyperclip
if len(sys.argv)<2:
    print("使い方: python pw.py[アカウント名]")
    print("パスワードをクリップボードにコピー")
    sys.exit()

account = sys.argv[1]
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(account + "コピー成功")
else:
    print(account + "コピー失敗")

