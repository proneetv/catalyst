# Distributed under the GNU General Public License version 2
# Copyright 2003-2004 Gentoo Technologies, Inc.

import builder

class generic_amd64(builder.generic):
	"abstract base class for all amd64 builders"
	def __init__(self,myspec):
		builder.generic.__init__(self,myspec)
		self.settings["mainarch"]="amd64"
		self.settings["CHROOT"]="chroot"

class arch_amd64(generic_amd64):
	"builder class for generic amd64 (athlon64/opteron)"
	def __init__(self,myspec):
		generic_amd64.__init__(self,myspec)
		self.settings["CFLAGS"]="-O2"
		self.settings["CHOST"]="x86_64-pc-linux-gnu"

def register(foo):
	"Inform main catalyst program of the contents of this plugin."
	foo.update({"amd64":arch_amd64})
		