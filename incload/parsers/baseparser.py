# an extension to the HTMLParser class which supports some additional functionalities
# will be inherited by all other parsers of this project
from html import parser
class BaseParser(parser.HTMLParser):
  def __init__(self):
    # call parent class constructor
    parser.HTMLParser.__init__(self)
    # define some stuff here
    self.__EmptyChars=' '+chr(10)+chr(194)+chr(160) # will be stripped later on to detect empty strings
    
  # we will add some helpers here
  def getAttribute(self,attr,attrname):
    for a in attr:
      if a[0]==attrname:
        return a[1]
    return ""
  def isEmpty(self,str):
    for c in self.__EmptyChars:
      str=str.replace(c,"")
    return len(str)==0