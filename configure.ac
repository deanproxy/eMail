#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.
AC_PREREQ(2.60)
AC_INIT(email, 3, <dean.nospam@dean.nospam.proxy.com>)
AC_CONFIG_SRCDIR([src/addr_parse.c])
AC_CONFIG_HEADER([include/config.h])
AC_GNU_SOURCE


# Checks for programs.
AC_PROG_CC
AC_PROG_MAKE_SET

AC_ARG_WITH(utc, [  --with-utc              Use Coordinated Universal Time (UTC) instead of localtime], [AC_DEFINE(USE_GMT, 1, [Tell's us to use gmtime()])], )
AC_ARG_WITH(ssl, [  --with-ssl		    force use of TLS/SSL], [use_ssl=$withval], )
AC_SYS_LARGEFILE

if test -n "$GCC"; then
    CFLAGS="$CFLAGS -Wall -W"
fi

# Checks for libraries.
AC_SEARCH_LIBS(socket, socket)
AC_SEARCH_LIBS(sqrt, m)
AC_SEARCH_LIBS(gethostbyname, nsl)
if test -z "$use_ssl" -o "$use_ssl" = "yes"; then
	AC_SEARCH_LIBS(X509_free, crypto)
	AC_SEARCH_LIBS(RAND_seed, crypto)
   AC_CHECK_HEADERS([openssl/crypto.h openssl/x509.h openssl/pem.h openssl/ssl.h openssl/err.h])
   AC_CHECK_LIB([ssl], [SSL_CTX_new])
fi

echo $LIBS

# Checks for header files.
AC_HEADER_STDC
AC_HEADER_SYS_WAIT
AC_CHECK_HEADERS([arpa/inet.h fcntl.h libintl.h netdb.h netinet/in.h stdlib.h string.h strings.h sys/ioctl.h sys/socket.h sys/time.h termios.h unistd.h])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_TIME
AC_STRUCT_TM

# Checks for library functions.
AC_FUNC_FORK
AC_PROG_GCC_TRADITIONAL
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_TYPE_SIGNAL
AC_FUNC_STAT
AC_FUNC_STRFTIME
AC_FUNC_VPRINTF
AC_CHECK_FUNCS([gethostbyname gethostname getpass gettimeofday memset putenv socket sqrt strcasecmp strchr strerror strrchr uname])

echo $ECHO_N "checking if strftime is GNU or Non-GNU... "
${srcdir}/check_strftime.sh $CC
if test $? -ne 0
then
    echo "Non-GNU"
else
    echo "GNU"
    CFLAGS="$CFLAGS -DUSE_GNU_STRFTIME"
fi

AC_ARG_WITH(
	[system-dlib],
	AS_HELP_STRING(
		[--with-system-dlib],
		[Use system dlib, default if off]),
	[cwd="${includedir}"; dlib_include=${includedir}/dlib; dlib_static=${libdir}/libdlib.a],
	[cwd="$(pwd)"; dlib_include=$(pwd)/dlib/include; dlib_static=../dlib/libdlib.a]
)
AC_SUBST(cwd)
AC_SUBST(dlib_static)

CFLAGS="$CFLAGS -I$cwd -I$cwd/src -I$cwd/include -I../include -I${dlib_include}"
VERSION="${VERSION:-$(cat VERSION)}"
AC_SUBST(VERSION)
CFLAGS="$CFLAGS -I../dlib/include -DEMAIL_VERSION='\"${VERSION}\"' "
CFLAGS="$CFLAGS -DEMAIL_DIR='\"${sysconfdir}/email\"'"

AC_CONFIG_FILES([Makefile
                 src/Makefile
                 email.help
                 email.1])
AC_OUTPUT
if test "$use_ssl" = "no"; then
	args="--without-ssl"
fi
cd dlib
./configure $args --host=$host_alias
cd ..
