import os
import shutil
import subprocess
import sys
import os.path as path
import nuke

###adding pluginpaths for rapid images globals###





nuke.pluginAddPath('.../shared/workgroups/nuke/globals/')
nuke.pluginAddPath('.../shared/workgroups/nuke/globals/gizmos')
nuke.pluginAddPath('.../shared/workgroups/nuke/globals/templates')
nuke.pluginAddPath('.../shared/workgroups/nuke/globals/python')

nuke.pluginAddPath('.../shared/workgroups/nuke/ExternalTools/')
nuke.pluginAddPath('.../shared/workgroups/nuke/ExternalTools/gizmos')
nuke.pluginAddPath('.../shared/workgroups/nuke/ExternalTools/templates')
nuke.pluginAddPath('.../shared/workgroups/nuke/ExternalTools/python')

nuke.pluginAddPath('.../shared/workgroups/nuke/clientTools01/')
nuke.pluginAddPath('.../shared/workgroups/nuke/clientTools01/gizmos')
nuke.pluginAddPath('.../shared/workgroups/nuke/clientTools01/templates')
nuke.pluginAddPath('.../shared/workgroups/nuke/clientTools01/python')

nuke.tprint("successfully loaded dyNuke globals directory")

nuke.pluginAddPath('.../shared/workgroups/nuke/globals/Tools/Icons')
nuke.pluginAddPath('.../shared/workgroups/nuke/globals/Tools')


