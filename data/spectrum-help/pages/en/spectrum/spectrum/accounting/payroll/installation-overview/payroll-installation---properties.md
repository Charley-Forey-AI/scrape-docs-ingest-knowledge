---
title: "Payroll Installation - Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---properties"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---properties"
---

# Payroll Installation - Properties

Select Payroll from the Installation list.
When the installation screen is selected for the first time, an installation dialog box
 displays on the screen. Once this installation screen has been completed and the
 information saved, the message will not appear again.
If you are setting up a new company, four basic employee status codes (Active, Inactive, Terminated, and Deceased) will be automatically set up by the software when this screen is completed. You can edit or add to these status codes later on while completing the Employee screen.
Fields
Descriptions

Require period start date on payroll cycle?
Select this checkbox to require that
 the user enter a payroll period start date.
Show pre-time card pay rates?
If you select this checkbox, the
 hourly pay rates are shown during Pre-Time Card Entry and on the Pre-Time Card
 Edit List.For security reasons, you may want to leave
 this checkbox blank so that hourly pay rates will not display. This is
 appropriate if you have a data entry person who does not have security for
 Time Card Entry or the associated listings. You can set this person up with
 security for only the Pre-Time Card Entry page and the associated listings,
 then that person could enter hours, but could not see the actual pay rates
 paid to your employees.

Multi-state job validation?
Select this checkbox to provide a
 warning message during Pre-Time Card Entry and Time Card Entry if the job file
 does not contain a state code in the "payroll tax codes" window. The software
 will provide a warning message stating that there is no state in the Job
 Maintenance, but will allow you to continue.Typically, if
 a company works in a single state, this checkbox will be left
 blank.

Recalculate pay rates during pre-time card update?
Select this checkbox to automatically
 recalculate pay rates during pre-time card update. If this checkbox is
 selected and you overwrite pay rates during Pre-Time Card Entry, the rate
 entered will NOT be retained during the transfer to Time Card Entry. Instead,
 the rate will be set based on the [Payroll Installation - Defaults](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---defaults) screen
 settings such as Default rate
 table and Default
 pay rate.
Multi-company payroll?
If this checkbox is selected, the
 software will allow you to specify an alternate company code. When you do this,
 the software will accept G/L and Job Cost codes from the other company and will
 update accordingly. The software will credit the liability and cash G/L account
 codes in the current company and debit the inter-company G/L account specified
 below. The payroll expense distribution will debit G/L (and job if applicable)
 in the other company, and credit the inter-company account code.

- If inter-company transactions are not desired, this
 checkbox should be clear.

- If this checkbox and the Is this a confidential payroll
 company field (see below) are selected, then the main
 company's employees will post in summary to the job (for example, PR
 summary and $$).

Cost Center Information
If
 cost centers are being used but multi-company processing is NOT being used
 in this company, a Cost center
 inter-posting G/L account code field replaces the Inter-company G/L account
 code field on the Payroll Installation - G/L Codes tab.


Is this a confidential payroll company?
Select this checkbox if this is a
 confidential payroll company.
Post confidential hours to Job Cost?
This checkbox is available only if the
 Is this a confidential payroll
 company checkbox is selected.
Confidential company
This field only displays if the
 Multi-company
 payroll and Is
 this a confidential payroll company checkboxes have been
 selected.Enter the company ID of your main company
 (for example, if the main company is XYZ and confidential payroll is
 performed from company XPR, on the installation screen of company XPR, enter
 "XYZ" in this field). This sets up the default for expense posting during
 Pre-Time Card Entry and Time Card Entry. This company ID is also where
 liabilities will post. The company ID entered here must be installed and you
 must have General Ledger in this company ID.

Accounts Payable invoice batch code
The payroll system allows A/P invoices
 to be automatically created for garnishments taken on employee checks. This
 batch code will be used on all A/P invoices created from deductions during
 Payroll Update. This allows all A/P invoices created from the Payroll system to
 be updated separately.
Next Accounts Payable invoice number
Enter the next A/P invoice number to
 use when posting to A/P from deductions. The payroll
 system allows A/P invoices to be automatically created for garnishments
 taken on employee checks. If this feature is used, then this sequence number
 will be used to ensure that each A/P invoice is created with a unique
 number. This sequence number will only be used for A/P invoices created from
 the Payroll system.

Descriptions for other pay types 1-3
The entries specified here will be
 shown on the Payroll check stub when any of these pay types (1, 2, 3, and SA)
 are used in Time Card Entry. Examples of possible user-defined earnings
 descriptions include BONUS, TRUCK and EDUC. Descriptions may be any combination of letters and
 numbers, up to 6 characters.More info If you are
 initializing the Payroll module and are unsure what special uses you may
 assign these pay types in the future, enter OTHER1, OTHER2, and OTHER3. You may return to
 this page as necessary to define the descriptions for these pay types.


Descriptions for special amount pay type
Enter the special amount pay type
 description. The entries specified here will be shown on the payroll check stub
 when any of these pay types (1, 2, 3, and SA) are used in time card entry.
 Examples of possible user-defined earnings descriptions include BONUS, TRUCK and EDUC. Descriptions may be any
 combination of letters and numbers, up to 6 characters. If you are initializing
 the Payroll module and are presently unsure what special uses you may assign
 this pay type in the future, the following descriptions is recommended:
 SPEC. You may
 return to this screen as necessary to define the descriptions for these pay
 types; the software utilizes information stored in these fields at the time
 checks are printed.
Incentive pay code
Enter the character you want to
 designate for incentive pay. This character will then be added to the pay types
 R, O, or D (regular, overtime, double
 time), for use in the Pre-Time Card Entry, Time Card Entry, and Layoff Check
 Entry screens. For example, if the character is "I" then the regular
 incentive code would be IR, and so forth). The character can be different for different
 companies.Protection is incorporated into this page to
 prevent use of an incentive pay code that would conflict with existing
 Payroll deduction or add-on codes. For example, if the code JR was already
 set up as a deduction code, J would not be permitted as an incentive code in this field.


Next crew number
Enter the first crew number that should
 appear in the sequence when setting up new crews.
Create transactions to distribute overtime among jobs on paycheck?
Select this checkbox if you want to
 redistribute job overtime across all jobs included in the employee's paycheck.
 This allows you to automatically reallocate overtime so that the last job(s) of
 the day/week are not charged all of the overtime. This
 feature exclusively reallocates the time card extension for Job entries, but
 not hours. Also, this feature does not reallocation overtime charged to
 non-job payroll departments.
When this option has
 been selected, the Payroll Update includes an additional step during the
 update to generate Job Cost transactions, backing out time card amounts
 charged as overtime (or double time) and then reallocating the total across
 all job-related time cards on the particular paycheck, based on hours
 worked. Because this procedure is simply reallocating cost, the net effect
 across transactions generated during the update will be zero. The date
 assigned to these 'JC' transactions will match the period end date of the
 pay cycle.

Auto-number employee codes?
Mask
Next employee code
Auto-number employee codes:
 Select this checkbox to automatically apply sequential numbering to employee
 codes.Mask: Enter a mask up to 11 characters long.
Next
 employee code: Enter the first employee code that should
 appear in the sequence when creating new employee codes or press Enter to accept the
 software default, which is based on the next employee value variable and
 the Mask (for
 example, if the next employee number is 30 and the mask AXXXX, the next
 employee code will be A0030). If you designate the next employee code rather
 than accept the default, the code you designate cannot consist of more
 characters than what is allowed by the designated Mask.
This number will automatically increase incrementally
 whenever an employee code is assigned in Payroll > Employees or in Human Resources > New Hire Entry.

Non-US payroll processing?
Select this checkbox if you want to
 specify a federal tax code other than 'US', and to allow changes to be made to
 the Federal tax code field in the [Employee Tax Setup](/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-tax-setup)
 screen. After you specify a Federal tax code, this code will be assigned
 automatically when a new employee is added. This allows
 Payroll Managers to set up a code (such as CN) that is meaningful to their
 operations and does not contain special calculations and labels.
Note: While this checkbox is clear, the Employee Tax Setup
 will not allow access to the 'Federal tax code' field.

Default Federal tax code for new employee
Specify a tax code that will default
 for employees; up to 10 characters are allowed. This
 field only displays if the Allow non-US payroll processing checkbox is
 selected.

Payroll reporting
From the available drop-down list,
 select the country where payroll will be processed. This
 selection controls the check formatting in all modules. When the 'Canada'
 designation is selected, all Payroll, Accounts Payable, and Cash Management
 checks will be reformatted to display dates in the required format (in
 compliance with the Canadian Payments Association) and verbiage will be
 altered to reflect the Canadian lexicon (that is, cheques).

Accrue expense to

- If you select the 'Check date' option all G/L
 entries will be posted based on the check date of the payroll cycle, and
 expenses will post to General Ledger and Job Cost.

- If you select the 'Period-end date' option expenses
 will be recorded in the General Ledger based on the period-end date of
 the pay cycle; the liabilities and cash outlay will be recorded on the
 check date. An accrued payroll G/L account code will be used in this
 case; this G/L account code will be credited on the period-end date of
 the payroll cycle, and debited in the same amount on the check date. In
 addition, if the Period-end
 date option is specified, the transaction date in Job Cost
 and Equipment Control files will be the period-end date; if the
 Check date
 option is selected, the transaction date will be the payroll
 check date.

- If you select the 'Work date' option it will post to
 Job Cost history using the work date. For G/L it is similar to the
 Period-end date
 option: liabilities and cash outlay post to the G/L check
 date, and expenses post to the period ending date. However, if the work
 cycle goes over a month end, then the Payroll Update will split and post
 expenses in two postings – one on the last day of the previous month and
 one on the period ending date. Furthermore, if the Work date option is
 selected, for a Direct Job Cost time card entry or Direct Work Order Cost
 time card entry, the software stores the work date of the time card line
 as the Transaction
 date in Job Cost History or Work Order Actual Cost
 History, respectively. The date assigned to this transaction in G/L is
 dependent upon whether or not the transaction date is in a period earlier
 than the Pay cycle period
 end date: If the transaction date is in the same period as
 the Pay cycle period end
 date, the Payroll Update will assign the pay period end
 date to the G/L entry. If the transaction date is in an earlier period
 than the Pay cycle period
 end date, the Payroll Update will assign the G/L period
 end date of the period containing the transaction to the G/L entry. Note: The credit side of the job percent
 overhead costs post to the same General Ledger period, even when the
 period end date is in a different month from the check date and this
 field is set to Work date or Period-end date.

Related information

- [Setting Up Bonus Checks in Payroll Installation](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---properties/setting-up-bonus-checks-in-payroll-installation)
