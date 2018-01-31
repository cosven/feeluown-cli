# feeluown cli
_Python3 only._

## Install

```shell
pip install fuocli --upgrade
```

## Usage

```python
fuocli status  # 查看播放器状态
fuocli add fuo://netease/songs/408814900   # 将一首歌添加到当前播放列表
fuocli play fuo://netease/songs/408814900  # 播放一首歌
fuocli search "周杰伦 - 晴天"  # 搜索歌曲
fuocli show fuo://netease/songs/408814900  # 查看一首歌的详细信息
fuocli show fuo://netease/users/18731323  # 展示一个用户的详细信息
fuocli show fuo://netease/playlists/80263692  # 展示一个播放列表的详细信息
```

## TODO

- [ ] 加入 help 命令
- [ ] 更加友好的提示
- [ ] 命令自动补全

## FQA

#### 提示 What? are you kidding?
说明你当前使用的命令是存在，但是使用方法错误

#### 提示 Unknown Command
当前使用的命令不存在
