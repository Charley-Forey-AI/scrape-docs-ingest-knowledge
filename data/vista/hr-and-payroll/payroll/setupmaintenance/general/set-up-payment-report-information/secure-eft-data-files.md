---
title: "Secure EFT Data Files | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/secure-eft-data-files"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/secure-eft-data-files"
---

# Secure EFT Data Files

You can secure the data files created when generating and sending EFT information to financial institutions.
Vista supports your need to create and send EFT data files to financial institutions as part of your routine processing to remit payments to both vendors and employees.
You have the option to secure the data file that Vista creates during this process so that the user generating the data file cannot open or view them. Instead of presenting the user with a Save As window at the moment they generate the file, Vista channels the files to your predetermined location.
Important: The person sending the file electronically needs access to your chosen secure file location in order to retrieve and send. The one exception to this is ePayments users (U.S. only), who can use Vista to submit AP invoice data files automatically. For more information about ePayments, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form#ID-000066a4--en__ID-000066a4).

1. Depending on whether you are sending AP or PR EFT files, do one of the following:

- AP EFT: Open the AP Company Parameters form, Payment Reports tab

- PR EFT: Open the PR Company Parameters form, Report Info tab

1. Select the Use Secure File Path checkbox.The system enables the Secure File Path field.

1. Select Browse to navigate to and select your chosen location.Your chosen file path appears in the field.

1. Select Save.

Vista sends your EFT data files to the chosen location. For AP EFTs, this includes data files created in AP EFT Download and AP EFT Prenote Download. For PR EFTs, this means data files created using the PR EFT Payments form.
Important: Users with access to either AP Company Parameters or PR Company Parameters forms can modify the Secure File Path and therefore the location at which Vista saves the EFT data files.

Related information

- [AP EFT Download Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-download-form)

- [AP EFT PreNote Download Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-eft-prenote-download-form)

- [Process Payroll EFT Payments](/en/vista/vista/hr-and-payroll/payroll/payments/process-payroll-eft-payments)

- [About Setting Company Tax and Insurance Information](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-company-tax-and-insurance-information)
