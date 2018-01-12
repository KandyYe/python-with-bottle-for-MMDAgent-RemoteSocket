import sys
import re
from bottle import route, static_file, get, post, request, run
import socket
import threading

host = "127.0.0.1"  # お使いのサーバーのホスト名を入れます
port = 39390  # 適当なPORTを指定してあげます


clientmmd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # オブジェクトの作成をします
clientmmd.connect((host, port))  # これでサーバーに接続します

imagenum = 0
#thread1 = threading.Thread(target=recvthread, name='recvthread', args=(clientmmd,))  # 受信用スレッド作成
#thread1.start()

#while True:
#    rcvmsg = clientsock.recv(4096)
#    print(rcvmsg)
# 音声認識用スレッド作成
# t2 = threading.Thread(target=voicerecog, name='voicerecog')
# t2.start()

def sendmmd(input_line):
    global imagenum
    #input_line = input()
    #if 'end' in input_line:
        #break

    if '!' in input_line:  # !が書かれたとき右のメイちゃんが話す
        outstr = 'SYNTH_START|rapin|newvoice|' + input_line
        clientmmd.send(outstr.encode("Shift-JIS"))

    if '?' in input_line:  # ?が書かれたとき左のメイちゃんが話す
        outstr = 'SYNTH_START|sdmei|mei_voice_normal|' + input_line
        clientmmd.send(outstr.encode("Shift-JIS"))

    if '#' in input_line:  # #が入っているときメイちゃんが画面の方を向く
        outstr = 'TURN_START|rapin|-0.1,0.0,0.0|LOCAL'
        clientmmd.send(outstr.encode("Shift-JIS"))
        outstr = 'TURN_START|sdmei|0.1,0.0,0.0|LOCAL'
        clientmmd.send(outstr.encode("Shift-JIS"))

    if '$' in input_line:  # $が入っているときメイちゃんが開始時の向きに戻る
        outstr = "TURN_START|rapin|0.1,0.0,0.0|LOCAL"
        clientmmd.send(outstr.encode("Shift-JIS"))
        outstr = "TURN_START|sdmei|-0.1,0.0,0.0|LOCAL"
        clientmmd.send(outstr.encode("Shift-JIS"))

    if '.' in input_line:  # 画像表示
        outstr = "IMAGE_DELETE|hoge" + str(imagenum) + "|"
        clientmmd.send(outstr.encode("Shift-JIS"))
        imagenum += 1
        outstr = "IMAGE_ADD|hoge" + str(imagenum) + "|" + str(imagenum) + ".jpg|15,15|0,15,3.1|0,0,0|OFF"
        clientmmd.send(outstr.encode("Shift-JIS"))

        #outstr = "MOTION_ADD|rapin|mei_motion|Motion\\mei_point\\mei_point_right_top.vmd|FULL|ONCE|ON|OFF"
        #clientmmd.send(outstr.encode("Shift-JIS"))
        #outstr = "MOTION_ADD|sdmei||sd_mei_motion|Motion\\sd_mei_guide\\sd_mei_guide_normal.vmd|FULL|ONCE|ON|OFF"
        #clientmmd.send(outstr.encode("Shift-JIS"))

    if "greeting" in input_line:  # あいさつ
        outstr = "MOTION_ADD|sdmei|sdmei_greeting|Motion\\sd_mei_guts\\sd_mei_greeting.vmd|FULL|ONCE|ON|OFF"
        clientmmd.send(outstr.encode("Shift-JIS"))
        outstr = "MOTION_ADD|rapin|mei_greeting|Motion\\sd_mei_greeting\\sd_mei_greeting.vmd|FULL|ONCE|ON|OFF"
        clientmmd.send(outstr.encode("Shift-JIS"))

    if "_" in input_line:  # おわかれ
        outstr = "MOTION_ADD|sdmei|sdmei_bye|Motion\\sd_mei_bye\\sd_mei_bye.vmd|FULL|ONCE|ON|OFF"
        clientmmd.send(outstr.encode("Shift-JIS"))
        outstr = "MOTION_ADD|rapin|mei_bye|Motion\\mei_bye\\mei_bye.vmd|FULL|ONCE|ON|OFF"
        clientmmd.send(outstr.encode("Shift-JIS"))

    if ">" in input_line:  # 右にメイちゃん回転
        outstr = "ROTATE_START|rapin|0.0,-15.0,0.0|GLOBAL"
        clientmmd.send(outstr.encode("Shift-JIS"))

    if "<" in input_line:  # 左にメイちゃん回転
        outstr = "ROTATE_START|rapin|0.0,-55.0,0.0|GLOBAL"
        clientmmd.send(outstr.encode("Shift-JIS"))

    if "-" in input_line:  # 戻す
        outstr = "ROTATE_START|rapin|0.0,-35.0,0.0|GLOBAL"
        clientmmd.send(outstr.encode("Shift-JIS"))

    #clientmmd.close()