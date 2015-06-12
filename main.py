import lxml.etree as ET
import sys

if len(sys.argv) < 2:
    sys.exit("No filename specified.")

xsl = '''<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:output indent="yes" />
<xsl:strip-space select="*" />
  
<xsl:key name="respuestas" match="orderedlist" use="generate-id(preceding-sibling::para[1])"  />

<xsl:template match="/">
	<quiz>
      <xsl:apply-templates select="article/para" />
	</quiz>
</xsl:template>
  
<!--<question type="multichoice|truefalse|shortanswer|matching|cloze|essay|numerical|description">-->

<xsl:template match="article/para">
    <question type="multichoice">
        <!--<xsl:attribute name="type">
            </xsl:attribute>
        -->
      <xsl:variable name="alternativas" select="key('respuestas', generate-id(current()))" />
         <name>
             <text> <xsl:value-of select="concat('Pregunta ', count(preceding-sibling::para) + 1)"/></text>
         </name>
         <questiontext format="plain_text">
             <text><xsl:value-of select="." /></text>
         </questiontext>

         <xsl:apply-templates select="key('respuestas', generate-id(current()))" />

         <single>
           <xsl:choose>
             <xsl:when test="count($alternativas/listitem/para/emphasis[1]) > 1">
                 <xsl:text>true</xsl:text>
             </xsl:when>
             <xsl:otherwise>
                 <xsl:text>false</xsl:text>
             </xsl:otherwise>
           </xsl:choose>
         </single> <!-- multiple choice or single answer -->
      
        <shuffleanswers>1</shuffleanswers>
        <answernumbering>abc</answernumbering>
    </question>

</xsl:template>

<xsl:template match="orderedlist" name="answers">
     
         <xsl:apply-templates select="listitem" />
     
</xsl:template>

<xsl:template match="listitem" >
  <answer>
         <xsl:attribute name="fraction">
             <xsl:choose>
                 <xsl:when test="para/emphasis">
                     <xsl:text>100</xsl:text>
                </xsl:when>
             <xsl:otherwise>
                     <xsl:text>0</xsl:text>
             </xsl:otherwise>
           </xsl:choose>
         </xsl:attribute>
         <text><xsl:value-of select="para" /></text>
  </answer>
</xsl:template>

</xsl:stylesheet>
''' 

quiz_filename = sys.argv[1]
quiz = ET.parse(quiz_filename)

xslt = ET.fromstring(xsl)
transform = ET.XSLT(xslt)

newdom = transform(quiz)
moodle_xml = ET.tostring(newdom, pretty_print=True)

file_ = open('output.xml', 'w')
file_.write(moodle_xml)
file_.close()

