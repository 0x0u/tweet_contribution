![Scheduler](https://github.com/0x0u/tweet_contribution/workflows/Scheduler/badge.svg?branch=master)
# tweet_contribution
GithubActionsのCronJobsを使い毎日定時にGithubのContribution数をツイートするやつ

## Demo
![](https://user-images.githubusercontent.com/34241526/77849570-aa8e2000-7207-11ea-84f2-d59e7cd1b0df.png)

## Requirement
以下のURLからTwitterのアクセストークンを取得する  
TwitterDeveloper: https://developer.twitter.com/en

## Usage
### 1. リポジトリのフォーク
当リポジトリをフォーク
### 2. 環境変数の追加
Setting > Seacret > Add a new seacret でGithubのIDと取得したTwitterトークンを追加
```
GH_ID: "***********"
CONSUMER_KEY: "***********"
CONSUMER_SECRET: "***********"
ACCESS_TOKEN: "***********"
ACCESS_TOKEN_SECRET: "***********"
```
### 3. ツイートする時刻の設定
デフォルトでは23:50(JST)に設定されている  
変更する場合は`tweet_contribution/.github/workflows/main.yml`の`cron`部を書き換える  
GithubのタイムゾーンがUTCでなので日本時間の0:00に実行する場合、ここから9時間引いて `"０ 15 * * *"`とする必要がある
