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


    <!--質問：<input type="text" id="query-id" bgcolor="red">-->
            <!--<input type="button" onclick="send_query_message()" /><br>-->
    <!--応答：<input type="text" id="reply-id"><br>-->

    <!--<input type="button" value="Stop" onclick="recognition.stop()" />-->
    <!--<input type="button" value="Restart" onclick="recognition.start()" /><br>-->
    
    <input type="button" value="!:こんにちは！今日も機械学習について勉強していきましょう。" onclick="send_button_message(1)" id="sentence1"/><br>
    <input type="button" value="?:よろしくおねがいしまーす。" onclick="send_button_message(2)" id="sentence2"/><br>
    <input type="button" value="!:早速ですが、今日の単元ではサポートベクトルマシンと言われる識別手法について説明していきます。" onclick="send_button_message(3)" id="sentence3"/><br>
    <input type="button" onclick="send_button_message(4)" value="!:扱う問題は、数値特徴に対する教師ありの識別問題です。" id="sentence4"/><br>
    <input type="button" onclick="send_button_message(5)" value="!:めいさんは教師あり学習ってどんなものか覚えていますか？" id="sentence5"/><br>  
    <input type="button" onclick="send_button_message(6)" value="?:教師あり学習って言うくらいだから、認識結果を間違う度にちゃんと訂正されて、またそれを用いて学習を進めるって言う手法じゃなかったっけ？" id="sentence6"/><br>
    <input type="button" onclick="send_button_message(7)" value="!:そうですね、あなたはBさんの言う認識であってると思いますか？" id="sentence7"/><br>
        <!-- 正解 -->
    <input type="button" onclick="send_button_message(8)" style="color:darkred;background-color:sandybrown;" value="!:その通りです。Bさんの認識は少し違いますね。教師あり学習はデータと正解のペアを与えておいて、それをもとに学習する方法ですよ。では、今日の本題に戻りましょう。" id="sentence8"/><br> 
        <!-- 不正解 -->
    <input type="button" onclick="send_button_message(9)" style="color:#ffffff;background-color:#0000ff;" value="!:二人とも少し間違って覚えているようですね。教師あり学習はデータと正解のペアを与えておいて、それをもとに学習する方法ですよ。" id="sentence9"/><br> 
    <input type="button" onclick="send_button_message(100)" style="color:#ffffff;background-color:#0000ff;" value="!:またちゃんと復習しておいてくださいね。では、今日の本題に戻りましょう。" id="sentence100"/><br>    
    <!-- スライド1枚目 -->
    <input type="button" onclick="send_button_message(10)" value="!:.この図に示すような特徴空間で、直線によって分離することのできる学習データがあるとします。" id="sentence10"/><br>  
    <input type="button" onclick="send_button_message(11)" value="!:丸で表されているのが学習データです。" id="sentence11"/><br>
    <input type="button" onclick="send_button_message(12)" value="!:この学習データに対して、識別を行える直線は無数に存在します。" id="sentence12"/><br>
    <input type="button" onclick="send_button_message(13)" value="!:例えば、この図で実線で表されている二本ですね。" id="sentence13"/><br>
    <input type="button" onclick="send_button_message(14)" value="!:どちらの線も学習データに関しては識別率100パーセントです。" id="sentence14"/><br>
    <input type="button" onclick="send_button_message(15)" value="!:また、これらを識別面としたとき、最も近いデータとの距離をマージンと呼びます。" id="sentence15"/><br>  
    <input type="button" onclick="send_button_message(16)" value="!:それでは、ここでBさんに質問です。今回なら、斜めの線と垂直の線のどちらを用いて、未知データを識別した方が良い結果になりそうですか？" id="sentence16"/><br>
    <input type="button" onclick="send_button_message(17)" value="?:えっと、垂直の線！" id="sentence17"/><br>
    <input type="button" onclick="send_button_message(18)" value="!:その通りですね。じゃあ、次はあなたに質問です。何故、垂直な線の方が良いと言えるでしょうか？" id="sentence18"/><br>
        <!-- 正解 -->
    <input type="button" onclick="send_button_message(19)" style="color:darkred;background-color:sandybrown;" value="!:その通りです。次に、問題の定式化に移りましょう。" id="sentence19"/><br>
        <!-- 不正解 -->
    <input type="button" onclick="send_button_message(20)" style="color:#ffffff;background-color:#0000ff;" value="!:少し難しかったみたいですね。" id="sentence20"/><br>  
    <input type="button" onclick="send_button_message(21)" style="color:#ffffff;background-color:#0000ff;" value="!:垂直な方がマージンが広く、未知データが学習データと識別面の間に入る余地があり、誤識別されにくいため、垂直な線を識別面とした方が汎用性が高くなる、と言えます。" id="sentence21"/><br>
    <input type="button" onclick="send_button_message(22)" style="color:#ffffff;background-color:#0000ff;" value="!:それでは、次に、問題の定式化に移りましょう。" id="sentence22"/><br>
    <!-- スライド2枚目 -->
    <input type="button" onclick="send_button_message(23)" value="!:.まず、さっきの例のように学習データが線形識別可能な状況で、マージンが最大となる識別面を求める方法を考えていきましょう。" id="sentence23"/><br>
    <input type="button" onclick="send_button_message(24)" value="?:はーい。" id="sentence24"/><br>
    <input type="button" onclick="send_button_message(25)" value="!:学習データは数値特徴に対して正解情報の付いたデータです。ここでは二値分類問題に限定して、正解情報の値を正例1、負例を-1とします。" id="sentence25"/><br>  
    <input type="button" onclick="send_button_message(26)" value="?:教師あり学習、教師あり学習。" id="sentence26"/><br>
    <input type="button" onclick="send_button_message(27)" value="!:識別面は平面なので、特徴空間ではこのような式で表されます。" id="sentence27"/><br>
    <input type="button" onclick="send_button_message(28)" value="!:識別面の式は右辺が0になりますので、左辺を定数倍しても表す平面は変わりません。" id="sentence28"/><br>
    <input type="button" onclick="send_button_message(29)" value="!:そこで、識別面に最も近いデータを識別面の式に代入したとき、その絶対値が1になるように重みを調整すると、識別面の制約に示した式となります。" id="sentence29"/><br>
    <input type="button" onclick="send_button_message(30)" value="!:この二つの式から一番の下の式が導かれ、これがマージンを表します。" id="sentence30"/><br>  
    <input type="button" onclick="send_button_message(31)" value="?:はい！じゃあマージンを最大にするにはダブリューを最小化すればいいんですよね！" id="sentence31"/><br>
    <input type="button" onclick="send_button_message(32)" value="!:じゃあ、Bさんはダブリューが0になれば良いと思いますか？" id="sentence32"/><br>
    <input type="button" onclick="send_button_message(33)" value="?:最小化するっていうことはそういうことじゃないの？" id="sentence33"/><br>
    <input type="button" onclick="send_button_message(34)" value="!:あなたの意見も聞いてみましょう。それでいいと思いますか？" id="sentence34"/><br>
        <!-- 正解 -->
    <input type="button" onclick="send_button_message(35)" style="color:darkred;background-color:sandybrown;" value="!:そうですね。ダブリューを0にしてしまうと、識別面にはなりません。そこで、また新たに制約条件を付けないといけないのですが、詳しくは次のスライドを見てみましょう。" id="sentence35"/><br>       
        <!-- 不正解 -->
    <input type="button" onclick="send_button_message(36)" style="color:#ffffff;background-color:#0000ff;" value="!:言いたいことはわかりますが,二人とも少し誤りです" id="sentence36"/><br>                
    <input type="button" onclick="send_button_message(37)" style="color:#ffffff;background-color:#0000ff;" value="!:ダブリューを0にしてしまうと,識別面には成り得ません そこで,また新たに制約条件を付けないといけないのですが,詳しくは次のスライドを見てみましょう" id="sentence37"/><br>
    <!-- スライド3枚目 -->                                                                          
    <input type="button" onclick="send_button_message(38)" value="!:.ここまでで、マージンを最大にする識別面を求める問題の定式化が終わりました。" id="sentence38"/><br>                                                                          
    <input type="button" onclick="send_button_message(39)" value="!:制約条件はさっき言った通り、すべての学習データを識別できるという式の条件を加えます。また、微分を利用して極値を求めて最小解を導くので、乗数の二分の一を付けておきます。" id="sentence39"/><br>                                                                          
    <input type="button" onclick="send_button_message(40)" value="!:よって、目的関数はこのようになります。" id="sentence40"/><br>                                                                          
    <input type="button" onclick="send_button_message(41)" value="!:で、続いて、この問題を解くために、ラグランジュの未定乗数法を用いて解決していきます。" id="sentence41"/><br>                                                                          
    <input type="button" onclick="send_button_message(42)" value="?:またなんか難しいこと言い出したよ……。" id="sentence42"/><br>                                                                          
    <input type="button" onclick="send_button_message(43)" value="!:ラグランジュの未定乗数法を用いると、エフエックスの最小値を求める問題は,こちらにあるラグランジュ関数を導入することで、関数の極値を求めるという問題に置き換えることができます。"  id="sentence43"/><br>       
    <!-- スライド4枚目 -->                                                                   
    <input type="button" onclick="send_button_message(44)" value="!:.計算内容について細かく見ていきましょう。" id="sentence44"/><br>                                                                          
    <input type="button" onclick="send_button_message(45)" value="!:最小化問題は、いちばん上の式にあるように関数エルの最小値を求めるという問題に置き換えることができます。" id="sentence45"/><br>                                                                          
    <input type="button" onclick="send_button_message(46)" value="!:また最小値ではエルの勾配が0になるはずなので、その下の二つの式が成り立ちます。" id="sentence46"/><br>                                                                          
    <input type="button" onclick="send_button_message(47)" value="!:これを一番上の式に代入することで一番下の式を得られます。" id="sentence47"/><br>                                                                          
    <input type="button" onclick="send_button_message(48)" value="!:次はこれを最小化するのですが、これはアルファに関する二次計画問題と呼ばれるものになります。" id="sentence48"/><br>                                                                          
    <input type="button" onclick="send_button_message(49)" value="!:よって、数値計算ソフトウェアを使って解くことができます。" id="sentence49"/><br>                                                                          
    <input type="button" onclick="send_button_message(50)" value="?:楽できるってこと？" id="sentence50"/><br>
    <input type="button" onclick="send_button_message(51)" value="!:そうですね、コンピュータを用いて計算しやすい形になります。" id="sentence51"/><br>
    <input type="button" onclick="send_button_message(52)" value="!:ここから少し応用編になります。頑張ってくださいね。" id="sentence52"/><br>
    <input type="button" onclick="send_button_message(53)" value="?:がんばりまーす。" id="sentence53"/><br>
    <input type="button" onclick="send_button_message(54)" value="!:いい返事です。じゃあ、皆さん早速ですが、一般的に特徴空間の次元数が大きい場合は線形識別面が存在する可能性が高くなると思いますか？　それとも、低くなると思いますか？" id="sentence54"/><br>
    <input type="button" onclick="send_button_message(55)" value="!:まずは、メイちゃん" id="sentence55"/><br>
    <input type="button" onclick="send_button_message(56)" value="?:うーん、次元数が増えると、データの配置がややこしくなるから、低くなるんじゃないの？" id="sentence56"/><br>
    <input type="button" onclick="send_button_message(57)" value="!:じゃあ、あなたの考えはどうですか？" id="sentence57"/><br>
    <!-- スライド5枚目(正解) -->
    <input type="button" style="color:darkred;background-color:sandybrown;" onclick="send_button_message(58)" value="!:.正解は高くなる、です。めいちゃんはこの図を見ながら、もう一度考えてくださいね。話を続けます。" id="sentence58"/><br>
    <!-- スライド5枚目(不正解) -->
    <input type="button" onclick="send_button_message(59)" style="color:#ffffff;background-color:#0000ff;" value="!:.正解は高くなる、です。この図を見れば分かりやすいかと思います。二次元で線形分離不可能なデータも、三次元にすれば線形分離が可能になっていますね。話を続けます。" id="sentence59"/><br>
    
    <input type="button" onclick="send_button_message(60)" value="!:その性質を逆手にとって、低次元の特徴ベクトルを高次元に写像し、その高次元空間上でサポートベクトルマシンを使って、識別面を求めるという方法が考えられます。" id="sentence60"/><br>
    <input type="button" onclick="send_button_message(61)" value="!:識別に役立つ特徴で構成されたディー次元空間に対して、もとの空間におけるデータ間の距離関係を保存する方式で高次元に非線形変換しても、" id="sentence61"/><br>
    <input type="button" onclick="send_button_message(101)" value="!:線形識別器の性能は、もとの空間の性能を反映できます。" id="sentence101"/><br>
    <input type="button" onclick="send_button_message(62)" value="?:でも、そんな都合のいい非線形写像がそう簡単に見つかるんですか？" id="sentence62"/><br>
    <input type="button" onclick="send_button_message(63)" value="!:良い着眼点ですね。ここで役に立つのがスライドにもあるカーネル関数というものです。" id="sentence63"/><br>
    <!-- スライド6枚目 -->
    <input type="button" onclick="send_button_message(64)" value="!:.まず、非線形関数をファイエックスとし、カーネル関数をケーエックス、エックスダッシュとした時、この式が成り立つことを仮定します。" id="sentence64"/><br>
    <input type="button" onclick="send_button_message(65)" value="!:これは、元の空間での距離が空間の内積に対応していることを示しています。" id="sentence65"/><br>
    <input type="button" onclick="send_button_message(66)" value="!:また、カーネル関数の例として、多項式カーネル関数やガウシアンカーネル関数があります。" id="sentence66"/><br>
    <input type="button" onclick="send_button_message(67)" value="!:この形であれば、対応する非線形変換関数ファイが存在することが数学的に保証されています。" id="sentence67"/><br>
    <!-- スライド7枚目 -->
    <input type="button" onclick="send_button_message(68)" value="!:.先程の式から、識別関数は一番上のような式になります。" id="sentence68"/><br>
    <input type="button" onclick="send_button_message(69)" value="!:そして、ここでサポートベクトルマシンで求めたダブリューの値を代入します。" id="sentence69"/><br>
    <input type="button" onclick="send_button_message(70)" value="!:式からファイが消えていることに気付きましたか？" id="sentence70"/><br>
    <input type="button" onclick="send_button_message(71)" value="!:つまり、カーネル関数さえ定まれば、識別面を得ることができます。" id="sentence71"/><br>
    <input type="button" onclick="send_button_message(72)" value="!:このように複雑な非線形変換を避ける方法をカーネルトリックと呼びます。" id="sentence72"/><br>
    <input type="button" onclick="send_button_message(73)" value="!:これがサポートベクトルマシンがいろいろな応用に使われている理由です。" id="sentence73"/><br>
    <input type="button" onclick="send_button_message(74)" value="?:応用って、どういうことに使われてるの？" id="sentence74"/><br>
    <input type="button" onclick="send_button_message(75)" value="!:そうですね。例えば、文書分類などにも使われていますよ。" id="sentence75"/><br>
    <input type="button" onclick="send_button_message(76)" value="?:文書を？"/><br>
    <input type="button" onclick="send_button_message(77)" value="!:ええ。今まで数値特徴を対象にサポートベクトルマシンを説明してきましたが、文書の文字列データを上手く処理してやれば、サポートベクトルマシンで分類可能です。 " id="sentence77"/><br>
    <input type="button" onclick="send_button_message(78)" value="?:えー、言語を数値特徴にすることなんてできるの？" id="sentence78"/><br>
    <input type="button" onclick="send_button_message(79)" value="!:Bag-of-Wordsという手法なのですが、Bさん……は無理そうですね。あなたはご存知ですか？　できそうなら、説明してあげてください。" id="sentence79"/><br>
        <!-- 正解 -->
    <input type="button" onclick="send_button_message(80)" style="color:darkred;background-color:sandybrown;" value="!:素晴らしい！よく理解できていますね。仰る通りです。めいちゃんは分かりましたか？　分からなかったら、今度もう一度教わってくださいね。" id="sentence80"/><br>
        <!-- 不正解 -->
    <input type="button" onclick="send_button_message(81)" style="color:#ffffff;background-color:#0000ff;" value="!:突然すぎましたかね。一応、私からも説明させてもらいます。" id="sentence81"/><br>
    <input type="button" onclick="send_button_message(82)" style="color:#ffffff;background-color:#0000ff;" value="!:Bag-of-Wordsという手法では、文書に現れ得る全単語をそれぞれの次元に設定します。" id="sentence82"/><br>
    <input type="button" onclick="send_button_message(83)" style="color:#ffffff;background-color:#0000ff;" value="!:そして、各次元の値を文書中に出現する単語は1、出現しない単語は0、としてやります。" id="sentence83"/><br>
    <input type="button" onclick="send_button_message(84)" style="color:#ffffff;background-color:#0000ff;" value="!:勿論、特徴ベクトルは高次元になりますが、サポートベクトルマシンは汎化性能が高いので、このような高次元の識別問題にも用いることができるんですよ。" id="sentence84"/><br>
    <input type="button" onclick="send_button_message(85)" value="!:それでは、今日はここまでです。お疲れ様でした。また次回も頑張りましょう。" id="sentence85"/><br>                                            

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


