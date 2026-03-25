---
title: "Field Definitions: PM CO Items Initialize Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form"
---

# Field Definitions: PM CO Items Initialize Form

The following is a list of field descriptions for the PM CO
 Items Initialize form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Beginning/Ending Contract Item

 Enter the beginning and ending item in a range of contract items to initialize as change order items. Leave blank to initialize all contract items as change order items.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Contract Item Start Month

Enter the contract item 'Start Month' by which to restrict initialization. Only contract items with this start month (in JC Contract Items) that meet all other restriction criteria will be initialized as change order items.
Leave blank to include all contract items within the specified range, regardless of start month.

## Contract Item Bill Group

Enter the contract item 'Bill Group' to restrict by. Only contract items assigned this bill group (in JC Contract Items) that meet all other restriction criteria will be initialized as change order items.
Leave blank to include all contract items within the specified range, regardless of bill group.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Include Lump-Sum (LS) Contract Items

Check this box to include contract items (within the specified range) that have a 'LS' unit of measure.
Leave this box unchecked to exclude all contract items (within the specified range) that have a 'LS' unit of measure.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Use Contract Item Descriptions

Check this box to use the contract item's description as the change order item's description.
Leave this box unchecked if you do not want to use contract item descriptions as change order item descriptions. Change order item descriptions will default from the PCO or ACO description.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Set Fixed Price Flag as checked

Enabled only if initializing items for PCO’s where the Int/Ext flag is set to ‘E-External’.
Check this box to set the 'Fixed Amount' flag to Y (checked) for all change order items initialized to the grid.
Leave this box unchecked to set the ‘Fixed Amount’ flag to N (unchecked) for all change order items initialized to the grid.
Note:If you elect to 'include LS contract items' for initialization, the 'Fixed Amount’ flag will be checked for all items, regardless of how you set this flag.

[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Set Generate Detail Flag as checked

Check this box to set the 'Generate Detail' flag to Y (checked) for all change order items initialized to the grid.
Leave this box unchecked to set the ‘Generate Detail’ flag to N (unchecked) for all change order items initialized to the grid.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Calculate Add'l Units/Amount to Equal Billing

Check this box to initialize additional units or amounts for each contract item based on billing values. Additional units and amounts will be calculated based on BilledUnits or Billed Amounts in JCCI (Contract Items), plus UnitsBilled or AmtBilled for non-interfaced billings from JBIT (Bill Items), less ContractUnits or ContractAmt from JCCI.
Leave this box unchecked if you do not want additional units or amounts calculated based on billing values. Additional Units and Amount columns will be set to 0.00.
Note:The Thru Month specified below determines the month through which billings are pulled for calculating additional units/amounts. Calculations will include values posted in months equal to or less than the Thru Month.

[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Positive Additional Units/Amount only

Enabled only if the Calculate Add’l Units/Amount to Equal Billing option is checked above.
Check this box to show only calculations resulting in positive units or amounts in the grid. Calculations resulting in negative units/amounts will be set to 0.00 for the contract item.
Leave this box unchecked to show all calculations in the grid, regardless of whether they are positive or negative values.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

## Thru Month

Enabled only if the Calculate Add’l Units/Amount to Equal Billing option is checked above.
Specify the month through which to pull billings for calculating additional units/amounts. Calculations will include values posted in months equal to or less than this month.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Clear Items/Refresh Items

##  Contract Item

 This column displays all contract items within the specified beginning/ending range that meet restriction criteria.
 If manually adding change order items, specify the contract item for which you are creating a change order item.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Create CO Items/Process CO Items

## CO Item

Enter a number for this change order item, up to 10 characters, or enter ‘+’ to assign the next sequential number available for the change order. You can also leave this field blank and use the ‘Create CO Items’ feature to auto-generate numbers for all items on the change order.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Create CO Items/Process CO Items

## Description

Enter a description of this change order item, up to 60 characters. Initially defaults either the contract item's description (if 'Use Contract Item Description' flag is checked) or the description defined for the pending/approved change order (if 'Use Contract Item Description' flag is unchecked).
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Create CO Items/Process CO Items

## Additional Units

For unit-based items only, specify the additional units for this change order item. This is the number of units by which this item changes the contract item's units. Initially defaults a value based on the following:

- If you checked the Calculate Add'l
 Units/Amount to equal billing box (above), default will be based on
 this contract item's BilledUnits in JCCI (Contract Items), plus UnitsBilled for
 non-interfaced billings from JBIT (Bill Items), less ContractUnits from JCCI. If the
 calculation produced negative units and you checked the Positive Additional
 Units/Amount Only option, default will be 0.00.

- If you did not check the Calculate Add'l
 Units/Amount to equal billing box, or the item is LS, default will be
 0.00. (If LS, field is display only and default cannot be overridden.)

[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Create CO Items/Process CO Items

## Amount

Specify the additional amount for this change order item. This is the amount by which this item changes the contract item's units. Initially defaults a value based on the following:
LS Items

- If using the ‘Calculate Additional Units/Amount to Equal Billing’ option (above), default will be based on this contract item's BilledAmt in JCCI (Contract Items), plus AmtBilled for non-interfaced billings from JBIT (Bill Items), less ContractAmt from JCCI. If the calculation produced a negative amount and you checked the ‘Positive Additional Units/Amount Only’ option, default will be 0.00.

- If not using the ‘Calculate Additional Units/Amount to Equal Billing’ option, default will be 0.00.
Unit-based Items

Defaults an amount based on the units x the unit price. Changes to this amount will cause the unit price to be recalculated.
[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Create CO Items/Process CO Items

## Fixed Amount

Enabled only for PCOs with the ‘I/E’ flag set to E (External).
Check this box to set this item's amount as 'fixed'. The Amount initialized for this change order item will exclude any markup and/or add-on amounts. (Note: This option is automatically checked for all LS items, regardless of how the 'Set Fixed Price…' flag is set in the filter criteria. It is also automatically checked for all items on an 'internal' pending change order.)
Leave this box unchecked if this item's amount is not 'fixed'. The Amount initialized for this change order item will include markup and/or add-on amounts.
Note:This flag defaults as unchecked for all ACO items and is disabled.

[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Create CO Items/Process CO Items

## Generate Detail

Check this box to automatically generate phase detail for this change order item. Phase detail will be generated using the same process used when generating phase detail in [PM Pending Change Orders ](/en/vista/vista/project-management/change-orders/pm-pending-change-orders-form) and [PM Approved Change Orders ](/en/vista/vista/project-management/change-orders/about-the-pm-approved-change-orders-form).
Leave this box unchecked if you want to manually enter or generate phase detail for this change order item.

[](/en/vista/vista/project-management/change-orders/about-the-pm-co-items-initialize-form/field-definitions-pm-co-items-initialize-form#ID-000235c5--en)Create CO Items/Process CO Items

##  Clear Items/Refresh Items/Create CO Items/Process CO Items

 Click the Clear button to clear the grid and start over.
 Click the Refresh button to populate the grid once you have entered filter criteria and set default options. Only contract items meeting the criteria will be added to the grid. You can then enter the appropriate values and edit the flag settings as necessary. You can also delete unwanted items from the grid by highlighting the item, then clicking the Delete button in the toolbar. To clear the grid and start over, click the Clear button.
 Click the Create CO Items button to auto-generate change order items based on the next sequential number available for the change order. When clicked, contract items not already assigned a CO Item and having additional units or amounts (LS) not equal to 0.00, will be assigned the next sequential CO Item.
 Once you are satisfied with the entries in the grid, click the Process CO Items button. This will initialize the change order items and add them to the appropriate change order items grid (i.e. PCO Items or ACO Items).
