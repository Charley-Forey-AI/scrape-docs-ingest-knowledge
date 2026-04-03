---
title: "General Ledger Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/general-ledger-installation---properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/general-ledger-installation---properties"
---

# General Ledger Installation - Properties

The Confidential Payroll company must have the General Ledger module installed. The General Ledger for the "confidential" company should be identical to the "main" company.
Use this tab to select default properties settings for the General Ledger module. This screen should be completed even if General Ledger is not installed, and these settings can be changed at any time. After completing entry of the General Ledger Installation screen, proceed through the installation screens for all of the modules that you will be using in this company.
To access this screen from the Site Map screen, select Admin  >  Installation  >  General Ledger. When the installation screen is selected for the first time, a message stating "CONTROL RECORD HAS NOT BEEN CREATED. OK TO PROCEED" displays. After this installation screen has been completed and the information has been saved, the message will not appear again. In addition, the first time you access this screen,a Build Calendar button will display, and after the calendar has been set up (using the New Year button), the button name will display as View Calendar. You may create up to ten fiscal years as part of the initial setup process.
Fields Descriptions
Account code mask The account code mask stores the display pattern of your General Ledger account code, and will be used throughout the application.
Example: If you set up a four-digit G/L chart of accounts (1000, 1100, 1101, and so on), then the mask for this chart of accounts would be XXXX.
Alternately, if you opt for a six-digit code in your chart of accounts with the first two digits indicating the department (01-4000, 01-5050, 02-4000, and so on), then the mask for this chart of accounts would be XX-XXXX.
You may specify up to 12 characters, but most users opt for shorter codes. You must enter an account code mask even if the General Ledger module is not installed.
Note: We recommend that you do not alter the account code mask after initial installation.

Department code length If your chart of accounts will include at least one digit per department, enter the appropriate number.
Example: If your account code mask is XX-XXXX, enter 2. If the General Ledger module is not installed on your computer, or if you are not planning a departmentalized chart of accounts, enter 1.
The departments in your chart of accounts can define regions or activities within your company where you plan to track departmental revenue and expense. It is not necessary to departmentalize your chart of accounts to track revenue and expense, so consult your Spectrum trainer or refer to the Spectrum Overview manual for further information about planning your chart of accounts.
Note: The department code length can be changed after the initial installation, using the G/L Code Change Maintenance screen. For example, the department length might be altered in conjunction with an expansion of the G/L account code from 4 to 6 digits.
After changing the account code length, it is necessary to add new departments in G/L Department File Maintenance before continuing operations.

Retained earnings account code Enter the G/L account code number you plan to title "retained earnings" (or a similar name) in your Spectrum chart of accounts. Be sure to include this code when you enter your chart of accounts.
Note: If you do not have the General Ledger module installed, entry in this field is irrelevant.The system will use the G/L account number during the year-end Opening Forward Balance Update; all income and expense account balances will automatically roll into this account at year-end when the update is performed. No closing journal entry is required between fiscal years in Spectrum.
Cost centers
The Override button displays if the Allow G/L account overrides by cost center checkbox is selected in the Cost Center Settings window on the Enterprise Installation > Company tab. Select to enter override G/L account codes for each cost center set up in the software.

Post to G/L
Accounts Payable checks? Select to update accounting information from payment processing in the Accounts Payable module to the General Ledger. If this checkbox is selected, the General Ledger will update with debits and credits according to the Payments G/L Detail Report. If left clear, then no information will pass to the General Ledger during the Payments G/L Update.
Normally, this checkbox is left clear during the conversion process as the vendors' open balances are recorded. Thereafter, it should be selected so payment entries (manual, void, and computer-generated checks) will be recorded in your General Ledger files.
If you do not have the General Ledger or Accounts Payable modules installed in this company, leave this field clear.

Accounts Payable invoices? Select this checkbox to update accounting information from invoices during A/P Transaction Register Update. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Transaction Register. If this checkbox is left clear, then no information will pass to the General Ledger during invoice processing.
Normally, this checkbox is left clear during the conversion process as the vendors' open balances are recorded; thereafter, this checkbox should be selected so A/P invoice and credit memo entries (and pre-paid checks) will be recorded in your General Ledger files. If you do not have the General Ledger or Accounts Payable modules installed in this company, this field should be left clear.

Accounts Receivable cash receipts? Select this checkbox to update accounting information from cash receipt processing in the Accounts Receivable module to the General Ledger. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Cash Receipts G/L Detail Report. If this field is left clear, then no information will pass to the General Ledger during Cash Receipts Journal Update.
Normally, this checkbox will be left clear during the conversion process as the customers' open balances are recorded; thereafter, this checkbox should be selected so cash receipt and adjustment entries will be recorded in your General Ledger files. If you do not have the General Ledger or Accounts Receivable modules installed in this company, this checkbox should be left clear permanently.

Accounts Receivable invoices? Select this checkbox to update accounting information from invoice processing in the Accounts Receivable module to the General Ledger. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Sales Journal. If this checkbox is left clear, information will not pass to the General Ledger during Sales Journal Update.
Normally, this checkbox will be left clear during the conversion process as the customers' open balances are recorded; thereafter, this checkbox should be selected so invoice and credit memo entries will be recorded in your General Ledger files. If you do not have the General Ledger or Accounts Receivable modules installed in this company, this checkbox should be left clear permanently.

Cash Management transactions? Select this checkbox to update accounting information from the Cash Management module to the General Ledger module during the Bank Reconciliation Transaction Update, the Direct Checks Update, the Void Direct Checks Update, the Wire Transfers Update, and the Void Wire Transfers Update. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the reports. If this checkbox is left clear, then no information will pass to the General Ledger during processing.
Normally, this checkbox is left clear during the conversion process.

Fixed Assets depreciation? Select this check to update accounting information from the Fixed Assets module to the General Ledger. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the G/L detail report.
If this checkbox is left clear, then no information will pass to the General Ledger duringUpdate Depreciation to Master.
Normally, this checkbox will be left clear during the conversion process as the depreciation-to-date cycle is performed; thereafter, this checkbox should be selected so monthly depreciation entries will be recorded in your General Ledger files. If you do not have the General Ledger or Fixed Assets modules installed in this company, this checkbox should be left clear permanently.

Human Resources transactions? Select this checkbox if you want Human Resources transactions posted to the General Ledger during the Vac/Hol/Sick Accrual G/L Update and the Reverse Vac/Hol/Sick G/L Accrual. If you do not want Human Resources transactions posted to the General Ledger, leave this checkbox clear.
Normally, this checkbox will be left clear during the conversion process. If you do not have the General Ledger or Human Resources modules installed in this company, this checkbox should always be left clear.

Inventory Control adjustments? Select this checkbox to update accounting information from adjustments entry and job requisition processing in Inventory Control module during Inventory G/L Summary Update. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Inventory G/L Detail Report. If this checkbox is left clear, then no information will pass to the General Ledger during inventory adjustment or job requisition processing/updating.
Normally, this checkbox is left clear during the conversion process as the quantity-on-hand information is recorded; thereafter, this checkbox should be selected so inventory adjustment and job requisition entries will be recorded in your General Ledger files. If you do not have the General Ledger or Inventory Control modules installed in this company, this checkbox should be left clear permanently.

Inventory Control receipts? Select this checkbox to update accounting information from receipts processing in Inventory Control module during Inventory G/L Summary Update. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Inventory G/L Detail Report. If this checkbox is left clear, then no information will pass to the General Ledger during receipts processing/updating.
Normally, this checkbox will be left clear during the conversion process as the quantity-on-hand information is recorded; thereafter, this checkbox should be selected so inventory receipt entries will be recorded in your General Ledger files. If you do not have the General Ledger or Inventory Control modules installed in this company, this checkbox should be left clear permanently.

Job Cost transactions? Select this checkbox to update accounting information from Job Cost module during Job Cost G/L Detail Update. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Job Cost G/L Detail Report. If this checkbox is left clear, then no information will pass to the General Ledger during Job Cost transaction processing/updating.
Normally, this checkbox is left clear during the conversion process as the job-to-date costs are recorded; thereafter, this checkbox should be selected so Job Cost transaction entries will be recorded in your General Ledger files. If you do not have the General Ledger or Job Cost modules installed in this company, this checkbox should be left clear permanently.

Order Processing invoices? Select this checkbox to update accounting information from the Order Processing module to the General Ledger during Invoice Register Update. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Invoice General Ledger G/L Summary Report. If this checkbox is left clear, then no information will pass to the General Ledger during invoice processing.
Normally, this checkbox is left clear during the conversion process as the customer balances are recorded; thereafter, this checkbox should be selected so invoice entries will be recorded in your General Ledger files. If you do not have the General Ledger or Order Processing modules installed in this company, this checkbox should be left clear permanently.

Payroll? Select this checkbox to update accounting information from Payroll module during Payroll Update. If this checkbox is selected, the General Ledger will be updated with debits and credits according to the Payroll G/L Detail Report. If this checkbox is left clear, then no information will pass to the General Ledger during payroll processing/updating.
Normally, this checkbox will be left clear during the conversion process as the year-to-date payroll cycle is performed; thereafter, this checkbox should be selected so payroll entries will be recorded in your General Ledger files. If you do not have the General Ledger or Payroll modules installed in this company, this checkbox should be left clear permanently.

Service Contract transactions? Select this checkbox to include transactions from Service Contract to the General Ledger.
This checkbox defaults to cleared when General Ledger is first installed.

Fixed Assets update method Select Book or Tax, depending on the depreciation method you want to use when depreciation figures are updated from the Fixed Assets module to the General Ledger.
This option button is applicable only if the Fixed Assets depreciation checkbox is selected.

Related information

- [View Fiscal Calendar](/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/view-fiscal-calendar)
