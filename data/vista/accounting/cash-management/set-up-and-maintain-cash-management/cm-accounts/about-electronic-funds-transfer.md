---
title: "About Electronic Funds Transfer | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-electronic-funds-transfer"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-accounts/about-electronic-funds-transfer"
---

# About Electronic Funds Transfer

Information required for electronic funds transfer (EFT) is stored in the CM Accounts program and applies to both Accounts Payable EFT’s and Payroll Direct Deposits.
This information is required by the rules governing the Automated Clearing House (ACH) Network. It is used to create a downloadable file that can be sent to your bank on diskette or by modem.
Banks differ on their requirements for the file format of EFT’s. Some banks only need the account information for those accounts being credited (receiving the payment), whereas other banks require both the debit and credit account data. The download file format is determined by the Service Class Code. Code 200 indicates that the file contains a mix of debit and credit account data, whereas Code 220 indicates a transmission of credits only. If you use Code 200, then you must enter the routing transit number, account number, and account type for the bank account that will be debited for the amount of the EFT.
Note: To ensure that the text files used for transmitting EFT and Direct Deposit data to your bank are formatted to meet NACHA (National Automated Clearing House Association) requirements, Viewpoint uses the “CCD” (Cash Concentration or Disbursement) standard entry class code for EFTs, and the “PPD” (Prearranged Payment and Deposit) standard entry class code for direct deposits.

Related information

- [Direct Deposits](/en/vista/vista/hr-and-payroll/payroll/payments/direct-deposits)

- [Electronic Funds Transfers (EFTs)](/en/vista/vista/accounting/accounts-payable/payments/electronic-funds-transfers-efts)
