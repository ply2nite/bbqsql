#!/usr/bin/python
import os,subprocess,sys
import bbqcore
from bbqcore import bcolors
import text


# main menu

define_version = 1.0

try:
 
     # intitial user menu
    if not os.path.isfile("agreement"):
        print """Copyright 2012, bbqsql injection tool
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer
      in the documentation and/or other materials provided with the distribution.
    * Neither the name of Social-Engineer Toolkit nor the names of its contributors may be used to endorse or promote products derived from
      this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The above licensing was taken from the BSD licensing and is applied to bbqsql injecton tool as well.

Note that the bbqsql injection toolkit is provided as is, and is a royalty free open-source application.
#
Feel free to modify, use, change, market, do whatever you want with it as long as you give the appropriate credit where credit
is due (which means giving the authors the credit they deserve for writing it).\n"""

        print bcolors.RED + """ The bbqsql injection toolkit is designed for legal use only """
        choice = raw_input("\nDo you agree to the terms of service [y/n]: ")
        if choice == "yes" or choice == "y":
            filewrite = file("agreement", "w")
            filewrite.write("user accepted")
            filewrite.close()
            print bcolors.ENDC
        else: 
            print "[!] Exiting the bbqsql injection toolkit" + bcolors.ENDC
            sys.exit()
             
    while 1:
        bbqcore.show_banner(define_version,'1')
        show_main_menu = bbqcore.CreateMenu(text.main_text, text.main_menu)
 
         # special case of list item 99
        print '\n  99) Exit the bbqsql injection toolkit\n'
 
        # mainc ore menu
        main_menu_choice = (raw_input(bbqcore.setprompt("0", "")))

        # quit out
        if main_menu_choice == 'exit' or main_menu_choice == "99" or main_menu_choice == "quit":
            bbqcore.ExitBBQ(0)
           # cleans up stale processes from SET

        if main_menu_choice == '1': # Blind SQL Injection Test
            print '1'
            try: reload(blind_sql)
            except: import blind_sql
    
# ## handle keyboard interrupts
except KeyboardInterrupt:
    print "\n\n Cath you later " + bbqcore.bcolors.RED+"@" + bbqcore.bcolors.ENDC+" the dinner table."
# #
# ## handle exceptions
except Exception, error:
# # #       setcore.log(error)
    print "\n\n Something went wrong, printing the error: "+ str(error)
