# freetype-build

freetypeのライブラリ `freetype` を以下のターゲット向けに生成します。

- Windows: `x86`, `x64`
- Linux: `x86_64`, `aarch64`
- Android: `x86_64`, `arm64-v8a`

## ビルド

`freetype` のソース一式を以下からダウンロードします。

- <https://www.freetype.org/download.html>

`zlib` と `libpng` は以下を参考にして事前にインストールしておきます。

- <https://github.com/kota-kota/zlib-build>
- <https://github.com/kota-kota/libpng-build>

### Windows

```bash
$ python build_window.py
```

### Linux

```bash
$ python build_linux.py
```

### Android

```bash
$ python build_android.py
```
