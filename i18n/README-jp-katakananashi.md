## 🐑eweOS WSLについて

[eweOS](https://os.ewe.moe/)に基づくWSL分布(Windows 10 FCU以降対応/[wsldl](https://github.com/yuk7/wsldl)ベース)

## 💻系統要件

Windows 10 1709 Fall Creators Update x64以上
Windows Subsystem for Linux機能が有効であること.

## 💾導入

1. zip文件を[取得](https://github.com/YisuiDenghua/eweOS-WSL/releases)
2. zip内の文件をすべて同じ場所に展開
3. `eweos.exe`を実行してWSLに導入します。

EXE文件名はWSL実例名として使用されます。EXE文件名を変更することで、競合することなく複数のeweOS実例を作成できます。

## 📝使い方

> 参照[wsldl usage reference](https://github.com/yuk7/wsldl#how-to-usefor-installed-instance).

```dos
Usage :
    <引数なし>
      - 既定設定で新しいShellを起動します

    run <command line>
      - 与えられた命令を実例内で実行します。 現在の文件集が引き継がれます。

    runp <command line (windowsのパスを含む)>
      - 与えられた命令行の路径を変換した上で実例内で実行します。

    config [setting [value]]
      - `--default-user <user>`: 実例の既定使用者を<user>に設定します。
      - `--default-uid <uid>`: 実例の既定使用者のuidを<uid>に設定します。
      - `--append-path <true|false>`: Windows側のPATH設定をLinux側に引き継ぐ機能のtrue/falseを設定します。
      - `--mount-drive <true|false>`: Windowsの駆動機をマウントする機能のtrue/falseを設定します。
      - `--wsl-version <1|2>`: 実例のWSL版本の1/2を設定します。
      - `--default-term <default|wt|flute>`: 既定のTerminalを設定します。

    get [setting]
      - `--default-uid`: 実例の既定使用者のuidを取得します。
      - `--append-path`: Windows側のPATH設定をLinux側に引き継ぐ機能のtrue/falseを確認します。
      - `--mount-drive`: Windowsの駆動機をマウントする機能のtrue/falseを確認します。
      - `--wsl-version`: WSLの版本(1/2)を確認します。
      - `--default-term`: この起動器に設定された既定のTerminalを確認します。
      - `--lxguid`: 系統内部で使用されているLxGUIDを取得します。

    backup [contents]
      - `--tar`: 現在の文件集にbackup.tarを出力します。
      - `--tar`: 現在の文件集にbackup.tarを出力します。
      - `--tgz`: 現在の文件集にbackup.tar.gzを出力します。
      - `--vhdx`: 現在の文件集にbackup.ext4.vhdxを出力します。 (WSL2のみ)
      - `--vhdxgz`: 現在の文件集にbackup.ext4.vhdx.gzを出力します。 (WSL2のみ)
      - `--reg`: 設定の現在の文件集をbackup.regとして現在文件集に出力します。
      
    clean
      - 実例を抹消します。

    help
      - helpを表示します。
```
## 🚮削除

`eweos.exe clean`

## ⛏構築

要件：Python, module `requests`.

1. Pythonを準備する
2. pipによる `requests` を取得する: `python -m pip install requests`
3. Scriptを実行. AMD64の場合は `python ./build-amd64.py`、ARM64の場合は`build-arm64.py`
