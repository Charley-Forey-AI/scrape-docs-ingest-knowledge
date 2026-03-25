---
title: "Field Definitions: SL Subcontract Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form/field-definitions-sl-subcontract-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form/field-definitions-sl-subcontract-entry-form"
---

# Field Definitions: SL Subcontract Entry Form

The following is a list of field descriptions for the SL
 Subcontract Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

 If this is a new batch, this field automatically defaults to New. The system assigns sequence numbers, so accept the default.
 If this is an existing batch, enter the sequence number to work on, or, enter “New” to add a new sequence to the batch.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Action

Select the action that you would like to
 perform.

- Add - When you are creating a new subcontract, the Action field
 is disabled and it will display Add.

- Change - Select this option when changing an existing subcontract.
 For example if you select File > Add
 Subcontract to add a subcontract to the batch, the Action field
 will default with this option.

- Delete - Select this option to delete a subcontract. [More](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/delete-a-subcontract-or-subcontract-item)

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Subcontract

Enter a number to identify the subcontract.
 The value in this field can be up to 30 characters long.
To work on an existing subcontract, select
 File > Add
 Subcontract to enter the subcontract number. Do not press F4 and try to select an
 existing subcontract.
Note: If you will be exporting subcontract information to
 Textura (via the SL Textura Subcontract Export and SL Textura Subcontract Compliance Export
 reports), you will need to limit your subcontract numbers to 20 characters. Textura allows
 a maximum of 20 characters for subcontract numbers; subcontract numbers that exceed 20
 characters will be truncated during the export.

## JC Co#

This field initially defaults to the currently active Job Cost company. Accept the default or enter the Job Cost company that this subcontract will update. The job and phase codes specified for this subcontract must be valid for this company.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Job

Enter the job that applies to the subcontract. The job description displays below this field.
Note: If you enter a soft- or hard-closed job, the status displays in red above the tab page. Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Description

Enter a description of the subcontract. The value in this field can be up to 60 characters long.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Vendor

Enter the subcontractor, or the vendor of the
 subcontract. You can also press F4 to select the vendor from a list.

- The vendor cannot be changed when a subcontract has: been invoiced; had a change order applied against it; or is on a worksheet (SL Worksheet).

- If you use the PM module and you change the vendor
 on an interfaced subcontract, the system checks to see if the vendor exists as a PM
 module firm. If the vendor does exist, the system updates the PM module and deletes
 the Send To
 Contact field in [PM Subcontracts](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form). If the vendor does not exist as a
 firm, the system deletes both the Send to Firm and Send to
 Contact fields in PM Subcontracts.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Pay Terms

Use this field to enter the payment terms of
 the subcontract. Enter a payment term code or press F4 to select one from a list.
Payment terms are created and maintained using
 the [ HQ Payment Terms ](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form) form. You can open this form by pressing
 F5
 in this field.

##  Compl Group

 Enter
 the compliance group for this subcontract. Press F4 for a list of valid compliance groups
 set up in HQ Compliance Groups. If you assigned a compliance group to the job in JC Jobs,
 that compliance group defaults here, although you can override the setting.
 When you post the SL Subcontract Entry batch, all of the compliance codes assigned to the compliance group are automatically assigned to the subcontract in SL Compliance.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Status

This field indicates the status of the subcontract and is only accessible in Change mode. The following statuses are available:

- Open – This status is automatically assigned to all new subcontracts, and indicates that changes and posting payables are allowed. Subcontracts with a “Complete” or “Closed” status may be changed to this status in Change mode.

- Complete – This status is assigned manually, and indicates that no changes or invoicing are allowed (in SL Worksheet or AP). Subcontracts with an “Open” or “Closed” status may be changed to this status in Change Mode.

- Closed – This status is automatically assigned to subcontracts that are closed in SL Close. This status cannot be assigned to any subcontract in this form. Closed status indicates that no changes or invoicing are allowed (SL Worksheet or AP), and that the subcontract is ready for purging.

Note: If you change the status of a closed subcontract to “Open” or “Complete” when posting the batch, the system records the closing month as null, and the status updated to 0 (Open) or 1 (Complete) in the SLHD (SL Header) table.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

##  Start Date

 Specify the start date for this subcontract. This can be the date of the subcontract or the date the work specified on the subcontract is expected to begin.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Hold Code

If all invoices posted to this subcontract should be placed on hold, enter a hold code here. This can be any valid hold code (defined in HQ Hold Codes) except the hold code specified for 'Retainage' in AP Company Parameters. The hold code identifies the reason that payment is withheld on AP invoices posted to this subcontract.
Note: Retainage is applied at the item level. Any item specifying a retainage percent is automatically assigned to the retainage hold code specified in AP Company Parameters.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Claim Approval Required

This box only applies to the subcontract claims process. [More](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)
When this box is checked, the claim must be processed using AP Unapproved Invoice Entry.
When this box is not checked, the claim can be processed using either AP Transaction Entry or AP Unapproved Invoice Entry.
Note: This checkbox defaults to unchecked, and never auto-checks—you must manually select it in any instance.
Note: Likewise, it does not auto-check with [DETAILS FORTHCOMING - CURRENTLY THIS IMPORTANT/NOTE BOX IS "EXCLUDED" FROM HELP]
Click [here](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims) for an overview of the claims process.
How do I remove this field from the form?
If you do not use the Claims feature, follow
 the steps below to remove this field from the form. You must be set up as a form
 administrator to complete these steps (VA User Profile form> Info tab> Form
 Administrator field).

1. Press F3 while in the field. This will
 open the Field Properties form.

1. Open the System Overrides tab.

1. Change the Show on Form and Show on Grid
 boxes to the "not checked" option ().

1. Click OK. The Claim Approval
 Required field will be removed from the form for all users.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Item #

Enter a number for this subcontract item.
Note: When working with an existing subcontract item, use the Costs tab to view the current costs, invoiced amounts, and remaining amounts associated with the item.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Sequence

Enter the inclusion/exclusion sequence number or press '+' or 'N' if you would like the system to automatically generate one.
The system will also automatically assign a sequence number when you click the New Record icon.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Action

Select the action that you would like to perform.

- Add - Select this option when you are creating a new subcontract item.

- Change - Select this option when changing an existing subcontract item.

- Delete - Select this option to delete a subcontract item. [More](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/delete-a-subcontract-or-subcontract-item)

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Type

There are four different types of subcontract items.

- 1-Regular – Use this type for all regular subcontract items. Units, unit costs, and total costs may be entered for these items.

- 2-Change Order – Use this type to set up change orders. No units, unit costs, or total costs may be entered here—that must be done in SL Change Order Entry.

- 3-Backcharge – Use this type to set up items that need to be backcharged to the subcontractor. Costs may be entered that will not be updated as committed costs.

- 4-Add-on – Use this type to set up additions and/or deductions to subcontract that need to be separate from the other items on the subcontract. No units or unit costs are entered—the add-on amount is determined by the add-on type, but may be overridden.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Job

This field defaults the job entered in the subcontract header. Accept the default or enter the job to which committed costs for this item will be posted in Job Cost. The job’s description displays below this field.
Note: If you enter a soft- or hard-closed job, the status displays in red to the right of the item description. Record will only be saved if you allow posting to soft- or hard-closed jobs (flags in JC Company Parameters).
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Phase

Specify the phase that committed costs for this item will be posted to
 in Job Cost. The phase’s description displays below this field.
If this is an add-on item, this field initially defaults the phase assigned to the add-on in SL Add-ons; may be overridden.
Note: If the Lock Phases option (JC Jobs) is in use for this
 job, the default phase must be set up for the job in JC Job Phases before it will be
 accepted here.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

##  CT

 Specify the cost type that will be posted to this subcontract item.
 If this is an add-on item, this field initially defaults the cost type assigned to the add-on in SL Add-ons; may be overridden.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Description

The Description field on the SL Subcontract Entry form, items Info tab.
Use this field to enter a description of the
 subcontract item. The value in this field can be up to 60 characters long.
By default, this field populates with the
 description of the phase selected in the Phase field.

##  Add-on#

 Enter the add-on number (from SL Add-ons) for this add-on item.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

##  Add-on%

 This field is used with percent type add-ons only. Initially defaults the percentage specified for this add-on in SL Add-ons; may be overridden.
 The add-on amount is calculated based on the percentage specified here and the subcontract total.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## UM

Enter a unit of measure for this subcontract item or press F4 to select a UM from a list.
If you enter LS (lump sum), the Original Units
 and Unit
 Cost fields are disabled.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

##  Original Units

The Original Units field on the SL Subcontract Entry form, items Info tab.
This field is enabled for non-LS (lump sum) items only.
Enter the original number of units for this subcontract item. If the unit of measure is not LS (lump sum), then enter the units.
Note: If you need to change the units for this subcontract item after the subcontract/item has been invoiced and closed, you must set the header status to 0 - Open.

## Original Unit Cost

The Original Unit Cost field on the SL Subcontract Entry form, items Info tab.
Enter the original cost per unit for this subcontract item. If this field is skipped and a total amount is entered, the unit cost automatically calculates.
Note: Original unit cost cannot be changed if a change order exists or if the subcontract/item has been invoiced and closed.

## Original Total Cost

The Original Total Cost field on the SL Subcontract Entry form, items Info tab.
Enabled for LS (lump sum) items only.
Enter the total original cost for this item.
Note: If you need to change the total cost for this subcontract item after the subcontract/item has been invoiced and closed, you must set the header status to 0 - Open.

## Tax Type

Use this
 field to select a tax type for the subcontract item.

- 1-Sales– Tax amounts are payable to the vendor and are added to the invoice total. This tax amount is directly charged to Job Cost, Equipment, and GL.

- 2-Use– Tax amounts are accrued, and will be paid at a later date to the appropriate State or Local taxing authority. Calculated tax amounts do not affect the gross or net balance due to the vendor. Instead, the transaction’s gross amount and tax amount is charged to Job Cost, Equipment, and GL account with an offsetting liability account as defined in HQ Tax Codes. Use the AP Tax Report to obtain an itemization of use tax amounts.

- 3-VAT(Value Added Tax) – This tax is paid on goods and services at each stage of production or distribution, and is based on the value added at each stage. This tax is tracked in the GL and reduces the payment to a taxing authority through an Input Tax Credit (ITC). This tax is not directly expensed. This option is the default for Canadian and Australian companies (Default Country field, HQ Company Setup). Use the AP Value Added Tax Report to obtain an itemization of VAT amounts.

 This field initially defaults as follows:

- If the Use default tax code for subcontracts box
 is checked in JC Jobs and,

- the active company's Default
 Country is 'US' (in HQ Company Setup), defaults as 1-Sales.

- the active company's
 Default Country
 is other than 'US' (e.g Canada or Australia), defaults as 3-VAT.

- If the
 Use default tax code for subcontracts
 box is unchecked, tax type defaults as null, regardless of country.

Note: Once you specify a code in this field and a tax type
 in the Tax
 Type field, the system displays the tax amount in the Tax Rate display
 field. The tax amount will also display on the Purchase Order when printed, and will also show
 when invoicing in AP.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Tax Code

Enter a tax code for this subcontract item, or press F4 to select one
 from a list.
This field initially defaults based on the following:

- If the Use default tax code for subcontracts box
 is checked in JC Jobs and,

- the active company's Default
 Country is other than 'US' (in HQ Company Setup), defaults the tax code
 defined for the job (in JC Jobs).

- the active company's Default
 Country is 'US' (in HQ Company Setup), the default for this field is
 determined by the setting of the Base Tax On drop-down field in JC
 Jobs. If the field is set to J-Job , the tax code defaults from JC
 Jobs ( Tax
 Code field). If the field is set to V-Vendor , the tax code defaults from
 AP Vendors ( Tax Code field). If the field is set to O-Vendor
 Override , the tax cod defaults from AP Vendors. If a tax code is not
 specified there, the tax code will default from JC Jobs. You can override the default
 as necessary.

- If the
 Use default tax code for subcontracts
 box is unchecked, tax code defaults as null, regardless of country.

- If using F4 to look up valid tax codes, the Tax Type determines the lookup to display. For Sales and Use tax, the standard Tax Codes lookup is used. If the tax type is VAT, the VAT Tax Codes lookup displays.

- Once you specify a code in this field and a tax type in the
 Tax Type
 field, the system displays the tax amount in the
 Tax Rate
 display field. The tax amount will also display on the Purchase Order when printed, and will also show when invoicing in AP.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## GL Account

This is the GL account debited when AP transactions are posted to
 this subcontract item. Enter a valid GL account with a subledger code of “J” or blank.
This field initially defaults a GL account as
 follows:

- If an override account is defined for the specified
 phase (in JC Departments, Phase Overrides tab), the override account is used.

- If an override account is not defined for the phase,
 the GL account for the specified cost type is used.

Entry in this field is only allowed if:

- The Allow GL Account Override When Posting
 Costs box is checked in JC Company Parameters (GL Cost tab).

- The Allow GL Account Override When Posting
 Costs is not checked, but a GL account was not specified for the phase
 or cost type in JC Departments.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Work Completed Retainage %

Enter the work completed retainage percentage.
When creating a new subcontract item, this
 field will default based on the phase entered in the Phase field on the subcontract item.
The diagram below outlines how the system determines the default value for this field.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Stored Materials Retainage %

 Enter the stored materials retainage percentage.
When creating a new subcontract item, this
 field will default based on the phase entered in the Phase field.
The diagram below outlines how the system
 determines the default value for this field.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Supplier

 Use this field for subcontract items in which a second party, other than the subcontractor,
 is involved.
Enter the supplier number (from AP
 Vendors).

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Notes

The Notes tab on the SL Subcontract Entry form, items section.
Use this field to enter notes on the
 subcontract item.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.

## Set WC Maximum Retention

Use this field to select how you would like to set the maximum retention amount.

- None - Select this option if you do not want to set a maximum retention amount for the subcontract.

- Percent of Subcontract - Select this option if you
 want to set the maximum retention amount for the subcontract by percentage. When you
 select this option, the system enables the % of Subcontract,  Include Chg Orders
 in Max Retention by %, and the Adjust Maximum Invoice fields.

- Maximum Amount - Select this option if you want to set a flat amount for maximum retention. When you select this option, the system enables the
 Retention Amount
 and
 Adjust Maximum Invoice
 fields.

Setting maximum retention amounts
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## % of Subcontract

The % of Subcontract field on the SL Subcontract Entry form, Maximum Retention Settings/PBA tab.
This field is only enabled when setting up maximum retention as a percentage of the contract.
Enter the percent of the subcontract amount used to calculate the total retainage allowed. The percentage specified here will be used with the Total Original Subcontract amount or Total Current Subcontract amount (if including change orders in maximum retention) to determine the maximum retention amount.
For example:
Subcontract Totals
Total Original: $550,000
Total Current: $675,000
Maximum Retention Amount
% of Subcontract: 10%
Max Amt by % (Include Chg Orders box unchecked): $55,000 (550,000 x .10)
Max Amt by % (Include Chg Orders box checked): $67,500 (675,000 x .10)
 The system allows retainage to be withheld until the maximum amount (in this example, $55,000 or $67,500) is reached; once this limit is reached, the system will no longer continue withholding retainage for the subcontract.

## Retention Amount

The system enables this field when you select
 Maximum
 Amount for setting maximum retention amounts.
Enter the maximum retention amount for this subcontract.

Setting maximum retention amounts
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Include Chg Orders in Max Retention by %

Check this box to include change order amounts in percentage-based maximum retainage calculations. When you check this box, the system calculates the maximum retention amount based on the current subcontract value.
Uncheck this box to exclude change order amounts in percentage-based maximum retainage calculations. The system will calculate the maximum retention amount based on the original subcontract value.
This box is only enabled when Percent of
 Subcontract is selected.

Setting maximum retention amounts
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Adjust Maximum Invoice

Select the correct method for retention distribution when the system reaches the maximum amount.
Composite Percentage
With this option, the system takes the final retention amount and calculates an overall percentage rate which it applies to all subcontract items equally.
For example, if you have set the maximum retention amount for a subcontract at $10,000, and you have already created invoices with retention amounts totaling $8,000, you will only have $2,000 left before you reach the maximum retention setting.
If you invoice $3,000 retention for two more items, the system will calculate a composite retention percentage and apply it to each item.
Retention Amounts Prior to Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
10%
$1,000

Item #2
$20,000
10%
$2,000

The system uses this calculation to determine the composite retention percentage: Maximum retention remaining ($2,000) / New Invoice Items Total ($30,000) = Composite Retention Percentage (.066666). The system then updates the work complete retention percentage and work complete retention amounts based on the composite retention percentage.
Retention Amounts After Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
6.67%
$668

Item #2
$20,000
6.66%
$1,332

Item Percentage from Invoice
With this option, the system distributes the final retention amount based on the work complete retainage percent value for each line. The system continues to distribute in this manner until the retention amount is depleted. The system places any leftover amount on one final item on the subcontract, resulting in a calculated retention percentage value for that item only. The system sets the work complete retainage percent to zero for all remaining items on the subcontract.
The tables below display how the system would distribute the retention amount for a subcontract with a maximum retention of $400.
Retention Amounts Prior to Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
10.00%
$300

Item #4
$3,000
10.00%
$300

Retention Amounts After Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
3.33%
$100
* Notice how the remaining amount is added to a single subcontract item.

Item #4
$3,000
0.00%
$0

Setting maximum retention amounts
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)Using SL Subcontract Entry

## Qualified for PBA Reporting?

Qualified for PBA Reporting? checkbox on the SL Subcontract Entry form, PBA tab, Australia only
This checkbox is selected by default if the contract associated with the project/job is flagged as subject to PBA.

When selected, the system will track and report payment activity when you apply payments against subcontracts (SL Subcontract Claims) and include those payment amounts when computing results for the CM PBA Reconciliation report.

## Eligible Date

Eligible Date field on the SL Subcontract Entry form, PBA tab, Australia only
Required only if the Qualified for PBA Reporting? checkbox is selected.

Enter the date when the subcontract qualified as subject to PBA tracking and reporting (not necessarily the subcontract start date).

## Notes

The Notes tab on the SL Subcontract Entry form, header section.
Use this field to enter notes on the subcontract.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
