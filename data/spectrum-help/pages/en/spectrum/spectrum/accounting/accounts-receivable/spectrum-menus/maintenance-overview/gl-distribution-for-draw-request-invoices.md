---
title: "G/L Distribution for Draw Request Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/gl-distribution-for-draw-request-invoices"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/gl-distribution-for-draw-request-invoices"
---

# G/L Distribution for Draw Request Invoices

This window allows for the distribution by G/L account code (and cost center, if applicable) for each contract when posting A/R draw requests to A/R invoices. This feature is similar to the G/L distribution available in Vendor File Maintenance. If the G/L distribution table is specified in Contract Maintenance, this allocation will replace the detail draw request billing by billing item, and remove the need for G/L codes (and cost center specification) in the contract billing item detail.
Because billing items are generally established by the customer and do not necessarily correspond to their organization's desired accounting allocation. Many Spectrum users work around this issue by splitting billing items out into sub-billing items and then summarizing these items for the owner (customer). For example, if the contract indicates an allocation of 40% to the Construction Revenue G/L account, 35% to Service Revenue, and 25% to Transportation Revenue, this allocation will be used during Update Draws to Invoice Entry--regardless of the Contract Maintenance revenue G/L account, G/L accounts assigned to individual billing items, and items that are being billed on the current application.
Field
Description

Allocate draw request revenue among multiple G/L accounts?
Select this checkbox to distribute the draw request to invoice based on G/L account codes. If this checkbox is selected, then a list box for the G/L distribution displays. Note that once you select this checkbox, you will not be able to enter G/L codes on specific billing items.
Click the New button and enter the fields below to create a new draw request allocation.

G/L account
Enter the General Ledger account code for revenue distribution, or double-click on this field.

Cost center
Enter the applicable cost center that is associated with the G/L code. Spectrum will verify that you have permission to access any cost groups/cost centers selected before proceeding.
Note: This field displays only if the Enterprise Installation screen's Use cost centers option is set to Yes or Pending in this company.

Invoice description
Enter a brief description about the invoice.

Distribution %
Enter the percent of the revenue that will be distributed to the selected G/L account. The sum of all percents included in this window must equal 100%.
