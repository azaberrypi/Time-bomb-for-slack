# Time-bomb-for-slack
enjoy with Slack's api, chat.scheduleMessage, etc

## 目標
Cloudflare等を用いて、特定のコマンドをSlackに入力するとBotと会話形式でリマインダーを設定できるようにすること。

## 概要（現状）
cheap_bomb_creater.pyにて、利用予定のSlack Web APIのいくつかのmethodの動作確認をしました。
cheap_bomb_creater.pyでは<br>
"リマインダー"等のテキストを特定チャンネルで発言した後、<br>
・リマインダーを流したいチャンネルID<br>
・リマインダーのテキスト<br>
・リマインダーを流したい時刻のUnixtime<br>
を順番に書き込むことで、cheap_bomb_creater.py実行時にそのテキストの並びを見つけてリマンインダーを作成してくれます。<br>
エラーが起きた時やキャンセルと書きこまれた時の動作もしておらず、Unixtimeで時間指定させる等利用者のことを全く考えてない雑なバージョンです。<br>


## python-slack-sdk

https://github.com/slackapi/python-slack-sdk

```
The MIT License (MIT)

Copyright (c) 2015-2016 Slack Technologies, Inc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```
