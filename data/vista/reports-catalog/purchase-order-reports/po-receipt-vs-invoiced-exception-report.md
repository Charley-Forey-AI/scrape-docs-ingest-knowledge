---
title: "PO Receipt Vs Invoiced Exception Report | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/purchase-order-reports/po-receipt-vs-invoiced-exception-report"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/purchase-order-reports/po-receipt-vs-invoiced-exception-report"
---

# PO Receipt Vs Invoiced Exception Report

You can use the PO Receipt Vs Invoiced Exception Report
 report by selecting Purchase Order > Reports > PO Receipt Vs Invoiced Exception
 Report.
The PO Receipt Vs Invoiced Exception Report lists PO items with differing invoiced and received costs, and should be run prior to changing the "Update GL/Sub-Ledgers on Receipt" flag in PO Company Parameters. The PO item amounts shown in this report will be used for updating the applicable GL accounts in the batch created by the PO Initialize Expense program in PO Company Parameters. Therefore, this report provides the purchase order data necessary for making changes prior to posting the initial PO receipt expense batch in PO Company Parameters. A single input for Job / PO are available to see a list of differences when attempting to close a Job / PO and the system has returned an error.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

JC Company (Blank for All)
Click the Field Lookup
 button or press F4 to select the job cost company or leave
 blank for all.

Job (Blank for All)
Click the Field Lookup
 button or press F4 to select the job or leave blank for
 all.

PO (Blank for All)
Click the Field Lookup
 button or press F4 to select the purchase order or leave blank
 for all.

Open POs Only?
checkbox to show open purchase orders only.
