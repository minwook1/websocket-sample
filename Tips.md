# difference between websocket and websocket #

<img src='http://websocket-sample.googlecode.com/svn/trunk/images/ws_vs_http.png' width='500'>

<h1>pywebsocket works like as follows (protocol sequence and indicating when api works)</h1>

<img src='http://websocket-sample.googlecode.com/svn/trunk/images/pywebsocketSequence.png' width='500'>

<h1>what's Origin based Security Model?</h1>

<img src='http://websocket-sample.googlecode.com/svn/trunk/images/originBasedSecurityModel.png' width='500'>

<h1>Introduction</h1>

<blockquote>Tips for websocket coding.</blockquote>

<h1>Details</h1>
<h2>mod_pywebsocket</h2>

<blockquote><h3>handler name</h3></blockquote>

<blockquote>Suffix : <code>_wsh.py</code><br>
if script name is <b>var_wsh.py</b> and located in <code>&lt;handler_root&gt;</code>/foo/bar_wsh.py, resouce name is <b>/foo/bar</b>. URI will be like as follows.<br>
<pre><code>ws://somewhere/foo/bar<br>
</code></pre></blockquote>

<blockquote><h3>properties (request object)</h3></blockquote>

<ul><li>ws_location</li></ul>

<blockquote>uri of websocket handler<br>
<pre><code>e.g.<br>
ws://somewhere/foo/var  <br>
</code></pre></blockquote>

<ul><li>ws_origin</li></ul>

<blockquote>Indicates web sites which calls ws. If web site's uri is <b><a href='http://somewhere/foo'>http://somewhere/foo</a>,</b> ws_origin will be<br>
<pre><code>http://somewhere<br>
</code></pre>
This property is useful in secure coding( <i>Origin-based security model</i> ).</blockquote>

<ul><li>ws_protocol</li></ul>

<blockquote>This property indicates sub-protocol name.<br>
<pre><code>e.g.<br>
  NULL<br>
</code></pre></blockquote>

<ul><li>ws_resource</li></ul>

<blockquote>Resource name of ws. If ws_location is <b>ws://somewhere/foo/bar</b> resource name will be<br>
<pre><code>/foo/bar<br>
</code></pre></blockquote>

<blockquote><h3>functions</h3></blockquote>

<ul><li>web_socket_do_extra_handshake(request)</li></ul>

<blockquote>This function is called if clients handshake message is valid. Valid message is like as follows.<br>
<pre><code>GET /demo HTTP/1.1<br>
Upgrade: WebSocket<br>
Connection: Upgrade<br>
Host: example.com<br>
Origin: http://example.com<br>
WebSocket-Protocol: sample<br>
</code></pre></blockquote>

<blockquote>If you consider "Origin-based security model", you should check <b>request.ws_origin</b> .</blockquote>

<blockquote>If you <b>pass</b> this function, clients receives server messages like as follows and connection is established.<br>
<pre><code>HTTP/1.1 101 Web Socket Protocol Handshake<br>
Upgrade: WebSocket<br>
Connection: Upgrade<br>
WebSocket-Origin: http://example.com<br>
WebSocket-Location: ws://example.com/demo<br>
WebSocket-Protocol: sample<br>
</code></pre>
If <b>raise exception</b> , server deny handshakes.</blockquote>

<ul><li>web_socket_transfer_data(request)</li></ul>

<blockquote>This function is called after connection established. This function manages <b>data frames.</b> If you want to close the connection, simply "return" this function.</blockquote>

<ul><li>message = msgutil.receive_message(request : request)</li></ul>

<blockquote>Note::<br>
<blockquote><i>message</i> is 'unicode' (not 'string'), so you should use .encode('utf-8') if you want to treat as 'string' like as follows.<br>
<pre><code>message = msgutil.receive_message(request)<br>
<br>
message #=&gt; u'あいう'<br>
print type(message) #=&gt; &lt;type 'unicode'&gt;<br>
print message.encode('utf-8') #=&gt; 'あいう'<br>
</code></pre></blockquote></blockquote>

<blockquote>Receive message from client<br>
<pre><code>%x00 + *( UTF8-char / %x80-%x7E ) + %xff<br>
</code></pre></blockquote>

<ul><li>msgutil.send_message(request : <i>request</i> , message : <i>unicode</i> )</li></ul>

<blockquote>Note::<br>
<blockquote><i>message</i> is 'unicode' (not 'string'), so you should use .decode('utf-8') if you want to send 'string'<br>
<pre><code>message = 'あいうえお'<br>
msgutil.send_message(request, message.decode('utf-8'))<br>
</code></pre></blockquote></blockquote>


<blockquote>Send server initiate message to client.<br>
<pre><code>%x00 + *( UTF8-char / %x80-%x7E ) + %xff<br>
</code></pre></blockquote>

<blockquote><h3>how to check Origin-based security model</h3></blockquote>

<blockquote>request.ws_origin value indicates which site is attempting to connect your ws server. To prevent unreliable web pages to use your ws server's resource, you may check this value.<br>
If ws server's resource is restricted to <b>localhost,</b> script will be like as follows<br>
<pre><code>def web_socket_do_extra_handshake(request):<br>
  if request.ws_origin != 'http://localhost':<br>
    raise "ws_origin error "+request.ws_origin<br>
  pass  # if origin is acceptable.<br>
</code></pre></blockquote>

<blockquote><h3>don't forget to close thread</h3></blockquote>

<blockquote>In many cases, you'll type thread programming, because each <i>websocket_handler</i> works individually (fork process). To share each client's message, shared file or some socket connection is reasonable and this phenomena requires thread programming. If you are in this situation, don't forget to close thread if the connection is going to close. Forgetting this process sometimes make zombie.</blockquote>

<blockquote>python script will be as follows.<br>
<pre><code>from mod_pywebsocket import msgutil<br>
<br>
import thread<br>
<br>
_CONNECTING_ = 0<br>
_OPEN_ = 1<br>
_CLOSE_ = 2<br>
<br>
_status_ = _CONNECTING_<br>
<br>
def proc():<br>
  while True:<br>
    if _status_ != _OPEN_:<br>
      break<br>
    ....<br>
<br>
def web_socket_do_extra_handshake(request):<br>
	pass  # Always accept.<br>
<br>
def web_socket_transfer_data(request):<br>
  global _status_<br>
  _status_ = _OPEN_<br>
  attr = ()<br>
  thread.start_new_thread(proc().run, attr)<br>
  while True:<br>
    try:<br>
      line = msgutil.receive_message(request)<br>
      ...<br>
<br>
    except Exception: # client calls ws.close()<br>
      _status_ = _CLOSE_<br>
      return # close connection<br>
</code></pre>
<hr />
<h2>apache's configuration</h2></blockquote>

<blockquote><h3>persistent connection</h3></blockquote>

<blockquote><i>conf/extra/httpd-default.conf</i>
<pre><code>KeepAlive Off<br>
</code></pre>
(default:On)</blockquote>

<blockquote><i>Note::</i>
<blockquote>Don't forget to remove comment out (#) for "Include httpd-default.conf" in httpd.conf.</blockquote></blockquote>

<blockquote>Without this configuration, server retains connection for several seconds after ws connection was closed due to HTTP/1.1's persistent-connection.</blockquote>

<blockquote><i>Note::</i>
<blockquote>Delay time is configured in<br>
<pre><code>KeepAliveTimeout 5<br>
</code></pre>
in extra/httpd-default.conf</blockquote></blockquote>

<hr />
<h2>javascript</h2>
<blockquote><h3>not to use encodeURIComponent</h3></blockquote>

<blockquote>Among multibytes-language people ( for example, japanese ), they tend to use encodeURIComponent() while sending message to server. In Websockets this manner works well, but it requires more bandwidth than spec required.<br></blockquote>

<blockquote>Websocket is designed to communicate with utf-8.<br>
<pre><code>text-frame = (%x00) *( UTF8-char ) %xFF<br>
  http://tools.ietf.org/html/draft-hixie-thewebsocketprotocol-68#page-6<br>
</code></pre>
encodeURIComponent encodes UTF8 to ascii character. For example, 'あ' is encoded to '%E3%81%82'. In this case, these encoded string consume 9 bytes. However, 'あ' is 3 bytes in native utf-8 (%xe3%x81%x82). Therefore, sending messages in utf-8 ( this means not to use encodeURIComponent ) may be reasonable to keep network traffic lower and make shortage of messaging delay. So, you'd better to write web page in UTF-8 encode and use ws.send() simple way like as follows.<br>
<pre><code>&lt;!doctype html&gt;<br>
&lt;html lang="ja"&gt;<br>
&lt;head&gt;<br>
&lt;meta charset="utf-8"&gt;<br>
&lt;/head&gt;<br>
&lt;body&gt;<br>
....<br>
&lt;script type="text/javascript"&gt;<br>
....<br>
  var message = 'もももすももももものうち';<br>
  ws.send(message);<br>
&lt;/script&gt;<br>
&lt;/body&gt;<br>
&lt;/html&gt;<br>
</code></pre>
Note, not to type <code> ws.send(encodeURIComponent()); </code>...</blockquote>

<blockquote><h3>heartbeat</h3></blockquote>

<blockquote>After connection established, ws connection is closed by apache after several minutes without any clent side message ( even if server sent message in this minutes!!).</blockquote>

<blockquote><i>Note::</i>
<blockquote>Default is 300 seconds ( "Timeout" in extra/httpd-default.conf ）</blockquote></blockquote>

<blockquote>Sending periodically message every few minutes avoid this situation.</blockquote>

<blockquote>Javascript will be like as follows.<br>
<pre><code>setInterval(function() {<br>
  ws.send('Heartbeat');<br>
}, 60000);<br>
</code></pre></blockquote>

<blockquote><h3>window.onunload</h3></blockquote>

<blockquote>Sometime, it seems to be keep ws connection in Chrome4+, even if window is closed/reloaded. To set <b>unload</b> event handler and call <b>ws.close()</b> will avoid this situation.</blockquote>

<blockquote>Javascript will be like as follows.<br>
<pre><code>window.onunload = function() {<br>
  ws.close();<br>
};<br>
</code></pre>