---
title: "Field Definitions: MS Quote Close Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quote-close--purge-form/field-definitions-ms-quote-close-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quote-close--purge-form/field-definitions-ms-quote-close-purge-form"
---

# Field Definitions: MS Quote Close Purge Form

The following is a list of field descriptions for the MS
 Quote Close Purge form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Restrict Based on Quote Type & Purchaser

Check this box to limit the quotes that display in the grid based on the quote type and purchaser.
Do not check this box if you want all quote displayed in the grid, regardless of quote type and purchaser.

##  Quote Type

 Specify the type of quote to restrict by. Once you select the quote type, corresponding fields for entering purchaser information display.

##  Customer

 For Customer quotes only.
 Specify the customer (from AR Customers) to restrict by. Only quotes set up for this customer that meet all other selection criteria will display in the grid below. If this field is blank, all customer type quotes display in the grid below.

##  Cust Job

 For Customer quotes only.
 Specify the customer job (up to 20 characters) to restrict by. Press F4 for a list of job quotes for this customer. Only quotes set up for this customer/customer job that meet all other selection criteria display in the grid below. If this field is blank, all quotes for the customer indicated above display in the grid, regardless of job.

##  Cust PO#

 For Customer quotes only.
 Specify the customer PO# (up to 20 characters) to restrict by. Press F4 for a list of customer job PO quotes for this customer. Only quotes set up for this customer/customer PO that meet all other selection criteria display in the grid below. If this field is blank, all quotes for the customer or customer/customer job indicated above is display in the grid, regardless of PO#.

##  JC Co#

 For Job quotes only.
 Specify the JC company to restrict by. Only quotes set up for this JC company will display in the grid below. If this field is blank, all Job type quotes display in the grid.

##  Job

 For
 Job quotes only.
 Specify the job (from JC Jobs) to restrict
 by. Only quotes set up for this JC company and job display in the grid below. If this field
 is blank, all quotes for the JC company indicated above display in the grid, regardless of
 job.

##  IN Co#

 For Inventory quotes only.
 Specify the IN company to restrict by. Only quotes set up for this IN company display in the grid below. If this field is blank, all Inventory type quotes display in the grid.

##  To Location

 For Inventory quotes only.
 Specify the ‘To’ location (from IN Locations)
 to restrict by. Only quotes set up for this Inventory company and ‘To’ location display in
 the grid below. If this field is blank, all quotes for the IN company indicated above
 display in the grid, regardless of ‘to’ location.

##  Include Quotes Expired On or Before:

 Enter the expiration date for restricting the display of quotes in the grid. All quotes with an expiration date that falls on or before this date display in the grid below. Quotes without an expiration date do not display in the grid.
 If this field is blank, all quotes display, regardless of expiration date. This includes quotes without an expiration date.

##  Display Active Quotes Only

 Check this box to include active quotes in the grid. Only quotes with the Active flag checked display in the grid below.
 Do not check this box if all quotes, active and inactive, should display in the grid.

##  Close

The Close checkbox on the MS Quote Close & Purge form, Quote Close and Purge grid.
 Select this checkbox to close this quote when the close/purge process runs. The Quote’s status will change to “Inactive”, but all detail, defaults, and override information will remain on file.
Note: If you close a quote accidentally, reopen it in MS Quotes by selecting the Active checkbox.

##  Purge

The Purge checkbox on the MS Quote Close & Purge form, Quote Close and Purge grid.
 Select this check box to purge this quote. Purging completely removes the quote from the system.
Note: Before implementing the purge process, verify each selected quote. Once the system purges a quote, you cannot recover it!
