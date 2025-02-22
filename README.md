<h1 align="center">
  <br>
  <a href="https://getmythic.app">
    <img src="https://github.com/MythicApp/Engine/assets/41133734/b602e46b-f5bd-4175-bd6c-196e6228584f" 
      style="width: 20%; height: 20%;">
  </a>

  Mythic Engine
  <br>
  <sub><sub><sub>Part of <a href="https://getmythic.app">Mythic.</a></sub></sub></sub>

  ![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/MythicApp/Engine/.github%2Fworkflows%2Fbuild.yml)
  [![Discord](https://img.shields.io/discord/1154998702650425397?color=5865F2)](https://discord.com/invite/58NZ7fFqPy)
</h1>

Mythic Engine is Mythic's implementation of Apple's [Game Porting Toolkit (GPTK)](https://developer.apple.com/games/game-porting-toolkit/), which uses [wine](https://www.winehq.org/) translation technology and the Apple-designed Direct3D-to-Metal translator, D3DMetal, to create an effective windows gaming experience on macOS. Similar to Proton, Mythic Engine is a backend that enables native Windows games to be playable on macOS, while coming closer to native performance than ever before.

<sub>
A derivative of <a href="https://github.com/Whisky-App/wine">WhiskyWine</a>, credit to those who contribute to and presently work on it.
<br>
Please note that performance will vary between games.
<br>
Also note that GPTKv2 is currently still in its beta phase; bugs and hiccups are to be expected.
</sub>

---

# wine

# 1. INTRODUCTION

Wine is a program which allows running Microsoft Windows programs
(including DOS, Windows 3.x, Win32, and Win64 executables) on Unix.
It consists of a program loader which loads and executes a Microsoft
Windows binary, and a library (called Winelib) that implements Windows
API calls using their Unix, X11 or Mac equivalents.  The library may also
be used for porting Windows code into native Unix executables.

Wine is free software, released under the GNU LGPL; see the file
LICENSE for the details.


# 2. QUICK START

From the top-level directory of the Wine source (which contains this file),
run:

```
./configure
make
```

Then either install Wine:

`make install`

Or run Wine directly from the build directory:

`./wine notepad`

Run programs as "`wine program`".  For more information and problem
resolution, read the rest of this file, the Wine man page, and
especially the wealth of information found at https://www.winehq.org.


# 3. REQUIREMENTS

To compile and run Wine, you must have one of the following:

  * Linux version 2.0.36 or later
  * FreeBSD 8.0 or later
  * Solaris x86 9 or later
  * NetBSD-current
  * Mac OS X 10.8 or later

As Wine requires kernel-level thread support to run, only the operating
systems mentioned above are supported.  Other operating systems which
support kernel threads may be supported in the future.

## FreeBSD info:
  Wine will generally not work properly on versions before FreeBSD 8.0.
  See https://wiki.freebsd.org/Wine for more information.

## Solaris info:
  You will most likely need to build Wine with the GNU toolchain
  (gcc, gas, etc.). Warning : installing gas does *not* ensure that it
  will be used by gcc. Recompiling gcc after installing gas or
  symlinking cc, as and ld to the gnu tools is said to be necessary.

## NetBSD info:
  Make sure you have the USER_LDT, SYSVSHM, SYSVSEM, and SYSVMSG options
  turned on in your kernel.

## Mac OS X info:
  You need Xcode/Xcode Command Line Tools or Apple cctools.  The
  minimum requirements for compiling Wine are clang 3.8 with the
  MacOSX10.10.sdk and mingw-w64 v8.  The MacOSX10.14.sdk and later can
  only build wine64.


## Supported file systems:
  Wine should run on most file systems. A few compatibility problems
  have also been reported using files accessed through Samba. Also,
  NTFS does not provide all the file system features needed by some
  applications.  Using a native Unix file system is recommended.

## Basic requirements:
  You need to have the X11 development include files installed
  (called xorg-dev in Debian and libX11-devel in Red Hat).

  Of course you also need "make" (most likely GNU make).

  You also need flex version 2.5.33 or later and bison.

## Optional support libraries:
  Configure will display notices when optional libraries are not found
  on your system. See https://wiki.winehq.org/Recommended_Packages for
  hints about the packages you should install. On 64-bit platforms,
  you have to make sure to install the 32-bit versions of these
  libraries.


# 4. COMPILATION

To build Wine, do:

```
./configure
make
```

This will build the program "wine" and numerous support libraries/binaries.
The program "wine" will load and run Windows executables.
The library "libwine" ("Winelib") can be used to compile and link
Windows source code under Unix.

To see compile configuration options, do ./configure --help.

For more information, see https://wiki.winehq.org/Building_Wine


# 5. SETUP

Once Wine has been built correctly, you can do "make install"; this
will install the wine executable and libraries, the Wine man page, and
other needed files.

Don't forget to uninstall any conflicting previous Wine installation
first.  Try either "`dpkg -r wine`" or "`rpm -e wine`" or "`make uninstall`"
before installing.

Once installed, you can run the "winecfg" configuration tool. See the
Support area at https://www.winehq.org/ for configuration hints.


# 6. RUNNING PROGRAMS

When invoking Wine, you may specify the entire path to the executable,
or a filename only.

For example: to run Notepad:

```
wine notepad            (using the search Path as specified in
wine notepad.exe         the registry to locate the file)

wine c:\\windows\\notepad.exe      (using DOS filename syntax)

wine ~/.wine/drive_c/windows/notepad.exe  (using Unix filename syntax)

wine notepad.exe readme.txt          (calling program with parameters)
```

Wine is not perfect, so some programs may crash. If that happens you
will get a crash log that you should attach to your report when filing
a bug.


# 7. GETTING MORE INFORMATION

## WWW:	A great deal of information about Wine is available from WineHQ at
	https://www.winehq.org/ : various Wine Guides, application database,
	bug tracking. This is probably the best starting point.

## FAQ:	The Wine FAQ is located at https://www.winehq.org/FAQ

## Wiki:	The Wine Wiki is located at https://wiki.winehq.org

## Mailing lists:
	There are several mailing lists for Wine users and developers;
	see https://www.winehq.org/forums for more information.

## Bugs:	Report bugs to Wine Bugzilla at https://bugs.winehq.org
	Please search the bugzilla database to check whether your
	problem is already known or fixed before posting a bug report.

## IRC:	Online help is available at channel #WineHQ on irc.libera.chat.

## Git:	The current Wine development tree is available through Git.
	Go to https://www.winehq.org/git for more information.

If you add something, or fix a bug, please send a patch (preferably
using git-format-patch) to the wine-devel@winehq.org list for
inclusion in the next release.

--
Alexandre Julliard
julliard@winehq.org
