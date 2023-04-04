import rclpy
from rclpy.node import Node
import xml.etree.ElementTree as ET


class Change(Node):
   def __init__(self):
      super().__init__("Change")
      tree= ET.parse('/home/pmlab/yueju/asd.urdf')
      root=tree.getroot()

      for i in root.iter('joint'):
         if i.attrib['name']=="Gripper_Joint":
            i.find('origin').set('xyz','400 100 100')

            tree.write('asd1.urdf')

            print(i.find('origin').get('xyz'))
            file=open('/home/pmlab/yueju/asd1.urdf','r+',encoding='utf-8')
            co=file.read()
            file.seek(0,0)
            file.write('<?xml version="1.0" encoding="utf-8"?>\n'+co)
            
        
def main():
    rclpy.init()
    rclpy.spin(Change())    
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
   











""" 
kl=file.readlines()

lie = '    <color rgba="0.792156862745098 0.819607843137255 0.933333333333333 1" />\n'
for line in kl:
   if line==lie: 
      print(lie)  
        
 """
