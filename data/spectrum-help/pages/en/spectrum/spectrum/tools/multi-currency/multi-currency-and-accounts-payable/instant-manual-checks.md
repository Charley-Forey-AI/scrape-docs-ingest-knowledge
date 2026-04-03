---
title: "Instant Manual Checks | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/instant-manual-checks"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/instant-manual-checks"
---

# Instant Manual Checks

It is a requirement that the vendor currency and the account
 currency be the same when creating instant manual checks. The currency code displays at
 the end of the check amount.
VAT Invoice from Above – Paid by Instant Manual Check
Assume that the Vendor Invoice Entry with VAT enabled is paid using an
 Instant Manual Check.
Currency
 Vendor Currency: GBP
 Reporting Currency: USD
 Reporting Currency: USD

Amount
 1,800.00 GBP
 $2,291.60
 $458.32 DR VAT Payable & $2,749.92 CR A/P
 Trade

Exchange Rate
 1.00 USD = £ 0.6545564

Posts to
 A/P and Bank Account Reconciliation
 G/L and Job Cost
 G/L


Journal Entry
Transaction
 G/L Code
 In GBP (0.654564)
 In USD (1.00)

DR
 1515 Direct Job
 1,500.00
 2,291.00

DR
 0216 VAT Payable
 300.00
 458.32

CR
 0209 A/P Trade - GBP
 1,800.00
 2,749.92

DR
 0209 A/P Trade - GBP
 1,800.00
 2,749.92

CR
 0109 Currency - GBP
 1,800.00
 2,749.92


The Credit Card Purchase Register explains the British Pound (GBP)
 invoice was paid with the Bank of Canada credit card.
Note: Reminders:

- G/L reports show entries in the reporting
 currency.

- There is no Currency Gain / Loss on Credit Card Purchases.

No Currency Gain / Loss on Instant Manual Checks
By rule, instant manual checks have no currency gains or losses to
 account for.
