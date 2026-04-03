---
title: "Vendor Invoice Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/vendor-invoice-entry"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/multi-currency-and-accounts-payable/vendor-invoice-entry"
---

# Vendor Invoice Entry

The vendor code entered in Vendor Invoice Entry determines
 the vendor currency used for the transaction. The currency code of the transaction will be
 displayed after the 'Total amount' field and on the Vendor Info Bar.

## Processing Rules

- The currency is determined once the vendor code is
 entered into the screen. From this point on, the currency code stored in the
 invoice header table is used for all processing. This is to protect from the
 case where the user changes the currency on a vendor as the transaction will
 retain the original information.

- It is important that the user select the vendor with the
 same currency as found on the invoice. If the invoice was written in Euros
 and the company will pay the invoice in Euros, enter all numerical values in
 Euros. Example of Vendor Invoice Entry with VAT enabled

## Example of Vendor Invoice Entry with VAT
 enabled

Enter the following £1,500 invoice for Grahams
 Hi-Fi. It is subject to 20% VAT. Charge it to job 300, phase 01-0200, cost type M.
 No other use tax is charged to the invoice.
Example:
Currency
Vendor Currency: GBP
Reporting Currency: USD
Reporting Currency: USD

Amount
1,800.00 GBP
$2.291.60
$458.32 DR VAT Payable & $2,749.92 CR
 A/P Trade

Exchange Rate
1.00 USD = £ 0.654564

Posts to
A/P and Bank Account Reconciliation
G/L and Job Cost
G/L Only

## Journal Entry

Transaction
G/L Code
In GBP (0.654564)
In USD (1.00)

DR
1515 Direct Job
1,500.00
2.291.00

DR
0216 VAT Payable
 300.00
 458.32

CR
0209 A/P Trade - GBP
1,800.00
2,749.92

## Segregating Accounts by Currency

Once the vendor is entered and the currency derived, the invoice
 will use any 'override G/L account codes' set up on the currency code. Enforcing
 these G/L payable account codes will assist when the Controller has to manually
 translate these values back into their respective currencies for financial reporting
 purposes.
During data entry, when a transaction uses a non-reporting
 currency, the software replaces the standard installation G/L accounts with these
 currency defined G/L accounts as defaults.
Exception to the rule: If cost centers are present and 'G/L
 Account Overrides' are enabled, the system will always use the Override G/L account
 code setup instead of the currency-specific settings.
At the end of each accounting period, GAAP requires that
 receivables and payables held in non-reporting currencies be revalued using the
 month-end FX rate. The Controller will run the Aged Payables report and Aged Open
 Items Report by currency, revalue it into the reporting currency and make
 appropriate reversing journal entries.

## Determining the Invoice Exchange Rate

In
 general, the system will determine the appropriate exchange rate based on the invoice's
 G/L date. The following explains how the exchange rate is determined and when it is
 locked into the transaction.Unposted Transactions RuleThe exchange rate is determined dynamically for unposted transactions. Here,
 the exchange rate is not stored and any changes to the FX rate for the
 entered G/L date will be used in translating unposted transactions. Posted TransactionsThe exchange rate is determined and stored permanently in the transaction
 history table when the invoice is updated. This stored rate will be used for
 any subsequent reporting or processing of this invoice. Special Rules for Multi-Company Exchange RatesFor a multi-company invoice, the system will look up the exchange rate in
 the distribution company. For this reason, the currency of the transaction
 must be set up in that other company. The system will not allow the user to
 continue their entry when the currency code has not been set up in the other
 company. The exchange rate must be maintained in the distribution company as well. As
 it is possible that the distribution company has a different exchange rate
 than the payables company, the rates must be managed and updated by company. For Accounts Payable, the only multi-company transaction is the Vendor
 Invoice. In order to distribute an invoice to another company, the currency
 of the vendor invoice must be a valid currency in that other company. The
 exchange rates must be maintained in the distribution company as well.
