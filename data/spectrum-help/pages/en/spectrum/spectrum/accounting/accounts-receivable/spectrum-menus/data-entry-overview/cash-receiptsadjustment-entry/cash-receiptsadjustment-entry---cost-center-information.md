---
title: "Cash Receipts/Adjustment Entry - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/cash-receiptsadjustment-entry---cost-center-information"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/cash-receiptsadjustment-entry/cash-receiptsadjustment-entry---cost-center-information"
---

# Cash Receipts/Adjustment Entry - Cost Center Information

If the cost center feature is enabled in the Enterprise Installation screen, Spectrum will allow entry for a customer only if the operator has permission to access the customer's information. Spectrum compares the customer's list of shared cost centers with cost centers in the operator's assigned scheme; if there are no common cost centers, then entries for that customer are not allowed.
The screen prompts for a payment cost center for the cash receipt transaction. For payment transactions, the cost center will be assigned to the G/L cash account (debit). For adjustment transactions, the cost center will be assigned to the G/L account for the transaction code (debit if transaction amount is positive or credit if the amount is negative). Spectrum verifies that the operator has authorization to assign the cost center before proceeding . Spectrum also verifies that the cost center is allowed for the transaction G/L accounts specified in the Transaction Code Maintenance screen.
In the Selections window, Spectrum allows the operator to specify a cost group or a cost center. If a selection other than ALL is made, then only invoices, credit memos, and other transactions assigned to that cost group/cost center will display.When individual invoices are entered in the "Invoice" sub-window, the software will verify that the operator has security authorization for the invoice when cost centers are set to Yes in the current company. The operator must have authorization to the cost center assigned in the invoice header. Likewise, when the SuperSelect and Dates method is used, the software will only display items that the operator has security authorization for. Cost center scheme overrides are not applicable for this validation.
Selecting invoices/credit memos by cost center will only display the records with the selected cost center in the header.
Example:

## Invoice 2-300 header cc 301 detail 102 Invoice 2-100 header cc 401 detail 301 If invoices are selected for cost center 301, only invoice 2-300 displays.

In the Adjust window in the detail portion of the screen, Spectrum prompts for cost center adjustments. The cost center in this window is validated using the same criteria as the cost center field in the heading of the screen.
The cost center assigned to the detail transaction is shown. When the detail displays, Spectrum shows only invoices, credit memos, and other transactions that the operator is allowed to view. Spectrum compares the cost center assigned to the open transaction with cost centers in the operator's assigned scheme; if the cost center is not present, then that transaction is not shown.
