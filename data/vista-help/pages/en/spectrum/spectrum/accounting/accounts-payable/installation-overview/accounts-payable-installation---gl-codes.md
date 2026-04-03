---
title: "Accounts Payable Installation - G/L Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---gl-codes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/installation-overview/accounts-payable-installation---gl-codes"
---

# Accounts Payable Installation - G/L Codes

Use this screen to set up your default G/L code settings
 for the Accounts Payable module.
 Be sure to complete the G/L account codes for the items shown even if the General Ledger
 module is not installed. You will also need to make sure you include the numbers entered
 here when you enter your chart of accounts.
Fields/Buttons
Descriptions

Default A/P trade G/L account code
Enter the primary G/L account code you plan to title "accounts payable trade" (or similar name) in your Spectrum chart of accounts.

Subcontractor payable G/L account code
This G/L account code may be the same code designated as the Accounts Payable G/L account code, but specifying a different liability will cause contractual payables to appear as a separate line item on the balance sheet. Spectrum conveniently uses this G/L account code whenever subcontract transactions are entered.

Retention payable G/L account code
This G/L account code may not be the same code designated as your accounts payable or subcontracts payable. Enter your retention payable account even if you do not plan to record retention.
The system will automatically update retention amounts to this G/L account code when you designate retention during invoice entry, as well as during payment of retention balances.

Default cash in bank G/L account code
This should be the cash account that you use when paying your accounts payable checks.
The system will offer this G/L account code during payment processing and
 prepaid check entry in Invoice / Credit Memo Entry
 but you may override this account code if desired.
If the Cash Management module is present, the system will determine the cash
 account code based on settings in the Cash Management > Bank Account File Maintenance page.

Discount taken G/L account code
Enter the G/L account code you plan to title "purchase discounts" (or similar
 name) in your Spectrum chart of accounts, or press F4
 to select from a list of valid G/L codes already entered in the software.
 This G/L account code may not be the same code designated elsewhere in the
 Accounts Payable Installation. Enter your
 discounts taken account even if you do not plan to take purchase
 discounts.
The system will automatically update discounts taken to this G/L account code when you designate discounts during [A/P Payment Processing](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/ap-payment-processing).

Automate G/L Defaults
Click this button to open the Automate G/L Defaults in Purchase Order and Invoice Entry window. Use this window to assign specific G/L account codes to default automatically based on the type of expense the user is recording.
You can also select whether to override G/L account codes based on the specific distribution entry. Select the Equipment G/L defaults from cost category checkbox to assign a specific G/L account in Purchase Order Entry and Vendor Invoice Entry based on the specified cost category.
If the Automate G/L defaults checkbox is selected, the button will say 'Yes'. If this checkbox is not selected, the button will say 'None'.

Inter-company G/L account code
Enter the inter-company G/L account code you plan want to use for
 inter-company payables in your Spectrum chart of accounts, or press
 F4 to select
 from a list of valid G/L account codes. This G/L code cannot be the same
 code designated elsewhere in the Accounts Payable Installation > G/L Codes screen.
Entry in this field is not required if inter-company A/P transactions are not desired. Spectrum will automatically update inter-company transactions to this G/L account code when you designate alternate company code(s) during Vendor Invoices Entry.

Inter-company G/L Code
Enter the company and associated G/L account code you plan to title
 "inter-company payable" (or similar name) in your Spectrum chart of
 accounts, or press F4 to select from a list of valid G/L codes already entered
 in the software. This G/L account code may not be the same code designated
 elsewhere in Accounts Payable Installation. Be sure
 to include this G/L account number when you enter your chart of
 accounts.
Entry is not required if inter-company A/P transactions are not desired. Spectrum will automatically update inter-company transactions to this G/L account code when you designate alternate company code(s) during Vendor Invoices Entry.

Overrides
If cost centers are being used, you can use the Override buttons to enter cost
 center G/Laccount codes that will be used to override the defaults entered
 on this screen.
For example, when working in cost center company '01' you might want to override the default trade account with 00-2001.
Hover over image to enlarge.
