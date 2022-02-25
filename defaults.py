
import os
import nuke

# Write
nuke.knobDefault("Write.exr.compression","0")
nuke.knobDefault("Write.channels", "rgba")

# RotoPaint
nuke.knobDefault("RotoPaint.toolbox", "brush {{brush ltt 0} {clone ltt 0}}")

# labels
nuke.knobDefault('Blur.label','size: [value size]')
nuke.knobDefault('Defocus.label','size: [value defocus]')
nuke.knobDefault('TimeOffset.label','[value time_offset]')
nuke.knobDefault("Dot.note_font_size","22")
nuke.knobDefault("StickyNote.label", '<align left>')
nuke.knobDefault("Remove.label", "[value channels]")
nuke.knobDefault("Shuffle.label", "[value in] => [value out]")

nuke.knobDefault("BackdropNode.note_font_size", "128")
nuke.knobDefault("BackdropNode.note_font", "bold")
nuke.knobDefault("BackdropNode.note_font_color", "0xffffffff")
nuke.knobDefault("Output.note_font_size", "18")
nuke.knobDefault("Output.note_font", "bold")
nuke.knobDefault("Write.note_font_size", "18")
nuke.knobDefault("Write.note_font", "bold")

nuke.knobDefault("Blur.channels","rgba")
nuke.knobDefault("Remove.channels", "rgba")
nuke.knobDefault("Remove.operation", "keep")

##################   PROJECT SETTINGS   ##################
nuke.knobDefault("Root.format", "HD_1080")
nuke.knobDefault("Root.project.directory", "[file dirname [knob root.name]]")
# os.chdir(os.path.dirname(nuke.root().name())) # set this to onScriptLoad of the project setting to automatically set the working directory to where the nuke file is located

# Formats
nuke.addFormat ("1280 720 0 0 1280 720 1.0 720p")
nuke.addFormat ("2048 1108 0 0 2048 1108 1.0 2k_185")
nuke.addFormat ("2048 1157 0 0 2048 1157 1.0 2k_3perf")
nuke.addFormat ("2048 872 0 0 2048 872 1.0 2k_235")

# shortCuts
nuke.menu( 'Nodes' ).addCommand( 'Channel/Shuffle', "nuke.createNode( 'Shuffle' )", 'alt+s')
nuke.menu( 'Nodes' ).addCommand('Comp/Stencil','nuke.createNode("Merge2","operation stencil")', 'ctrl+alt+shift+s')
nuke.menu( 'Nodes' ).addCommand('Comp/Mask','nuke.createNode("Merge2","operation mask")', 'ctrl+alt+shift+a')
nuke.menu( 'Nodes' ).addCommand("Stencil", 'nuke.createNode("Merge2", "operation stencil")','Ctrl+m')
nuke.menu( 'Nodes' ).addCommand("Copy", 'nuke.createNode("Merge2", "operation copy")','Ctrl+shift+m')
