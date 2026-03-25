---
title: "SM Tax Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-tax-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/service-management-reports/service-management-general-reports/sm-tax-report"
---

# SM Tax Report

You can use the SM Tax report to show tax information for Service Management transactions by selecting Service Management > Reports > SM Tax Report.

This report shows cost-related tax information (Sales, Use, and VAT) for transactions associated with SM work orders (work completed line types 3-Misc, 4-Inventory, and 5-Purchase only). It does not show bill-related tax information.

For Sales and VAT tax, the report displays data from the AP invoice line (APTL) for work completed 3-Misc lines posted via AP Transaction Entry or AP Unapproved Invoice Posting, and for 5-Purchase lines (entered in SM Purchase Order Entry or PO Purchase Order Entry), as long as an AP invoice has been posted against the PO. For Miscellaneous lines entered directly in SM Work Orders (Work Completed grid), Sales and VAT tax information is pulled from the SMWorkCompleted table.

Note: Inventory lines allow for Use tax only; they do not allow Sales tax or VAT.

For Use tax, the report acquires data from the SMDetailTransaction table for any work completed 3-Misc, 4-Inventory, or 5-Purchase lines.

For each transaction detail record, the report presents the tax basis, posted tax amount, tax rate, and a 'recalculated' tax amount representing the tax basis multiplied by the tax rate.

For any transaction using a multi-level tax code, the report shows a transaction detail record for each single-level-member tax code. The system does not store the tax amount for each single-level member of the multi-level tax code; therefore, the posted Tax Amount is informational only and represents, for each single-level-member tax code, the combined total across all single-level members of the multi-level tax code. The Rate x Basis shows how much the tax should be. The rate is based on effective date for the current and a single previous rate.
You can print the report for specific sources of transactions or for all. Sources with tax include AP, IN, PO, and MI. If AP transactions are included, they will be duplicates of the same transactions shown on the AP Tax Report.
Report Parameters
Description
SM Company
Accept the default, or press F4 to select a company.

Month From Enter or select the applicable beginning month.

Month ToEnter or select the applicable ending month.

Tax Code FromEnter the beginning tax code or press F4 to select a tax code.
Tax Code ToEnter the ending tax code or press F4 to select a tax code.
Work Order FromEnter or select the applicable beginning work order.

Work Order ToEnter or select the applicable ending work order.

Show (S)ales, (U)se, (V)AT, or (A)ll taxesSelect S to show sales tax only, U to show use tax only, V to show VAT tax only, or A to show all taxes.
New Page for each Tax Code?Select this checkbox to start a new page for each tax code. If not selected, each page may contain multiple tax codes.
Transaction Types? (AP, PO, IN, MI)Enter the transaction types to include in report, separated by a comma (for example, AP,IN). Leave blank to include all transaction types.
