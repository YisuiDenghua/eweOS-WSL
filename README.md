# eweOS WSL

![图片](https://github.com/YisuiDenghua/eweOS-WSL/assets/102890144/7eab9cb5-35b4-48b5-961d-504cb798a946)


## About

[eweOS](https://os.ewe.moe/) on WSL, based on [wsldl](https://github.com/yuk7/wsldl).

## Installing

1. Download the zip from releases.
2. Extract all files in zip file to same directory
3. Run `eweos.exe` to extract rootfs and register to WSL

Exe filename is used as WSL instance name - you can rename it to create multiple installations.

## Usage

Refer to the [wsldl usage reference](https://github.com/yuk7/wsldl#how-to-usefor-installed-instance).

## Build

Requirements: Python, module `requests`. 

1. Install python
2. Install `requests` via pip: `python -m pip install requests`
3. Run the script. `python ./build-amd64.py` for AMD64 or `build-arm64.py` for ARM64

