# feeluown cli


## Usage

```python

@cmd('create_playlist')
def create_playlist(name):
    pass
```

## Examples

```
> create_playlist 'My Love'

> play 'My Love'
> play 晴天

> resume
> pause
> stop
> seek 2:34
```

## 大致的设计描述

1. 用类似目录结构（文件系统）的方式来组织音乐资源

## Design Considerations

### 用虚拟的还是实际的文件系统

## 命令设计

### virtual fs

```
(root) Providers/
├── Netease
│   ├── Authors
│   │   └── ZhouJielun
│   │       ├── Albums
│   │       │   └── ($ac) 我很忙
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
│       │       └── $(bs) 安安静静的
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
