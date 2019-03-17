
## This will explain the email program as well as it can.  

First thing is first.  This file will take place as sort of a FAQ sheet, because I already know what questions will be asked.


#### Q: How do I checkout the source from github and get everything I need?


A: Type the following in a shell:
    
        git clone --recursive git@github.com:deanproxy/eMail.git

---

#### Q: What is `eMail` ?


A:  `eMail` is a program I designed that will send email via the command line
    to remote smtp servers or use 'sendmail' internally, and fully interact with
    GNUPG to encrypt and sign your e-mails, so you decide to do so...
    You can get GNUPG at: http://www.gnupg.org

---

#### Q: How do I compile and Install this thing?


A: Just do this as root:
    
    ./configure
    make
    make install

If you want to use system dlib from e.g. /usr/include/dlib, then run `./configure --with-system-dlib`.

---

#### Q: Where is it installed?


A: the executable is called 'email' and is installed in a directory that is under the prefix or bindir specified during the `./configure` of email. If you choose to specify a prefix during configure, it will go under `$bindir`. Which, by default, is an offset of `$prefix/bin`.  If you specify `--bindir` then the binary will be put in `$bindir`.

If you do not specify a directory prefix during configure, then it will go under `/usr/local/bin/email`. The configuration files are installed by default in `/usr/local/etc/email`.  However, if you specify the `--sysconfdir` option during ./configure, then the configuration files will go in `$sysconfdir`. Please view `./configure --help`

---

#### Q: How do I make your freakin' program work?


A: Well, first thing you should do, is configure this email client. You will have the configuration file in `/usr/local/etc/email/email.conf` Some less important options are not set `(address_book, save_sent_mail, temp_dir reply_to, signature_file, signature_divide)` but you can easily set these by hand and they are not needed to properly run email.

You will see it has a few options you must set to your environment.

> `SMTP_SERVER:`	 Please specify your smtp server name, or IP address here

> `SMTP_PORT:`   	 Please specify your smtp servers port number for use

> `MY_NAME:`     	 Please specify your Name here

> `MY_EMAIL:`        Please specify your email address here

> `REPLY_TO:`        Specify a seperate reply to address here

> `SIGNATURE_FILE:`  Specify your signature file

> `ADDRESS_BOOK:`	 Where to find your address book file

> `SAVE_SENT_MAIL:`  What directory to save the email.sent file to

> `TEMP_DIR:`        Specify where to store temporary files

> `GPG_BIN:`         Specify where the gpg binary is located.

> `GPG_PASS:`        Optional passphrase for gpg.

> `SMTP_AUTH:`       LOGIN or PLAIN are supported SMTP AUTH types

> `SMTP_AUTH_USER:`  Your SMTP AUTH username

> `SMTP_AUTH_PASS:`  Your SMTP AUTH Password

> `USE_TLS:`         Boolean (true/false) to use TLS/SSL

> `VCARD:`           Specify a vcard to attach to each message

`SMTP_SERVER` can be either a remote <strong>SMTP</strong> servers fully qualified domain name, or an IP address.  You may also opt to use `sendmail` internally instead of sending via remote SMTP servers.  To do this you just put the path to the sendmail binary and any options you would like to use with sendmail (Use `-t`) in the place of the smtp server name... HINT: If you would like to send emails to people on your local box (i.e. `djones@localhost` ), then you must use the sendmail binary.

When you are specifying file paths, you can use the tilde wildcard as you  could in the shell to specify your home directory. Example: `~/.email.conf` would mean `/home/user/.email.conf` to the email program.

Once you are done here, you can leave your email in `/usr/local/etc/email/email.conf` or the directory you specified during the configure with `--sysconfdir=...` for a global configuration, or in your local home directory as `~/.email.conf` for a personal configuration.  Personal configs override global configs.  

You can get online help by using the `--help` option with email and specifying the command line option you need help with.  Example: `email --help encrypt`

If you use the `-encrypt` or `-sign` option, you MUST have GNUPG installed on your system. `email` uses gpg to encrypt the email to the FIRST email recipient

Example: 

    email -s "This is the subject" -encrypt dean@somedomain.org
    
In that example, I would be sending the email to dean@somedomain.org and gpg would encrypt it with the key of `dean@somedomain.org`

You can use `-high-priority` ( or -o ) to send your message in a high priority matter.  In MS Outlook you will see a little `!` mark next to the letter so that the recipient will see that the message is high priority!

You can send a message in one of two ways:
The first way is to already have a message ready to send.  Say if I have a file named `this.txt`  and I want to send it to `dean@somedomain.org`.  I can redirect this file to the email program in one of two ways.  

Example below:

    cat this.txt | email -s "Sending this.txt to you" dean@somedomain.org

> or

    email -s "Sending this.txt to you" dean@somedomain.org < this.txt

If you want to create a message, you will need to do two things here.

First set the environment variable "EDITOR" to your favorite editor. 

Example: 

    export EDITOR=vi

Please use your favorite editor in place of vi.

Now all you have to do is execute the example below:

Example:

    email -s "Subject" dean@somedomain.org

This will open up your favorite editor and let you write a email to `dean@somedomain.org` email will default to `vi` if you do not set EDITOR.

You can send to multiple recipients with `email`.  All you have to do is put commas between the email addresses you want the message to be sent to.

Example below:

    dean@somedomain.org,another@domain.com,you@domain.com 

Here are some more examples below:

Example: the below command will send a message that is encrypted with `dean@somedomain.org` key

    email -s "my email to you" -encrypt dean@somedomain.org,software@cleancode.org

Example: the example will sign the message directed to it.

    email -s "signed message" -sign dean@somedomain.org < secret_stuff.txt

Example: This will send to multiple recipients

    email -s "To all of you" dean@somedomain.org,you@domain.com,me@cleancode.org 

Example: Set message to high priority

    email -s "High priority email" -high-priority dean@somedomain.org

Example: Send message with 2 attachements

    email -s "here you go..." -attach file -attach file2 dean@somedomain.org

Example: Add headers to the message

    email -s "New Message" --header "X-My-Header: Stuff" \ --header "X-Another-Header: More Stuff" dean@somedomain.org

---

#### Q: Do you allow signatures?

A: Yes, we do.

Look in `email.conf` and edit the signature variables as needed.

If you're wondering what a signature divider is, it's the little thingy that divides your email message from the signature.

Usually it's '---' (Default)

Also, you can specify wild cards in the signature file.

    %c = Formated time, date, timezone ( looks like the output of 'date' )
    %t = Time only ( US Standard format )
    %d = Date Only ( US Standard format )
    %v = Version ( For us folks who want to endorse 'email' )
    %h = Host type (ex. Linux 2.2.19 i686 )
    %f = Prints output from the 'fortune(6)' command
    %% = Prints a % mark

Your sig could look like this:

    ---
    This message was sent: %c
	
    This would end up looking like: 
	This message was sent: Thu Dec 13 04:54:52 PM EST 2001

---

#### Q: How does the address Book work?

A: Set up your email.conf file to point to your very own address book.

There is a template in the email source directory that you can view to set up your own address book.  The format should be as below:

Any single name to email translation will have to have a 'single:' token before it:

	single: Software    = software@yourmomshouse.org
	single: Dean        = dean@somedomain.org
	single: "Full Name" = someone@somedomain.org

Any group name to email translation will have to have a 'group:' token before it: 

With groups, you can only use the Names of your single statements above... Format below:

	  group: Both = Software,Dean

See the `email.address.template` file for more information

---

### Q: Do you allow attachments?

A: YES!  We now support attachments with email!

Simply specify the files you want attached to your email by specifying the --attach option, with a list of files delemited by commas.  All files will be encoded with base64 and attached with the appropriate MIME headings.
    
Example:
    
    email -s Attachment --attach file dean@somedomain.org

    # Multiple files

    email -s Attachments --attach file1 --attach file2 dean@somedomain.org

---      

#### Q: Do you allow SMTP AUTH?

A: Yes! Email does `SMTP AUTH`.  You will need to set a few options in the `email.conf` file.  `SMTP_AUTH, SMTP_AUTH_USER and SMTP_AUTH_PASS`.  If you want to know more about this, please view the email manual page 'man email'.

---

#### Q: Can I join the development team?

A: Yes, send an email at http://deanproxy.com/contact/ and ask how, or just clone it with git (see above on how to do that) and start coding and committing!

---

#### Q: Why email?

A: Because 'mailx' won't send to remote smtp servers and I didn't have access to sendmail.

I needed something that would communicate with Remote smtp servers and encrypt my messages on the fly instead of taking numerous steps to do so.

---

#### Q: What does 'email' stand for?

A: Well, despite popular belief, it stands for "Encrypted Mail"  Not "Electronic Mail"

My initial purpose was to make e-mail easier to send via command line and encrypt it with out taking all the damn steps 'mailx' makes you take!   Sorry mailx!  

---

#### Q: Who are the developers?

A: Dean Jones - Main developer

http://deanproxy.com/contact/

That's about it so far. 
I hope you like the program `eMail`.

If you have any questions, bugs, or concerns please use:

https://github.com/deanproxy/eMail/issues
