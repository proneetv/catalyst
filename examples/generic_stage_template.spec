# generic installation stage specfile
# used to build a stage1, stage2, or stage3 installation tarball

# The subarch can be any of the supported catalyst subarches (like athlon-xp).
# Refer to "man catalyst" or <http://www.gentoo.org/proj/en/releng/catalyst/>
# for supported subarches
# example:
# subarch: athlon-xp
subarch:

# The version stamp is an identifier for the build.  It can be anything you wish
# it to be, but it is usually a date.
# example:
# version_stamp: 2006.1
version_stamp: 

# The target specifies what target we want catalyst to do. For stages, the
# supported targets are: stage1 stage2 stage3
# example:
# target: stage2
target:

# The rel_type defines what kind of build we are doing.  This is merely another
# identifier, but it useful for allowing multiple concurrent builds.  Usually,
# default will suffice.
# example:
# rel_type: default
rel_type:

# This is the system profile to be used by catalyst to build this target.  It is
# specified as a relative path from /usr/portage/profiles.
# example:
# profile: default-linux/x86/2006.1
profile:

# This specifies which snapshot to use for building this target.
# example:
# snapshot: 2006.1
snapshot:

# This specifies where the seed stage comes from for this target,  The path is
# relative to $clst_sharedir/builds.  The rel_type is also used as a path prefix
# for the seed.
# example:
# default/stage3-x86-2006.1
source_subpath:

# These are the hosts used as distcc slaves when distcc is enabled in your 
# catalyst.conf.  It follows the same syntax as distcc-config --set-hosts and
# is entirely optional.
# example:
# distcc_hosts: 127.0.0.1 192.168.0.1
distcc_hosts:

# This is an optional directory containing portage configuration files.  It
# follows the same syntax as /etc/portage and should be consistent across all
# targets to minimize problems.
# example:
# portage_confdir: /etc/portage
portage_confdir:

# This option specifies the location to a portage overlay that you would like to
# have used when building this target.
# example:
# portage_overlay: /usr/local/portage
portage_overlay:

# This allows the optional directory containing the output packages for
# catalyst.  Mainly used as a way for different spec files to access the same
# cache directory.  Default behavior is for this location to be autogenerated
# by catalyst based on the spec file.
# example:
# pkgcache_path: /tmp/packages
pkgcache_path:

# These options are only available when building a stage1 or stage2 target and
# are all optional.  These allow for emulating the changes possible during ai
# bootstrap.  Some possible uses of these would be building embedded stages
# requiring a different CHOST or building a stage2 with NPTL support from a
# stage1 tarball that is built without it.
# If left blank, then the catalyst defaults from arch.py are used.

# This option is used to change the CHOST from what is default in the profile
# to whatever you specify.  This is useful for building NPTL, for example.
# example:
# chost: i686-pc-linux-gnu
chost:

# This option allows you to change the default CFLAGS that will be used in
# building this stage.  This really should remain generic, as putting
# optimizations flags here will build a stage1 tarball that is no longer
# generic.
# example:
# cflags: -Os -pipe -fomit-frame-pointer -mcpu=i686
cflags:

# This is for setting the CXXFLAGS.  Generally, this would be set to the same
# as CFLAGS.  In fact, it will mirror CFLAGS by default.
# example:
# cxxflags: -Os -pipe -fomit-frame-pointer -mcpu=i686
cxxflags:

# Setting this option sets LDFLAGS in make.conf in your stage.  This would be
# useful for setting up an embedded or hardened system.
# example:
# ldflags: -Wl,-O1 -Wl,-z,now
ldflags:
