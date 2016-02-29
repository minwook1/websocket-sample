# websocket sample (for pywebsocket) #

## what's this? ##

> This project provides sample code for [Websockets](http://tools.ietf.org/html/draft-hixie-thewebsocketprotocol). Samples are based on [Apache HTTP server](http://httpd.apache.org/) and [mod\_pywebsocket](http://code.google.com/p/pywebsocket/) (fantastic websockets imprementation for apache developer!!), so other websocket servers are out of scope here.

> I also intend to figure how to install mod\_pywebsocket and other tips.


---

## Websockets pipeline'll make faster web services!! ##

![![](http://websocket-sample.googlecode.com/svn/trunk/images/WebsocketMeetsMeCab.png)](http://websocket-sample.googlecode.com/svn/trunk/images/WebsocketMeetsMeCab.png)
<p></p>
> Sorry, these demonstrations are described only Japanese now. But, simply click "via ws" and "via xhr", you'll feel it! (I'll describe in English). These sites require websocket supported browsers, ie chrome4+ or webkit nightly builds.
<p></p>
> <a href='http://bloga.jp/koma/ws/pipelinetest.html'>text-mining demonstration with handreds of japanese sentences.</a><br>
<blockquote><a href='http://bloga.jp/koma/ws/100images/wspipeling.html'>100 images(my lovely dog:)) download demonstration</a><br></blockquote>

<h3>blogs and articles about this demonstrations.</h3>

<blockquote><a href='http://www.kaazing.com/blog/?p=301'>HTML5 Web Sockets and the Need for Speed!</a><br />
<a href='http://www.kaazing.com/blog/?p=310'>HTML5 Web Sockets and Pipelining</a><br />
<a href='http://www.atmarkit.co.jp/news/201001/27/google.html'>Chrome 4.0でWebアプリはローカルアプリに近付くか</a><br /></blockquote>

<hr />

<img src='http://websocket-sample.googlecode.com/svn/trunk/images/litechat.png' width='100'>
<img src='http://websocket-sample.googlecode.com/svn/trunk/images/count.png' width='100'>

<h2>contents</h2>

<ul><li>How to install py_websocket ( ubuntu9.x ) <a href='http://code.google.com/p/websocket-sample/wiki/HowToInstallMod_pywebsocket'>link</a>
</li><li>Tips for websocket coding <a href='http://code.google.com/p/websocket-sample/wiki/Tips'>link</a>
</li><li>How to use samples <a href='http://code.google.com/p/websocket-sample/wiki/samples?ts=1262888726&updated=samples'>link</a></li></ul>

<h2>how to get samples?</h2>

<pre><code>svn checkout http://websocket-sample.googlecode.com/svn/trunk/ websocket-sample-read-only<br>
</code></pre>

<h3><font color='red'>not to use encodeURIComponent!!</font></h3>

<code>&lt;!-- &lt;lang = "ja"&gt; --&gt;</code>
<blockquote><b>web socketのコーディングでは、encodeURIComponent()は使うべきではありません。サイトをutf-8で構成し、メッセージはutf-8のままで送受信してください。</b><br>
<code>&lt;!-- &lt;lang = "en"&gt; --&gt;</code>
<b>In web socket coding, you should not use encodeURIComponent(). Site's encoding should be 'utf-8', and send & receive messages in raw utf-8 text.</b><br></blockquote>

<pre><code>var message = 'もももすももももものうち';<br>
ws.send(message);<br>
</code></pre>

<a href='http://code.google.com/p/websocket-sample/wiki/Tips'>detail (see tips.)</a>

<hr />
<h2>pywebsocket works like this figure</h2>
<img src='http://websocket-sample.googlecode.com/svn/trunk/images/pywebsocketSequence.png' width='320'>

<h2>Useful links</h2>

<blockquote><h3>documents.</h3></blockquote>

<ul><li><a href='http://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-68'>The Web Socket protocol (Inrernet-Draft)</a>
</li><li><a href='http://bwtp.wikidot.com/'>BWTP:Bidirectional Web Transfer Protocol</a></li></ul>

<blockquote><h3>imprementation</h3></blockquote>

<ul><li><a href='http://code.google.com/p/pywebsocket/'>pywebsocket</a>
</li><li><a href='http://dev.chromium.org/spdy'>SPDY(get chromium, and having fun!!)</a></li></ul>

<blockquote><h3>jQuery plugin.</h3></blockquote>

<ul><li><a href='http://plugins.jquery.com/project/ws'>jQuery plugin for websockets(0.3-pre)</a>
</li><li><a href='http://bloga.jp/ws/jq/conn/wsdemo2.htm'>websocket's chat demo</a>
<ul><li>server side script is extended one which is served in this project :)