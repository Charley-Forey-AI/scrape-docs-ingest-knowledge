---
title: "Field Definitions: PM Subcontract Detail Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form/field-definitions-pm-subcontract-detail-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form/field-definitions-pm-subcontract-detail-form"
---

# Field Definitions: PM Subcontract Detail Form

The following is a list of field descriptions for the PM
 Subcontract Detail form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Specify the project for which to set up/modify subcontract detail.
If you enter a project with a closed status (hard or soft), the status displays in red to the right of the project description. You will only be able to add or modify subcontract detail for the project if you allow posting to hard- and/or soft-closed jobs (flags in JC Company Parameters checked).

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Record Type

Disabled when this form is accessed from PM Project Phases, PM Pending Change Orders, and PM Approved Change Orders.

- O-Original – Select this option to enter/modify subcontract detail for an Original Estimate.

- A-Approved CO’s – Select this option to enter/modify subcontract detail for approve change orders.

- P-Pending CO’s – Select this option to enter/modify subcontract detail for pending change orders.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

##  Phase

 Enter the phase (from JC Phases Maintenance)
 for which to enter subcontract detail.
 Once the subcontract item is interfaced to accounting, the phase cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Cost Type

Enter the cost type for this phase. This will typically be a subcontractor cost type, but other cost types may be used.
If phase was imported from a third-party estimating package or entered in PM Project Phases, PM SL Header, PM Pending Change Orders, or PM Approved Change Orders, this field defaults the cost type specified in the originating source. Otherwise, defaults the subcontract cost type specified in PM Company Parameters (SL Params tab).
Once the subcontract item is interfaced to accounting, the cost type cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## ACO

Check this box if this material record is ready to be interfaced (in PM Interface).
Uncheck this box if this material is not ready to be interfaced. When quote is interfaced to accounting, this material record will be skipped.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## ACO Item

Displays only when this form is accessed from
 the main menu and the Record Type is A-Approved CO’s.
Enter the approved change order item to which this subcontract detail applies. Must be a valid item for the specified change order.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## PCO Type

Displays only when this form is accessed from
 the main menu and the Record Type is P-Pending CO’s.
Enter the pending change order type. Must be a document type (set up in PM Document Types) assigned a Document Category of ‘Pending Change Order’.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## PCO

Displays only when this form is accessed from
 the main menu and the Record Type is P-Pending CO’s.
Enter the pending change order to which this
 subcontract detail applies. Pending change order must already exist for the project.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## PCO Item

Displays only when this form is accessed from
 the main menu and the Record Type is P-Pending CO’s.
Enter the pending change order item to which
 this material detail applies. Must be a valid item for the specified change order.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Vendor

Use this field to select the vendor associated
 with the subcontract. Enter the vendor number or press F4 to select the vendor from a list.
 If the selected vendor has not been set up in PM Firms or PM Project Firms, the system will automatically add the vendor once you initialize this line.
Vendor initially defaults as follows:

- If you imported this phase from a third-party estimating package,
 defaults the vendor from the import file.

- If you entered the phase in PM Project Phases, PM Subcontract, PM
 Pending Change Orders, or PM Approved Change Orders, defaults the vendor specified in
 the originating source.

Once the subcontract item is interfaced to
 accounting, the vendor cannot be changed.
When creating a new subcontract item
When creating a new subcontract item using the Non-Interfaced tab for a vendor that is not already associated with the project, the system will automatically add the new vendor to the project (PM Projects> Firms tab).
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## SL

Enter a subcontract number, up to 30 characters, or leave blank if using the Initialize feature. If manually assigning subcontract numbers, it is suggested that you use the format specified for subcontract numbers in PM Company Parameters.

- If you will be exporting subcontract information to Textura (via the SL Textura Subcontract Export and SL Textura Subcontract Compliance Export reports), you will need to limit your subcontract numbers to 20 characters. Textura allows a maximum of 20 characters for subcontract numbers; subcontract numbers that exceed 20 characters will be truncated during the export.

- If you did not specify a vendor for this entry, the subcontract entered here must already exist for the project. You can only assign new subcontract numbers once you have assigned a vendor.

To initialize subcontract numbers, click on the Initialize button above the tab pages. You can only initialize subcontract numbers for subcontract detail lines with a vendor assigned.
Once the subcontract item is interfaced to accounting, the subcontract number cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## SL Item

Enter the subcontract item number (1-32,767) or leave blank if using the Initialize feature.
If you checked the Disable Initialize button
 for change order subcontract detail box in PM Company Parameters, and you
 are entering a change order, this field defaults as blank and you will need to manually
 enter the subcontract item number; the Initialize feature is not available. If you do not
 check the PM Company Parameters box, and you are manually assigning subcontract numbers for
 change orders, this field defaults the next sequential number available for the specified
 subcontract.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## SL Item Type

Specify the subcontract item type.
1 = Regular
2 = Change Order - Select this option if you
 are going to modify the original subcontract. This option is only available if the
 Record
 Type is A-Approved CO's or P-Pending CO's.
3 = Backcharge - Select this option if any
 deductive change orders are prohibited for the subcontract. This option is only available
 if the Record
 Type is O-Original
4 = Add-on - Select this option if any
 standard deductions or additions are going to be made. This option is only available if the
 Record
 Type is O-Original.
Once the subcontract item is interfaced to accounting, the subcontract item type cannot be changed.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## SL Add-on

Enabled only if the SL Item Type
 for this line is 4–Add-on.
Enter a valid add-on (as defined in SL Add-ons) for this phase.
Once the subcontract item is interfaced to accounting, this field cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## SL Item Description

Enter a description for this subcontract item. The description can be up to 60 characters long.
Default Value
If you uploaded this subcontract item using [PM Import Estimates Upload ](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-upload-form), this field defaults with the subcontract description defined in [PM Import Estimates Edit](/en/vista/vista/project-management/import-project-estimates/about-the-pm-import-estimates-edit-form).
If the subcontract item is manually created or
 associated with a change order, the selection in the Default SL Item Description from Phase
 Description box on the in [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form)determines the default value in this
 field.

- If checked, this field defaults with the phase description.

- If unchecked, this field defaults with the description of the contract item associated with the phase. For example if you create subcontract detail using the Estimate / Purchase Details tab on the PM Pending Change Orders form, the subcontract detail that is created will have the description of the contract item associated with the PCO item.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Add-on %

Enabled only if the SL Item Type
 for this line is 4–Add-on and the add-on type is Percent.
Enter the add-on percent to use when calculating the add-on amount for this subcontract detail line. Initially defaults the percentage specified for the add-on in SL Add-ons.
Once the subcontract item is interfaced to accounting, the add-on percentage cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Units

Disabled if UM is ‘LS’.
Enter the number of units for this phase. If phase was imported from a third-party estimating package or entered in PM Project Phases, PM SL Header, PM Pending Change Orders, or PM Approved Change Orders, defaults the units specified in the originating source.
Note:For add-on lines (SL Item Type ‘4 – Add-on’), this field defaults as 0.00 and will be disabled.

Once the subcontract item is interfaced to accounting, the number of units cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## U/M

Enter the unit of measure for this phase.
For add-on lines, default will be ‘LS’ and cannot be changed.
If phase was imported from a third-party estimating package or entered in PM Project Phases, PM SL Header, PM Pending Change Orders, or PM Approved Change Orders, defaults the unit of measure specified in the originating source.
Once the subcontract item is interfaced to accounting, the unit of measure cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Unit Cost

Enter the unit cost.
If phase was imported from a third-party estimating package or entered in PM Project Phases, PM SL Header, PM Pending Change Orders, or PM Approved Change Orders, defaults the unit cost specified in the originating source.
Once the subcontract item is interfaced to accounting, the unit cost cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Amount

If UM is ‘LS’, enter the total amount for this subcontract detail line. For non-LS lines, amount is calculated automatically based on Units x Unit Cost.
For add-on lines (SL Item Type
 4), this amount defaults based on the add-on type. If Amount, default will be the amount
 specified for the add-on in SL Add-Ons. If Percent, amount will calculate as follows:

- Original Estimates - If the add-on is a percentage, the amount will be calculated based on the percentage specified and the total of regular items only (i.e. lines with a SL Item Type of ‘1-Regular’). For example, your subcontract total is $15,000, but the total of regular items is 10,000. If add-on percentage is ‘5.00%’, add-on amount will default as 500.00.

- Change Orders (Pending or Approved) – If the add-on is a percentage, the amount will be calculated based on the percentage specified and the change order item amount. For example, if the change order item amount is 1,000.00 and the add-on percentage is ‘5.00%’, the add-on amount will default as 50.00.

Once the subcontract item is interfaced to accounting, the amount cannot be changed.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Send

Check this box if this record should be sent to accounting when subcontracts are interfaced.
Do not check this box if this record is not ready to be interfaced. The record will be skipped when the interface is performed.
Note:If this subcontract detail line is for a pending or approved change order, you will need to assign a SCo number before it can be interfaced.

Once the subcontract item is interfaced to accounting, this flag cannot be changed.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## SubCO

Use this field to associate the subcontract detail record with a subcontract change order(SubCO).
This field is only displays when the subcontract detail is associated with a pending or approved change order - select
 Pending CO's
 or
 Approved CO's
 from the
 Record Type
 drop down at the top of the form.
Create a new subcontract change order
Enter a subcontract change order number that
 has not already been used. For example press F4 to see the existing SubCOs on the
 subcontract selected in the SL field and then enter a subcontract change
 order number that has not been used. This will create a new SubCO in [PM Subcontract Change Orders](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form).
Select an existing
Press F4 to select an existing SubCO from a list -
 only existing SubCOs that are associated with the subcontract in the SL field will
 display in the list.
Subcontract change orders are created and maintained using [PM Subcontract Change Orders](/en/vista/vista/project-management/subcontracts/pm-subcontract-change-orders-form). Click [here](/en/vista/vista/project-management/subcontracts/subcontract-change-orders---overview) for general information on subcontract change orders.
When creating new subcontract items
If the subcontract item is new, is associated
 with an approved or pending change order, and has a SL Item Type of 1-Regular, assigning a
 subcontractor change order (SubCO) will result in the following message:
"Warning: This is a new item set up as a regular item type. Assigning a SubCO may result in some reporting inaccuracies. "
The system allows the entry, but this is not recommended because several reports include records with no SubCO in the original amounts.
ACOs - The SubCO is automatically approved
If the subcontract detail item is associated
 with an approved change order, any SubCO selected in this field will automatically be
 approved. This means that you can use this field to create a new SubCO and interface it using
 the PM Interface form without having to manually approve the SubCO using the Approve button on
 the PM Subcontract Change Orders form.
Select
 A-Approved CO's
 in the
 Record Type
 drop down at the top of the form to see which subcontract detail items are associated with approved change orders.
Note:The SubCO field on the Non-Interfaced Items tab
 of the PM Subcontracts form functions the same way.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## WC Retg % - Work Completed Retainage Percentage

Enter the work complete retainage percentage for the subcontract item. This is used to calculate default retainage amounts on AP invoices or when initializing work completed retainage in [SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form).
 When creating new subcontract items, this
 field will default based on the phase entered in the Phase field.
How is the default value selected?
The diagram below outlines how the system determines the default value for this field.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## SM Retg % - Stored Materials Retainage Percentage

Enter the stored materials retainage percentage for the subcontract item. This is used to calculate retainage amounts when initializing stored materials retainage in SL Worksheet.
When creating new subcontract items, this
 field will default based on the phase entered in the Phase field.
The diagram below outlines how the system determines the default value for this field.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Tax Type

Specify the tax type for this subcontract
 item. The Tax
 Type and Tax Code fields are used to add taxes on top of the subcontract item. Select a
 tax type and then enter a tax code using the Tax Code field.

- 1-Sales
 – Use for tax amounts that are payable to the vendor.

- 2-Use– Use for tax amounts that are accrued and paid later to the appropriate State or Local taxing authority.

- 3-VAT(Value Added Tax) – Use for taxes paid on goods and services.

 This field initially defaults as follows:

- If the Use default tax code for subcontracts box
 is checked in PM Projects and,

- the active company's
 Default Country
 is 'US' (in HQ Company Setup), defaults as 1-Sales.

- the active company's
 Default Country
 is other than 'US' (e.g Canada or Australia), defaults as 3-VAT.

- If the
 Use default tax code for subcontracts
 box is unchecked, tax type defaults as null, regardless of country.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Tax Code

Enter the tax code for this subcontract or press F4 to select a tax code
 from a list. The Tax Type and Tax Code fields are used to add a tax on top of the subcontract
 item. Select a tax type in the Tax Type field before entering a tax
 code.
Tax code defaults as follows:

- If the Use default tax code for subcontracts box
 is checked in PM Projects, the default for this field is determined by the setting of the
 Base Tax
 On drop-down field in PM Projects. If the field is set to J-Job, the tax
 code defaults from PM Projects ( Tax Code field). If the field is set to
 V-Vendor, the tax code defaults from AP Vendors ( Tax Code
 field). If the field is set to O-Vendor Override, the tax cod defaults
 from AP Vendors. If a tax code is not specified there, the tax code will default from PM
 Projects.

- If the
 Use default tax code for subcontracts
 box is unchecked, tax code defaults as null.

Note:If using F4 to look up valid tax codes, the Tax Type determines the lookup to display. For Sales and Use tax, the standard Tax Codes lookup is used. If the tax type is VAT, the VAT Tax Codes lookup displays.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)PM Subcontract Detail

## Interface Date

The Interface Date field on the PM Subcontract Detail form, Interfaced tab.

Display only, the date the selected subcontract/subcontract item was interfaced.
Note: This date is populated by the system when an interface occurs for the selected item and cannot be edited, even when using the Correct Item option (Tasks > Correct Item).

## Interface Month

The Interface Month field on the PM Subcontract Detail form, Interfaced tab.

Display only, the original interface month for the selected subcontract/item.
 If you make corrections to a subcontract/item (via Tasks > Correct Item), you must interface the changes in this month.
Note: This date is populated by the system when you first interface the selected item and cannot be edited, even when using the Correct Item option (Tasks > Correct Item).
