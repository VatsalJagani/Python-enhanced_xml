# python test.py
# This file test the enhanced_xml functionality

from __init__ import EnhancedXMLElement
import xml.etree.ElementTree as ET

A = ET.ElementTree(file='a.xml')
a = A.getroot()
a = EnhancedXMLElement(a)


B = ET.ElementTree(file='b.xml')
b = B.getroot()
b = EnhancedXMLElement(b)

print(a.compare(b))
print(a == b)

a = a + b   # or a.merge(b)

A.write("c.xml")