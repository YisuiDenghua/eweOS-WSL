## 🐑关于

WSL 的[eweOS](https://os.ewe.moe/) 封装, 基于 [wsldl](https://github.com/yuk7/wsldl)。

## 💻系统需求

Windows 10 1709 或更高版本（x64/arm64）。
已经开启适用于 Linux 的 Windows 子系统（WSL）功能。


## 💾安装

1. 从 [Release](https://github.com/YisuiDenghua/eweOS-WSL/releases) 下载 zip 安装包。
2. 解压缩 zip 文件中的全部内容到相同的目录。
3. 运行 `eweos.exe` 以安装 rootfs 和注册表配置

EXE 文件名可用作 WSL 实例名称。可通过重命名 EXE 文件以创建多个 eweOS 实例，且互不冲突。

## 📝用途

> 参见 [wsldl usage reference](https://github.com/yuk7/wsldl#how-to-usefor-installed-instance).

exe usage:
```
Usage :
    <no args>
      - Open a new shell with your default settings.

    run <command line>
      - Run the given command line in that instance. Inherit current directory.

    runp <command line (includes windows path)>
      - Run the given command line in that instance after converting its path.

    config [setting [value]]
      - `--default-user <user>`: Set the default user of this instance to <user>.
      - `--default-uid <uid>`: Set the default user uid of this instance to <uid>.
      - `--append-path <true|false>`: Switch of Append Windows PATH to $PATH
      - `--mount-drive <true|false>`: Switch of Mount drives
      - `--wsl-version <1|2>`: Set the WSL version of this instance to <1 or 2>
      - `--default-term <default|wt|flute>`: Set default type of terminal window.

    get [setting]
      - `--default-uid`: Get the default user uid in this instance.
      - `--append-path`: Get true/false status of Append Windows PATH to $PATH.
      - `--mount-drive`: Get true/false status of Mount drives.
      - `--wsl-version`: Get the version os the WSL (1/2) of this instance.
      - `--default-term`: Get Default Terminal type of this instance launcher.
      - `--lxguid`: Get WSL GUID key for this instance.

    backup [contents]
      - `--tar`: Output backup.tar to the current directory.
      - `--tgz`: Output backup.tar.gz to the current directory.
      - `--vhdx`: Output backup.ext4.vhdx to the current directory. (WSL2 only)
      - `--vhdxgz`: Output backup.ext4.vhdx.gz to the current directory. (WSL2 only)
      - `--reg`: Output settings registry file to the current directory.

    clean
      - Uninstall that instance.

    help
      - Print this usage message.
```

## 🚮删除

`eweos.exe clean`

## ⛏构建

需求: Python, 模块 `requests`。

1. 安装 python
2. 使用 pip 安装 `requests` : `python -m pip install requests`
3. 运行脚本。 `python ./build-amd64.py` 用于 AMD64。 `build-arm64.py` 用于 ARM64。

