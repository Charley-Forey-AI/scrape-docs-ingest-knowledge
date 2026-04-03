---
title: "Credit Card Purchases | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/credit-card-purchases"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/credit-card-purchases"
---

# Credit Card Purchases

Unlike instant manual checks, credit card purchases do not
 require that the account currency be the same as the vendor currency because it is common to
 purchase goods in different currencies.
Enter amounts in the vendor currency. During the update, the system will
 translate the vendor currency into the account's currency for Cash Management purposes.
 All transactions to the G/L will be translated into the reporting currency.

Credit Card Purchase Example
Assume a 100 British Pound invoice was paid for using a Canadian
 credit card. In this transaction, no VAT or GST was recorded. The invoice was charged to
 a job. The reporting currency is US Dollars.
The system will calculate the exchange rate from Vendor currency to
 the Account currency as it relates to the Reporting currency. Using the invoice's G/L
 dates, the following FX rates are in effect:

- 1.00 USD = 0.654564 GBP

- 1.00 USD = 1.320910 CAD

Use the following formula to calculate the effective interest rate
 between two non-reporting currencies:

- From Currency FX Rate divided by
 To Currency FX RateGBP FX / CAD FX =
 0.654564 / 1.320910 = 0.495540
100 GBP / 0. 495540
 = $201.80 CAD

Thus, £100 .00 GBP is $152.77 USD which is $210.80 CAD.

Currency
Vendor Currency: GBP
Account Currency: CAD
Reporting Currency: USD

Amount
100.00 GBP
$201.80 CAD
$152.77 USD

Exchange Rate
1.00 USD = £0.654564
1.00 USD = 1.320910 CAD
N/A

Posts to
Accounts Payable
Credit Card Reconciliation
G/L and Job Cost

Journal Entry
The following is the journal entry that was booked when the Canadian invoice was
 updated.
Transaction
G/L Code
In GBP (0.654564)
In USD (1.00)

DR
1515 Direct Job
100.00
152.77

CR
0209 A/P Trade - GBP
100.00
152.77

This is the journal entry to record payment of the Canadian invoice with a GBP credit
 card.
Transaction
G/L Code
In CAD (0.1.1320910)
In USD (1.00)

DR
0209 A/P Trade - GBP
201.80
152.77

CR
0243 Bank of CAN - CAD
201.80
152.77
