---
title: "Field Definitions: EM Cost Adjustments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-cost-adjustments-form/field-definitions-em-cost-adjustments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-cost-adjustments-form/field-definitions-em-cost-adjustments-form"
---

# Field Definitions: EM Cost Adjustments Form

The following is a list of field descriptions for the EM Cost
 Adjustments form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter ‘N’, ‘New’, or ‘+’ to add a new sequence. The system will automatically assign the next available sequence number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## EM Type

Select the transaction type of the cost adjustment entry. The selection determines which fields on the form are enabled.
You must enter Equip and WO type transactions directly in EM Cost Adjustments. The remaining types (Depn, Fuel, Parts, and Alloc) will generally be initialized in the forms specific to those types (EM Depreciation Processing, EM Fuel Posting, EM WO Parts Posting, and EM Process Cost Allocation); however, you can enter these types directly in this form.

- Equipment
 - Use to post cost adjustments to equipment.

- Work Order
 - Use to post cost adjustments to work orders.

- Depreciation
 - Automatically assigned to transactions posted in EM Depreciation Posting; however, you can enter transactions directly in this program that use this type.

- Fuel
 - Automatically assigned to transactions posted in EM Fuel Posting form; however, you can enter transactions directly in this program that use this type.

- Parts
 - Automatically assigned to transactions posted in EM WO Parts Posting form; however, you can enter transactions directly in this program that use this type.

- Allocations
 - Automatically assigned to transactions posted in EM Process Allocations; however, you can enter transactions directly in this program that use this type.

##  Date

 Specify the date to assign as the ‘actual’ date for this adjustment. May update the equipment's odometer and/or hour meter reading dates (in EM Equipment) depending on the update option selected for cost adjustments in EM Company Parameters.
Note: Most tables updated by cost adjustment batches have
 both an ‘Actual’ date and a ‘Posted’ date (the date entered in the Batch Processing form).
 If you want to report the actual date of the adjustment, enter that date here.

## Work Order

Enter the work order that the cost adjustment
 applies to or press F4 to select one from a list.
 This field is only enabled when Work Order is
 selected in the EM
 Type field.

##  WO Item

 This field is only accessible for Work Order type entries.
 Enter the WO item number. If you specify an item with a ‘Final’ status, a message displays warning you that the item’s status is ‘Final’. Entry will only be allowed if you specified to allow posting costs to ‘final’ status items (flag in EM Company Parameters, Work Orders tab).

##  Equipment

 This field disabled for Work Order type entries.
 Specify the piece of equipment (from EM Equipment) to which this cost adjustment applies.

##  Comp Type

 This field disabled for Work Order and Depreciation type entries, or for non-Work Order/Depreciation entries where the equipment’s Post to Components flag is unchecked (in EM Equipment).
 Enter a component type, if applicable. Entry here provides a default component code (next field) based on the first component of that type for the equipment. However, you may skip this field and enter the component code directly. Once you enter the component code, the component type defaults automatically.

##  Component

 This field disabled for Work Order
 and Depreciation type entries, or for non-Work Order/Depreciation entries where the
 equipment’s Post to Components flag is unchecked (in EM Equipment).
 Enter the component to which this cost
 adjustment applies. If you entered a component type in the previous field, initially
 defaults the first component (of the component type) set up for the equipment in EM
 Equipment.

##  Asset

 This field is accessible for ‘Depreciation’
 entries only (EM
 Type is set to Depn - Depreciation in EM Cost
 Adjustments).
 Enter the asset to which this depreciation cost adjustment applies. The asset must be valid for the specified equipment. If you processed depreciation using EM Depreciation Processing, this field defaults to the asset number assigned to the equipment in EM Asset Setup.

##  Cost Code

 Enter the cost code for this cost adjustment. If you specified a component for this transaction, defaults the cost code assigned to the component type (in EM Component Types).
 For Work Order adjustments, this field is only accessible if you have checked the Allow Cost Code Change option for Work Orders in EM Company Parameters.

##  Cost Type

 Enter the EM cost type for this cost adjustment.

##  IN Co

 This field disabled for Depreciation type entries.
 If you are entering parts for this cost adjustment and the specified parts are 'stocked', enter the IN Co supplying the parts.

##  IN Loc

 This field disabled for Depreciation type entries.
 If you are entering parts for this cost adjustment and the parts are ‘stocked’, enter the location supplying the part.

##  Part Code

 Enter the part code that applies to the
 adjustment or press F4 to select one from a list.
If the Validate Parts/Materials box on the Parts
 tab of [EM Company Parameters ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form) is checked, the part must be a valid
 HQ material, vendor part, or an equipment part cross-referenced to a valid HQ material. (If
 the part code is referenced to an HQ material, the program will use the HQ material number
 and validate the unit of measure from either HQ Materials or from IN Location.)
 If you are not validating parts, any part code may be used, as long as you did not specified an Inventory location in the previous field; otherwise, the part must be a valid material set up for the location in IN Location Materials, regardless of how you set the Validate Parts option.
Note: This field disabled when Depreciation is selected in
 the EM
 Type field.

## Description

Enter a description of the adjustment transaction. The description can be up to 60 characters long.
 If you selected a part code in the Part Code
 field, this field populated with the description of the part in [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form).

##  Trans Acct

 Required.
 Specify the GL account to debit (positive cost) or credit (negative cost) for this adjustment. The account must be valid (set up in GL Charts of Accounts) and have a subledger code of ‘E’ (equipment) or blank.
 This field initially defaults the cost type GL account (specified in EM Departments) or the cost code GL account (if an override is set up for cost code in EM Departments). You can only override the default account if you have specified to allow GL account overrides (option in EM Company Parameters).

## Offset Acct

Specify the GL account (from GL Chart of Accounts) to credit for this
 adjustment transaction. For adjustments that do not reference a part/material, this account
 must have a sub ledger code of E-Equipment or blank (null) . For adjustments that do
 reference a part/material, the account must have a sub ledger code of blank (null).
This field initially defaults as follows:

-  If you specified a non-stocked material for this adjustment, defaults the Non-Stocked GL Account designated for the material in HQ Material Categories.

-  If you specified a stocked material, defaults the
 Equipment Sales account designated for the specified location in IN Locations.

- If posting miscellaneous parts/materials (not set up
 in HQ) and you are not validating materials (Validate Parts/Materials box is
 unchecked), defaults the Misc Parts GL Acct specified in EM Company Parameters.

Note: This account offsets the transaction account specified
 in the previous field. You will only need to enter an account here if you are posting
 additional costs or making an accrual or reversal entry for this transaction.

##  Units

 Enter the number of units to adjust. Enter negative units with a minus sign (e.g. –150.00).
Note: If the unit of measure is LS, this field defaults as
 0.00 and is disabled.

##  UM

 Enter the unit of measure for this cost
 adjustment or press F4 to select one from a list. Enter LS if the adjustment is for dollars only
 (i.e. no units).
If you entered a part code, this field defaults the unit measure set up on the part in the [HQ Materials ](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form) form.
If you entered a non-stocked material, you must manually enter the unit of measure.

##  Unit Price

 Enter the unit price for this adjustment. If you entered a part code, defaults the unit price specified for the part (material) in HQ Materials. If you specify a stocked material, unit price defaults from IN Location Materials based on the pricing option specified for ‘Equip Sales’ in IN Company Parameters and the markup/discount rate for Equipment in IN Location Materials (Costs/Qtys tab).

##  Cost Amount

 Enter the adjustment amount. Initially defaults an amount based on Units x Unit Price. Enter negative amounts with a minus sign (e.g. –150.00).

##  Tax Code

 This field is only accessible if the Use Tax on Materials option is checked EM Company Parameters (Parts tab).
 Enter the tax code for this cost adjustment. If you entered a stocked part and the part is taxable (flag in HQ Materials), defaults the location’s tax code, if one is specified. Otherwise, defaults as null.
Note: The system computes the use tax amount when you
 process the batch.

##  Tax Basis

 This field is only accessible if the Use Tax on Materials option is checked EM Company Parameters (Parts tab).
 Enter the tax basis for this cost adjustment. Initially defaults from the transaction’s Cost amount (previous field). You should only need to change this if the tax basis is different from the Cost amount.
 If the EM Type is ‘Fuel’, this field defaults as 0.00. You may override the default as necessary.

##  Odometer

 Enter the equipment’s current
 odometer reading. Entry here updates the odometer reading in EM Equipment (based on the
 update option for cost adjustments in EM Company Parameters), and creates a Meter History
 (EMMR) record.
Note: If you enter 0.00 or set reading to NULL (blank), no
 update to EMMR (Meter Readings) or EMEM (Equipment) will occur.

##  Hours

 Enter the equipment’s current hour
 meter reading. Entry here updates the current hour meter reading in EM Equipment (based on
 the update option for cost adjustments in EM Company Parameters), and creates a Meter
 History record.
Note: If you enter 0.00 or set reading to NULL, no update to
 EMMR (Meter Readings) or EMEM (Equipment) will occur.

##  Serial #

 If applicable, enter the serial number (up to 20 characters) of the specified part. This number is stored in the Cost Detail file (EMCD).

##  Reversal

 Specify the reversal type for this cost adjustment.
New Transactions

- 0-Regular – Select this type for transactions that do not require reversal. If using this type, you must enter an offset account or a balancing entry.

- 1-Auto Reverse – Select this type for transactions you expect to reverse in a later month (using EM Initialize Reversals).
Initialized Reversal Transactions

- 2-Reversal – System assigned, this type applies to reversal transactions created using EM Initialize Reversals. If you do not want a transaction reversed, set it to type ‘4’ (Cancel Reversal).

- 3-Reversed – System assigned, this type applies to processed reversal transactions.

- 4-Cancel Reversal – Select this option to cancel a reversal transaction (type ‘2’).

Note: After you process a reversal batch, reversals are set to ‘3’ and cancelled reversals retain a type of ‘4’. You cannot change or delete these types (or pull them back into a batch).
