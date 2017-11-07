import imp
import os
import shutil

def initReadNode():

    print "initiation ReadNode"

     #g = nuke.toNode('dyRead2')
    g = n = nuke.thisNode()

    #init
    g['clientdd'].setValues(['Vikingbad', 'tmp', 'Vedum','_Projekt_införsäljning','Ikea'])

    # load project definition object
    p = imp.load_source('projectdefinition', '//DISKSTATION/Projects/Vikingbad/startup/projectdefinition.py')
    project = p.projectDefinition()
    project.init()

    # set projects list
    g['projectdd'].setValues(project.dyProjectList)

    # set tasks
    g['taskdd'].setValues(project.tasklist)
    g['taskdd'].getValue()

    # set dateFolders
    folder = project.dyProjectBase+project.client +"/"+ project.project  +"/Development/"+str(g['taskdd'].value() )+ "/Max/RenderOutput/"
    tlist = [str(i) for i in os.listdir( folder ) if os.path.isdir(folder+i) ]
    g['datedd'].setValues(tlist)

    # set images
    folder = folder + g['datedd'].value()
    images = [i for i in os.listdir(folder)]
    g['imagedd'].setValues(images)


def dyReadCallback():
    print "callback"
    g = nuke.thisNode()
    #k = nuke.thisKnob()
    if (g['title'].value() in   "DYNAGRAPH READ NODE"):
        initReadNode()






def renderAllWrites():

    g = nuke.toNode('dyRead')

    images = g['imagedd'].values()

    writeNodes = [node for node in  nuke.allNodes() if node.Class() == 'Write' ]

    for image in images:

        print image

        g['imagedd'].setValue(image)

        for node in writeNodes:
            try:
                print''
                print 'Preparing to render:'
                print node.knob('file').value()
                nuke.execute(node,0,0)
                print 'Render Complete for',str(node.knob('file').value())
            except:
                print '----ERROR executing',node.knob('name').value(),'----'


def initImages():

    # load project definition object
    p = imp.load_source('projectdefinition', '//DISKSTATION/Projects/Vikingbad/startup/projectdefinition.py')
    project = p.projectDefinition()
    project.init()


    g = nuke.toNode('dyRead')
    images = g['imagedd'].values()
    for image in images:

            g['imagedd'].setValue(image)

            fullpath = ""

            with g:
                n = nuke.toNode('dyreadBase')
                fullpath = n['file'].evaluate()

            d =  folder = project.dyProjectBase+project.client +"/"+ project.project  +"/Development/"+str(g['taskdd'].value() )+ "/Max/RenderOutput/Master/"
            if not os.path.exists(d):
                os.makedirs(d)
            newpath =  d + image

            # copy
            print fullpath
            print newpath
            shutil.copyfile(fullpath,newpath)

    # reload and set to master
    initReadNode()
    g['datedd'].setValue("Master")


#nuke.removeKnobChanged(dyReadCallback, nodeClass="Read")
nuke.addKnobChanged(dyReadCallback, nodeClass="Read")
initReadNode()






