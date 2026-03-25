---
title: "AR Sales Tax Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/accounts-receivable-reports/accounts-receivable-general-reports/ar-sales-tax-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/accounts-receivable-reports/accounts-receivable-general-reports/ar-sales-tax-report"
---

# AR Sales Tax Report

You can use the AR Sales Tax Report report for a report of
 tax incurred by the "Base" code (typically the state code). You can access this report by
 selecting Accounts Receivable > Reports > AR Sales Tax Report.
The AR Sales Tax Report is a report of tax incurred by the "Base" code (typically the state code). When the Base code is a multi-level code, the report provides a separate recap of each "Local" code (typically city, county, or other codes that combine to produce the "Base" code tax rate). The calculated tax is the total of the tax code rate for either the Base code or all corresponding Local codes multiplied by the tax basis on the transaction. Please be aware that the "Base" rate is entered into AR entry programs and is a stored column, and that "local" rates are only maintained in HQ Tax Codes. Therefore, the rate used in the Calculated Tax column depends on how tax links are set at runtime for multi-level codes. If tax links/rates are changed, this report will no longer match the rate calculated in the entry program. The report will use either the old or new rate based on the effective date in HQ Tax Codes. Also, the Calculated Tax may differ from the Actual Tax when the tax amount field in AR Invoice Entry is overridden.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Beginning Tax Code
Click the Field Lookup
 button or press F4 to select the beginning tax code

Ending Tax Code
Click the Field Lookup
 button or press F4 to select the ending tax code

Beginning Month
Select the date-range arrows to select the Beginning Month

Ending Month
Select the date-range arrows to select the Ending Month

Print Transaction Level Detail?
Check the box to Print Transaction Level
 Detail

Page After Each Base Tax Code?
Check the box to insert Page After Each Base Tax
 Code

Include Tax Discounts?
Check the box to Include Tax Discounts

Print Lines with no Tax Code?
Check the box to Print Notes
