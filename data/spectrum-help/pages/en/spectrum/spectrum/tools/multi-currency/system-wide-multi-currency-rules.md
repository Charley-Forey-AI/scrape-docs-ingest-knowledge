---
title: "System-wide Multi-Currency Rules | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/multi-currency/system-wide-multi-currency-rules"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/multi-currency/system-wide-multi-currency-rules"
---

# System-wide Multi-Currency Rules

Learn about the system wide multi-currency
 rules.

- Currency Description: For ease of use, the account codes include the currency in their description (for example, 25 USD).

- Debits and Credits in Reporting Currency: To assist in balancing to the G/L, all reports that include debits and credits are in the reporting currency.

- Translation Date: The translation is always based on the G/L date of the transaction.

- <BLANK >  Currency Code: Blank is assumed to be the reporting currency. Also an invalid Currency code is assumed to be the reporting currency as well.

- Cost Center Overrides Used Instead of Currency-Specific Settings: If cost centers are present and 'G/L Account Overrides' are enabled, the system will always use the Override G/L account setup (as in past versions) instead of the currency-specific settings.

- Currency Must Exist in Distribution Company: The currency that is used on a transaction must exist in the distribution company as well. If a multi-company vendor invoice is created, the currency code must exist in both companies. The currency code in the distribution company is used to revalue open commitments and unposted amounts.
