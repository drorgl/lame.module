# lame GYP Module

** Experimental **

expose lame mp3 through gyp

To save time, config taken from:
https://github.com/TooTallNate/node-lame

- can be used stand alone to compile lame as static/shared libraries ( / dll) 
	static/shared library can be changed in the variables section of lame.gyp
- can be used as part of a bigger gyp project (which was the original intent) :

```
'dependencies':[
	'lame.module/lame.gyp:mp3lame'
]
```

lame source https://github.com/rbrito/lame
Note that patents are involved in using lame library, please refer to lame's website
http://lame.sourceforge.net/
http://lame.sourceforge.net/links.php#Patents


I'm in no way associated with lame or its developers.

```
gyp lame.gyp -DOS=win -Dtarget_arch=ia32 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/

gyp lame.gyp -DOS=win -Dtarget_arch=x64 --depth=. -f msvs -G msvs_version=2013 --generator-output=./build.vs2013/

gyp lame.gyp -DOS=linux -Dtarget_arch=ia32 --depth=. -f make --generator-output=./build.linux32/

gyp lame.gyp -DOS=linux -Dtarget_arch=x64 --depth=. -f make --generator-output=./build.linux64/

gyp lame.gyp -DOS=android -Dtarget_arch=arm --depth=. -f make --generator-output=./build.android/
```

known issues:
- frontend won't build on linux
