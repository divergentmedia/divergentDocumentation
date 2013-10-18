#!/usr/bin/env Python

# sdaau 2013

import re
import markdown
from markdown.util import etree
from markdown.blockparser import BlockParser
from markdown import odict

class SkipProcessor(markdown.blockprocessors.BlockProcessor):
  def test(self, parent, block):
    return True #bool(self.RE.match(block))
  def run(self, parent, blocks):
    block = blocks.pop(0)

class MdTocProcessor(markdown.treeprocessors.Treeprocessor):
  hdigitregex = re.compile(r'h(\d)+')
  aidregex = re.compile(r'<a.*?(id=["\'](.*?)["\']).*?>.*?</a>')
  def test(self, parent, block):
      return True
  def run(self, tree): #(self, parent, blocks):
    stack = [tree]
    while stack:
      currElement = stack.pop()
      for child in currElement.getchildren():
        hdigmatch = self.hdigitregex.match(child.tag)
        if hdigmatch:
          hlevel = int(hdigmatch.groups()[0])
          indent = "    "*(hlevel-1)
          aidsplit = self.aidregex.split(child.text, 4)
          aslen = len(aidsplit)
          sectname = aidsplit[aslen-1]
          # out as markdown link in an unordered list
          if aslen > 3:
            idref = aidsplit[2]
            ulstr = "* [{0}](#{1})".format(sectname, idref)
          else:
            ulstr = "* {0}".format(sectname)
          outstr = indent + ulstr
          print(outstr)
    return ""

class QuietPostprocessor(markdown.postprocessors.Postprocessor):
  def run(self, text):
    return ""

# blockprocessors.py (see build_block_parser()):
def build_heading_parser(md_instance, **kwargs):
  """ Build the default block parser used by Markdown - only check for headings; else skip/pass. """
  parser = BlockParser(md_instance)
  parser.blockprocessors['hashheader'] = markdown.blockprocessors.HashHeaderProcessor(parser)
  parser.blockprocessors['setextheader'] = markdown.blockprocessors.SetextHeaderProcessor(parser)
  parser.blockprocessors['skip'] = SkipProcessor(parser)
  return parser

def build_htreeprocessors(md_instance, **kwargs):
  """ Build the default treeprocessors for Markdown - only mdtoc (prints custom output). """
  treeprocessors = odict.OrderedDict()
  treeprocessors["mdtoc"] = MdTocProcessor(md_instance)
  return treeprocessors

def build_qpostprocessors(md_instance, **kwargs):
  """ Build the default postprocessors for Markdown - only suppress default output. """
  postprocessors = odict.OrderedDict()
  postprocessors["quiet"] = QuietPostprocessor(md_instance)
  return postprocessors


class MdTocExtension(markdown.Extension):
  """ Replace Markdown's BlockParser with MdToc specific. """
  def extendMarkdown(self, md, md_globals):
    """ Replace the BlockParser. """
    md.parser = build_heading_parser(md)
    md.treeprocessors = build_htreeprocessors(md)
    md.postprocessors = build_qpostprocessors(md)

def makeExtension(configs={}):
  return MdTocExtension(configs=configs)


# command line test:
"""
import markdown
from markdown.util import etree
from markdown.blockparser import BlockParser
import re

md = markdown.Markdown()
ims = md.convert(""\"
Hello
=====

## <a id="sect one"></a>SECTION ONE ##

something here

### <a id='sect two'>eh</a>SECTION TWO ###

something else

#### SECTION THREE

nothing here

### <a id="four"></a>SECTION FOUR

also...

""\")


#~ def set_link_class(self, element):
  #~ for child in element:
    #~ if child.tag == "a":
      #~ child.set("class", "myclass") #set the class attribute
    #~ set_link_class(child) # run recursively on children


class SkipProcessor(markdown.blockprocessors.BlockProcessor):
  def test(self, parent, block):
    return True #bool(self.RE.match(block))
  def run(self, parent, blocks):
    block = blocks.pop(0)


# blockprocessors.py (see build_block_parser()):
def build_heading_parser(md_instance, **kwargs):
  parser = BlockParser(md_instance)
  parser.blockprocessors['hashheader'] = markdown.blockprocessors.HashHeaderProcessor(parser)
  parser.blockprocessors['setextheader'] = markdown.blockprocessors.SetextHeaderProcessor(parser)
  parser.blockprocessors['skip'] = SkipProcessor(parser)
  return parser

hdigitregex = re.compile(r'h(\d)+')
aidregex = re.compile(r'<a.*?(id=["\'](.*?)["\']).*?>.*?</a>')

#~ # __init__.py
#~ def build_parser(self):
  #~ #""\" Build the parser from the various parts. ""\"
  #~ #self.preprocessors = build_preprocessors(self)
  #~ self.parser = build_block_parser(self)
  #~ #self.inlinePatterns = build_inlinepatterns(self)
  #~ #self.treeprocessors = build_treeprocessors(self)
  #~ #self.postprocessors = build_postprocessors(self)
  #~ return self

# root = self.parser.parseDocument(self.lines).getroot()
#~ md.reset()
hd_parser = build_heading_parser(md)

#root = md.parser.parseDocument(md.lines).getroot()
root = hd_parser.parseDocument(md.lines).getroot()

import inspect

#def run in class InlineProcessor:
stack = [root]
while stack:
  currElement = stack.pop()
  #etree.dump(currElement) # <div><h2>&lt;a id="one"&gt;&lt;/a&gt;ONE</h2><h3>...
  for child in currElement.getchildren():
    #print(child.tag, etree.dump(child), child.attrib, child.text, child.getchildren(), child.find("a"), dir(child))
    hdigmatch = hdigitregex.match(child.tag)
    if hdigmatch:
      hlevel = int(hdigmatch.groups()[0])
      indent = "    "*(hlevel-1)
      #subnode = etree.fromstringlist([child.text]) # xml.etree.ElementTree.ParseError: junk after document element:
      #print(subnode)
      aidsplit = aidregex.split(child.text, 4)
      aslen = len(aidsplit)
      #print(aslen, aidsplit)
      sectname = aidsplit[aslen-1]
      if aslen > 3:
        # out as markdown link in an unordered list
        idref = aidsplit[2]
        ulstr = "* [{0}](#{1})".format(sectname, idref)
      else:
        ulstr = "* {0}".format(sectname)
      outstr = indent + ulstr
      print(outstr)

#~ print(md.lines)
#~ print(root)
#~ print(ims)
# markdown.py -x myextension(SOME_PARAM=2) inputfile.txt > output.txt
# http://pythonhosted.org/Markdown/
# http://pythonhosted.org/Markdown/cli.html
# python -m markdown [options] [args]

#~ $ python3.2 -c 'import markdown; print(markdown.version)' # has __main__ cli
#~ 2.3.1                                                     # __init__ markdownFromFile stdin
#~ $ python2.7 -c 'import markdown; print(markdown.version)' # no __main__ cli
#~ 2.1.0                                                     # __init__ no stdin
# cp /usr/local/lib/python3.2/dist-packages/Markdown-2.3.1-py3.2.egg/markdown/__main__.py ~/.local/lib/python2.7/site-packages/markdown/
# AttributeError: 'NoneType' object has no attribute 'write'
# with that cp, only this works (no stdin piping, and -f must be specified for output as /dev/stdout):
# python2.7 -m markdown -f /dev/stdout inpa.txt
# now can call extension with:
# python2.7 -m markdown -f /dev/stdout -x md_toc inpa.txt
# python3.2 -m markdown -x md_toc inpa.txt
"""