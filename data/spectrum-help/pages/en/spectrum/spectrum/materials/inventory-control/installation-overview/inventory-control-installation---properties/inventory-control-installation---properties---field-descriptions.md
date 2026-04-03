---
title: "Inventory Control Installation - Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/installation-overview/inventory-control-installation---properties/inventory-control-installation---properties---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/installation-overview/inventory-control-installation---properties/inventory-control-installation---properties---field-descriptions"
---

# Inventory Control Installation - Properties - Field
 Descriptions

Use the table below for reference when completing the
 fields on this screen.
Field/Button
Description

Transfer job costs with actual costs?
The system is prompting for you to decide whether to
 update actual cost to Job Cost files through Job Requisition Entry or using
 standard cost. If this checkbox is selected, then actual cost, plus any
 mark-up, will be charged to jobs when requisitions are updated. "Actual
 cost" will be determined based on the costing method designated for the
 category of the particular item (FIFO, LIFO or Average Cost). If this check
 box is blank, then current standard cost, plus any mark-up, will be updated
 to Job Cost module. The system will determine costing method at the time of
 update, based on the current entry in this field; this field may be revised
 at any time if a different method of transferring cost is desired. The 'use
 tax', if any, will always be based on the actual cost, regardless of entry
 in this field.

Validate item location?
Select this checkbox if you want to require that the
 location of the item specified in the Item Detail File Maintenance screen is
 equal to a valid location in the location file. If this checkbox is
 selected, the software will confirm that the item location is in Item
 Location File Maintenance.
 If this checkbox is left clear, then the software won't
 confirm that the item location is in Item Location File Maintenance.

Multi-company requisitions?
Select this checkbox to have the option to enter job
 requisitions for jobs in another company on the Spectrum system. The company
 id will display on the Job Requisition Entry screen header, and may be
 changed to another company id. This will expense those requisition lines to
 the company indicated; when updated, the software will post those expenses
 to the corresponding General Ledger and Job Cost for the company indicated.
 The corresponding credit will be posted where you have indicated in the
 Inter-company G/L accountcode field found on the G/L Codes tab. Selecting
 this checkbox will also allow multi-company requisitions to be created from
 the Materials Management and Equipment Tracking modules.
Note: If this option is selected, the
 Inter-company G/L account code field must be completed on the G/L Codes tab.
If this checkbox is left clear, requisitions cannot be
 entered for jobs in another company on the Spectrum system.

Post requisition to General Ledger as internal job
 sale?
Select this checkbox to control how the Inventory
 Transaction Update will post job requisitions to G/L. This affects how
 Spectrum posts to G/L from all entities in the current company.

One warehouse?
Select this checkbox if you have only one warehouse and
 want the software to skip past the warehouse code prompt throughout
 Spectrum.
If this checkbox is left clear, the software will prompt
 the operator for the warehouse code when applicable. This prompt may be
 changed at any time if, for example, the company adds a second warehouse to
 the operations.

Default warehouse
Enter the code of the default principal warehouse, or
 double-click in this field to search for warehouse codes already entered in
 the software. Even if there is just one warehouse in this company, it is
 necessary to designate this code here and in Warehouse File Maintenance.
 Typically, this code is defined as warehouse 1, but the code may be
 alphabetic or numeric, as desired.
 This warehouse code will appear throughout Spectrum,
 wherever a warehouse code is required during entry. This installation
 setting can be changed at any time if, for example, the company reorganizes
 warehouse operations and selects a new warehouse for default purposes.
 Warehouse codes may be up to 10 characters long.

Next transaction sequence number
Enter the next inventory transaction sequence number the
 software should assign during inventory transaction processing data entry.
 Spectrum features auto-count transaction numbers for ease of entry.
 Otherwise, the operator may specify a desired transaction sequence number
 when adding receipts, returns, transfers and adjustments. We recommend that
 this number be initialized at a meaningful point for the company. For
 example, you might choose "01006" for the first transaction in 2006, or
 simply "100" if it's easier. If you are already utilizing the Inventory
 Control module, the most recently used transaction sequence number will
 display, and can be changed as needed. This number is updated automatically
 as part of inventory transaction processing, and will be offered as the next
 highest number as a default the next time you enter transactions.

Next requisition sequence number
Enter the next inventory requisition sequence number the
 software should assign during Job Requisition Entry. Spectrum features
 auto-count job requisition numbers for ease of entry. We recommend that this
 number be initialized at a meaningful point for the company. For example,
 you might choose "01006" for the first transaction in 2006, or simply "100"
 if it's easier.
If you are already utilizing the Inventory Control
 module, the most recently used requisition sequence number displays and can
 be changed as needed. This number is updated automatically as part of
 requisition processing, and will be offered as the next highest number as a
 default the next time you enter requisitions.

Default costing method
Select one of the following option buttons, depending on
 the default costing method you want to use in your Inventory Control module:

- FIFO
 (first in first out) - removes from inventory the
 oldest stock on hand first

- LIFO
 (last in first out) - relieves the most recently
 received stock on hand first

- Average Cost - provides a continuously updated average
 value of stock on hand

- Standard cost

The option you select will serve as a default when future
 categories are added. Any entry in this field will have no effect on
 existing category costing methods; desired changes to existing costing
 methods must be done in Category File Maintenance.
You can utilize different costing methods category by
 category, but as a practical matter, most companies select a single method.
 Consult your accountant for further inventory costing information.

Update standard cost
Select one of the following option buttons, depending on
 whether you want the software to update the standard cost figure in
 Inventory Item File Maintenance based on entries during inventory receipts
 processing:

- Yes. When the unit item is received, the unit cost of
 the item will be recorded as the new standard cost in Inventory Item
 File Maintenance. If entering inventory receipts directly in Inventory
 Control, this option will always update standard cost for inventory
 receipts.

- No. When the unit item is received, there will be no
 change made to the standard cost figure in Inventory Item File
 Maintenance as a result of receipts activity. Additionally, you may
 want to select this option to update standard cost when packing lists
 are updated to Inventory Control as part of two-step purchase order
 processing. If entering inventory receipts directly in Inventory
 Control, this option will never update.

- Update inventory receipts only. When the item is
 received, the standard cost will only be updated from Inventory
 Receipts Entry when the unit cost of the item received is lower than
 the current standard cost in Inventory Item File Maintenance. The
 standard cost is set when inventory receipts are updated using
 Inventory Transaction Update. If entering inventory receipts directly
 in Inventory Control, this setting will only update if the new
 received unit cost is lower than the current standard cost.
Note: This option will not be
 applicable for items configured to use the Standard cost costing
 method.

Quantity price break
Select one of the following option buttons, depending on
 the default quantity price break you want to use throughout the Inventory
 Control module.
Note: The system uses this option only when
 Order Processing module is utilized. If Order Processing module is not
 present in this company, entry in this field is irrelevant.

- List
 price - select this option if the price quantity breaks
 should be based on the list price of items

- Sell
 price - select this option if the quantity breaks
 should be based on the sell price of items
