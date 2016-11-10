Summary: A command line SMTP client that's simple
Name: email
Version: 3.2.3
Release: 2%{?dist}
License: GPL
Group: Applications/Text
URL: https://github.com/deanproxy/eMail

Source0:  https://github.com/deanproxy/eMail/archive/%{version}.zip
# dlib version tag
%global dlibtag 1.0
Source1: https://github.com/deanproxy/dlib/archive/%{dlibtag}.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make, autoconf, automake
BuildRequires: glibc-devel
BuildRequires: openssl-devel
Requires: gnupg

Provides: %{_bindir}/email

%description
Email is a program for the Unix environment that sends messages. You may think
that this has already been done, and it has, but not with the quality and
enhancements that email has! Have you ever wanted to send email from the
command line using your SMTP server instead of sendmail? Have you ever wanted
to send email without entering a confusing menu application and you only wanted
to push a few command line options to route your email to the SMTP server of
your choice? Did you want to encrypt that email with gpg before it was sent but
wanted the email client to do it for you? If you answered yes to all of these
questions, then email is for you. You can now send email via the command line
to remote SMTP servers. You can have it encrypted to the recipient of your
choice. This and many other possibilities are easily implemented with email.

Email boasts a lot of other qualities as well.

    * Email supports SMTP Authentication.
    * Email makes it possible to send to multiple recipients and also CC and
      BCC multiple recipients.
    * You can use an address book that is in an easy to format method.
    * You are also able to send attachments using a swift flick on the command
      line to specifying multiple files.
    * Personalized signature file with dynamic options.


%prep

%setup -q -n eMail-%{version} -a 1
rmdir dlib
mv -f dlib-%{dlibtag} dlib
echo %{version} > VERSION


%build
export CFLAGS="%{optflags} -I../include -I../dlib/include"
export LDFLAGS="-L../dlib"
%configure

%{__make} %{?_smp_mflags} 

%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog README.md THANKS AUTHORS
%doc %{_mandir}/man?/*
%{_bindir}/*
%dir %{_sysconfdir}/email/
%config(noreplace) %{_sysconfdir}/email/*

%changelog
* Mon Aug 29 2016 Igor Velkov <iav@iav.lv> - 3.2.3-2
- Roll up to upstream

* Fri Nov 27 2009 Steve Huff <shuff@vecna.org> - 3.1.2-2
- Entered the correct project URL.

* Thu Nov 19 2009 Steve Huff <shuff@vecna.org> - 3.1.2-1
- Initial package.
