---
title: "Set Payment Reporting Information: United States | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information/set-payment-reporting-information-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information/set-payment-reporting-information-united-states"
---

# Set Payment Reporting Information: United States

You can specify the reports used when printing checks and when generating electronic payments and credit service remittances.

 Payment report information determines the type of reports that the system uses when printing checks, the number of lines that display on a check stub, and the reports the system uses for EFT (Electronic Funds Transfer) and credit service remittances.

1. Open the AP Company Parameters form.

1.  Select the Payment Reports tab.

1. In the Report Title for Check Print field, enter the report to use when printing checks or press F4 to select from a list of valid reports.Note: There are currently two standard reports for check printing. Use the AP Check Print report if you are printing on pre-printed checks with pre-printed check stubs. If you leave this field blank, this report is the default. Use the AP Check Print Stub report if you are printing on pre-printed checks with blank check stubs. In addition to transaction information, this report automatically prints the actual borders and headings for you.

1. In the Report title for Check Overflow field, enter the report to use for printing overflow vouchers when the remittance information exceeds the available space on the check stub. Press F4 to select from a list of valid reports.If you leave this field blank, the system uses the AP Check Overflow report.

1. Enter the maximum number of check stub lines in the Maximum Lines per Check Stub field.

1. In the Report title for EFT Remittance field, enter the report to use when printing EFT remittance information (via Tasks > EFT Remittance Report in AP Payment Posting).If you leave this field blank, the system uses the AP EFT/ePayments Remittance report. This report is the only standard report provided and functions the same as the AP EFT Remittance report if you are not using ePayments (U.S. only).

1. In the Report title for Payment Service  field, enter the report to use when printing credit service remittance information (via Tasks > Credit Service Remittance Report in AP Payment Posting). If you leave this field blank, the system uses the AP Credit Service Remittance by Vendor report.

The system uses the above settings when printing checks in the AP Check Print form or when generating EFT and/or credit service payment remittance reports.
