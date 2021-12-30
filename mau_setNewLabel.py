#--------------------------------------------------
# mau_setNewLabel.py
# version: 1.0.0
# last updated: 28.03.21
#--------------------------------------------------

import nuke

def setNewLabel():
    #CREATE LIST TO CHECK HOW MANY NODES ARE SELECTED
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

            txt = nuke.getInput("Set New Label")

            if txt == None:
                pass
            else:
                for i in nuke.selectedNodes():
                    i.knob('label').setValue(txt)
                
        except:
            pass
