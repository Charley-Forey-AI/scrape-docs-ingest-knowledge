---
title: "HQ BAS GST Reconciliation Drilldown | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/headquarters-reports/headquarters-australia-specific-reports/hq-bas-gst-reconciliation-drilldown"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/headquarters-reports/headquarters-australia-specific-reports/hq-bas-gst-reconciliation-drilldown"
---

# HQ BAS GST Reconciliation Drilldown

You can use the HQ BAS GST Reconciliation Drilldown report
 to facilitate verification of GST-related summary amounts reportable on the Business
 Activity Statement. To access this report, select Headquarters > Reports > HQ BAS GST Reconciliation
 Drilldown.
The purpose of this drilldown report is to facilitate verification of GST-related summary amounts reportable on the Business Activity Statement, as recorded on the GST/PAYG Amounts tab of the HQ BAS Process form.
This report summarizes sales, purchase, and GST amounts from transactions in AP, AR, and CM, and compares the resulting totals to summary amounts reportable on the BAS. Any differences are noted as variances. A variance may occur if summary amounts recorded on the HQ BAS Process form are out-of-date as a result of more recent transaction activity in AP, AR, or CM, or if those summary amounts were edited manually on the HQ BAS Process form subsequent to generation by the system.
Inputs for the report are Company, Tax Year, and Sequence, all required. The reporting period is defined by Start Month and End Month values designated on the Info tab of the HQ BAS Process form for the BAS sequence specified by your input values.
For each GST Item -- BAS labels G1, G2, G3, G10, and G11 -- the report calculates three sums from current transaction data: total sales or purchase amount exclusive of GST, total GST amount, and total sales or purchase amount inclusive of GST. Only transactions in CM or transaction lines in AP or AR, whose tax codes are mapped to a GST Item on the GST Tax Codes tab of the HQ BAS Process form contribute amounts to these totals. Transactions whose posted month is within the reporting period are included and evaluated in the report. Additionally, the report includes and evaluates any retention-type AP sequence whose paid month is within the reporting period, whether or not its posted month also falls within the period. Retention amounts and related GST, both in AP and AR, are included in the totals calculated by the report only if the retention was released -- and in the case of AP, also paid -- within the reporting period.
Level 1 of the drilldown displays totals by GST Item, summarized from transaction data within the reporting period; parallel summary amounts as recorded on the HQ BAS Process form; and any variances between the two.
Upon drilling into a specific GST Item, Level 2 displays the AP, AR, and CM transactions that contribute to the totals for that GST Item within the reporting period. Transactions are grouped by Source, with AP transactions listed first, followed by AR, followed by CM. Within a given Source group (e.g., AP), individual transactions are listed in order of Company, Month, and Trans.
Upon drilling into a specific transaction, Level 3 displays details for the transaction, with an indication of how each detail row contributes to transaction-level amounts as well as GST Item-level totals. For an AP transaction, all AP sequences for the transaction are displayed. For an AR transaction, AR lines that apply to the transaction (or invoice) and were posted within the reporting period are displayed. For a CM transaction, additional information pertaining to the transaction is displayed.
Report Parameters
Description

Company
Accept the default, or press F4 to select a company.

Tax Year
Click the Field Lookup
 button or press F4 to select tax year.

Sequence
Click the Field Lookup
 button or press F4 to select sequence.
