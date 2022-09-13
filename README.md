# PyDB-SQL

このリポジトリでは，Python から SQL ベースのデータベース (ここでは MySQL を想定) を操作し，
データ管理するための Python ライブラリを開発する．

## 開発環境の操作

### MySQL Server

MySQL Server コンテナの取り扱い

- 起動
  ```
  ./docker_srv/docker_run_mysql.sh
  ```
  ※ ログ情報など，起動中のメッセージを取得したい場合は，shell の -d オプションを外すこと．
- 起動中コンテナの確認
  ```
  docker ps
  ```
- コンテナの削除
  ```
  docker rm -f <CONTAINER ID>
  ```

### MySQL Server Client

起動したコンテナは様々なアプリケーションから接続できる．
例えば，GUI アプリなら MySQL Workbench，
コマンドラインなら mysql-client，
プログラムで Python のライブラリから接続するなら `mysql.connector` がある．

アプリケーションでの接続は `docker/docker_run_with_console.sh` に記載の通り，
下記の設定で接続できる．

- ログインユーザ
  - root user で接続する場合
    ```
    user name: root
    pass: rootpass
    port: 3306
    ```
  - test user で接続する場合
    ```
    user name: testuser
    pass: testpass
    port: 3306
    ```

### Python 環境

#### 初期化
- docker のビルド
  ```bash
  ./docker/build.sh
  ```

#### 使い方
- テストの実行
  ```bash
  ./run_test.sh
  ```
- 特定のテストだけ実行
  ```bash
  ./run_test.sh test/test_xxx.py
  ```
