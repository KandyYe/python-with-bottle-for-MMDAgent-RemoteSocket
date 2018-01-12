※今は実験の為、音声認識を使わない形（コメントアウト）にして運用しています

今使ってるのは
ajax-2.py
ajax.js
connectmmd.py
bottle.py
の4つです

ajax-2.pyがブラウザ上でのURL毎のget,postによる動作を定義しています
ajax.jsはajax-2.py内のHTML内で使っている関数を定義しています
connectmmd.pyはMMDAgentとのソケット通信及びMMDAgentに送信する内容を決めています
bottle.pyはフレームワークです

おわり
