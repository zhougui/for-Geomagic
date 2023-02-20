import geomagic.api.v2
import geomagic.app.v2
for m in geomagic.app.v2.execStrings: exec m in locals(), globals()
from geomagic.app.v2.gui.dialog import *
from geomagic.app.v2.gui.selector import *

class SelectionDemo(DialogHandler):

   def __init__(self, name, modal):
      super(SelectionDemo, self).__init__(name, modal)
    
   def formDialog(self):
      self.dialog().setButtonVisible (1, False);
      self.dialog().setButtonVisible (2, False);
      return True

   def onStart(self):
      self.selector = FeatureSelector()
      self.selector.featureSelected += self.onFeatureSelected
      return True
      
   def onStop(self):
      self.selector.stop()
      
   def onFeatureSelected(self, sender, feature):
      p = feature.position
      px = p.x()
      py = p.y()
      pz = p.z()
      print "%s" % (feature.name),";",px*1000,";",py*1000,";",pz*1000


   def onOK(self):
      return True
      
demo = SelectionDemo(u'Selection Demo', false)
demo.start()
