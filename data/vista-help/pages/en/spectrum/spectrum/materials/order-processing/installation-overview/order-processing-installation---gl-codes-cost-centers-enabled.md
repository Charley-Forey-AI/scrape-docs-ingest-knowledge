---
title: "Order Processing Installation - G/L Codes (Cost Centers enabled) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/installation-overview/order-processing-installation---gl-codes-cost-centers-enabled"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/installation-overview/order-processing-installation---gl-codes-cost-centers-enabled"
---

# Order Processing Installation - G/L Codes (Cost Centers
 enabled)

Use this tab to select the G/L code settings for the Order
 Processing module. These setting can be changed as needed at any time.
For each of the account entry fields in this screen you can select from
 a list of available account codes. Be sure to include these G/L account numbers when you
 enter your chart of accounts. Complete all the G/L account fields even if you do not have
 the General Ledger module installed.
Note: If the cost center feature is not enabled, the available fields
 are slightly different.
Fields
Descriptions

Default Accounts Receivable trade G/L account code
The system will default to this G/L account code in
 quote, order and invoice entry, but the code may be overwritten if desired.
 The A/R trade G/L account code stored in the item header is used when
 invoices and credit memos are updated from invoice processing to G/L in
 Invoice Register Update.

Commissions payable G/L account code
The system will use this G/L account code when invoices
 and credit memos that include sales commissions are updated from invoice
 processing to General Ledger.

Commissions expense G/L account code
The system will use this G/L account code when invoices
 and credit memos that include sales commissions are updated from invoice
 processing to the general ledger.

Freight G/L account code
The system will use this G/L account code when invoices
 and credit memos that include freight charges are updated from invoice
 processing to the general ledger.

Default sales tax G/L account code
This G/L account code will only be used when invoices and
 credit memos that include sales tax are updated if the designated sales tax
 code has been deleted from the sales tax code file; the system will utilize
 the account code in this field only as a last resort.

Default inventory sales G/L account code
The system will only use this G/L account code during the
 invoice register update if there is no designated sales category for the
 line item; the system will utilize the account code in this field only as a
 last resort.

Default inventory cost of sales G/L account code
This G/L account code will only be used when invoices and
 credit memos that include sales tax are updated if the designated sales tax
 code has been deleted from the sales tax code file; the system will utilize
 the account code in this field only as a last resort.

Default inventory value G/L account code
The system will only use this G/L account code during the
 invoice register update if there is no designated sales category for the
 line item; the system will utilize the account code in this field only as a
 last resort.

Cost center inter-posting G/L account code
This field is used to define a default cost center
 inter-posting account code for the selected company. Enter the default cost
 center inter-posting account code or select from a list of available G/L
 account codes. This field is available only if cost centers are activated in
 the current company.
Click the Override button to enter override G/L account codes fro each
 cost center set up in the software. More info The Override buttons displays
 only if the Allow G/L account
 overrides by cost center checkbox is selected in the Cost
 Center Settings window on the Enterprise Installation – Company screen.

Overrides button
This window is available only if the Allow G/L account overrides by cost
 center checkbox is selected on the Cost Center Settings
 window on the Enterprise Installation – Company screen.
Click this button to display the Cost Center to G/L
 Overrides window for either cost center inter-posting accounts or for
 retained earnings. When this window displays, G/L override accounts can be
 entered for each cost center set up in the company. If you do not want to
 designate an override account for a cost center, leave the G/L account field
 for the cost center blank.
