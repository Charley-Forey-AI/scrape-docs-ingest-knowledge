---
title: "JB Progress Invoice By Bill Group | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/job-billing-reports/job-billing-general-reports/jb-progress-invoice-by-bill-group"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/job-billing-reports/job-billing-general-reports/jb-progress-invoice-by-bill-group"
---

# JB Progress Invoice By Bill Group

You can use the JB Progress Invoice By Bill Group report
 to print an invoice grouped together by the Bill Group entered in JC Contract Items (JCCI)
 by selecting Job Billing > Reports > JB Progress Invoice By Bill
 Group.
This report prints an invoice in landscape orientation, showing quantity, price, and amount information per contract item. Contract items are displayed in groups by Bill Group, assigned in JC Contract Items (JCCI).
 The invoice displays the contract item and description, current contract amount and quantity, UM, job-to-date quantity, unit price, materials on-site, total completed to date, percentage complete, previous amounts, and the amount and quantity currently billed.

You have the option to print contract info notes, set up on the Notes tab of the JB Contract Info form (or on the JB Bill Notes tab of the JC Contracts form). These display under the contract number and description in the report header.

You also have the option to print contract item notes, set up on the Notes tab of the JC Contract Items form. These display under the contract item within the body of the report.

Finally, you have the option to print details of the current invoice tax amount ("Tax This Invoice"). These details display in the totals section at lower right on the invoice, broken out by individual tax codes. Details includes a breakout by single-level member tax codes within any multi-level tax code.
Note: For legacy invoices (created prior to 2022), no tax detail data is available in the system for display. For any such invoice, a single summary value for the current tax amount appears in place of tax details in the totals section, along with an indicator of the unavailability of tax details for that particular invoice.

Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Processing Group (Blank for All)
Select the Field Lookup button or press F4 to select the processing group or leave blank for all.

Beginning Bill Month
Enter beginning bill month (MM/YY) or leave blank for all.

Ending Bill Month
Enter ending bill month (MM/YY) or leave blank for all.

Sort By (B)ill Number or (I)nvoice
Enter B or I.

Beginning Invoice
Select the Field Lookup button or press F4 to select the beginning invoice or leave blank for all.

Ending Invoice
Select the Field Lookup button or press F4 to select the ending Invoice or leave blank for all.

Beginning Bill Number
Select the Field Lookup button or press F4 to select the beginning bill number or leave blank for all.

Ending Bill Number
Select the Field Lookup button or press F4 to select the ending bill number or leave blank for all.

Print Billed Items Only?
Select checkbox to only print billed items.

Print JB Contract Info Notes?
Select checkbox to print notes from JB Contract Info.

Print JC Contract Item Notes?
Select checkbox to print notes from JC Contract Item.

Print Detail for Tax This Invoice?Select checkbox to break out multi-level tax codes into their single-level tax code components. Each single-level tax code prints as a separate "Plus Tax This Invoice" line, and includes the tax code description.
