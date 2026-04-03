---
title: "Data Format Guidelines | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/api-web-services/data-format-guidelines"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/api-web-services/data-format-guidelines"
---

# Data Format Guidelines

Information to help understand web service formatting guidelines.

## Date Fields

The Spectrum Data Exchange (SDX) requires all dates in MM/DD/CCYY format.

- MM - a two-digit month where 01 = January and so on

- DD - a two-digit date

- CCYY - a four-digit year

Each date must include either a slash (/) or dash (-) as a separator between the month, day, and year.

- Acceptable date formats: 01/02/2026, 05/22/2026, 05-22-2026, 12/31/2026

- Invalid date formats: 1/2/22, 01-02/2026, 05222026, December 31, 2026

## Numeric Fields

The SDX layouts have specific formats and length requirements for each numeric field which are defined within each layout. Some general guidelines for the numeric fields are as follows:

- The Field Information column defines the specific rules and provides format examples if needed.

- The Field Information column defines whether the numeric field is a positive number only.

- Do not include dollar signs ($) or commas (,) in numeric fields.

- Negative numbers must be defined with the negative sign (-) at the beginning of the number and without a space.

- Acceptable format: -10.2, -6785.52, -15000

- Unacceptable format: 10.2-, 6785.52 -, - 15000

- The Max column defines the total number of characters that can be defined for each field. For numeric fields, the total number includes the negative sign (-) and the decimal place (.) if allowed.

- Example: Max value is 14 with no limitations defined in the Field Information column in the layout.

- Allows -1234567890.12

- Example: Max value is 6 for a positive percentage definition in the layout.

- Allows 123.12

- Example: Max value is 10 for a 'Positive numeric format of XXX.XXXXXX' defined in the layout.

- Allows 123.456789

## Formatting Tips

Below are some tips to assist with the Web service method logic.

- Key fields (for example, Vendor code or Customer code) must not contain these special characters:

- / forward slash

- * asterisk

- ? question mark

- " double quote

- ' single quote

- > greater than

- < less than

- # pound sign

- , comma

- & ampersand

- ~ tilde

- Phone numbers and Social Security numbers are stored in the database without dashes.

- Each element in the Web service method contains a maximum field length (defined in the Max column). Characters in excess are truncated, which may result in bad data transferring into the database.

- Each 'Notes' Web Service only supports printable ASCII characters (32-126). This means that not all the special characters available are supported due to restrictions of specific characters and limited space as these characters may be one space but in the SQL table it uses more than one character to store it. See [www.ascii-code.com](http://www.ascii-code.com/) to see list of characters and their codes.

- The Excel Office Add-in allows the dashes to be entered, with the program removing them prior to updating to Spectrum.

## User-Defined Fields

User-defined fields (UDFs) allow the importing of additional information into the Spectrum system. These fields are controlled based on what the default user-defined field settings on the specific module installation screens are, and how they are set up. If a Web service contains the UDF field names, then the UDF field names must be defined, or mapped, to the Authorization ID in order to import the fields. To map the fields, go to the Data Exchange Installation screen.
Please see the [Data Exchange Authorization Setup Guide](https://trimble.deploy.heretto.com/v4/deployments/mVyHSMAo9PbkfqcxUBWF/object/9bd043d0-8ea8-11ec-9179-02420ae60f1a?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJodHRwczovL2pvcnNlay5jb20vZXpkX29yZ2FuaXphdGlvbiI6InZpZXdwb2ludCIsImh0dHBzOi8vam9yc2VrLmNvbS9lemQvb2JqZWN0X3V1aWQiOiI5YmQwNDNkMC04ZWE4LTExZWMtOTE3OS0wMjQyMGFlNjBmMWEiLCJleHAiOjE3NzUzMjc3MjksImp0aSI6ImY5ZDU2ZTRlOTMzNDQ3YzZiMTZjMDA0YTBlMGJjNWQ5IiwiaHR0cHM6Ly9qb3JzZWsuY29tL2V6ZF9maWxlc2V0IjoiOE1GRmpJZEw3ZEZLQmJiVGwxTXMifQ.tJbopl1SQ8i-wGB8uJLijKv4fSc0Bohn2n4hfHI70zI&response-content-disposition=filename%3D%22SDX-AUTHORIZATION-SETUP-2021R2.pdf%22) for details on how to map the Web services user-defined field options.

## Layout Definitions

Each Web service created in the Spectrum Data Exchange module has a specific pre-defined layout with rules and definitions for each field. Each Web service has some underlying file maintenance areas that need to be completed prior to using the Data Exchange along with specific assumptions and dependencies for the Web service. The file format provides the following details.
ExcelDefines the Excel column that ties to the Spectrum Office Add-in template.Field NameThe Field name defines the field assignment in Spectrum for the value being sent.DescriptionProvides a description for the element name and relates to the name shown on the Spectrum entry screen.ReqDefines if data must be provided for the element, or if the field can be left blank or contain spaces.TypeDefines the data type required for the field such as text, numeric, or date.Max

- Defines the total number of characters allowed for the field name.

- The total amount of characters includes any characters required by the numeric or date field.

- Example: Date field = 10 characters, including slashes.

- 10/12/2026

- Example: Numeric field = 8 characters, including the negative sign and decimal.

- -1525.66

Format

- Provides rules for the specific field such as:

- Format rules

- Character options allowed

- Rules if field is left blank

- Specific rules that may apply

Validation

- Defines the tables that the field will be validating against.

- Provides any specific logic used for the field.
