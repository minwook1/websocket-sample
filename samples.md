# Introduction #

> Explain how to install sample codes and how to use these. These samples works well in chrome4+ only.

  * samples
    * litechat
    * simple counter

# How to install #

> Getting sample codes via svn checkout

```
svn checkout http://websocket-sample.googlecode.com/svn/trunk/ websocket-sample-read-only
```

> step 1.
  * copy ./html/`*` to your `<DocumentRoot>`

> step 2.
  * copy ./python/`*` to your `<websocket_handler>`

> step 3.
  * rewrite valiables named **file** ( contained by `<websocket_handler>`/pub/`*`/do\_wsh.py ) with your path.

# sample codes. #

> ## lite chat ##
> > Images::

> ![![](http://websocket-sample.googlecode.com/svn/trunk/images/litechat.png)](http://websocket-sample.googlecode.com/svn/trunk/images/litechat.png)

> Url::
> > `http://somewhere/pub/litechat.html`


> ## how it works ##

> <img src='http://websocket-sample.googlecode.com/svn/trunk/images/liteChat.png' width='500'></li></ul>

<blockquote>What's this?::
> > This is lite chat sample. Click 'connect' makes connection to websocket server and 'send' button become available. Type message in the box and click 'send', message will be available to other members. Simply, open at least 2 windows will realize bidirectional connection with websocket protocol.<br>
<blockquote>To communicate messages, shared file is utilized. Each websockets forked processes monitor it, and send server initiate messages ( if file is updated ).<br>
Additionally, it is useful for other websocket service. For example, change 'resource' box to 'echo' and click 'connect', you'll be able to play with "echo_wsh.py" ( which is pywebsocket's sample code ) on browser. With at least 2 windows, you'll see each messages are really independent.</blockquote></blockquote>

<hr />

<blockquote><h2>simple counter</h2>
<blockquote>Images::<br>
</blockquote><a href='http://websocket-sample.googlecode.com/svn/trunk/images/count.png'><img src='http://websocket-sample.googlecode.com/svn/trunk/images/count.png' /></a></blockquote>

<blockquote>Url::<br>
<blockquote><code>http://somewhere/pub/counter.html</code></blockquote></blockquote>

<blockquote>What's this?::<br>
<blockquote>This is simple counter sample. It shows number of users connecting this service, ( that's all, what a simple!!) . This sample simply shows how ease to manage connections. Since websocket is state-full protocol, we can manage connection without id ( required cookies for state-less protocol, HTTP ).</blockquote></blockquote>

<hr />
<blockquote><h2>text mining with websocket pipeline</h2>
<blockquote>Images::<br>
<a href='http://websocket-sample.googlecode.com/svn/trunk/images/WebsocketMeetsMeCab.png'><img src='http://websocket-sample.googlecode.com/svn/trunk/images/WebsocketMeetsMeCab.png' /></a></blockquote></blockquote>

<blockquote>Url::<br>
<blockquote><code>http://somewhere/pub/mecab/ruby.html</code>
<code>http://somewhere/pub/mecab/wakachi.html</code></blockquote></blockquote>

<blockquote><h2>what's difference between web socket pipeline and http request & response model</h2></blockquote>

<blockquote>Under http (request & response model), it is hard to send request message while waiting for response messages. Http also has http pipeline technique, but it is difficult to use via browser (for example, firefox requires conifguration via about:config with alert message:p). As a result, it requires long waiting time for users. Test data shows that to request & response about 100 messages, over 30 seconds were measured between japan and U.S.A.</blockquote>

<blockquote><img src='http://websocket-sample.googlecode.com/svn/trunk/images/httpResponseRequest.png' width='500'></blockquote>

<blockquote>WebSocket makes easy way to utilize websocket pipelining. As shown below, websockets are able to send message repeatedly. Protocol does not require waiting for response, then test data showed that websocket pipeling was extremely faster than http ... about 1 sec!! between japan and U.S.A.</blockquote>

<blockquote><img src='http://websocket-sample.googlecode.com/svn/trunk/images/websocketPipeline.png' width='500'></blockquote>

<blockquote>You can confirm detailed testing data via my blog site's comment ( <a href='http://blog.livedoor.jp/kotesaki/archives/1376548.html'><a href='http://blog.livedoor.jp/kotesaki/archives/1376548.html'>http://blog.livedoor.jp/kotesaki/archives/1376548.html</a> : japanese...</a> ).</blockquote>

<blockquote>This demonstratoin includes two text mining. One is appending "ruby" (not language :)) to "Kanji" and another is inserting spacer between each words (either are japanese only).  This demo needs <a href='http://mecab.sourceforge.net/'>MeCab</a>, famous japanese text mining open-source product, so on the server side, installing MeCab and python bind are required. This demonstration shows how fast the websocket pipelining is. Comparing "via websocket" vs "via xhr" you'll realize websocket pipelining at least x10 faster than parallel XMLHttpRequest. (I don't know how to type HTTP pipelining in Ajax.Request orz)