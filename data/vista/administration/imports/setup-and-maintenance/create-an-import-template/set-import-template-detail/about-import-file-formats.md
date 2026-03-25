---
title: "About Import File Formats | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats"
---

# About Import File Formats

Import templates require a file format to identify how the data is formatted in the import file.
When you set up an import template in IM Template, there are three file formats available: Delimited, Fixed Width, and XML. When importing data into Vista, you must create a data file from your third-party system using one of these formats.
The functionality of IM Template changes depending on what file format you decide to use. This article discusses each format in depth and provides instructions on how to configure a template with each format and examples of related import data files.
Note:Supported Use of Quotation Marks in Import Files:Regardless of the file format you use, Vista supports the use of single quotes ( ' ), double quotes ( " ), and grave accents ( ` ) in import files.

## Delimited File Format

Delimited files use a delimiter, such as a comma, tab, or pipe, to separate the fields in the data file. When the system is processing the import, it begins the next field each time it encounters the specified delimiter. Each line in the data file that starts with a value is a new record entry in the system.
ExampleIf you are importing a data file with six columns, it might look like the example below. Each new line in the data file is a row, or new record entry in the system. You would then assign each column to a field in the import template in [Details](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail) tab of IM Template.
The example below shows data that would be imported into PR Employees. In the first line, column 1 would be imported into the Employee Number field with a value of 100001, column 2 would be imported into the Last Name field with a value of FakeLastName, etc.).

AttachmentsIf you are importing attachments with your data records, you must use a comma delimited file format.
There are two kinds of lines in a data file that includes attachments: data to be imported, and the documents that are attached to those data records during the import process into PR Employees.

- Data record lines: Each new data record line is a row, or new record, in the system. You will assign each column to a field in the import template using the Template Details tab in IM Template. One of the columns must apply to the Record Key column in the Details tab; in the example below, this is column 1. In the first line of the example below, column 1 would be imported into the Record Key field with a value of 1 , column 2 would be imported into the Employee Number field with a value of 100001, column 3 would be imported into the Last Name field with a value of FakeLastName, etc.

- Attached document lines: To include an attached document, the lines that indicate the document files must begin in column 1 with #ATTACHMENT (case insensitive). Column 2 must contain the same value as the value in the associated data record's Record Key column, which indicates the record to which the attachment belongs. Column 3 contains the document's relative file path (relative to the location of the data file). Column 4 can optionally include the document's attachment type; if no attachment type is specified, the form's default attachment type will be applied.The following is a sample comma delimited data file for use in including documents with a data import:

For certain header/detail forms (such as AP Transaction Entry and AP Unapproved Invoice Entry), Vista supports line level attachments. If you are importing data for these forms, the invoice line attachment records in your import file must include the Record Type and invoice line number for line level attachments.
Here is a sample import file for AP invoices containing both header and line attachments. The first attachment line is a header attachment, so it does not include the record type. However, the next two attachment lines are line level attachments, indicated by the inclusion of the record type and invoice line number (highlighted text).

## Fixed Width File Format

Fixed width data files base field positions on the specified length of each field. When using this format, you specify the beginning and ending position of a field so that the system knows where one field ends and the next one begins (making sure to base the ending position on the total allowable length of field).
For example, if column 1 is job number, and the total number of allowable characters in the field is 10, specify 1 as the beginning position and 10 as the ending position. The system then starts column 2 on the 11th position. If the second field is 13 characters, the system will begin column 3 on the 24th position, and so on.

## XML File Format

Use the XML format when importing data from XML files (.xml).
Note: XML format is available for single table forms only.
The system uses a raw XML format, meaning it does not use a style sheet or any formatting information. However, like all XML files, it uses tags to identify and separate data within the data file. The structure is hierarchical, meaning there are tags within tags within tags (parent tags, child tags, child tags within child tags, etc.). Each record within this hierarchy must start with the same tag, contain all possible tags, and all tags within the record must be unique.
As shown in the following example, the data file contains two different addresses for each record, each using unique tags. In this case, the shipping address is identified by the <SAddr>, <SCity>, <SState>, and <SZip> tags, and the billing address by the <BAddr>, <BCity>, <BState>, and <BZip> tags.
Each tag in the file has both a start tag and end tag (<Record>, </Record>; <Customer>, </Customer>; <Name>, </Name>; and so on). Data (indicated in blue) will always be contained between a start and end tag. This allows the import process to identify the beginning and ending of each field within the record, much the same as the use of delimiters (delimited files) and beginning/ending positions (fixed width files).

Once you import XML data into IM Work Edit, the system treats it like any other import.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [Set Import Template Detail](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

- [About the IM Work Edit Form](/en/vista/vista/administration/imports/processing/about-the-im-work-edit-form)
