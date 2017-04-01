# input-paste

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
接下來，設定系統熱鍵能夠執行input-paste即可

## 用法
點擊應用程式輸入框並**維持游標位置**,叫出input-paste輸入文字後

按Enter/Ctrl+Enter就會將文字貼上游標位置,或按Esc/Alt+F4關閉input-paste



[1]: https://www.sublimetext.com/3
[2]: https://www.spotify.com/tw/download/linux/
[3]: https://github.com/lyfeyaj/sublime-text-imfix
[4]: https://wiki.gnome.org/Projects/PyGObject
