#!/usr/bin/env python
"""
enhanced_xml module
Repo: https://github.com/VatsalJagani/enhanced_xml
"""

__author__ = "Vatsal Jagani"
__copyright__ = ""
__credits__ = ""
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Vatsal Jagani"
__email__ = "vatsaljagani85@gmail.com"
__status__ = "Production"


import warnings
import xml.etree.ElementTree as XML_ET
from xml.etree.ElementTree import Element as XML_Element


CHECK_ALL = 1
CHECK_NONE = 0


class EnhancedXMLException(Exception):
    pass


class EnhancedXMLElement:
    """
    This class is enhancement over python's default xml element.
    This class supports following functions:
    - compare - Two xml element can be compare (can also be used with == operator)
    - merge - Two xml elements can be merged (can also be used with + operator)
    """
    def __init__(self, xml_element):
        """
        Initialization of EnhancedXMLElement.
        Verifies the xml_element should be an object of import xml.etree.ElementTree.Element
        """
        if type(xml_element) != XML_Element:
            raise EnhancedXMLException("xml_element should be the type of xml.etree.ElementTree.Element")
        self.xml_element = xml_element
    
    def __add__(self, other):
        """
        Two EnhancedXMLElement can be merged like a + b (uses merge function)
        """
        return self.merge(other)
    
    def merge(self, other):
        """
        Merge two xml elements. (+ operator is also supported)

        - other - second EnhancedXMLElement to merge into this EnhancedXMLElement object.
        """
        if self.xml_element.tag == other.xml_element.tag:
            self._xml_element_add(self.xml_element, other.xml_element, None)
            return self
        else:
            raise EnhancedXMLException("The root tag should be the same to merge the xml.")
    
    def __eq__(self, other):
        """
        Two EnhancedXMLElement can be compared like a == b (uses compare function)
        """
        return self.compare(other)

    def compare(self, other, check_attributes=CHECK_ALL, check_text=True, check_children=False):
        """
        Compare two xml elements. (== operator is also supported)

        - other - second EnhancedXMLElement to compare with
        - check_attributes - accepts three values (defaults to CHECK_ALL)
          - CHECK_ALL - compare all the attributes
          - A list of attributes - compares the attributes available in the list and ignore other attributes
          - CHECK_NONE - does not compare attributes
        - check_text - accepts boolean (defaults to True)
        - check_children - accepts boolean (defaults to False)
          - Checking children is not implemented in the current version of the library.
        """
        return self._xml_element_compare(self.xml_element, other.xml_element, check_attributes, check_text, check_children)

    def _xml_element_compare(self, a, b, check_attributes=CHECK_ALL, check_text=True, check_children=False):
        """
        Compare two xml element
        """
        #  checking tag
        if a.tag != b.tag:
            return False

        # checking attributes
        if check_attributes == CHECK_ALL:
            for i in a.attrib:
                if i not in b.attrib:
                    return False
                elif a.attrib[i] != b.attrib[i]:
                    return False
        elif check_attributes != CHECK_NONE and type(check_attributes) == list:
            for attr in check_attributes:
                if (attr not in a.attrib and attr in b.attrib) or (attr not in b.attrib and attr in a.attrib):
                    return False
                if attr in a.attrib and a.attrib[attr] != b.attrib[attr]:
                    return False
        
        # checking text
        if check_text:
            if a.text != b.text:
                return False

        # checking children
        if check_children:
            warnings.warn(
                "This function of verification of children is not implemented yet."
                "Use False for check_children",
                NotImplementedError, stacklevel=2
                )
            return False
        
        return True
        
    def _xml_element_present(self, elm, element_to_check_in, check_children=False):
        """
        Checks if the xml elm is present in the children of element_to_check_in
        """
        if not check_children:
            for i in list(element_to_check_in):
                if self._xml_element_compare(i, elm):
                    return i
            return False
        else:
            warnings.warn(
                "This function of verification of children is not implemented yet."
                "Use False for check_children",
                NotImplementedError, stacklevel=2
                )
            return False

    def _xml_element_add(self, a, b, parent_of_a):
        """
        Helper function for two xml merge
        """
        if self._xml_element_compare(a, b):
            # if the element is same
            for child_of_b in list(b):
                child_of_a = self._xml_element_present(child_of_b, a)
                if child_of_a == False:
                    # add element in c
                    a.append(child_of_b)
                else:
                    # go in depth
                    self._xml_element_add(child_of_a, child_of_b, a)
        else:
            # if the element is different
            parent_of_a.append(b)
