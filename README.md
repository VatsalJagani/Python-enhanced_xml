# enhanced_xml
The enhanced_xml is a python library gives some more feature over python's default xml library.

Version = 1.0.0


## Features
Currently library is giving following extra features than the default xml library.
- Merge an xml element into another xml element.
- Compare two xml element.
  - Currently xml element comparison is works only on below elements:
    - tag
    - attributes
    - text
  - children comparison is not supported yet.


## Usage

### XML element
- EnhancedXMLElement can be initialized like:
```
A = ET.ElementTree(file='a.xml')
a = A.getroot()
a = EnhancedXMLElement(a)
```
- An XML element can br retrieved from EnhancedXMLElement like:
```
a.xml_element
```

### XML element comparison
`compare` function can compares the two XML element.

`compare` function of EnhancedXMLElement has below signature.
```
def compare(self, other, check_attributes=CHECK_ALL, check_text=True, check_children=False)
```
- other - second EnhancedXMLElement to compare with
- check_attributes - accepts three values (defaults to CHECK_ALL)
  - CHECK_ALL - compare all the attributes
  - A list of attributes - compares the attributes available in the list and ignore other attributes
  - CHECK_NONE - does not compare attributes
- check_text - accepts boolean (defaults to True)
- check_children - accepts boolean (defaults to False)
  - Checking children is not implemented in the current version of the library.

EnhancedXMLElement comparison supports == operator comparison.
- == operator works on the default signature of compare function which does not check for children.

### XML element merge
`merge` function can merge the XML element into another XML element. Find example in test.py file.

`merge` function of EnhancedXMLElement has below signature.

```
def merge(self, other):
```
- other - second EnhancedXMLElement to merge into this EnhancedXMLElement.

EnhancedXMLElement comparison supports + operator merging.
- `a + b` merges XML element of b into a.



# Contact Info
- Author: Vatsal Jagani
- Email: vatsaljagani85@gmail.com