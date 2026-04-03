---
title: "Payroll Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/installation-overview/payroll-installation---properties"
---

# Payroll Installation - Properties

The Confidential Payroll company must have the Payroll module installed.
All employees with highly sensitive payroll records (for example, administrative staff) will be paid from the "confidential" company; they will not be paid through the "main" company's payroll procedure. Note, however, that these confidential salaries will be reflected in the "main" company's General Ledger.
To install the Payroll module, select Payroll from the Installation list. When the installation screen is selected for the first time, an installation dialog box displays on the screen. Once this installation screen has been completed and the information saved, the message will not appear again.
There are four basic employee status codes (Active, Inactive, Terminated, and Deceased). You can edit or add to these status codes later, while completing the Employee screen.
FieldsDescriptions
Show pre-time card pay rates?If you select this checkbox, the hourly pay rates are shown during Pre-Time Card Entry and on the Pre-Time Card Edit List.
For security reasons, you may want to leave this checkbox blank so that hourly pay rates will not display. This is appropriate if you have a data entry person who does not have security for Time Card Entry or the associated listings. You can set this person up with security for only the Pre-Time Card Entry page and the associated listings, then that person could enter hours, but could not see the actual pay rates paid to your employees.

Multi-state job validation?Select this checkbox to provide a warning message during Pre-Time Card Entry and Time Card Entry if the job file does not contain a state code in the "payroll tax codes" window. The software will provide a warning message stating that there is no state in the Job Maintenance, but will allow you to continue.
Typically, if a company works in a single state, this checkbox will be left blank.

Recalculate pay rates during pre-time card update?Select this checkbox to automatically recalculate pay rates during pre-time card update. If this checkbox is selected and you overwrite pay rates during Pre-Time Card Entry, the rate entered will NOT be retained during the transfer to Time Card Entry. Instead, the rate will be set as if the transaction had been entered directly in Time Card Entry, taking into account the other Payroll Installation screen settings such as Pay rates effective based on and Default pay rate.
Multi-company payroll?If this checkbox is selected, the software will allow you to specify an alternate company code. When you do this, the software will accept G/L and Job Cost codes from the other company and will update accordingly. The software will credit the liability and cash G/L account codes in the current company and debit the inter-company G/L account specified below. The payroll expense distribution will debit G/L (and job if applicable) in the other company, and credit the inter-company account code.

- If inter-company transactions are not desired, this checkbox should be clear.

- If this checkbox and the Is this a confidential payroll company field (see below) are selected, then the main company's employees will post in summary to the job (for example, PR summary and $$).

If cost centers are being used but multi-company processing is NOT being used in this company, a Cost center inter-posting G/L account code field replaces the Inter-company G/L account code field on the Payroll Installation - G/L Codes tab.
Is this a confidential payroll company?Select this checkbox if this is a confidential payroll company.
Post confidential hours to Job Cost?This checkbox is available only if the Is this a confidential payroll company checkbox is selected.
Confidential companyThis field only displays if the Multi-company payroll and Is this a confidential payroll company checkboxes have been selected.
Enter the company ID of your main company (for example, if the main company is XYZ and confidential payroll is performed from company XPR, on the installation screen of company XPR, enter "XYZ" in this field). This sets up the default for expense posting during Pre-Time Card Entry and Time Card Entry. This company ID is also where liabilities will post. The company ID entered here must be installed and you must have General Ledger in this company ID.

Accounts Payable invoice batch codeThe payroll system allows A/P invoices to be automatically created for garnishments taken on employee checks. This batch code will be used on all A/P invoices created from deductions during Payroll Update. This allows all A/P invoices created from the Payroll system to be updated separately.
Next Accounts Payable invoice numberEnter the next A/P invoice number to use when posting to A/P from deductions.
The payroll system allows A/P invoices to be automatically created for garnishments taken on employee checks. If this feature is used, then this sequence number will be used to ensure that each A/P invoice is created with a unique number. This sequence number will only be used for A/P invoices created from the Payroll system.

Descriptions for other pay types 1-3The entries specified here will be shown on the Payroll check stub when any of these pay types (1, 2, 3, and SA) are used in Time Card Entry. Examples of possible user-defined earnings descriptions include BONUS, TRUCK and EDUC. Descriptions may be any combination of letters and numbers, up to 6 characters.
If you are initializing the Payroll module and are unsure what special uses you may assign these pay types in the future, enter OTHER1, OTHER2, and OTHER3. You may return to this page as necessary to define the descriptions for these pay types.

Descriptions for special amount pay typeEnter the special amount pay type description. The entries specified here will be shown on the payroll check stub when any of these pay types (1, 2, 3, and SA) are used in time card entry. Examples of possible user-defined earnings descriptions include BONUS, TRUCK and EDUC. Descriptions may be any combination of letters and numbers, up to 6 characters.
If you are initializing the Payroll module and are not yet sure what special uses you may assign this pay type in the future, the following descriptions is recommended: SPEC. You may return to this screen as necessary to define the descriptions for these pay types.
Note: The application uses this field's value at the time checks are printed.

Incentive pay codeEnter the character you want to designate for incentive pay. This character will then be added to the pay types R, O, or D (regular, overtime, double time), for use in the Pre-Time Card Entry, Time Card Entry, and Layoff Check Entry screens. For example, if the character is "I" then the regular incentive code would be IR, and so forth). The character can be different for different companies.
Protection is incorporated into this page to prevent use of an incentive pay code that would conflict with existing Payroll deduction or add-on codes. For example, if the code JR was already set up as a deduction code, J would not be permitted as an incentive code in this field.

Next crew numberEnter the first crew number that should appear in the sequence when setting up new crews.
Auto-number employee codes?
Mask
Next employee code
Select this checkbox to automatically apply sequential numbering to employee codes.
Mask:
Enter a mask up to 11 characters long.
Next employee code:
Enter the first employee code that should appear in the sequence when creating new employee codes or press Enter to accept the software default, which is based on the next employee value variable and the Mask (for example, if the next employee number is 30 and the mask AXXXX, the next employee code will be A0030). If you designate the next employee code rather than accept the default, the code you designate cannot consist of more characters than what is allowed by the designated Mask.
This number automatically increases incrementally whenever an employee
 code is assigned in Payroll > Employees or in Human Resources > New Hire Entry.

Accrue expense to

- If you select the 'Check date' option, all G/L entries will be posted based on the check date of the payroll cycle, and expenses will post to General Ledger and Job Cost.

- If you select the 'Period-end date' option, expenses will be recorded in the General Ledger based on the period-end date of the pay cycle; the liabilities and cash outlay will be recorded on the check date. An accrued payroll G/L account code will be used in this case; this G/L account code will be credited on the period-end date of the payroll cycle, and debited in the same amount on the check date. In addition, if the Period-end date option is specified, the transaction date in Job Cost and Equipment Control files will be the period-end date; if the Check date option is selected, the transaction date will be the payroll check date.

- If you select the 'Work date' option, it will post to Job Cost history using the work date. For G/L it is similar to the Period-end date option: liabilities and cash outlay post to the G/L check date, and expenses post to the period ending date. However, if the work cycle goes over a month end, then the Payroll Update will split and post expenses in two postings – one on the last day of the previous month and one on the period ending date. Furthermore, if the Work date option is selected, for a Direct Job Cost time card entry or Direct Work Order Cost time card entry, the software stores the work date of the time card line as the Transaction date in Job Cost History or Work Order Actual Cost History, respectively. The date assigned to this transaction in G/L is dependent upon whether or not the transaction date is in a period earlier than the Pay cycle period end date: If the transaction date is in the same period as the Pay cycle period end date, the Payroll Update will assign the pay period end date to the G/L entry. If the transaction date is in an earlier period than the Pay cycle period end date, the Payroll Update will assign the G/L period end date of the period containing the transaction to the G/L entry.Note: The credit side of the job percent overhead costs post to
 the same General Ledger period, even when the period end date is in a
 different month from the check date and this field is set to Work date
 or Period-end date.
