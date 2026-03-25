---
title: "Field Definitions: PM Import Estimates Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-template-form/field-definitions-pm-import-estimates-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-template-form/field-definitions-pm-import-estimates-template-form"
---

# Field Definitions: PM Import Estimates Template Form

The following is a list of field descriptions for the PM
 Import Estimates form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Template

 Enter a name or number that uniquely identifies this template. Up to 10 characters allowed.

##  Description

 Enter a description for this template, up to 30 characters.

## Import Routine

Specify one of the following standard import routines to use with this template:

- Bid2Win (Bid2Win Estimating)

- Estimating (Viewpoint Estimating)

- Generic (User Defined File Layout)

- HCSSHeavy (HCSS Heavy Bid)

- HardDollar (HardDollar Estimating)

- MEP Estimating (Viewpoint MEP Estimating) 

- Timberline (Timberline Precision Estimating)

## User Routine

Optional.
Specify the user-defined routine to use for this template. User-defined routines are used to perform additional functions not existing in the Import Routine. The routine specified here will be executed at the end of the import process.
The following stored procedure parameters must be passed to the user procedure, making sure the datatype and parameter name match.
(@pmco tinyint, @importid varchar(10), @errmsg varchar(500) output)

## Is This An Override Template?

Check this box to link this template to a standard template. You will only need to use this option if you need to establish override templates for specific area of work that differ from those covered by the standard template.
Uncheck this box if this template is not an override to a standard template.

## Std Template

This field is enabled only if you checked the
 Is this an
 Override Template box.
Specify the standard template to which this template is linked.

## Choose the Format That Best Describes Your Data

Enabled only for templates using the Generic import routine. For all other routines, the format is predefined and cannot be changed.
Specify the format of the file you are importing.

- Delimited – Select this option if your import file is delimited. Delimited files use characters (delimiters) such as a comma or tab to separate each field. When the system is reading the data file, it knows to begin the next field each time it encounters the specified delimiter. 

- Fixed Width –Select this option is your import file is fixed width. Fixed width files base field positions on the specified length of each field. For example, if the first field is Job number and it is 10 characters, the system will know to begin the second field at position 11. If the second field is Phase (13 characters), the system will know to start the third field at position 24, and so on.

- XML –Currently not available.

Note:If you do not know the format of your data files, you should be able to get this information from the software developer of the third-party program(s) you are using. If you are importing data from a spreadsheet, the file type you select when saving the spreadsheet will determine the format you specify here. For example, files saved as a CVS (*.cvs) use a delimited format. Files saved as Formatted Text (*.prn) would use a fixed width format.

## Choose the Delimiter That Separates Your Data

Enabled only for templates using the Generic import routine. For all other routines, the format is predefined and cannot be changed.
Specify the delimiter that is used to separate your data.

- Tab

- Semicolon

- Comma

- Space

- Pipe

- Other (If you select this option, use the field to the right to specify the delimiter to use.)

## Other

Enabled only for templates using the Generic import routine and a delimited data format, where Other is selected as the delimiter.
Specify the ‘non-standard’ delimiter that is used to separate your data (e.g. colon (:), back slash (\), or asterisk (*)).
Note:If you use a standard delimiter (tab, semicolon, comma, space, or pipe), do not use this field to specify your delimiter. Instead, use the radio buttons to the left of this field to select the appropriate delimiter.

## Record Type Column

Enabled only for templates using the Generic import routine and a Delimited data format.
Specify the column (up to 10 digits) within the import file that identifies the record type (e.g. item, phase, cost type, etc.).

##  Beginning/Ending Position

 Enabled only for templates using the ‘Generic’ import routine where the data format is ‘Fixed Width’.
 Specify the beginning and ending position within the import file that identifies the record type. For example, if the record type is 6 characters and begins at the first position, the positions would be 1 and 6.

## Create Items As

Use to create a ‘schedule of values’ for imports where no item records are available (e.g. Timberline and Generic imports). The schedule of values identifies how items will be created when importing data.

- One Item Only – Select this option to create a single contract item (specified in the Contract Item field below), and assign all phases to that contract item.

- Use Import Phase – Select this option to create items based on the phase data being imported. You specify the beginning and ending character to use and the contract item number is generated from the phase code based on those specifications.

- Use Viewpoint Phase – Select this option to create contract items based on the cross-referenced Viewpoint phase. You specify the beginning and ending character to use and the contract item number is generated from the phase code based on those specifications.

- None – Select this option if your export files already contain contract items and therefore do not require any of the above options to create them.

## Contract Item

This field is enabled only if you selected the One Item Only option above.
Enter the contract item to which all phases will be assigned.
Note:Data previously entered and saved in this field will be cleared if you change the "...create items as defined below" option to Use Import Phase, Use Viewpoint Phase, or None.

## Item Description

Enabled only if you selected the One Item Only 'create items as' option above.
Enter a description of the contract item, up to 30 characters.
Note:Data previously entered and saved in this field will be cleared if you change the 'create items as' option (above) to Use Import Phase, Use Viewpoint Phase, or None.

## Beginning/Ending Character

Enabled only if you selected the Use Import Phase or Use Viewpoint Phase 'create items' options above.
Enter the beginning and ending character position from which the contract item for each phase will be created. The contract item number will be created from the phase using the beginning and ending positions.
For example, if you specify position 1 and 3, and your phase code is 03110-100-001, the contract item number will be 031.

## Import Item Code as Standard Item Code

This checkbox is enabled only if the
 When no records
 are available to import, create items as defined below option is set to
 None.
Check this box to have the import process bring item codes into the work file as standard item codes.
Note:If you check this box and set the Create Item
 Option drop-down to S-Used Standard Item Code, when importing items with
 no description, the system will use the description from JC Std Item Codes if one
 exists. If a description does not exist or a standard item code is not found, the
 description will default as “Missing Description”.

Uncheck this box if item codes will not be imported into the work file as standard item codes. Item codes will instead become contract items.
Note: You should only use this option if your import data
 includes item data.

## Create Item Option

Enabled only if Import Item Code as
 Standard Item Code box is checked ( above).

- I-Use Next Sequential Item – Select this option to have contract items assigned sequentially (beginning with ‘1’) to standard item codes. Numbers are assigned based on the order in which they were imported into the work file.

- S-Use Standard Item Code – Select this option to have contract item numbers be the same as the standard item code.

Note:If you select this option, when importing items with no description, the system will use the description from JC Std Item Codes if one exists. If a description does not exist or a standard item code is not found, the description will default as “Missing Description”.

##  Increment By

 Enabled only when importing item codes as standard item codes and using the ‘Use Next Sequential Item’ option.
 Required.
 Specify the value (1-99) by which to increment the sequentially assigned numbers. Default is '1'; however, increasing this number will allow for inserting additional items later on.

## Default Std Region

Enter the default region to which standard item codes will be assigned. The region specified here will be used if no standard region is defined in the import file.
Standard item codes do not have to be set up in JC Std Item Codes for the specified region at the time of the import. However, if you are allowing items to be set up automatically (Create Standard Item Codes option checked, Edit/Upload Parameters tab), the region must exist before the item can be added.

## Create Unique Phase Using Item or Sequential # . . .

Specify how to handle the creation of unique phases when duplicate phases exist for a project.

- D - Duplicates Only — Select this option to have unique phases
 created for duplicate phases only.

- A - Always — Select this option to create a unique phase for every
 phase in the text file. Note: If a phase exists multiple times in the text file and all
 occurrences have the same item and cost type, the import will roll all cost detail
 into the first occurrence of the phase and assign the last part of phase based on the
 item/bid number or a sequence number. All remaining occurrences of the phase will be
 removed

- N - Never — Select this option if unique phases will never be generated for phases in
 the text file. If duplicate phases exist, their costs will be rolled into one contract
 item, using the contract item of the first occurrence of the phase.

- S – Only Phase with Sub Cost Types — Select this option to create unique phases for
 only those phases in the text file with a cost type matching either of the two cost
 types defined for subcontracts in PM Company Parameters.

Note: When creating unique phases, the system first tries
 to attach the assigned contract item. If the contract item is too big, then a sequential
 number is applied instead. However, this feature will only work if the last part of the
 phase code is three characters in length and blank.

## When Material Codes Exist in the Import File . . .

Specify how to handle material codes when importing data.

- Y - Drop All Material Codes – Select
 this option to drop material codes when importing materials. Only material detail
 (e.g. description, phase codes, cost types, units of measure, unit price, etc.) will
 be imported. Material codes will be left blank in the work file. Because the PM
 Material Detail program allows the use of non-valid or null materials, using this
 option provides the ability to import the necessary material detail without having to
 set up cross-references to Vista™ material codes.Note: Selecting
 this option disables the Roll up material codes when loading import
 into work table checkbox.

- N - Import All Material Codes – Select
 this option to import all material codes, regardless of whether they are valid (i.e.
 exist in HQ Materials).

- X - Import Only Valid Material Codes – Select this option to only import valid material
 codes (i.e. material codes that are already set up in HQ Materials or are
 cross-referenced to a valid HQ material will be imported.

Note: The material group used to validate materials is the
 material group defined in HQ Company Setup for the active PM company.

## Roll Up Material Codes When Loading Import Into Work Table

Disabled if you are not importing material
 codes (that is, you selected the Y-Drop All Material Codes option from the When material codes exist
 in the import file, do the following drop-down in PM Import Estimates
 Template).
Select this checkbox to roll up materials
 when importing data from the text file. All materials that have the same material code,
 phase code, cost type, unit of measure, and unit price are rolled into one record, totaling
 all units and cost together. If material detail is not the same, the material record will
 be imported separately.
Note: If no material codes exist in the import file, the
 system will not roll up materials, regardless of whether this box is checked.
Do not select this checkbox if you want
 material records imported separately, regardless of whether duplicate data exists.

## Accumulate Phase Costs Into Contract Item Amount . . .

Check this box to have the upload process accumulate the costs for each phase into the contract items where the item's amount is zero. If multiple phases are assigned to a single contract item, costs for all phases will be pulled into the contract item.
Uncheck this box if phase costs will not be accumulated into contract items.
Note:This option should only be used if the item import records have no amounts or you are creating item records (e.g. Timberline or Generic imports). If item records exist with amounts, the phase costs are accumulative.

## Use Contract Item Quantity and UM for Cost Types

Check this box to use the contract item quantity and unit of measure for all cost types assigned to the contract item when importing data from the text file. 
Uncheck this box to import each cost type’s quantity and unit of measure from the text file.

## Create a Subcontract Record When Import Cost Type . . .

Check this box to have a subcontract detail record created for every occurrence of a subcontract cost type in the import text file where the import subcontract cost type is equal to either of the cost types specified for subcontracts in PM Company Parameters. If multiple records exist with the same unit of measure, the units and costs will be summed and the record created. However, records will only be created if the subcontract record does not already exist.
Uncheck this box if you do not want subcontract records created during the import process. Subcontract records will need to be entered manually.

## Use Description from SI Codes When Loading Contract Items . . .

This option is only applicable if you have selected the Use Import Phase or Use Viewpoint Phase 'create items as’ options.
Check this box to use standard item code descriptions for contract items. When checked, the contract item will be checked against available standard item codes. If a standard item code is found in JCSI (JC Standard Item Codes) that matches the contract item number, the description for the standard item code will become the contract item’s description. If there are duplicate standard item codes with different region codes, the description from the last record will be used. If no standard item code exists matching the phase characters, the contract item description will default as null.
Uncheck this box to have contract item descriptions come from the first phase assigned to that item.

## Use Phase UM and Units if Phase Exists . . .

For Timberline imports only.
Check this box to use the phase’s UM and Units for all cost types assigned to the phase where no unit of measure and no units are specified.
Uncheck this box to set the UM to ‘LS’ for all cost types assigned to a phase where no unit of measure and no units are specified. Units will be set to 0.00.

## Always Use the Phase Master Phase Description

Check this box to use the phase description
 from JC Phases (JCPM) when importing phases that already exist in JCPM. Imported phases
 that do not exist in JCPM will use the import phase description.
Uncheck this box if imported phases will
 always use the import phase description, regardless of whether phase exists in JC Phases.

## Phases

Indicate how the system should handle cross-referencing when making corrections to phases in the work file (PM Import Edit).

- Always – Select this option to always create a cross-reference phase record and correct every occurrence of missing or incorrect cross-references.

- Prompt – Select this option to prompt the user to specify whether to auto-create a cross-reference phase. If user selects Yes, the system will automatically create a cross-reference and correct every occurrence of missing or incorrect cross-references. If user selects No, they must manually create the cross-reference record and correct all errors.

- Never – Select this option if cross-reference phases should never be created. Every occurrence of missing or incorrect cross-references must be corrected manually.

## Cost Types

Indicate how the system should handle cross-referencing when making corrections to cost types in the work file (PM Import Edit).

- Always – Select this option to always create a cross-reference cost type and correct every occurrence of missing or incorrect cross-references.

- Prompt – Select this option to prompt the user to specify whether to auto-create a cross-reference cost type. If user answers ‘Yes’ to the prompt, the system will automatically create a cross-reference and correct every occurrence of missing or incorrect cross-references. If user answers ‘No’ to the prompt, the user must manually create the cross-reference record and correct all errors.

- Never – Select this option if cross-reference cost types should never be created. Every occurrence of missing or incorrect cross-references must be corrected manually.

## Unit of Measures

Indicate how the system should handle cross-referencing when making corrections to units of measure in the work file (PM Import Edit).

- Always – Select this option to always create a cross-reference UM and correct every occurrence of missing or incorrect cross-references.

- Prompt – Select this option to prompt the user to specify whether to auto-create a cross-reference UM. If user selects Yes, the system will automatically create a cross-reference and correct every occurrence of missing or incorrect cross-references. If user selects No, they must manually create the cross-reference record and correct all errors.

- Never – Select this option if cross-reference UMs should never be created. Every occurrence of missing or incorrect cross-references must be corrected manually.

## Vendors

Indicate how the system should handle cross-referencing when making corrections to vendors in the work file (PM Import Edit).

- Always – Select this option to always create a cross-reference vendor and correct every occurrence of missing or incorrect cross-references.

- Prompt – Select this option to prompt the user to specify whether to auto-create a cross-reference vendor. If user selects Yes, the system will automatically create a cross-reference and correct every occurrence of missing or incorrect cross-references. If user selects No, they must manually create the cross-reference record and correct all errors.

- Never – Select this option if cross-reference vendors should never be created. Every occurrence of missing or incorrect cross-references must be corrected manually.

## Materials

Indicate how the system should handle cross-referencing when making corrections to materials in the work file (PM Import Edit).

- Always – Select this option to always create a cross-reference material and correct every occurrence of missing or incorrect cross-references.

- Prompt – Select this option to prompt the user to specify whether to auto-create a cross-reference material. If user selects Yes, the system will automatically create a cross-reference and correct every occurrence of missing or incorrect cross-references. If user selects No, they must manually create the cross-reference record and correct all errors.

- Never – Select this option if cross-reference materials should never be created. Every occurrence of missing or incorrect cross-references must be corrected manually.

## Create Project Firm Record for Each Vendor . . .

Check this box to have the upload process automatically create a record in PM Project Firms for each vendor in the subcontract or material work file. A record will only be generated if the vendor is already set up in the PM Firms and at least one contact is set up for that firm. If multiple contacts are set up, the vendor will be set up in PM Project Firms with the first contact specified in the Firm Master.
Uncheck this box if you do not want vendors set up as firms automatically during the import process. You will need to set them up manually in PM Project Firms.

## When Uploading Change Order, Each Contract Item . . .

Check this box if you are uploading import data as a pending or approved change order and want the upload process to create a change order item for each contract item.
Uncheck this box if you do not want a change order item created for every contract item when uploading import data into a pending or approved change order.

## When Uploading Change Order, Set the Item Amount . . .

Check this box if you are uploading import data as a pending or approved change order and want the upload process to set each item’s amount as the Fixed Amt for the change order item (PM Pending Change Orders, Items section, Info tab).
Note:This option is only applicable if you are also using the option to create a change order item for each contract item.

Uncheck this box if you do not want contract item amounts set as fixed amounts for change order items when uploading change orders.

## Create Standard Item Codes

Check this box to have the upload procedure add standard item codes to JCSI (JC Std Item Codes) if they do not already exist for the region. (Note: A region code must exist in order for this feature to work.)
Uncheck this box if you do not want standard item codes added to JCSI during the upload if they do not already exist for a region. When unchecked, an error will display during the upload if the standard item code does not exist in JCSI for the region. You will need to add the standard item code(s) manually to JC Std Item Codes.

## Default Contract and Description from Project

Check this box to default the contract number and description from the project code and description.
Uncheck this box to use the contract number and description from the text file.

##  Cost Type

 Specify the cost type (from JC Cost Types) for which to create an associated cost type record.
 For example, if you want to create a burden record for every labor record, you would enter the Labor cost type here. (Note: You will enter the Burden cost type in the next field.)

##  Create C-T

 Specify the cost type (from JC Cost Types) you wish to create.
 For example, if you want to create a burden record for every labor record, you would enter the Burden cost type here. (Note: You will have entered the Labor cost type in the previous field.)

## Use UM

Check this box to have the created cost type use the same UM as the referenced Cost Type. For example, if creating a burden record for every labor record and the UM for the Labor cost type is CY, the UM for the Burden cost type will be set to CY.
Uncheck this box to assign a UM of 'LS' to the created cost type.

## Use Units

Check this box to have the created cost type use the same units as the referenced Cost Type. For example, if creating a burden record for every labor record and the Labor cost type specifies 100.00 units, the units for the Burden cost type will be set to 100.00.
Uncheck this box to set the units to 0.00 for the created cost type.

## Use Hours

Check this box to have the created cost type use the same hours as the referenced Cost Type. For example, if creating a burden record for every labor record and the Labor cost type specifies 80.00 hours, the hours for the Burden cost type will be set to 80.00 hours.
Uncheck this box to set the hours to 0.00 for the created cost type.

##  Phase: Import Code

 Specify the import phase code, up to 30 characters, to which you are cross-referencing a Viewpoint phase code.

##  Phase: Phase

 Specify the Viewpoint phase code (from JC
 Phases) to use as the cross-reference for the import phase code. When data is imported into
 the work file, this phase code will be used in place of the specified import phase code.

##  Cost Type: Import Code

 Specify the import cost type, up to 30 characters, to which you are cross-referencing a Viewpoint cost type.

##  Cost Type: Cost Type

 Specify the Viewpoint cost type (from JC Cost Types) to use as the cross-reference for the import cost type. When data is imported into the work file, this cost type will be used in place of the import cost type.

## Cost Type: Cost Only

Check this box to have only costs (not units) rolled up when consolidating multiple import cost types into a single Viewpoint cost type.
Uncheck this box if you do not want to roll up only costs when consolidating multiple cost types into a single Viewpoint cost type. Be aware that if unchecked, units will be imported, which may cause inaccurate accounting of units.

##  Unit of Measure: Import Code

 Specify the import unit of measure code, up to 30 characters, to which you are cross-referencing a Viewpoint cost type.

##  Unit of Measure: UM

 Specify the Viewpoint unit of measure (from HQ Units of Measure) to use as the cross-reference for the import unit of measure. When data is imported into the work file, this unit of measure will be used in place of the import unit of measure.

##  Material: Import Code

 Specify the material code, up to 30 characters, to which you are cross-referencing a Viewpoint material code.

##  Material: Material

 Specify the Viewpoint material code (from HQ Materials) to use as the cross-reference for the import material code. When data is imported into the work file, this material code will be used in place of the import material code.

##  Vendor: Import Code

 Specify the import vendor code, up to 30 characters, to which you are cross-referencing a Viewpoint vendor code.

##  Vendor: Vendor

 Specify the Viewpoint vendor (from AP Vendors) to use as a cross-reference for the import
 vendor code. When data is imported into the work file, this vendor will be used in place of
 the import vendor code.
