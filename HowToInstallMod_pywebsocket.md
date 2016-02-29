# Introduction #

> This page figures out how to install [mod\_pywebsockets](http://code.google.com/p/pywebsocket/).

# Details #

## Conditions ##

> OS : Ubuntu9.x
> Apache: apache2.2.x
```
install directory -> /usr/local/apache2
mod_so
```

If you use built-in apache, you may install httpd-devel (Mac doesn't need the step below :) )
```
sudo yum install httpd-devel
```
## Install mod\_python ##

> ### install python-dev ###

> (Mac doesn't need the step below :) )

(Ubuntu9.x)
```
$ sudo aptitude install python-dev
```

(CentOS4)
```
# wget ftp://mirror.switch.ch/pool/3/mirror/centos/5.5/os/x86_64/CentOS/python-devel-2.4.3-27.el5.i386.rpm
# rpm -ivh python-devel-2.4.3-27.el5.i386.rpm
```
> ### install mod\_python ###

```
$ wget http://archive.apache.org/dist/httpd/modpython/mod_python-3.3.1.tgz
$ tar xvzf mod_python-3.3.1
$ cd mod_python-3.3.1
$ vi src/connobject.c
- !(b == APR_BRIGADE_SENTINEL(b) ||
+ !(b == APR_BRIGADE_SENTINEL(bb) ||

#############################################################
# NOTE: path for apxs below is example, check your machine's enviroment
# for example, my mac's built-in apxs is located at /usr/sbin/apxs
#############################################################
$ ./configure --with-apxs=/usr/local/apache2/bin/apxs
$ make
$ sudo make install
```

> ### configure httpd.conf ###

```
# case source install
LoadModule python_module modules/mod_python.so
# case Mac(built-in install)
LoadModule python_module libexec/apache2/mod_python.so

AddHandler mod_python .py 
```

> ### restart apache ###

```
$ /usr/local/apache2/bin/apachectl restart 
```


---


## Install mod\_pywebsocket ##


> ### checkout pywebsocket ###

```
$ cd
$ svn checkout http://pywebsocket.googlecode.com/svn/trunk/ pywebsocket-read-only
```

> ### install mod\_pywebsocket ###

```
$ cd pywebsocket-read-only
$ cd src

# setup
$ python setup.py build
$ sudo python setup.py install
```

> ### tips:: read document by ###

```
$ pydoc mod_pywebsocket
```
> then pywebsocket library is installed in _/usr/local/lib/python2.6/dist-packages/_

> ### config apache ###

> append configuration shown below to httpd.conf.

> _Note::_
> > change "somewhere" to your arbitraly directory. "mod\_pywebsocket.handler\_root" means handler scripts root directory (like documentRoot or cgi-bin)


> Under CentOS4 mod\_pywebsocket library will be installed in directory below,
> > /usr/lib/python2.4/site-packages/

> Case MacOS
> > /Library/Python/2.6/site-packages

> So, change to adequate path\_name (it depends on your system).

```
<IfModule python_module>
  PythonPath "sys.path+['/usr/local/lib/python2.6/dist-packages']"
  PythonOption mod_pywebsocket.handler_root /somewhere/websock_handlers
  PythonHeaderParserHandler mod_pywebsocket.headerparserhandler
  PythonOption mod_pywebsocket.allow_draft75 On
</IfModule>
```

> _Note::_
> To work with chrome4, 5 or safari5, last configuration line is required. Because,
> those browsers implementation is based on former spec(called as 75).

> ### restart apache ###

```
$ sudo /usr/local/apache2/bin/apachectl restart
```

> ### make handler\_root directory ###

```
mkdir /somewhere/websock_handlers
```

> ### test sample ###

> copy echo server to handler\_root
```
$ cd pywebsocket-read-only/src/example
$ cp echo_wsh.py /somewhere/websock_handlers/
```

> ### execute client script ###

> _Note::_
> > this script access to ws://localhost/echo
```
$ ./echo_client.py
Send: Hello
Recv: Hello
Send: 日本
Recv: 日本
Send: Goodbye
Recv: Goodbye
```


> ### arbitrary message ###

> with option -m :)
```
$ ./echo_client.py -m 'Hello world!!','How are you?'
Send: Hello world!!
Recv: Hello world!!
Send: How are you?
Recv: How are you?
Send: Goodbye
Recv: Goodbye
```