# StudyLog

## 2024/3/7

1.  admin/base_site.html をadminディレクトリにコピー。  
    場所：python -c "import django; print(django.\_\_path\_\_)"
2.  Django Debug Toolbarをインストール。  
    python -m pip install django-debug-toolbar
3.  一通りチュートリアルが終わったのでいったん終了

## 2024/3/6

1. フィルターと検索を追加
2. DIRS は、Django がテンプレートを読み込む時にチェックする、ファイルシステム上のディレクトリのリスト。

## 2024/3/5

1. admin フォームのカスタマイズ  
   class ChoiceInline(admin.StackedInline):全て表示する  
   class ChoiceInline(admin.TabularInline):テーブル形式で表示する

## 2024/3/4

1. admin フォームのカスタマイズ

## 2024/3/3

1. エラーの原因はコメントアウトしていた部分だった。コメントアウトごと削除で出なくなった。
2. 背景画像が反映されなかったけどサーバー立ち上げなおしたら反映された。

## 2024/3/2

1. スタイルシートをstaticフォルダに作成。アプリケーション同様名前空間を付ける。
2. def get_queryset(self):のインデントが正しく設定されていなかったので修正。

## 2024/3/1

1. テストをどんどん追加。テストは重要らしい。エラーが出ているけどとりあえず進める。

## 2024/2/29

1. エラーかと思って見るとxxxx imported but unused だった。こういうことがよくある。
2. ショートカット関数 create_question

## 2024/2/28

1. テストを書き換えて通った。書き換え箇所を間違っていた。

## 2024/2/27

1. python manage.py shellでエラー確認
2. テスト実行python manage.py test polls

## 2024/2/26

1. エラー対策
   1. from django.views import generic　追加
   2. modelが原因かと思ってmakemigrationsしたけど違った（No changes detectedと返ってきた）

## 2024/2/25

1. results.html追加
2. URLから取得した値をプライマリーキーの値 "pk" として扱うよう変更
3. Django の汎用ビューを使用
4. 昨日のエラーは継続

## 2024/2/24

1.  viewを書き換えたけど意味がいまいちわからない…。あとエラーがでている。

## 2024/2/23

1.  リクエストIDが存在しない時404を返す書き方はget_objectもある。（get_object_or_404）
2.  アプリケーションの名前空間を設定することができる（app_name = "polls"）

## 2024/2/22

1.  リクエストIDが存在しない時404を返す。（from django.http import Http404）

## 2024/2/21

1.  /templates/pollsというように、アプリケーションと同じ名前のディレクトリにHTMLを入れる。  
    Djangoは最初に名前が一致したファイルを参照するため。

## 2024/2/20

1.  管理画面の各項目のHistoryから更新者の情報を見ることができる。
2.  Settingで言語を日本語、タイムゾーンをAsia/Tokyoに変更。管理画面も変更が反映された。

## 2024/2/19

1.  （管理者）作成。(python manage.py createsuperuseradmin)
2.  パスワードは8文字でないと警告が出る(This password is too short. It must contain at least 8 characters.)

## 2024/2/18

1. モデルの変更を実施する3ステップ
   1. モデル変更（models.py）
   2. マイグレーションを作成（ python manage.py makemigrations）
   3. データベースに変更を適用（python manage.py migrate ）
2. Pythonシェルを起動（python manage.py shell）
3. strメソッドは、オブジェクトを文字列で表現するための特殊メソッド。

## 2024/2/17

1. ファイル名ミス。  
   〇 urls.py  
   ✕ url.py
2. python manage.py migrateでテーブル作成。
3. python manage.py makemigrations polls でモデルの変更を保存。

## 2024/2/16

1. 作成
