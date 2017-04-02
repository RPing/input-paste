# input-paste

<img src="screenshot/input.gif" />

## 緣起
在linux平台上，有一些桌面應用程式會遇到不能打中文的情況，像是[Sublime Text][1]、[Spotify][2]

在不去對應用程式做hack的情況下(像是[這個][3])

就只能用最簡單的copy-paste方法了

這個非常簡單的小工具就是跳出小方塊讓你輸入並自動貼上

## 相依性
* GTK+ 3
* [PyGObject (aka PyGI)][4]
* Xlib Python binding
* Python 2.7+

## 安裝
以下示範是在debian/ubuntu上(其他版本將相依性安裝即可)

if run in python2:
```bash
$ sudo apt-get install python-gi python-xlib
$ pip install input-paste
```

if run in python3:
```bash
$ sudo apt-get install python3-gi python3-xlib
$ pip install input-paste
```
接下來，設定系統熱鍵能夠執行`input-paste`即可

## 用法
點擊應用程式輸入框並**維持游標位置**,叫出`input-paste`輸入文字後

按Enter/Ctrl+Enter就會將文字貼上游標位置,或按Esc/Alt+F4關閉`input-paste`

---
## Motivation
Sometimes, we can't type Chinese in application on Linux(or UNIX-like) system.

Without hacking it in low-level(like [this][3]), we should utilize clipboard to solve this problem.

This tool will bring convenience to you.

## Dependency
* GTK+ 3
* [PyGObject (aka PyGI)][4]
* Xlib Python binding
* Python 2.7+

## Installation
Following is on debian/ubuntu system.

if run in python2:
```bash
$ sudo apt-get install python-gi python-xlib
$ pip install input-paste
```

if run in python3:
```bash
$ sudo apt-get install python3-gi python3-xlib
$ pip install input-paste
```
Next, set up hotkey in your system to execute `input-paste`.

## Usage
Click input box in your application, and **retain the cursor position**.

Invoke `input-paste` with hotkey, and type some words in it.

Press Enter/Ctrl+Enter to copy text to your cursor position,

or press Esc/Alt+F4 to close `input-paste`.

[1]: https://www.sublimetext.com/3
[2]: https://www.spotify.com/tw/download/linux/
[3]: https://github.com/lyfeyaj/sublime-text-imfix
[4]: https://wiki.gnome.org/Projects/PyGObject
