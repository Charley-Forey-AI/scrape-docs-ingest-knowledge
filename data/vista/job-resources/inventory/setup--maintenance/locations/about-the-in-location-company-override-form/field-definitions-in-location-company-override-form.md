---
title: "Field Definitions: IN Location Company Override Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-company-override-form/field-definitions-in-location-company-override-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-location-company-override-form/field-definitions-in-location-company-override-form"
---

# Field Definitions: IN Location Company Override Form

The following is a list of field descriptions for the IN
 Location Company Override form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location

 Specify the location (from IN Locations) to set up override GL accounts
 for sales, haul revenue, and haul expense. This will be the location (in the currently
 active company) the materials will be sold from.

##  Company

 Specify the company that applies to the GL account override. This will be the company to which the materials are being sold.

##  Revenue: Job Sales

 Enter the GL account used to record revenue when selling materials from this location to jobs within the company specified above. This cannot be a Memo or Heading type account.

##  Revenue: Inventory Sales

 Enter the GL account used to record revenue when selling materials from this location to other Inventory locations within the company specified above. This cannot be a Memo or Heading type account.

## Revenue: Equipment Sales

Enter the GL account used to record revenue when selling materials to equipment from this location. This cannot be a Memo or Heading type account, and the subledger code must be 'I-Inventory' or blank (Null).

##  Quantity: Job Sales

 Enter the GL account that will be used to record units sold from this location to jobs within the company specified above. Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  Quantity: Inventory Sales

 Enter the GL account that will be used to record units sold from this location to other inventory locations within the company specified above.This may include component materials used in production if their source location differs from the production location, and if the Usage Option (IN Company Parameters) is set to Sales.Only materials flagged to “Update Units Produced or Sold to GL” (in IN Location Materials) will be included. This must be a Memo type account.

##  Own Equipment: Job Sales

 Enter the GL account to credit with haul revenue from sales to jobs within the company specified above that were delivered using your own equipment. This cannot be a Memo or Heading type account.

##  Own Equipment: Inventory Sales

 Enter the GL account to credit with haul revenue from sales to Inventory locations within the company specified above that were delivered using your own equipment. This cannot be a Memo or Heading type account.

##  Outside Haulers: Job Sales

 Enter the GL account to credit with haul revenue from sales to jobs within the company specified above that were delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

##  Outside Haulers: Inventory Sales

 Enter the GL account to credit with haul revenue from sales to Inventory locations within the company specified above that were delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

##  Own Equipment: Job Sales

 Enter the GL account to debit with haul expense from sales to jobs within the company specified above that were delivered using your own equipment. This field offsets equipment usage rate in EM. For example, if the usage rate for the haul equipment is $40, but you charge the job $50, $40 dollars will be debited to this account, and $10 will be credited to the Haul Revenue account.
 This cannot be a Memo or Heading type account.

##  Own Equipment: Inventory Sales

 Enter the GL account to debit with haul expense from sales to Inventory locations within in the company specified above that were delivered using your own equipment. This field Offsets equipment usage rate in EM. For example, if the usage rate for the haul equipment is $40, but you charge the inventory location $50, $40 dollars will be debited to this account, and $10 will be credited to the Haul Revenue account.
 This cannot be a Memo or Heading type account.

##  Outside Haulers: Job Sales

 Enter the GL account to debit when an AP transaction is created for the haul expense of materials sold to jobs within the company specified above that were delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

##  Outside Haulers: Inventory Sales

 Enter the GL account to debit when an AP transaction is created for the haul expense of materials sold to Inventory locations within the company specified above that were delivered using an outside haul vendor. This cannot be a Memo or Heading type account.

##  Material Expense: Job Sales

 Enter the GL account to debit when an AP transaction is created for the expense of purchased materials sold to a job within the company specified above.
Note: Purchased materials are those materials sold from MS that did not come from your inventory.
 This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.

##  Material Expense: Inventory Sales

 Enter the GL account to debit when an AP transaction is created for the expense of purchased materials sold to inventory locations within the company specified above.
Note: Purchased materials are those materials sold from MS that did not come from your inventory.
 This cannot be a Memo or Heading type account, and subledger type must be 'I' or null.
