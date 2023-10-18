# eweOS WSL

![图片](https://github.com/YisuiDenghua/eweOS-WSL/assets/102890144/7eab9cb5-35b4-48b5-961d-504cb798a946)

[日本語](i18n/README-jp.md) | [简体中文](i18n/README-zh-hans.md)

## 🐑About

[eweOS](https://os.ewe.moe/) on WSL, based on [wsldl](https://github.com/yuk7/wsldl).

## 💻Requirements

Windows 10 1709 Fall Creators Update or later(x64/arm64).
Windows Subsystem for Linux feature is enabled.


## 💾Install

1. Download the zip from [releases](https://github.com/YisuiDenghua/eweOS-WSL/releases).
2. Extract all files in zip file to same directory
3. Run `eweos.exe` to extract rootfs and register to WSL

Exe filename is used as WSL instance name - you can rename it to create multiple installations.

## 📝Usage

> [wsldl usage reference](https://github.com/yuk7/wsldl#how-to-usefor-installed-instance).

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

## 🚮Uninstall

`eweos.exe clean`

## ⛏Build

Requirements: Python, module `requests`. 

1. Install python
2. Install `requests` via pip: `python -m pip install requests`
3. Run the script. `python ./build-amd64.py` for AMD64 or `build-arm64.py` for ARM64

