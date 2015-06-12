
A simple script that transforms a DocBook file generated with Libre/OpenOffice into a Moodle XML quiz format. 

The source code should be like this:


    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE article PUBLIC "-//OASIS//DTD DocBook XML V4.1.2//EN" "http://www.oasis-open.org/docbook/xml/4.1.2/docbookx.dtd">
    <article lang="">
      <para>I'm a question.</para>
      <orderedlist>
        <listitem>
            <para><emphasis>I'm the correct answer.</emphasis></para>
        </listitem>
        <listitem>
          <para>I'm not correct.</para>
        </listitem>
        <listitem>
          <para>Neither am I.<para>
        </listitem>
      </orderedlist>
    </article>

A sample file is included for reference. In Libre/OpenOffice, you can use the styles panel (press F5) to select the emphasis style, which signals the correct answer.

## Usage

    python main.py docbookfile.xml

This generates an `output.xml` file in Moodle XML format.

## To-do

1. Add support for more question formats.
