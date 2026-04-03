---
title: "Equipment Control Installation - G/L Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-installation---gl-codes"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-installation---gl-codes"
---

# Equipment Control Installation - G/L Codes

Use this tab to set default G/L codes in the Equipment Control module.
Fields
Descriptions

Validate equipment division with G/L department?
Select this checkbox to validate the equipment division with the General
 Ledger department. If this checkbox is selected, the system will confirm
 that the Equipment Control division matches the G/L department in
 Equipment Control Transaction Entry for EU and ES revenue
 transactions. For example, if the G/L department is "02" for a given entry,
 the division of the equipment must also be "02."
Companies not using the departmentalization feature in the General Ledger should leave this checkbox clear.
This does not have any impact on the "use job division with G/L department"
 option found on the Job Cost Installation screen. Use this option
 when you desire that equipment revenue be charged to the department that
 "owns" the equipment.
Note: This checkbox only
 displays if cost centers are NOT being used in the current company.

Auto default G/L department?
Select this checkbox if you want the system to automatically default the General Ledger department code from the equipment division.
This option is available only if you have selected the Validate equipment
 division with G/L department checkbox. If this option is selected,
 then the equipment division will be used to default the general ledger
 department portion of the G/L code in Equipment Control Transaction
 Entry.
Note: This checkbox only
 displays if cost centers are NOT being used in the current company.

Depreciation cost, License cost,
 Insurance cost (G/L
 debit)
Enter the G/L account code(s) you plan to title "equipment depreciation
 expense", "license expense", "equipment insurance" (or similar names) in
 your Spectrum chart of accounts. Be sure to include these G/L account
 numbers when you enter your chart of accounts. Enter G/L account codes in
 these fields even if you do not have General Ledger module installed on your
 computer, if you wish to have the system default these G/L account codes
 when adding entries in Equipment Type File
 Maintenance. The system will only use these G/L account codes
 if the G/L fields in the equipment type file are blank.
The system will default the G/L account number(s) entered in these fields when
 you add equipment types. The codes then stored in Equipment Type
 File Maintenance will be utilized during equipment
 depreciation, license and insurance processing (Calculate DLI
 Costs) to determine where to debit monthly expense accrual
 amounts.

Depreciation cost, License cost,
 Insurance cost: (G/L
 credit)
Enter the G/L account code(s) you plan to title "accumulated equipment
 depreciation", "pre-paid license expense", "pre-paid insurance" (or similar
 names) in your Spectrum chart of accounts, or double-click on this field to
 select from a list of available codes. Be sure to include these G/L account
 numbers when you enter your chart of accounts. Enter G/L account codes in
 these fields (even if you do not have general ledger module installed on
 your computer) if you wish to have the system default these G/L account
 codes when adding entries in Equipment Type File
 Maintenance. The system will only use these G/L account codes
 if the G/L fields in the equipment type file are blank.
The system will default the G/L account number(s) entered in these fields when
 you add equipment types. The codes then stored in Equipment Type
 File Maintenance will be utilized during equipment
 depreciation, license and insurance processing (Calculate DLI
 Costs) to determine where to credit monthly expense accrual
 amounts.

Rental revenue credit G/L account code
Enter the G/L account code you plan to title "owned equipment rental revenue" or "equipment usage applied" (or similar name) in your Spectrum chart of accounts, or double-click on this field to select from a list of available codes. Be sure to include this G/L account number when you enter your chart of accounts. Enter a G/L account code in this field even if you do not have General Ledger module installed on your computer.
The system will use the G/L account number entered in this field during Update
 Payroll when non-job equipment usage is specified in Time Card Entry.
 Equipment revenue, based on recorded hours and rate, will debit the
 equipment G/L account code stored in the Payroll Department
 Expense Maintenance; the system will make the corresponding
 G/L credit entry based on the account code indicated in this field. In the
 Equipment Control module during Transaction Entry, the G/L account code
 specified here will default as the "credit" for rental transactions during
 entry. This G/L account code may not be your primary equipment revenue
 "income" account, particularly if accounts receivable module is installed in
 this company and income is recognized when the A/R invoice is updated.

Job revenue credit G/L account code
Enter the G/L credit account code you plan to title "owned equipment job revenue" or "equipment usage applied to jobs" (or similar name) in your Spectrum chart of accounts.

- Be sure to include this G/L account number when you
 enter your chart of accounts.

- Enter a G/L account code in this field even if you
 do not have the General Ledger module installed.

- This G/L code selected should not be the same as the
 direct equipment expense account and the "No direct cost" option must be
 selected in the G/L Master File Maintenance > Direct cost menu.

The system will use the G/L account number entered in this field during Update
 Payroll when job equipment usage is specified in the time card file.
 Equipment revenue, based on recorded hours and rate, will debit the
 equipment G/L account code stored in Payroll Department Expense
 Maintenance; the system will make the corresponding G/L
 credit entry based on the account code indicated in this field. In equipment
 control module during Transaction Entry, the G/L account code specified here
 will default as the credit for job transactions. This G/L account code may
 be the same account code specified for Post rental use
 from field, if desired.

Cost center inter-posting G/L account code
Enter the General Ledger account code to use for inter-company posting, double-click on this field to select from a list of available G/L codes, or press Enter to accept the system default.
Note: This field only displays if cost centers are being used in
 the current company.

Inter-company G/L account code
This prompt will only display if the Multi-company prompt on the
 Properties tab is selected.
To access this inter-company equipment G/L account code feature, enter the G/L
 account code you plan to title "inter-company receivable" (or similar name)
 in your Spectrum chart of accounts. This G/L account code may not be the
 same code designated elsewhere in the Equipment Control
 Installation. Be sure to include this G/L account number when
 you enter your chart of accounts. If no companies are entered here, the
 system will continue to use the one liability code already recorded on the
 Equipment Control Installation screen.
Entry in this field is not required if inter-company E/C transactions are not desired. The system will automatically update inter-company transactions to this G/L account code when you designate alternate company code(s) during Equipment Control processing.

Overrides buttons 1,2,3
When the cost center feature is enabled and the Enterprise Installation > Allow G/L account overrides
 by cost center checkbox is selected, these buttons display. Use these
 buttons to assign an override G/L account codes or review the current G/L
 account code overrides.

New/Edit/Delete
 buttons
Use these buttons to add, edit, or delete inter-company Gl/L account codes. In the G/L code column, enter the applicable G/L account code to be used in this company when inter-company equipment control transactions associated with the specified company are updated.

Related information

- [Multi-company processing in EC](/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-installation---gl-codes/multi-company-processing-in-ec)
