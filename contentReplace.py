import os
import re
import codecs

# 置換処理設定
reg_text = r'^\\'
replace_text = '..\\\\'
target_ext = '.m3u'

# ファイル一覧取得
target_path = os.getcwd()
files = os.listdir(target_path)

for file in files:
   if target_ext in file:
        f = codecs.open(os.path.join(target_path ,file), 'r','utf-8')
        file_path = []
        #指定ファイル内容置換処理
        for row in f:
            str = row.rstrip()
            str = str.replace('\ufeff','') # 不要な文字削除
            str = re.sub(reg_text,replace_text,str) #正規表現置換
            file_path.append(str)

        # 上書き書き込み
        with open(os.path.join(target_path ,file),'w',encoding = 'utf-8') as f:
            f.write("\n".join(file_path))
        print("修正完了:{}".format(file))
        f.close

