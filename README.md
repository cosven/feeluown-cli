# feeluown cli


## Usage

```python

@cmd('create_playlist')
def create_playlist(name):
    pass
```

## 大致的设计描述

1. 用类似目录结构（文件系统）的方式来组织音乐资源

## Design Considerations

### 命令行的哪种模式？

- REPL (mycli)
- fullscreen (rtv, mutt)
- shell command (hn)

理想是 REPL + fullscreen 模式。
播放器的状态显示理论上应该是一直存在的...
但是搜索歌曲、添加/删除歌曲等应该都是命令形式的...

### 用虚拟的还是实际的文件系统

### virtual fs

```
(root) Providers/
├── Netease
│   ├── Authors
│   │   └── ZhouJielun
│   │       ├── Albums
│   │       │   └── ($hash) 我很忙
│   │       └── HotSongs
│   └── Users
│       ├── (~) cosven
│       │   ├── Followers
│       │   ├── Following
│       │   │   └── miao -> /Netease/Users/miao/
│       │   └── Playlists
│       │       ├── cosven 喜欢的歌曲
│       │       │   ├── -
│       │       │   ├── Jaymay
│       │       │   └── see\ green,\ see\ blue
│       │       └── $(hash) 安安静静的
│       └── miao
├── Qq
└── Xiami
```

### commands

```shell
pwd  # show current context
cd ~  # context: user/
ls  # show all playlists
cd $favorite  # context: user/playlist/
ls  # show all songs
play $fc  # play music by id
```

### 一些习惯性的按键设置

- `X` -> selection (mutt, emacs(package-list-packages), )
