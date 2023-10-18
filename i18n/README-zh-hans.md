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

exe 使用方法:
```
用法 :
    <无参数>
      - 以你的默认设置打开一个新的Shell。

    run <命令行>
      - 在此实例中运行你所给出的命令，继承当前Shell的所在目录。

    runp <命令行 (包含 windows 路径)>
      - 在此实例里运行转译过的命令行。

    config [setting [值]]
      - `--default-user <用户>`: 设定此实例的默认用户到 <用户>。
      - `--default-uid <uid>`: 设定此实例的默认用户 UID 到 <uid>。
      - `--append-path <on|off>`: 加入 Windows PATH 到 $PATH 的开关。
      - `--mount-drive <on|off>`: 挂载驱动器的开关。
      - `--wsl-version <1|2>`: Set the WSL version of this instance to <1 or 2>
      - `--default-term <default|wt|flute>`: 设置默认的终端窗口样式。

    get [setting]
      - `--default-uid`: 输出此实例的默认用户UID。
      - `--append-path`: 输出”加入 Windows PATH 到 $PATH“的开关状态。
      - `--mount-drive`: 输出”挂载驱动器”的开关状态。
      - `--wsl-version`: 输出此实例的WSL版本（1/2）。
      - `--default-term`: 输出此实例启动器的默认终端样式。
      - `--lxguid`: 输出此实例的 WSL GUID key。

    backup [contents]
      - `--tar`: 在当前目录输出 backup.tar 文件。
      - `--tgz`: 在当前目录输出 backup.tar.gz 文件。
      - `--vhdx`: 在当前目录输出 backup.ext4.vhdx 文件。（仅 WSL2）
      - `--vhdxgz`: 在当前目录输出 backup.ext4.vhdx.gz 文件。（仅 WSL2）
      - `--reg`: 在当前目录输出注册表配置文件。

    clean
      - 卸载此实例。

    help
      - 显示此帮助信息。
```

## 🚮删除

`eweos.exe clean`

## ⛏构建

需求: Python, 模块 `requests`。

1. 安装 python
2. 使用 pip 安装 `requests` : `python -m pip install requests`
3. 运行脚本。 `python ./build-amd64.py` 用于 AMD64。 `build-arm64.py` 用于 ARM64。

