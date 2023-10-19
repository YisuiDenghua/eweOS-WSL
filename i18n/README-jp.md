## 🐑eweOS WSLについて

[eweOS](https://os.ewe.moe/)ベースのWSLディストリビューション(Windows 10 FCU以降対応/[wsldl](https://github.com/yuk7/wsldl)ベース)

## 💻システム要件

Windows 10 1709 Fall Creators Update x64以上
Windows Subsystem for Linux機能が有効であること.

## 💾インストール

1. zipファイルを[ダウンロード](https://github.com/YisuiDenghua/eweOS-WSL/releases)
2. zip内のファイルをすべて同じ場所に展開
3. `eweos.exe`を実行してWSLにインストールします。

EXEファイル名はWSLインスタンス名として使用されます。EXEファイルの名前を変更することで、競合することなく複数のeweOSインスタンスを作成できます。

## 📝使い方

> 参照[wsldl usage reference](https://github.com/yuk7/wsldl#how-to-usefor-installed-instance).

```dos
Usage :
    <引数なし>
      - デフォルト設定で新しいシェルを起動します

    run <command line>
      - 与えられたコマンドラインをインスタンス内で実行します。 カレントディレクトリが引き継がれます。

    runp <command line (windowsのパスを含む)>
      - 与えられたコマンドラインのパスを変換した上でインスタンス内で実行します。

    config [setting [value]]
      - `--default-user <user>`: インスタンスのデフォルトユーザーを<user>に設定します。
      - `--default-uid <uid>`: インスタンスのデフォルトユーザーのuidを<uid>に設定します。
      - `--append-path <true|false>`: Windows側のPATH設定をLinux側に引き継ぐ機能のtrue/falseを設定します。
      - `--mount-drive <true|false>`: Windowsのドライブをマウントする機能のtrue/falseを設定します。
      - `--wsl-version <1|2>`: インスタンスのWSLバージョンの1/2を設定します。
      - `--default-term <default|wt|flute>`: デフォルトのターミナルを設定します。

    get [setting]
      - `--default-uid`: インスタンスのデフォルトユーザーのuidを取得します。
      - `--append-path`: Windows側のPATH設定をLinux側に引き継ぐ機能のtrue/falseを確認します。
      - `--mount-drive`: Windowsのドライブをマウントする機能のtrue/falseを確認します。
      - `--wsl-version`: WSLのバージョン(1/2)を確認します。
      - `--default-term`: このランチャーに設定されたデフォルトのターミナルを確認します。
      - `--lxguid`: システム内部で使用されているLxGUIDを取得します。

    backup [contents]
      - `--tar`: カレントディレクトリにbackup.tarを出力します。
      - `--tar`: カレントディレクトリにbackup.tarを出力します。
      - `--tgz`: カレントディレクトリにbackup.tar.gzを出力します。
      - `--vhdx`: カレントディレクトリにbackup.ext4.vhdxを出力します。 (WSL2のみ)
      - `--vhdxgz`: カレントディレクトリにbackup.ext4.vhdx.gzを出力します。 (WSL2のみ)
      - `--reg`: 設定のレジストリファイルをbackup.regとしてカレントディレクトリに出力します。
      
    clean
      - インスタンスをアンインストールします。

    help
      - helpを表示します。
```
## 🚮アンインストール 

`eweos.exe clean`

## ⛏構築

要件：Python, module `requests`.

1. Pythonをインストール
2. pipによる `requests` をインストール: `python -m pip install requests`
3. スクリプトを実行. AMD64の場合は `python ./build-amd64.py`、ARM64の場合は`build-arm64.py`
