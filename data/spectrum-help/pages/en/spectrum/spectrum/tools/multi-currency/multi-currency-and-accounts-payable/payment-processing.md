---
title: "Payment Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/payment-processing"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/payment-processing"
---

# Payment Processing

The account currency controls which vendors can be paid. The
 account currency must match the vendor currency in order to select invoices to be paid with
 a computer check.
Exception to the rule: Comdata does not have to use the account's
 currency.

1. Start the process by selecting the Payment Selection button. Next, enter the account code that
 matches the currency you want to pay invoice in. Only one currency per check
 cycle is allowed.

1. Start the process by selecting the Payment Selection button. Next, enter the account code that
 matches the currency you want to pay invoice in. Only one currency per check
 cycle is allowed.

1. Select invoices to pay. Notice that the account currency is defined in the upper
 right hand corner of the screen.

1. Use Saved Selections
 to select the appropriate Print Checks format for the currency you are working
 in.

Currency
Vendor Currency: GBP
Reporting Currency: USD

Amount
1,800.00 GBP
$2,749.92

Exchange Rate
1.00 USD = £0.654564

Posts to
A/P and Bank Account Reconciliation
G/L

Journal
 Entry
Transaction
G/L Code
In GBP (0.654564)
In USD (1.00)

DR
0209 A/P Trade - GBP
1,800.00
2,749.92

CR
0109 Currency - GBP
1,800.00
2,749.92
