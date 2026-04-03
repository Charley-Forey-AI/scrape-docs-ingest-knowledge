---
title: "Contract Defaults | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-properties/contract-defaults"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/contracts/contract-properties/contract-defaults"
---

# Contract Defaults

Use this screen to add additional properties pertaining to the contract.
Field
Description

Billing defaults

Sales tax code
The sales tax code will default from the Customers screen. Press Enter, or enter the different sales tax code (up to 15 alpha-numeric digits) that will apply to this contract. The tax description will display.

Taxable?
Select Yes if this contract is taxable, otherwise select No or No default.

Cost center
If cost centers are set to 'Yes' or 'Pending' for the current company, enter the cost center in this field.

G/L sales account
The General Ledger account number for the sales account will default from the Accounts Receivable Installation screen. Press Enter to accept the default, or enter the account that will be credited for invoices posted with this contract number.
Click the G/L % Allocation button to open the [G/L Distribution for Draw Request Invoices](/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/maintenance-overview/gl-distribution-for-draw-request-invoices) window.
 If the Validate job division with G/L department checkbox is selected in the Job Cost Installation, the department of the G/L account specified for Default contract sales G/L account code field in the Accounts Receivable Installation will be overwritten by the division of the job.

Retention percent
The retention percentage for the G/L sales account will default from the job number.

G/L retention revenue
Enter the primary G/L account code you plan to title "retention revenue" (or similar name) in your Spectrum chart of accounts, or press F4 or double-click on this field to select from a list of available G/L account codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter your retention revenue account even if you do not have General Ledger module installed on your computer.
Note: This field will be hidden if the Use deferred retention revenue
 account checkbox in Accounts Receivable Installation is not
 selected.

Override standard customer terms?
Select this checkbox to specify a different terms code for this contract. If the box is cleared, any changes made to the customer file after a contract has been set up will not change the existing terms code on the contract.

Terms code
When editing a contract, click on this field to select a different customer terms code.

Customer P.O.
Enter a customer purchase order # in this field. The P.O. entered here will default on customer invoices.

Billing address

Print alternate address on draw request/invoice?
Select this checkbox to print the customer's alternate bill-to address on the contract's draw requests and invoices. If you select this checkbox, entry is required in the Bill-to code field. Customer alternate bill-to addresses are set up in Alternate Bill-To Address Maintenance.

Bill-to code
If you selected the checkbox above, entry in this field is required. Enter the alternate address bill-to code, or press F4 or double-click on this field to select from a list of available bill-to codes in the Alternate Bill-to Address window. Alternate bill-to codes can also be added or edited from this window.

Name
The name for the selected billing address displays. If you selected the checkbox above, then the alternate billing addressee name will display based on the code entered in the Bill-to code field.

Address
The customer's billing address displays. If you selected the Print alternate address on draw request / invoice checkbox, then the alternate billing address will display based on the code entered in the Bill-to code field.

Job site

Address
The job site address displays in this section.
