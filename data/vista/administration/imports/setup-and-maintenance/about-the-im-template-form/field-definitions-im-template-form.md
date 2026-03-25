---
title: "Field Definitions: IM Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form/field-definitions-im-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form/field-definitions-im-template-form"
---

# Field Definitions: IM Template Form

The following is a list of field descriptions for the IM
 Template form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Enter a name or number that uniquely identifies this template, up to 10 characters. This field defaults to the last active template.

##  Description

 Enter a description for this template, up to 30 characters. This field is used for identification purposes only.

##  Import Form

 Enter the import form to use for this template. The import form identifies the import destination tables. Press F4 for a list of valid pre-defined import forms.

## Import Routine

This field defaults the import routine for the
 form specified in the Import Form field. This routine pulls the
 import data into the Vista™ database tables. There are two routines available:

- bspIMImportIMWE – This is the standard import routine and it is used for imports using delimited or fixed width file formats.

- bspIMImportXML – This routine is used only for importing XML formatted data. XML data uses tags (e.g. <Co>, <Material>, etc.) instead of delimiters and fixed widths to identify records and fields within the records.

For more information, see [Setting Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats).

##  Upload Routine

 This field defaults the upload routine
 specified for the form in the Import Form field. This routine sends the
 imported data to the specified destination table(s), and identifies where the data goes,
 what fields are required, and whether the data is text, a date, or numeric. There are
 currently three upload routines available:

- bspIMUpload – Use this routine for single table imports.

- bspIMUploadHeaderDetail – Use this routine for multiple table import, that is, header/detail imports (e.g. AP Invoice, AR Invoice, Purchase Orders, etc.)

- bspIMUploadDirect – Use this routine for direct
 imports, that is, imports that do not update to a batch, but will insert and/or
 update the actual data tables. For example, the AP Vendors Import directly updates
 APVM, the AR Customers Import directly updates ARCM, and the GL Monthly Budget import
 directly updates GLBD.

 For more information, see [Import Types](/en/vista/vista/administration/imports/setup-and-maintenance/import-types).

##  Direct Import Type

 The system enables this field for direct imports (i.e., when you specify the bspIMUploadDirect routine in the Upload Routine field).
 Select one of the following options:

- 0-Insert and Update – Use this option to insert new records and update existing records. The upload adds all new records to the table and updates existing records based on the Update Column field on the Template Detail tab.

- 1-Insert Only – Use this option to insert new records only. The upload adds new records only; updates to existing records do not occur.

- 2-Update Only – Use this option to update existing records only. The upload updates existing records only (based on the Update Column field on the Template Detail tab); the upload will not add any new records.

Important: You cannot use the update options to attach new documents to existing records. You can import attached documents only when importing their related new records.
Note: If you are importing/uploading vendor data, and you elect to update existing records (options 0 and 2), the upload will not prompt to “update firms” for any vendors existing in [PM Firms](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firms-form). You must manually update the firms.

##  Viewpoint Routine

 This field defaults the routine specified by Viewpoint Construction Software for the import form. This routine applies default values to specific fields. Default values are generally used when the import data file does not contain specific inputs required by the system’s data file. For example, when importing timecard data, and the data file does not contain payroll groups, the Viewpoint Routine automatically assigns the employee to the appropriate PR group. You must check the [Use Viewpoint Default](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form/field-definitions-im-template-form#ID-00013001--en) box on the Template Detail tab for each specific field to enable the Viewpoint Routine.

## User Routine

This field is optional.
Enter the name of the user-defined routine to use for this template. User-defined routines are used to perform additional functions that do not exist in the import, upload, or Viewpoint default routines. For example, if records in the data file should be exempt from defined defaults or cross-references, set up a routine to locate these records and change the defaulted value. Viewpoint provides a sample stored procedure (bsplIMUserRoutineSample) in the Vista™ database that can be used as a starting point for creating custom routines. The system executes user routines at the end of the import process.

## Choose the Format That Best Describes Your Data

 Specify the format of the file you are importing.

- Delimited
 – Select this option if the data file uses characters (delimiters) such as commas or tabs to separate each field.When the import process is reading the text file, it begins the next field each time a specified delimiter is encountered. There are several pre-defined delimiters to choose from (tab, semicolon, comma, space, and pipe), but other delimiters can be used. If your import includes documents to be attached to data records in the same import, you must use the delimited format.

- Fixed Width
 – Select this option if the data file uses a fixed width format, where field positions are based on the specified length of each field. For example, if the first field is job number, and the total number of allowable characters is 10, specify “1” as the beginning position and “10” as the ending position. The system then starts the second field on the 11th position. If the second field is phase code (13 characters), the system will begin the third field on the 24th position, and so on.

- XML
 – Enabled only for single table uploads (i.e. imports with the Multiple Table Upload option unchecked, such as Bank Boston, CM Outstanding Entries, Gasboy, etc.). Select this option if the data file is in an XML (.xml) format; that is, it uses 'tags' (e.g. <Customer>, <Name>, etc.) to identify and separate data with the text file. When this option is selected, the XML Row Tag field (to the right) is enabled, which is used to specify the tag that identifies each row in the text file.

Note: If you do not know the format of the data file, this information should be available from the software developer of the third-party program(s) that you are using. If you are importing data from a spreadsheet, the file type you select when saving the spreadsheet determines the format specified here. For example, files saved as a CSV (*.csv) would use a delimited format. Files saved as Formatted Text (*.prn) would use a fixed width format.

## XML Row Tag

The system enables this field for single table upload templates with an XML file format.
Enter the XML tag (without the '<>' brackets) that determines each row (record) in the data file. For example, if you use a <Record> tag to identify a new row, enter 'Record' in this field. You must use the specified tag at the beginning of each record in the text file. For example:
<Record>
 <Customer></Customer>
 <Name></Name>
 <Address></Address>
</Record>
<Record>
 <Customer></Customer>
 <Name></Name>
 <Address></Address>
</Record>
Note: For every row tag (e.g., <Record>), there must also be an 'end row' tag (e.g., </Record>) to indicate the end of the record in the XML file.

## Choose the Delimiter That Separates Your Data

The system enables this group box when you select the Delimited file format for the template.
Select the appropriate delimiter.

- Tab

- Semicolon

- Comma

- Space

- Pipe

- Other (When selecting this option, enter the delimiter in the text field to the right.)

## Other

The system enables this field when you select
 the Other radio button from the Choose the delimiter that separates your data
 group box.
Enter the delimiter that the data file uses to separate data. For example, colon (:), back slash (\), or asterisk (*).
Note: It is important that you select a delimiter that does not appear in any fields within your data file, as this will cause your data to import and upload incorrectly. For example, if you typically use commas in descriptions or names, you might use a pipe ( | ) symbol as your delimiter. Additionally, you will need to make sure that your source program creates the text file using the same delimiter.

##  Multiple Table Upload

 Check this box if the imported data file will update more than one table. If you check this box, you must [set up additional record types](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-record-types-for-import-templates) for the template on the Record Types tab.
Note: This field is disabled when the XML format has been selected.

## Record Type Column

The system enables this field when you select
 the Multiple Table
 Upload checkbox for a template using a Delimited file format.
Enter the column number (up to 10 digits) that identifies the record type within the data file. In most cases, this will be the first column (position) in the data file.
Figure A shows an example of a data file with the record type in the first column. In this case, you would enter 1 in the Record Type Column field.
Figure A:
Header, 1, 10, 1500, 177834 Item, 1, 1-Job, 2, 10006-210

## Beginning/Ending Position

The system enables these fields when you select the
 Multiple
 Table Upload checkbox for a template using a Fixed Width file
 format.
Specify the beginning and ending positions within the import file that identifies the record type. For example, if the file type is 6 characters, and begins at the first position, the positions would be 1 and 6. Because the number of characters determines where a field begins and ends, use the number of characters permitted by the longest record type.
For example, if the record types are “Header” and “Item,” the system will base the beginning and ending positions on a total of six characters (the number of characters in the word “header”).

## Starting Line Number

The Starting Line Number field on the IM Template form, Info tab.
Enter the starting line number for imports using this template (must be greater than 0).
 For example, you might use this feature if you want the import to skip header rows or bad
 data in the import file.
If you are using the Auto Imports feature, the auto import process uses the value specified
 here to determine the starting line number for the import. If this field is blank, the
 import starts at Line 1.
If you manually import data (via IM Import), this number defaults in the
 Starting Line Number field in IM Imports. You may override the
 defaulted value in IM Import as needed.

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [About the IM Import Form](/en/vista/vista/administration/imports/processing/about-the-im-import-form)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

## Remove Quotes

The Remove Quotes checkbox on the IM Template form, Info tab.
Select this check box to automatically remove all surrounding double quotation marks contained in import files that are imported using this template. After your data is imported, you will see in IM Work Edit that the double quotation marks have been removed. Apostrophes are not affected.
For example, say the import file contains data for the Co, Job, and Description fields as follows:
 Co=1, Job=" 1001-", Description="SWF Flooring "Bldg G", Hamilton Office"
During the import, your data is inserted as:
Co=1, Job= 1001-, Description=SWF Flooring "Bldg G", Hamilton Office

Related information

- [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems)

- [About the IM Import Form](/en/vista/vista/administration/imports/processing/about-the-im-import-form)

- [About the IM Template Form](/en/vista/vista/administration/imports/setup-and-maintenance/about-the-im-template-form)

## Enabled

Enabled checkbox on the IM Template form
Note: This field only applies if you use Kofax, a third-party document management
 solution.
If you're using Kofax, select this checkbox if you
 want to include inline attachment information with your imports and auto
 imports.
Inline attachments are only allowed for delimited file types.
If you select this checkbox:

- you must also specify the column numbers for your
 import file's attachment file name and attachment type. Use
 Identifiers 960 and 965 on the Template Detail tab.Note: While column numbers are required in the
 Template Detail tab, the import process still allows null values
 in those columns.

- the import process does not recognize separate
 attachment lines, if any, and these are treated as errors.

For additional information, see [Importing Data from Third-Party Systems](/en/vista/vista/administration/imports/processing/importing-data-from-third-party-systems).

## RecordType

Record Type column in the IM Template form, Record Types tab.
Enter the record type, up to 10 characters. The record type identifies the different types of record in the import text file (e.g. Header, Item, Notes, etc.).
Important: Upon import, the system treats the record type that is alphabetically first as the header. If you name your header items "Header" and your line items "Lines," you will not have a problem; however, if your line items were named "Detail," your import will assume the "Detail" records are the header records because D precedes H.

## Form

Enter the import form for this record type. Press F4 for a list of forms.
The import form identifies the destination table for the import data. For example, if this is a 'header' record type for an AP invoice template, you will assign "APEntry" as the import form.

## TableName

This field is display only and defaults the table name associated with the form specified in the Form field.

##  Description

 Enter a description for this record type, up to 30 characters. Typically, you will want to use a description that identifies the type of imported information. For example, if you are importing a 'header' record type for AP invoices, the description might be 'AP Invoice Header'. If you are importing a 'line' record type for AP invoices, the description might be 'AP Invoice Line'.

## Skip

Check this box if you want the system to skip records for this record type when importing data from the data file. When you check this box:

- If the record type exists in the data file, the system skips associated records during the import.

- If the record type does not exist in the data file, the system ignores any missing records.

Note: If you do not check the Skip box for a
 record type, and the import file is missing that record type, you will receive an error
 indicating that the record type is missing. To successfully import the file, you will need
 to check the Skip option for that record type, and re-import the file. You can uncheck
 the box once you have finished importing the file.

## Record Type

Record Type column in the IM Template form, Template Detail tab.
 You cannot change the values in this column.
The system displays this column if there is more than one table listed on the Record Types tab. This column specifies the record type, which in turn identifies the table being updated.

##  Identifier

 This field displays an identifier that represents each column in the table. When adding a column to the grid (typically used for custom fields), enter an identifier greater than 999.

##  Column Name

 This field displays the name of the column in the import table (specified by record type).

##  Description

 This field defaults to the description defined by Viewpoint Construction Software for the Column Name. You may override this field, as necessary, up to 30 characters.

##  User Default Value

Use this field to assign default values for the specified column in this record, up to
 128 characters. Use this field to insert specific data that is not contained in the import
 data file or to replace values already existing in the data file.
If you are using this default value to replace
 values in the data file, select the Override Import Value checkbox. If you do not check the
 Override Import Value box, the system only replaces blank columns in the data file.
Note: Some fields automatically use the Viewpoint default value. This occurs in situations where field data is
 specific to Vista and does not exist in the import data file (e.g.
 Phase Group, PRGroup, InsCode, etc.).

##  Overwrite Import Value

 This checkbox works in conjunction with either the Use Viewpoint Default or User Default Value fields.

-  If you check this box, and enter a value in the User Default Value, the system will override the value in the data file with the entry in the User Default Value.

-  If you check this box, and check the Use Viewpoint Default box, the system will override the value in the data file with the Viewpoint default for the importing field.

- If you check this box, and enter a value in the User Default Value and check the Use Viewpoint Default box, the system will use the Viewpoint default for the importing field.

-  If you do not check this box, and enter a value in the User Default Value field or check the Use Viewpoint Default box, the system will use the override values (User Default or Viewpoint Default) only if the value in the data file is blank.

##  Use Viewpoint Default

 Check this box to use the Viewpoint default for this field when the value in the data file is blank. When you check the Overwrite Import Value box, and check this box, the system will override the value for this field regardless of the value in the data file.
 There are some special considerations when using this option. The following sections detail these considerations.

### AR Invoices

 When applying the Viewpoint default for the JCCo column, and an invoice is not contract related (i.e. the Contract field is blank), the system will set the JCCo value to blank during the import process.

###  MS Tickets

 If this template is for a MS Ticket Batch import (e.g. Alkon, AMI, Libra, Seltec, etc.), the quotes are flagged to Use Metric UM, and you are applying the Viewpoint default, the system converts the imported UM, Unit Price, and Units values to metric. If you do not want this conversion to occur, do not apply the Viewpoint default or uncheck the Use Metric UM option for all applicable quotes.
 If you are applying the Viewpoint default for the Haul Code column, the system pulls the haul code from the quote only if the Hauler Type is 'H' (Haul Vendor) and it is not a Cash or Credit Card sale. If a haul code is not specified on the quote, the import uses the haul code specified in HQ Materials (if applicable) or will default as blank.
If you are applying the Viewpoint default for the Hours column, the system will only calculate hours if values exist in both the StartTime and StopTime columns. If one or both columns are blank, the Hours column will default as blank.
If importing cash sale tickets, and you are applying the Viewpoint default for Unit Price or Material Total, the override is ignored. The system assumes that since you have paid for the material, that the actual unit price and material total should be included on the ticket and invoice.

###  PR Timecards

 If this template is for a PR Timecards import, and you are applying the Viewpoint default for the DayNum column, the data file must provide the payroll ending date and posting date. The system calculates the value for the Day Number column during the import.
 If you are applying the Viewpoint default for the PostDate column, the data file must provide the payroll ending date and day number. The system calculates the Posting Date during the import.
Note: Because the day number depends on the post date and the post date depends on the day number, this option you should apply the Viewpoint default to one of these columns. Applying the default for both the DayNum and PostDate columns will cause an error during the import.

## Cross Reference

Specify the cross-reference name, up to 30 characters, for this record. Cross-reference names are defined in IM Cross Reference Header by template and record type, and are used to locate the appropriate cross-reference values for imported data.
When the IM Import form is run, the Cross Reference name is used to locate the cross-reference values for the imported data.
For example, to cross-reference job codes in your text file with Vista™ job codes, you might set them up as follows:

### IM Cross Reference (Info tab)

Template:
100

Record Type:
JCCB

XRefName:
JOB

Target Identifier:
55 (Job)

### IM Cross-Reference (Cross Reference Values tab)

Cross Ref
Import Value
Viewpoint Value

JOB
1100100000
11001- -

1100120000
11001-200-

1100120001
11001-200-001

### IM Template (Template Detail tab)

Identifier
Column Name
X-Reference Name

55
Job
JOB

When IM Import is run and the JOB cross-reference name is encountered, the system will search the cross-reference table, locate the cross-reference name for the associated template and record type, and cross-reference the import values with the Viewpoint values as specified.

## Record Column

The system enables this column for Delimited file formats only.
Enter the column within the import data file where this field is located. For example, using the sample below, for the Phase column, you would enter 2 in this column.
Text File Record:1000,03110,1

Col 1
Col 2
Col 3

Job
Phase
CT

For more information on file formats, see [Setting Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats).

## Beginning/Ending Position

The system enables this column for Fixed Width file formats only.
Enter the beginning and ending position within the data file, where this field is located. Base the ending position on the total allowable length for the field. For example, if the Job number allows up to 6 characters, and the beginning position is 1, the ending position must be 6.
For more information on file formats, see [Setting Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats).

## XML Tag

The system enables this column for XML file formats only.
Enter the XML tag that identifies this field. The system imports data in the import file with this tag to this column in the work edit file, and updates it to this column in the destination table.
For example, if the destination table has a 'Vendor Number' column, and the import data file has a <Vendor> tag, enter Vendor here, making sure to exclude the brackets (<>). If you enter brackets, the system will remove them when you move focus to another column.
For more information on file formats, see [Setting Import File Formats](/en/vista/vista/administration/imports/setup-and-maintenance/create-an-import-template/set-import-template-detail/about-import-file-formats).

## Format Info

Use this column to reformat specific input fields in the file. There are four different categories of format methods available for reformatting fields, which are detailed below.
Character Stripping
These methods allow you to strip characters that are not used in the Vista™ data file.

- STRIP - This method will remove all leading and trailing spaces.

- STRIPL0- This method will remove any leading 0 (zero) or other specified character.

- STRIPT0- This method will remove any trailing 0 (zero) or other specified character.

- STRIPB0- This method will remove any leading and trailing 0 (zero) or other specified character.

- STRIPA0- This method will remove any occurrence of 0 (zero) or other specified character.

To specify a character other than zero for the options specified above, change the 0 to the desired character.
Date Format
Date format methods are somewhat different than other methods in that they are used to identify the Month (MM), Date (DD), and Year (YY) placement in the text file, not how the output will be formatted. The following is a list of date formats.
These formats will be converted to your standard date format (e.g., MM/DD/YY, YY/MM/DD, etc.), depending on the how the data is formatted in the software table.

- M/D/YY

- M/D/YYYY

- MM/DD/YY

- MM/DD/YYYY

- MM/DD/YY 00:00

- MM/DD/YYYY 00:00

- MMDDYY

- MMDDYYYY

- YYMM

- YYMMDD

- YYYYMMDD

These formats will be converted to your standard date format (e.g., MM/01/YY, YY/MM/01), depending on the how the data is formatted in the software table.

- MM/01/YY

- MM/01/YYYY

- MM01YY

- MM01YYYY

- YYMM01

- YYYYMM01

- MM01YY 00:00

- MM01YYYY 00:00

Length Format
Defines which characters of a field are used.

- LEN2, 12 - This method will pull in 12 characters, starting at the 2nd character in the text field. To change the parameters, change the 2 to the desired beginning character and the 12 to the desired ending character. For example: LEN4, 10 (pull in 10 characters starting at the 4th character in the text field).

- STRIPA- & LEN2, 12 - This method allows you to strip all minus signs (-) from the text, then use the 12 characters starting at the second position in the text field. Positions can be changed as indicated for previous method.

Print Mask
Used for numeric inputs only, to indicate decimal and digit positions.

- #.##

- #.###

These are standard default masks, but they can be changed by selecting the method, then making changes to the mask in this field.
Note: You can combine format methods where multiple functions are required. For example, if you have a text file in which your date fields are surrounded by quotes (e.g. "01/15/11"), but you want to remove the quotes and still be able to identify the data file date formats, combine Character Stripping and Date Format options as follows:
STRIPL" & STRIPT" & MM/DD/YY
This combination tells the import process to remove all leading and trailing quotes, and also identifies that the text file date is in MM/DD/YY format. When combining formats, separate each one with spaces and ampersands (&), as shown above.

##  Update Column

 This field is available only for direct imports (e.g. APVendor, ARCustomer, HQTrade, etc.).
 Check this box if this field/column will be updated (in the destination table) when uploading import data. Typically, this box is selected for fields that are normally updated (e.g. description, address, unit price, unit of measure, etc.). If you are using the 'Insert and Update' or 'Update Only' direct import options and the text file record is determined to already exist in the destination table (based on the Update Key identifiers), changes to this field will be updated for the existing record.
Note: If you have checked the Use Viewpoint Default Value and Overwrite Import Value boxes, the system will always use the Viewpoint value, regardless of whether you check this box and a value exists in the import file.
 Do not check this box if this field/column will not be updated when uploading import data, regardless of whether using the 'Insert and Update' or 'Update Only' direct import options.

##  Update Key

 This field is available only for direct imports (e.g. APVendor, ARCustomer, HQTrade, etc.) and is display only.
 When this box is checked, this field is used as a key for determining whether imported records already exist in the destination table. For example, if importing vendor data, the VendorGroup and Vendor identifiers are flagged as Update Key fields. When importing data, if you are using the 'Insert and Update' or 'Update Only' direct import options, and the VendorGroup and Vendor in the text file record matches a VendorGroup and Vendor record in the destination table (APVM), that record will be updated (based on Update Fields selections). If using the 'Insert Only' option, and the vendor already exists, the import record will not be inserted.

##  Prompt on Import

 Check this box to prompt the user for a value during the import process. This is useful when you want to specify a user default, but the default changes with each import (e.g. Company, CM Account, PR Group, Vendor Group, etc.). Having the import prompt for a value eliminates having to set up multiple templates with differing values in the User Default Value field, having to change the value manually in the template detail before you import the data file, or having to edit the value in IM Work Edit.
 When the import process comes across a record with this box checked, the IM User Input Detail form displays. Use IM User Input Detail to change the default value. For more information, see [IM User Input Detail](/en/vista/vista/administration/imports/processing/about-the-im-user-input-detail-form).

## Nullable

Nullable column in the IM Template form, Template Detail tab.
The Nullable column cells are read only and indicate whether the column of your source file can be left blank or not. When the checkbox is selected, the import value can be blank and the file will still pass the validation phase. If not checked, the system requires a value (which could include a zero, for example).

## Seq

Enter N, New, or + to start a new notification record.

## Type

Select the type of notification: E-Email or
 V-Viewpoint User.
Note: When you select V-Viewpoint User, the system uses the
 notification preferences set up for the user (specified in the Destination
 Name field) in [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form).

## Destination Name

If you selected
 E-Email
 from the
 Type
 drop-down, enter the email address for sending notifications. If you selected
 V-Viewpoint User
 from the
 Type
 drop-down, enter the user's login name; press F4 for a list of logins.
Note: When you specify a user's login name, the system uses the notification preferences set up for the user in [VA User Profile](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form).

## Notify On Success

Check this box to have the system notify the user when imports for the template are successful.

## Notify On Failure

Check this box to have the system notify the user when imports for the template fail.
Note: When you are performing manual imports, the system will not send a notification upon failure, as the IM Import form automatically notifies you of an error. When you have automated imports, the system will send notification upon failure.

## Attach Log File

Check this box if you want the system to include a detailed log file with the notification message.

## Export\Import Template Directory

The Export\Import Template Directory field on the IM Templates form, Import/Export tab.
Enter the directory to use for exporting and importing templates. This will typically be a network share directory to
 enable others to export and import files using the same location.
Note: The system saves the specified
template directory and defaults it for all templates.
