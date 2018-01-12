function include(file)
{
    var script = document.createElement('script');
    script.src = file;
    script.type = 'text/javascript';
    script.defer = true;
    document.getElementsByTagName('head').item(0).appendChild(script);
}

include( 'http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js' );

//var recognition = new webkitSpeechRecognition();

var ajax_success_func = function(reply) {
        console.log(reply);
        document.getElementById('reply-id').value = reply;
        recognizing = false;
        /*
        var synthes = new SpeechSynthesisUtterance( reply );
        synthes.lang = "ja-JP"
        speechSynthesis.speak( synthes );
        var timer = setTimeout( function() {
            document.getElementById('query-id').style.backgroundColor = "lightgreen";
        }, 3000);
        */
    };

//ajaxを利
var interact_by_ajax = function(msg) {
        $.ajax({
            type: "POST",
            url: "/test",
            data: "message=" + msg,
            success: ajax_success_func
        });
    };

//ユーザーの質問を受け取ってajaxへ
var send_query_message = function() {
        var msg = document.getElementById('query-id').value;
        interact_by_ajax( msg );
    };

var send_button_message = function(num) {
        var msg = document.getElementById('sentence' + num).value;
        interact_by_ajax( msg );
    };

//開始時に合成に音声による発話する内容
//var synthes = new SpeechSynthesisUtterance(
//    "マイクの使用を許可し、音声で、画面の例のように、天気をたずねてください。"
//    );
//synthes.lang = "ja-JP"
//speechSynthesis.speak( synthes );


/*
recognition.continuous = true;
recognition.onresult = function(event) {
    var length = event.results.length;
    if ( length > 0 ) {
        msg = event.results[length-1][0].transcript
        console.log( msg );
        query = document.getElementById('query-id');
        query.value = msg;
        send_query_message();
        document.getElementById('query-id').style.backgroundColor = "red";
    }
};
*/
//recognition.start();