---
title: "Use Tax Management - Job Cost | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/use-tax-management/use-tax-management---job-cost"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/accounts-payable-procedures/use-tax-management/use-tax-management---job-cost"
---

# Use Tax Management - Job Cost

The Job Cost Installation >  Properties > Utilize tax classification checkbox. If use tax tracking is not needed, do not select this checkbox.
 Job File Maintenance will then reflect the A/R sales tax
 codes.
Tax
 Classification File Maintenance – If the Utilize tax
 classification checkbox is selected, complete the Tax class
 code field in Job File Maintenance >  Properties.
In Tax Classification
 Maintenance, set up the tax classification codes. The tax class code has
 both the A/R sales tax code and the A/P tax codes, either sales or use. The A/P
 Invoice Tax Overrides window is used to set taxable status by cost type,
 with exceptions being noted by phases (for example, M = not taxable, materials would not be
 taxable except for phases listed in the window). If no items are exempt, no exemptions need
 to be listed here. Text entered in the Tax
 Instructions field on the Tax Classification File
 Maintenance screen (for example, Materials have been taxed) will show on
 the Accounts Receivable > Draw Request Billing Entry > Summary Billing Entry screen under the Tax code field and it will print on
 the first screen of the draw request. This field is not required.
Purchase orders and invoices entered against the job will use this file to determine tax codes to be used. If there are multiple tax codes that apply to be particular job, the different rates must be manually entered in invoice entry.
