---
title: "About the PM Import Estimates Edit Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-edit-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-edit-form"
---

# About the PM Import Estimates Edit Form

This form can only be accessed by clicking the Edit Work Tables button on the PM Import Menu, and is used to review and correct imported data before it is uploaded into PM.
Work tables contain estimate detail from the text file that was uploaded and cross-reference data from the template. They allow you to edit incorrect cross-references and enter proper destination codes if no cross-reference existed. Once the work table in correct, upload it into the Project Management module.
Once you enter the Import ID, all of the data imported from the text file is pulled into the work file. You can then use the various tabs to review the data and make any necessary corrections.

- Show Errors Only - The Show Errors Only option (Options menu) allows you to restrict the data display to only those records that contain missing or incorrect information. When selected, a 'Filter On' message displays in red above the tab pages and grids are refreshed to include only data where errors were encountered (does not apply to the Grid and Info tabs).

-  Info - Contains display-only information specific to the import ID (i.e.,
 who imported and uploaded data and import and upload dates), as well as editable
 information about the imported job such as the estimate number, phone and fax
 numbers, standard region, and mailing/shipping addresses.Note: If no standard
 region is entered, the SI Code column will not
 display on the Items tab. If a standard region is specified that is not
 defined in JC Std Item Codes, and you checked the Create
 Standard Item Code box for the import template, it will be
 added automatically (along with the associated item codes) when the project
 is uploaded to PM.

- Items - Contains item data, which will become item data on the contract. Each
 item code will become a contract item number, and the units, unit price, and
 amount will become the contract item’s original amounts. If you have specified a
 standard region (Info tab), the SI Code column displays and
 defaults the item codes from the import data file.Note: If a standard item code
 is not defined in JC Std Item Codes and you checked the Create
 Standard Item Code box for the import template (in PM Import
 Template, it will be added automatically during the update to PM.


- Phases - Contains the phases (which will become project phases) and the contract
 items to which they are assigned. Any corrections to invalid phases (those that
 are not cross-referenced) must be made here. Although you can access the Phase
 field on the Cost Types, Subcontracts, and Materials tabs, you can only use
 those fields to change the phase to which the cost type, subcontract, and/or
 material is associated. (Note: Phases must exist on this tab before they can be
 assigned to cost types, subcontracts, and materials.).

- Cost Types - Contains cost type data, including the phase, cost type, units,
 unit of measure, hours, costs, and the bill, item unit, and phase unit flags.
 The Totals line at the bottom of the grid displays the total Costs for the
 import. Since most estimating software does not deal with bill flag, item unit,
 and phase unit information, the import process will check JCPM (JC Phases) for
 this information and try to set it up for matching valid phases. Data may be
 edited as necessary. (Note: Phases assigned on this tab must exist on the Phases
 tab.)Note: If you have set the Auto Add Cost Type Header from
 Materialdrop-down to 2-With No Estimates (in PM Company
 Parameters) and you imported data from a text file containing material
 records without supporting cost type records, the costs will be set to 0.00
 for the cost type records created during the import.

- Subcontracts - Contains subcontract data, including the phase, cost type,
 vendor, units, unit of measure, unit price, amount, work complete percentage,
 and description for each item. The Totals line at the bottom of the grid
 displays the total subcontract Amount for the import. Data may be edited as
 necessary. (Note: Phases assigned on this tab must exist on the Phases tab.)
 Note: If you imported data using the
 Generic import template, the Description field will
 default the subcontract description from the import file. If no subcontract
 description exists or you imported data using any other import template, the
 description will default as null. Default may be overridden.

- Materials - Contains material data, including the material code (if applicable),
 phase, cost type, vendor, units, UM, unit cost, ECM, and amount for each
 material. The totals line at the bottom of the grid displays the total materials
 amount for the import. Data may be edited as necessary.

- Notes - In addition to estimate data, the import process will also import
 estimate notes. Each of the detail tabs (Items, Phases, Cost Types,
 Subcontracts, and Materials) contain a Notes column, which allows for adding
 and/or editing notes specific to that data. The Notes tab allows for entering
 and/or editing notes at the job level.

- Data Errors - For all tabs (except the Grid and Info tabs),
 the informational display includes a Data Errors message box. As you work
 through each tab, it is important to note any messages shown in this box, as it
 will alert you to any errors that need to be corrected. If any data errors exist
 for a record, the record (line) will be highlighted in red, and the Data Errors
 box will provide information about what is wrong with that particular record
 (e.g. invalid phase, material, UM, etc.). Once you correct the record, click the
 Refresh Grid to verify errors for the individual records. This is important if
 updating cross-references that affect more than one record. The grid will not
 reflect the changes made for any other records until the refresh is done.Note: When correcting errors, you can use the F5
 functionality to add the value in the related setup form (e.g. adding an
 invalid phase to JC Phases). However, because you are not actually
 'changing' the value for the record, the system does not recognize that
 there is anything to update and the line will remain red. You will need to
 change another value in the record to alert the system that the record has
 been changed, and then click Save (e.g. if you added a
 phase to the JC Phases, can check and uncheck the Active flag on the phase record and then click Save).

[Uploading Imported Data ](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form)
[PM Import Estimates - Overview](/en/vista/vista/project-management/import-project-estimates/pm-import-estimates-form)
