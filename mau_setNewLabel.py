#--------------------------------------------------
# mau_setNewLabel.py
# version: 1.0.1
# last updated: 08.01.22 (DD.MM.YY)
#--------------------------------------------------

import nuke

def setNewLabel():
    #CREATE LIST TO CHECK HOW MANY NODES ARE SELECTED
    node = nuke.selectedNode()
    a = [i.name() for i in nuke.selectedNodes()]
    
    #IF MORE THAN 1 NODE IS SELECTED, RETURN NUKE MESSAGE
    if len(a) > 1:
        nuke.message('Please select only one node.')
    
    #IF ONLY ONE NODE IS SELECTED, PROCEED TO ADD NEW LABEL
    else:
        try:
            
            #CREATE CUSTOM PANEL TO GET USER INPUT
             #p = nuke.Panel('Set New Label')
             #p.addSingleLineInput('New Label', '')
             #p.setWidth(350)
             #p.show()
             #txt = p.value('New Label')
                
            actualLabel = node.knob('label').value()
            txt = nuke.getInput("Set New Label",actualLabel)

            if txt == None:
                pass
            else:
                for i in nuke.selectedNodes():
                    i.knob('label').setValue(txt)
                
        except:
            pass
