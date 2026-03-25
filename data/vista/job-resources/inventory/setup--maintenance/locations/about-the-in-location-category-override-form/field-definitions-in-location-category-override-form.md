---
title: "Field Definitions: IN Location Category Override Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-category-override-form/field-definitions-in-location-category-override-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-category-override-form/field-definitions-in-location-category-override-form"
---

# Field Definitions: IN Location Category Override Form

The following is a list of field descriptions for the IN
 Location Category Override form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location

 Enter the location (from IN Locations) to which these category overrides
 apply.

##  Category

 Enter the material category (from HQ Material Categories) to which these overrides apply.

##  Cost Method

 Entry in this field is only allowed if the Valuation Method (IN Company)
 is not Standard Cost. Specify the cost method for this location/category. If set to ‘No
 Override’, the Cost Method defined for the location in IN Locations will be used.

- 0-No Override

- 1-Average Cost

- 2-Last Cost

- 3-Standard Cost

 The cost method controls how costs are calculated to relieve inventory when materials are sold, produced, adjusted, or transferred from this location.

##  Receivable Type

 Enter the receivable type (from AR Receivable Types) to use when entering
 Material Sales invoices. This type overrides the receivable type specified for the location
 (IN Locations), and should only be used if you need to classify receivables by material
 category.

##  Inventory

 Enter the GL account that will be updated when materials are purchased for, or sold from, this Inventory location and category. This will be the primary asset account for stocked materials in this category at this location. This cannot be a Memo or Heading type account.

##  Adjustments

 Enter the GL account that will be updated when posting manual, physical, or month-end reconciliation adjustments to materials within this category at this location. This cannot be a Memo or Heading type account.

##  Cost of Goods

 Enter the GL account that will be used to track the costs of goods sold. This account is used to offset the credit to Inventory when materials in this category are sold from this location. This cannot be a Memo or Heading type account.

## Cost Variance

Enter the GL account that will be used to
 record the difference between the standard and actual cost of a material when materials are
 posted to Inventory through PO receipts and/or AP invoices. It will also be updated when
 posting materials via MS Ticket Entry if you are using standard costing (i.e. the
 Cost
 Method in IN Location Category Override or IN Company Parameters is
 3-Standard Cost).
Note: The account specified here cannot be a Memo or Heading account.

##  Misc Expense

 Enter the GL account for miscellaneous expenses. This must be an active GL account with a subledger type of 'I' (Inventory) or null. The account entered here will override the Misc GL Account specified in IN Company Parameters or the Misc Expense account specified in IN Location Materials.
 If not using burdened cost, this is the account that will be debited with miscellaneous amounts posted to this location/category in AP.
 If using burdened cost, and you enter freight amounts with the "Inc" flag set to N for the transaction, freight amounts will be credited to this account to offset the charge to inventory.

##  Tax Expense

 This account is only available if you are not using burdened unit cost (the Burdened Unit Cost option in IN Company Parameters is unchecked).
 Enter the GL account to debit with tax amounts posted to Inventory for materials in this location/category in AP. This cannot be a Memo or Heading type account.

##  Cost of Production

 Enter the GL account that will be used to track the cost of raw materials used in the production of finished goods. This account will be debited when a finished good in this category is produced at this location (via IN Production Entry or MS Ticket Entry). This cannot be a Memo or Heading type (in this category) account.

##  Value of Production

 Enter the GL account that will be used to track the value of finished goods. This account will be credited when a finished good in this category is produced at this location (via IN Production Entry or MS Ticket Entry). This cannot be a Memo or Heading type account.

##  Production Qty

 Enter the GL account that will be used to record units of materials within this category that are produced at this location. Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  Sales Revenue

 Specify the GL account to credit with revenue when selling materials in this category to a customer from this location. If using intercompany invoicing (option in MS), the revenue from sales to other companies will also be credited to this account.

##  Sales Qty

 Specify the GL account to credit with units of material within this category sold to customers from this location. If using intercompany invoicing (option in MS), the units sold to other companies will also be credited to this account. Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  Own Equipment: Haul Revenue

 Specify the GL account to credit with haul revenue from materials in this category that are sold to customers from this location and delivered using your own equipment.

##  Own Equipment: Haul Expense

 Specify the GL account to debit with haul expenses of materials in this category that are sold to customers from this location and delivered using your own equipment. This field offsets equipment usage rate in EM. For example, if the usage rate for the haul equipment is $40, but you charge the customer $50, $40 dollars will be debited to this account, and $10 will be credited to the Haul Revenue account for customer sales.
 This cannot be a Memo or Heading type account.

##  Outside Haulers: Haul Revenue

 Specify the GL account to credit with haul revenue from materials in this category that are sold to customers from this location and delivered using an outside haul vendor.

##  Outside Haulers: Haul Expense

 Enter the GL account to debit when an AP transaction is created for the haul expense of materials in this category that are sold to customers from this location and delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

##  Material Expense

 Enter the GL account to debit when an AP transaction is created for the expense of purchased materials within this category that are sold to customers from this location.
Note: Purchased materials are those materials sold from MS that did not come from your inventory.
 This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.
