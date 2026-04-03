---
title: "Cash Receipts Edit List - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/cash-receipts-edit-list/cash-receipts-edit-list---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/cash-receipts-edit-list/cash-receipts-edit-list---field-descriptions"
---

# Cash Receipts Edit List - Field Descriptions

Field
Description

Batch
Enter the customer batch code for unposted cash receipts, or enter ALL to include all transactions regardless of batch assignment.

Customer
Enter the customeryou want to include on this report, or press Enter to select ALL.

Transaction code
Enter the code of the type of transaction you want to include on this report, or press Enter to include ALL transaction types. This must be a valid transaction code as entered in Transaction Code File Maintenance.

Transaction dates
Enter the first and last transaction dates to be included on this report, or press Enter to print ALL.

Cost group
If the cost center feature is enabled in the Enterprise Installation screen, the starting screen includes the Cost group field. When a cost group or cost center is specified in the cash receipts header, then the report will show only invoices assigned to that cost group/cost center. An option is also provided to sort primarily by cost center.
When the operator specifies a cost center on the starting screen, the software verifies the operator has permission to access that cost center before proceeding. The Cash Receipts Entry Edit List shows the cost center associated with each transaction line on the report. Spectrum will include transactions only if the operator requesting the report has permission to access the cost center assigned to the payment/adjustment. Spectrum compares the cost center assigned in the transaction with cost centers in the operator's assigned scheme; if the invoice cost center is not included, then that item is not shown on the report.
