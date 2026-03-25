---
title: "About Default Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/change-orders/about-processing-co-items/about-default-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/change-orders/about-processing-co-items/about-default-options"
---

# About Default Options

The Default options in the PM CO Items Initialize form are used to define the contract items you
 wish to initialize as change order items.
You can specify a range of contract items or
 leave blank to include all items on the contract. Other options allow for restricting
 contract items based on the contract item's start month and/or assigned bill group. You
 can also specify to include/exclude contract items with a lump sum (LS) unit of
 measure.
The Default options allow you to auto-set
 change order items with specific data.

- Use Contract Item Descriptions –
 This option allows you to specify the default description for each initialized
 change order item. If checked, the contract item description is used. If
 unchecked, the PCO or ACO change order description is used (depending on whether
 initializing PCO or ACO items).

- Set Fixed Price Flag as Checked – This option
 applies to PCO items only, and is used to auto-set the Fixed
 Amount box to checked or unchecked for each change order item.
 This flag determines whether the amount of the change order item will be a fixed
 amount (which excludes any markup/add-on amounts) or whether the amount will
 include markup and/or add-on amounts.

Note: Because markup/add-on amounts are not used on approved
 change orders, both this option and the Fixed Amount column (Grid & Info
 tabs) are disabled and unchecked when initializing items for approved change orders.

- Set Generate Detail Flag as
 Checked – This option allows you to auto-set the Generate
 Detail box (Grid & Info tabs) to checked or unchecked
 for each item. The Generate Detail checkbox
 determines whether or not phase/cost type detail will be auto-generated for
 each change order item initialized.

- Calculate Additional
 Units/Amount to Equal Billing – This option allows you to calculate
 additional units/dollars for change order items based on billed values. If
 checked, additional units or amounts (if LS) will be calculated for each
 contract item based on the BilledUnits or BilledAmt in JCCI (Contract
 Items), plus UnitsBilled or AmtBilled for non-interfaced billings from JBIT
 (Bill Items), less ContractUnits or ContractAmt in JCCI. If unchecked,
 Additional Units and Additional Amounts columns will be set to 0.00.

Note: Use the Thru Month below to specify the month
 through which to pull billings for calculating additional units/amounts. Calculations
 will include values posted in months equal to or less than this month.

- Positive Additional Units/Amount Only – This
 option is only enabled if you checked the Calculate
 Add'l Units/Amount to equal billing option above. If
 checked, only calculations resulting in positive units or amounts will be
 shown in grid. Calculations resulting in negative units/amounts will be set
 to 0.00 for the contract item. If unchecked, all calculations will be shown
 in the grid, regardless of whether they are positive or negative values.
