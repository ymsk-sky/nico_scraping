# ニコニコ動画スクレイピング

## 元動画を取得

`selenium` で一度動画ページを読み込み、元動画のインスタンスを生成する。

動画プレイヤーを操作してソースURLを取得する。

## 動画を再生

`OpenCV` で動画をフレームごとに取得してから連続表示することで再生。


# 今後

## OpenCVで解析

画像解析により動画の必要部分のみを切り出す（再生時間を取得する）。

## ニコニコAPIで動画を検索

キーワード検索でヒットした動画URLを収集する。

## Webページ作成

データベースで動画URL, 再生時間, etc. を管理してそれを表示する。

オンマウスで切り出した部分を再生させる。
