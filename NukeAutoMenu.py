import os,shutil,subprocess, sys
import os.path as path
import nuke

#


### import project manager ###
import re, nukescripts
#import revealInFolder
#import renameSlate
#import renameAutoRender
#import renameDisableNodes
#import labelAutobackdrop
#import mochaToNuke
#import gotoShotSettings





### original menu py file ### there might be duplicates..
#import ri_nuke_globals
from python import *
from gizmos import*
from templates import*
#from projects import*
#from dy_nuke_globals import*
#import DeadlineNukeClient


#add gizmos to tools menu


#nuke.menu("Nodes").addMenu("Dynagraph").addCommand("chromaticAbberation", "nuke.createNode('chromaticAbberation')", icon="lumaglowicon.png")
#nuke.menu("Nodes").addMenu("Dynagraph").addCommand("dy_edgeBlend", "nuke.createNode('ri_edgeBlend')", icon="EdgeBlur.png")
#nuke.menu("Nodes").addMenu("Dynagraph").addCommand("dy_lightWrap", "nuke.createNode('ri_lightWrap')", icon="LightWrap.png")
#nuke.menu("Nodes").addMenu("Dynagraph").addCommand("dy_PassGrader", "nuke.createNode('ri_PassGrader2')", icon="Grade.png")


# Adding gizmos from Nukepedia to tools menu
#nuke.menu("Nodes").addMenu("Dynagraph/Nukepedia", icon="nukepedia.png").addCommand('Backdrop_Label', 'labelAutobackdrop.autoBackdrop()', 'Alt+b', icon="Blur.png")



#'C:\Archive\Projects\ri_nuke_globals'





#print 'path defined'  


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
    #scriptsMenu.addCommand('Update menu', 'createMenu(scriptsFolder,menyname)')

    scriptsMenu.addSeparator()
    
    absolutFiles=[]
    relativeFiles=[]
    folders =[]
    allFiles=[]
    currentFile =''
    
    relativeGizmos =[]
    relativeNukes=[]
    
    #currentGizmo=[]
    
    for root, dirs, files in os.walk(scriptsFolder):
      
        for x in files:
           correct= root.replace('\\','/')

           currentFile = (correct + '/'+x)
           
           allFiles.append(currentFile)
           if currentFile.endswith('.py'):
               #print 'scriptFolder ', scriptsFolder

               
               relativeFiles.append(currentFile.replace((scriptsFolder + '/'),''))
               
               
           if currentFile.endswith('.gizmo'):              
               
               relativeGizmos.append(currentFile.replace((scriptsFolder + '/'),''))
               #relativeGizmos.append(currentFile)
               
           if currentFile.endswith('.nk'):
               relativeNukes.append(currentFile.replace((scriptsFolder + '/'),''))

    relativeFiles.sort()
    relativeGizmos.sort()
    relativeNukes.sort()
    newList = []
    
    for i in range(0,len(relativeFiles),1):
        if not re.search('__init__.py' , relativeFiles[i]):
            newList.append(relativeFiles[i])
            
            #print "INIT!"
    
            
    relativeFiles = newList
    #print 'relativeFiles ', relativeFiles

    rm = nuke.menu('Nuke').addMenu(menyname)
    for relativeFile in relativeFiles:
        
        
        split = relativeFile.split('/')
        fileName = split[-1].split('.')

      
        
        rm.addCommand(relativeFile, fileName[0] +'.' +fileName[0]+'()')
        
    for relativeGizmo in relativeGizmos:
       
       

       hej = relativeGizmo.split('/')
       fileName = hej[-1].split('.')[0]
       #print relativeGizmo
       rm.addCommand(relativeGizmo, "nuke.createNode('"+fileName+"')")
    
     
       # print 'filename', fileName

       # print relativeGizmo
       #nuke.menu('Nuke').addCommand(relativeGizmo , lambda: nuke.createNode( fileName ) )
       
       
       #templates
       
    for relativeNuke in relativeNukes:
        hej = relativeNuke.split('/')
        fileName = hej[-1].split('.')[0]
        #print relativeNuke
        templatepath= (scriptsFolder +'/' + relativeNuke)
        rm .addCommand(relativeNuke, "nuke.nodePaste('"+templatepath+"')")
       
        

 
scriptsFolder = '//DISKSTATION/Projects/_Admin/Lokaler_utrustning_can/Datorer_natverk/shared/workgroups/nuke/globals'
createMenu(scriptsFolder,"Dynagraph Global")
vbFolder = '//DISKSTATION/Projects/_Admin/Lokaler_utrustning_can/Datorer_natverk/shared/workgroups/nuke/vikingbad'
createMenu(vbFolder,"Vikingbad")
ExternalscriptsFolder = '//DISKSTATION/Projects/_Admin/Lokaler_utrustning_can/Datorer_natverk/shared/workgroups/nuke/ExternalTools'
createMenu(ExternalscriptsFolder,"External Tools")

#menubar = nuke.menu("Nuke")

print 'Interface Loaded'