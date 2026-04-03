---
title: "Credit Card Payment Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/credit-card-payment-entry"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/credit-card-payment-entry"
---

# Credit Card Payment Entry

Unlike Manual Checks, the account currency of the credit card
 does not control which vendors can be paid in Credit Card Payments. The vendor currency will
 display after the 'Transaction amount' field.
Enter amounts in the vendor currency. During the update, the system
 will translate the vendor currency into the account's currency for Cash Management
 purposes. All transactions to the G/L will be translated into the reporting
 currency.
Credit Card Purchase Example
Assume a 500 Canadian Dollar Pound invoice was paid for using a
 British GBP credit card. In this transaction, no VAT or GST was recorded. The reporting
 currency is US Dollars.
The system will calculate the exchange rate from Vendor currency to
 the Account currency as it relates to the Reporting currency. Using the invoice's G/L
 dates, the following FX rates are in effect:

- 1.00 USD = 1.320910 CAD

- 1.00 USD = 0.654564 GBP

Use the following formula to calculate the effective interest rate
 between two non-reporting currencies:

- From Currency FX Rate divided by To Currency FX Rate
CAD FX / GBP FX = 1.320910 / 0.654564 = 2.0179997
$500 CAD / 2.017997 = £247.77 GBP

Thus, $500 .00 CAD is $378.53 USD which is £247.77 GBP
Currency
Vendor Currency: CAD
Account Currency: GBP
Reporting Currency: USD

Amount
$500.00 CAD
£247.77 GBP
$378.53 USD

Exchange Rate
1.00 USD =$1.320910 CAD
1.00 USD = £0.654564
N/A

Posts to
Accounts Payable
Credit Card Reconciliation
G/L and Job Cost

Journal Entry
The following is the journal entry that was booked when the Canadian
 invoice was updated.
Transaction
G/L Code
In CAD (1.1.1320910)
In USD (1.00)

DR
1515 Direct Job
500.00
378.53

CR
0207 A/P Trade - CAD
500.00
378.53

This is the journal entry to record payment of the Canadian invoice
 with a GBP credit card.
Transaction
G/L Code
In GBP (0.654564)
In USD (1.00)

DR
0207 A/P Trade - CAD
201.80
378.53

CR
0244 Bank of London - GBP
201.80
378.53
