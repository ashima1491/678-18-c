
from .base import Base
from aggiestack_project.utility import def_image, def_flavor, def_hardware

class Show(Base):
    

    def run(self):
        outfile = open("aggiestack-log.txt", "a+")
#         print('show, world!')
        #print(self.options)
        if(self.options['images']):
            def_image.getImageList()
        elif(self.options['flavors']):
            def_flavor.getFlavorList()
        elif(self.options['hardware']):
            def_hardware.getHardwareList()
#         elif(self.options['admin']):
#             print("admin in show")
#             def_hardware.getHardwareList()    

      
         
        else:
            outfile.write('Status : FAILURE')
            outfile.write('\n')
            outfile.write("Invalid parameter")