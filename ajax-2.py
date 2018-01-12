# -*- coding: utf-8 -*-
import sys
from bottle import route, static_file, get, post, request, run
import socket
import threading
from connectmmd import sendmmd;

@route('/<file>')
def callback(file):

    return static_file(file, root='./')


@get('/test')
def test():
    return '''


    <!--質問：<input type="text" size=60 id="query-id" bgcolor="red">-->
            <!--<input type="button" value="Send" onclick="send_query_message()" /><br>-->
    <!--応答：<input type="text" size=60 id="reply-id"><br>-->

    <!--<input type="button" value="Stop" onclick="recognition.stop()" />-->
    <!--<input type="button" value="Restart" onclick="recognition.start()" /><br>-->

    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence1">
            <input type="button" value="Send" onclick="send_button_message(1)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence2">
            <input type="button" value="Send" onclick="send_button_message(2)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence3">
            <input type="button" value="Send" onclick="send_button_message(3)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence4">
            <input type="button" value="Send" onclick="send_button_message(4)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence5">
            <input type="button" value="Send" onclick="send_button_message(5)" /><br>  
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence6">
            <input type="button" value="Send" onclick="send_button_message(6)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence7">
            <input type="button" value="Send" onclick="send_button_message(7)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence8">
            <input type="button" value="Send" onclick="send_button_message(8)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence9">
            <input type="button" value="Send" onclick="send_button_message(9)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence10">
            <input type="button" value="Send" onclick="send_button_message(10)" /><br>  
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence11">
            <input type="button" value="Send" onclick="send_button_message(11)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence12">
            <input type="button" value="Send" onclick="send_button_message(12)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence13">
            <input type="button" value="Send" onclick="send_button_message(13)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence14">
            <input type="button" value="Send" onclick="send_button_message(14)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence15">
            <input type="button" value="Send" onclick="send_button_message(15)" /><br>  
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence16">
            <input type="button" value="Send" onclick="send_button_message(16)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence17">
            <input type="button" value="Send" onclick="send_button_message(17)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence18">
            <input type="button" value="Send" onclick="send_button_message(18)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence19">
            <input type="button" value="Send" onclick="send_button_message(19)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence20">
            <input type="button" value="Send" onclick="send_button_message(20)" /><br>  
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence21">
            <input type="button" value="Send" onclick="send_button_message(21)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence22">
            <input type="button" value="Send" onclick="send_button_message(22)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence23">
            <input type="button" value="Send" onclick="send_button_message(23)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence24">
            <input type="button" value="Send" onclick="send_button_message(24)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence25">
            <input type="button" value="Send" onclick="send_button_message(25)" /><br>  
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence26">
            <input type="button" value="Send" onclick="send_button_message(26)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence27">
            <input type="button" value="Send" onclick="send_button_message(27)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence28">
            <input type="button" value="Send" onclick="send_button_message(28)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence29">
            <input type="button" value="Send" onclick="send_button_message(29)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence30">
            <input type="button" value="Send" onclick="send_button_message(30)" /><br>  
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence31">
            <input type="button" value="Send" onclick="send_button_message(31)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence32">
            <input type="button" value="Send" onclick="send_button_message(32)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence33">
            <input type="button" value="Send" onclick="send_button_message(33)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence34">
            <input type="button" value="Send" onclick="send_button_message(34)" /><br>
    <input type="text" value="!:こんにちは、それでは機械学習の授業を始めるよ" size=60 id="sentence35">
            <input type="button" value="Send" onclick="send_button_message(35)" /><br>                                                                          

    <script src="ajax.js"></script>

    '''

@post('/test')
def test_post():
    if sys.version_info > (3,):
        msg = request.params.decode().get('message')
    else:
        msg = request.params.get('message')
    sendmmd(msg)

run(host='localhost', port=8080, debug=True)


