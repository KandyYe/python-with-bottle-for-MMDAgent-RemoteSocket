# -*- coding: utf-8 -*-

import re;

# 理解不能返信の判別用
rx01 = re.compile('理解できない')
rx02 = re.compile('もう一度')

# 正常な返信の判別用
rx10 = re.compile('の天気は(.+?)です')
rx11 = re.compile('どこの天気')

# 想定パタン
rx20 = re.compile('\s*(.+?)(の|-)((.+?)の)?天気')

# 時点表現
rx30 = re.compile('(今日|明日|昨日|あさって)')


def respond_to(msg):
    # 自分自身の返信メッセージならば無言の返信を行う。
    m0 = rx01.search(msg)
    if m0:
        return '';
    m0 = rx02.search(msg)
    if m0:
        return '';

    m1 = rx10.search(msg)
    if m1:
        return '';
    m1 = rx11.search(msg)
    if m1:
        return '';

    # 想定したメッセージのパタンにマッチするか判定する。
    m2 = rx20.search(msg)
    rpl = ''
    if m2:
        # マッチした場合
        p2 = m2.group(1)
        t2 = m2.group(4)

        # 時点が先行しているケースの場合
        m3 = rx30.search(p2)
        if m3:
            return 'どこの%sの天気ですか？' % p2

        if not t2:
            t2 = "今日"
        rpl = p2 + 'の' + t2 + 'の天気は晴れです'
    else:
        # マッチしない場合
        rpl = '「%s」は理解できないので、もう一度、どこのいつの天気か、はっきりたずねてください。' % msg

    return rpl