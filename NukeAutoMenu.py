import os,shutil,subprocess, sys
import os.path as path
import nuke
import re, nukescripts
from python import *
from gizmos import*
from templates import*

def createMenu(scriptsFolder, menyname):
    if scriptsFolder in sys.path:
        print ''

    else:
        sys.path.append(scriptsFolder)
    from python import *
    from gizmos import*
    from templates import*

    if nuke.menu('Nuke').findItem(menyname):
        nuke.menu('Nuke').removeItem(menyname)
        print 'menu rebooted'

    if scriptsFolder is sys.path:
        print ''
    else:
        sys.path.append(scriptsFolder)
    scriptsMenu = nuke.menu('Nuke').addMenu (menyname)
    scriptsMenu.addSeparator()

    absolutFiles=[]
    relativeFiles=[]
    folders =[]
    allFiles=[]
    currentFile =''
    relativeGizmos =[]
    relativeNukes=[]
    for root, dirs, files in os.walk(scriptsFolder):
        for x in files:
           correct= root.replace('\\','/')
           currentFile = (correct + '/'+x)
           allFiles.append(currentFile)
           if currentFile.endswith('.py'):
               relativeFiles.append(currentFile.replace((scriptsFolder + '/'),''))
           if currentFile.endswith('.gizmo'):
               relativeGizmos.append(currentFile.replace((scriptsFolder + '/'),''))
           if currentFile.endswith('.nk'):
               relativeNukes.append(currentFile.replace((scriptsFolder + '/'),''))

    relativeFiles.sort()
    relativeGizmos.sort()
    relativeNukes.sort()
    newList = []
    for i in range(0,len(relativeFiles),1):
        if not re.search('__init__.py' , relativeFiles[i]):
            newList.append(relativeFiles[i])
    relativeFiles = newList
    rm = nuke.menu('Nuke').addMenu(menyname)
    for relativeFile in relativeFiles:
        split = relativeFile.split('/')
        fileName = split[-1].split('.')
        rm.addCommand(relativeFile, fileName[0] +'.' +fileName[0]+'()')
    for relativeGizmo in relativeGizmos:
       hej = relativeGizmo.split('/')
       fileName = hej[-1].split('.')[0]    
       rm.addCommand(relativeGizmo, "nuke.createNode('"+fileName+"')")
    for relativeNuke in relativeNukes:
        hej = relativeNuke.split('/')
        fileName = hej[-1].split('.')[0]
        templatepath= (scriptsFolder +'/' + relativeNuke)
        rm .addCommand(relativeNuke, "nuke.nodePaste('"+templatepath+"')")

scriptsFolder = '.../shared/workgroups/nuke/globals'
createMenu(scriptsFolder,"Dynagraph Global")
vbFolder = '.../shared/workgroups/nuke/client01'
createMenu(vbFolder,"client01")
ExternalscriptsFolder = '.../shared/workgroups/nuke/ExternalTools'
createMenu(ExternalscriptsFolder,"External Tools")


print 'Interface Loaded'
from defaults import *