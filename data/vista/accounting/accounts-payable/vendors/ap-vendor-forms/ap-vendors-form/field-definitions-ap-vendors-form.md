---
title: "Field Definitions: AP Vendors Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form/field-definitions-ap-vendors-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form/field-definitions-ap-vendors-form"
---

# Field Definitions: AP Vendors Form

The following is a list of field descriptions for the AP
 Vendors form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Vendor

Enter a number, up to 6 digits, to identify this vendor or enter ‘+’ to have the system automatically assign the next sequential number.
Note: If the system determines that the next value exceeds
 the maximum value allowed (999999), you will receive a message that you must manually enter
 a number lower than the maximum.
Tip: When searching for an existing vendor, if you do not
 know the vendor’s number, enter up to 15 characters of the sort name. The system locates
 the first vendor matching the entered characters.

## Name

The Name field on the AP Vendors form, Info tab.
Enter the vendor's name, up to 80 characters, as you want it printed on computer-generated checks and reports.
Note: If you elected to update changes to PM (flag in PM
 Company Parameters), changes to this field will be updated to the corresponding field in PM
 Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will be updated here.

## Sort Name

Enter the sort name for this vendor, up to 15 characters. This field automatically defaults to the first 15 characters of the vendor’s name entered above.
Note: This sort name defaults to all caps, regardless of
 how the vendor name was entered and cannot be changed from all caps. Entry in posting
 programs can be done by sort name, so maintaining all caps for this name allows the system
 to find the correct vendor without being hindered by case sensitivity.
You can override the default, but you might only do this in the case that the sort name is alphabetically incorrect. For example, if the vendor’s name were J. Smith Electric, you would probably enter the sort name as Smith, J.
The sort name must be unique. If the default provided is the same as that of an existing vendor, a message will be given that the sort name is already in use by another vendor and a different sort name will be required. It is recommended that the last characters may be changed to make the sort name unique.
The system uses this sort name for alphabetical sorting, such as on reports and lookups (F4). Vendor input fields will allow entry of either the vendor number or the vendor sort name. If entering the vendor sort name, the software will automatically switch to the vendor number. Because of this feature, it is important not to enter all numerics into the vendor sort name field.
You can change sort name, even after transactions have been posted. If you change a sort name for any given vendor, the system automatically cycles through all existing transactions for that vendor and adjusts the appropriate records accordingly.
Note: If you elected to update changes to PM (flag in PM
 Company Parameters), changes to this field will be updated to the corresponding field in PM
 Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will be updated here.

## Contact

Enter the contact person for this vendor, up to 30 characters.
Note: If you elected to update changes to PM (flag in PM
 Company Parameters), changes to this field will be updated to the corresponding field in PM
 Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will be updated here.

## Phone

Enter the vendor’s phone number, up to 20 characters. Dashes must be entered manually.
Note:If you elected to update changes to PM (flag in PM Company Parameters), changes to this field will be updated to the corresponding field in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters), changes to the corresponding field in PM Firms will be updated here.

## Fax

Enter the vendor’s Fax number, up to 20 characters. Dashes must be entered manually.
Note: If you elected to update changes to PM (flag in PM
 Company Parameters), changes to this field will be updated to the corresponding field in PM
 Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will be updated here.

## Active

Check this box if this vendor is currently
 active (i.e. new transactions, POs, and Subcontracts can be entered for this vendor).
Do not check this box if this vendor is not
 active (no new transactions may be posted; only existing entries can be edited or deleted).
 This does not affect payments.

## Temporary

Select this checkbox if this is a temporary
 customer. If designated as temporary, this vendor may be removed from AP files once the
 last of his/her paid transactions is purged (in AP Purge).
Leave this checkbox unselected if this vendor
 is not temporary.

## Selective Purge

 Check this box if this vendor’s paid transactions will be kept on file when purging paid transactions from AP files. Paid transactions for this vendor will be deleted only if this vendor is specifically selected in the AP Purge program.
 Do not check this box if you want this vendor’s paid transactions to be purged with other paid transactions. This option is not available for temporary vendors.

## Account Number

Account Number field in the AP Vendors form.

This field is optional.
Enter the number this vendor has assigned to your company. It may be any series of up to 30 alphanumeric characters.
If you use ePayments to pay this vendor, your entry in this field helps the vendor link the payment to your company.
[AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form)

## Master Vendor

The Master Vendor field on the AP Vendors form, Info tab.
Enter the master vendor (from AP Vendors) for this vendor. Entering a
 master vendor here will make this vendor a sub vendor. The master vendor specified here
 cannot exist as a sub vendor. Likewise, this sub vendor cannot exist as a master vendor for
 another vendor.
Note: Using the master/sub vendor feature allows you to
 check for duplicate AP reference numbers within a master/sub vendor group.

## Vendor Type

Regular – Select this option if this vendor can be used when posting POs, Subcontracts, and regular invoices. Regular vendors may be suppliers too.
Supplier – Select this option if this vendor can only be used as the 2nd party on 2-party checks.

## Subcontractor

Subcontractor checkbox in the AP Vendors form.

This checkbox is optional.
Select this checkbox to affirm this vendor is a Subcontractor, and not another type of vendor.
Each time you use ePayments to pay this vendor, the system includes this designation in the data file that you generate.

## Payment Terms

 Specify the default payment terms (from HQ Payment Terms) that will be used when posting transactions (AP Transaction Entry, AP Recurring Invoices) for this vendor.

## Tax Code

Specify the default tax code to be used when posting non-job (Expense,
 Work Order, and Equip) purchase order items and transactions. Tax codes for job-related
 transactions will default from the JC Jobs.
Note: The Tax code specified here is used for Sales or Use
 tax, whichever is designated at the time of the transaction’s entry.

## GL Account

 Specify the default GL account to use when posting expense transactions for this vendor. May be overridden.

## CM Account

The CM Account field in the AP Vendors form.
Entry not required.
Enter a CM account only if you want the system to use this account by default when you create invoices for this vendor. You may opt to do this if you pay certain groups or types of vendors from only certain CM Accounts.
If you enter a CM account that is not on file
 with any AP Company that shares the assigned vendor group, the system prevents entry.
Considerations if your vendor master is shared across multiple companies
If you are sharing the vendor master across multiple
 companies (using a shared vendor group), make sure that
 the CM account that you specify exists in all
 companies, or the system may display errors and
 prevent saving when you process transactions using any of the these forms: AP
 Transaction Entry, AP Unapproved Invoice Entry, AP
 Recurring Invoices, MS Material Payment Worksheet, and
 MS Haul Payment Worksheet.
For example, let's say that you have two
 companies set up this way:

- APCo #1 uses CMCo #1 and is associated with
 Vendor Group #24

- APCo #24 uses CMCo #24 and is associated with
 Vendor Group #24

Now, let's say that for Vendor #1000, a
 user enters 250 in the CM
 Account field while in APCo #24. The problem in this case is that CM account number 250 does not exist for
 APCo #1.
The problem becomes apparent when another user creates a transaction in the AP
 Transaction Entry form in APCo #1, and specifies Vendor
 #1000: a warning displays and the system prevents the
 user from saving the record. The remedy is to either create CM
 account 250 in APCo #1 or use a CM Account that exists in both companies.

Related concepts

- [About Sharing the Vendor File](/en/vista/vista/accounting/accounts-payable/vendors/about-sharing-the-vendor-file)

## Last Invoice Date

Indicates the latest date posted on an invoice
 transaction for this vendor. This date is updated each time an invoice transaction is
 posted to a date later than the one indicated here.

## Payment Address: Add'l Info

Enter additional information, up to 60
 characters, to be printed on checks for this vendor (e.g. Attention line, Garnishment Case
 #, etc.).
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Payment Address: Address

Enter the street address for this vendor, up to 60 characters. This address will print on all checks paid to this vendor, and is used when printing 1099 forms.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- If you elected to update changes to PM (flag in PM Company Parameters), changes to this field update to the corresponding field in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters), changes to the corresponding field in PM Firms will update here.

## Payment Address: City

Enter the city name, up to 30 characters.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- If you elected to update changes to PM (flag in PM
 Company Parameters), changes to this field update to the corresponding field in PM
 Firms. Likewise, if you elected to update changes from PM (flags in AP Company
 Parameters), changes to the corresponding field in PM Firms will update here.

## Payment Address: State

Enter a valid state (as defined in HQ States).
 The system validates the state based on the Default Country specified in HQ Company
 Setup for the active company. If not valid, an error displays, but entry is allowed. You
 must then enter a valid country for this state in the Country field.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- If you elected to update changes to PM (flag in PM Company Parameters), changes to this field update to the corresponding field in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters), changes to the corresponding field in PM Firms will update here.

## Payment Address: Zip Code

Enter the zip code, up to 12 characters.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- If you elected to update changes to PM (flag in PM Company Parameters), changes to this field update to the corresponding field in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters), changes to the corresponding field in PM Firms will update here.

## Payment Address: Country

Enter the 2-character country code. Entry in this field is required when the address exists outside the default country specified in HQ Company Setup for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in the HQ States form.
If you need to enter a vendor from a foreign
 country, enter the country in this field prior to the rest of the address. This enables the
 proper lookup and validation for the State field.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- If you elected to update changes to PM (flag in PM Company Parameters), changes to this field update to the corresponding field in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters), changes to the corresponding field in PM Firms will update here.

## Payment Address: Additional Address

Use this field to enter additional address information for this vendor (up to 60 characters). For example, if the vendor receives mail at a P.O. Box, then you might enter the P.O. Box in the Payment Address field above, and use this field to enter the street address.
The address information entered here is not used by any of the posting programs, but may be used on certain reports.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- If you elected to update changes to PM (flag in PM Company Parameters), changes to this field update to the corresponding field in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters), changes to the corresponding field in PM Firms will update here.

## Purchasing Address: Address

Enter the street address for this vendor, up to 60 characters.
 This address is used when printing purchase orders for this vendor. Initially defaults the
 same address entered above.

- If you have Internet access, you can click the Map button
 for direct access to the default map site for your login (as defined in User Options,
 Main Menu). The selected map site will default the approximate location of the
 specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ Company Setup.

- If you elected to update changes to PM (flag in PM Company
 Parameters), changes to this field update to the corresponding field in PM Firms.
 Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will update here.

## Purchasing Address: City

Enter the city name, up to 30 characters. Initially defaults the
 same city entered above.

- If you have Internet access, you can click the Map button
 for direct access to the default map site for your login (as defined in User Options,
 Main Menu). The selected map site will default the approximate location of the
 specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ Company Setup.

- If you elected to update changes to PM (flag in PM Company
 Parameters), changes to this field update to the corresponding field in PM Firms.
 Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will update here.

## Purchasing Address: State

Enter a valid state (as defined in HQ States). The system
 validates the state based on the Default Country specified in HQ Company Setup for the
 active company. If not valid, an error displays, but entry is allowed. You must then enter
 a valid country for this state in the Country field.

- If you have Internet access, you can click the Map button
 for direct access to the default map site for your login (as defined in User Options,
 Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default
 Country specified in HQ Company Setup.

- If you elected to update changes to PM (flag in PM Company
 Parameters), changes to this field update to the corresponding field in PM Firms.
 Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will update here.

## Purchasing Address: Zip Code

Enter the zip code, up to 12 characters. Initially defaults the
 same zip code entered above.

- If you have Internet access, you can click the Map button
 for direct access to the default map site for your login (as defined in User Options,
 Main Menu). The selected map site will default the approximate location of the
 specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ Company Setup.

- If you elected to update changes to PM (flag in PM Company
 Parameters), changes to this field update to the corresponding field in PM Firms.
 Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will update here.

## Purchasing Address: Country

Enter the 2-character country code. Entry in this field is
 required when the address exists outside the Default
 Country specified in HQ Company Parameters for the active company. Country
 must be valid for the specified state (e.g. state, province, territory, etc.) as defined in
 HQ States.

- If you have Internet access, you can click the Map button
 for direct access to the default map site for your login (as defined in User Options,
 Main Menu). The selected map site will default the approximate location of the
 specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ Company Setup.

- If you elected to update changes to PM (flag in PM Company
 Parameters), changes to this field update to the corresponding field in PM Firms.
 Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will update here.

## Purchasing Address: Additional Address

Use this field to enter additional address information for this
 vendor (up to 60 characters). For example, if the vendor receives mail at a P.O. Box, then
 you might enter the P.O. Box in the Purchasing Address field above, and use this field to
 enter the street address.
The address information entered here is not used by any of the
 posting programs, but may be used on certain reports.

- If you have Internet access, you can click the Map button
 for direct access to the default map site for your login (as defined in User Options,
 Main Menu). The selected map site will default the approximate location of the
 specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ Company Setup.

- If you elected to update changes to PM (flag in PM Company
 Parameters), changes to this field update to the corresponding field in PM Firms.
 Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will update here.

## Business Number (ABN)

Enter the Australian Business Number (ABN) for this vendor. This field is used for reporting purposes.
Note: The system displays this field when the current
 company's country is set to Australia in HQ Company Setup.
ABNs can be entered as 11 consecutive digits, or as 11 digits with a space separating the 2nd and 3rd digits, the 5th and 6th digits, and 8th and 9th digits (e.g. ## ### ### ###).
ABNs must be unique per vendor within a vendor group.

## ACN

Enter the Australian Corporate Number for the vendor. This field is used for reporting purposes.
Note: The system displays this field when the current
 company's country is set to Australia in HQ Company Setup.

## Subject to 1099 Reporting

The Subject to 1099 Reporting checkbox on the AP Vendors form, Add'l Info tab.
This field's title changes based on the Default Country setting in HQ Company Setup. Click the links below for more information.

- Australia: [Subject to Taxable Payments Reporting](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form/field-definitions-ap-vendors-form#ID-00051c66--en)

- Canada: [Subject to T5018 Reporting](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form/field-definitions-ap-vendors-form#ID-00051c6f--en)

This checkbox defaults as selected for all new vendors.
Select this checkbox if payable transactions for this vendor are subject to 1099 reporting. If selected, the '1099' fields are enabled during transaction entry (AP Transaction Entry, AP Recurring Invoices, and AP Unapproved Invoice Entry) and will default the information set up here. You may override this setting during transaction entry.
Do not select this checkbox if payable transactions for this vendor are not normally subject to 1099 reporting. All transactions posted to this vendor are automatically flagged as not subject to 1099 reporting, and no 1099 totals are accumulated. You may override this setting during transaction entry.
Note: If you are unsure as to whether a vendor is subject to 1099 reporting, it is best to set this flag to Y (selected). This ensures that all transactions posted to this vendor are automatically flagged to be included in the vendor's 1099 totals. If you later learn that this vendor is not subject to 1099 reporting, you can change this flag to N (unselected), and no 1099 will print. You do not need to change any transactions. They will show on the "AP 1099 Report", but will include a message stating that 'transactions subject to 1099 report exist, but no 1099 form will print'.


### Subject to T5018 Reporting

(CA only) The Subject to T5018 reporting checkbox on the AP Vendors form, Add'l Info tab.
Select this checkbox if this vendor is subject to T5 reporting.
Typically, you will select this checkbox when you need to report payments to subcontractors using the T5018. When selected, the system automatically sets each invoice created for the vendor to be included in T5018 totals. You can override this setting at the invoice level as necessary.
Note: Selecting this checkbox requires entry of the vendor's GST Business number (Business # field).

If you leave this checkbox unselected, the system automatically sets transactions posted to this vendor as not subject to T5018 reporting.
For more information, see [Set Vendors Subject to T5018 Reporting (Canada)](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/set-vendors-subject-to-t5018-reporting-canada) or [About T5018 Reporting: Canada](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/about-t5018-reporting-canada).

### Subject to Taxable Payments Reporting

Check this box if this vendor/subcontractor is
 subject to Taxable Payments reporting. Once you check this box, the system will
 automatically check the Include in payment reporting box in AP
 Transaction Entry (Payment Overrides tab), AP Unapproved Invoice Entry (Payment Overrides
 tab), and AP Recurring Invoices for all vendors set as subject to Taxable Payments.
For more information on taxable payments, see [Generating Taxable Payments Annual Reports](/en/vista/vista/accounting/accounts-payable/year-end-reporting/taxable-payment-reporting/generate-taxable-payments-annual-reports-australia).

## Mailing Address Seq

### For United States users

The system enables this field when
 you check the Subject to 1099
 reporting box.
If you need to send the
 1099 to an address other than the payment address specified for
 the vendor on the Info tab of AP Vendors, enter the address
 sequence or press F4 to
 see a list of address sequences. These sequences are maintained
 on the Add'l Addresses tab of AP Vendors. If you enter a
 sequence in this field, the system will use the associated
 address when printing 1099s or when you generate an electronic
 file with AP 1099 Download. For more information, see [Setting Vendors Subject to 1099
 Reporting](/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/set-vendors-subject-to-1099-reporting-united-states).

### For Australian users

The system enables this
 field when you check the Subject to Taxable
 Payments Reporting box.
If you need to send the
 Taxable Payments report to an address other than the payment
 address specified for the vendor on the Info tab of AP Vendors,
 enter the address sequence or press F4 to
 see a list of address sequences. These sequences are maintained
 on the Add'l Addresses tab of AP Vendors. If you enter a
 sequence in this field, the system will use the associated
 address when when you generate an electronic file. For more
 information, see [Generating Taxable Payments
 Annual Reports](/en/vista/vista/accounting/accounts-payable/year-end-reporting/taxable-payment-reporting/generate-taxable-payments-annual-reports-australia).

### For Canadian users

The system enables this
 field when you check the Subject to T5018 reporting box.
If you need to send T5018
 slips, summaries, or electronic files to include an address
 other than the payment address specified for the vendor on the
 Info tab of AP Vendors, enter the address sequence or press
 F4 to
 see a list of address sequences. These sequences are maintained
 on the Add'l Addresses tab of AP Vendors. If you enter a
 sequence in this field, the system will use the associated
 address when you generate an electronic file. For more
 information, see [Generating T5018
 Reports](/en/vista/vista/accounting/accounts-payable/year-end-reporting/t5018s/about-generating-t5018-reports).

## 1099 Type

(US only) The 1099 Type field on the AP Vendors form, Add'l Info tab.
Specify the 1099 type to use for tracking payable amounts subject to 1099 reporting for this vendor.
Although you can accumulate totals under any 1099 type, if 1099 amounts for this vendor are to be included when printing 1099s or creating 1099 electronic files, you can only use 1099 types of “MISC” (Miscellaneous Income), “INT” (Interest Income), or “DIV” (Dividends/Distributions).

## Box#

(U.S. only) The Box # field on the AP Vendors form, Add'l Info tab.

Enter the box number for accumulating and printing 1099 amounts for this vendor. Press F4 to select from a list of valid boxes
 on the 1099 form.
 You may override this setting during transaction entry (in AP Transaction Entry, AP Unapproved Invoice Entry, and/or AP Recurring Invoices).

## Tax ID#

Specify this vendor’s federal tax identification number, which will print on
 the 1099 form. You can enter either the vendor's Social Security Number
 or Employer Identification Number. Then use the drop-down to the right to
 identify the number you entered here.Note: If the tax identification
 number already exists for another vendor, a message displays
 warning you that number is already in use, and by what
 vendor.

## EIN / SNN

The E - EIN / S - SSN drop-down is on the AP Vendors form,
 Add'l Info tab.
 Select one of the following options to identify the value entered in the Tax ID # field for this vendor.

- S - SSN - The vendor's Social Security Number.

- E - EIN - The vendor's Employer Identification Number.

Enter the corresponding value in the Tax ID field for
 the vendor.
Note: Both options are nine digit numbers. Do not use dashes or slashes for either option.

## Proprietor

The Proprietor field on the AP Vendors form, Add'l Info tab.
Enter the proprietor's (owner's) name, if any, to be included on the 1099 form. You must enter the name as "Last Name, First Name" to enable proper 1099 electronic filing. Up to 80 characters allowed.
This name, along with the vendor's name, is used to aid in Tax ID# reconciliation, and is typically used when an individual is to receive the 1099, but uses a business name for other purposes.

## First Name

(United States) The First Name field on the AP Vendors form, Add'l Info tab.

This field is only enabled when the Subject to 1099 reporting checkbox is selected and the Tax ID type is set to S - SSN.
Required.
Enter the proprietor's first name. When processing 1099s via Aatrix, the system includes this name in the generated e-file.

## Middle Initial

(United States) The Middle Initial field on the AP Vendors form, Add'l Info tab.

This field is only enabled when the Subject to 1099 reporting checkbox is selected and the Tax ID type is set to S - SSN.
Enter the proprietor's middle initial. When processing 1099s via Aatrix, the system includes this initial in the generated e-file.

## Last Name

(United States) The Last Name field on the AP Vendors form, Add'l Info tab.

This field is only enabled when the Subject to 1099 reporting checkbox is selected and the Tax ID type is set to S - SSN.
Required.
Enter the proprietor's last name. When processing 1099s via Aatrix, the system includes this name in the generated e-file.

## Include in 1099 Processing (Ignore Minimum)

Check this box if this vendor's 1099 totals
 should be included when processing or printing 1099s, regardless of the "Minimum Payment
 Amount" (AP 1099 Report).
Do not check this box if you do not want to
 print a 1099 for this vendor if the 1099 totals are below the minimum payment amount.

## 1099 Email Consent

(United States only) The 1099 Email Consent checkbox on the AP Vendors form, Add'l Info tab.

This checkbox is only enabled if the Subject to 1099 reporting checkbox is selected.
Select this checkbox if this vendor has consented to receive 1099s electronically (via email). This requires that you enter an email address for the vendor in the Email Address field.
Leave this checkbox unselected if the vendor has not consented to receive 1099s electronically. Instead, the vendor will receive printed 1099s.
The setting defined here defaults for the vendor in AP 1099 Processing, but may be overridden by tax year and 1099 type.

## Business Type Code

This field displays when the current company's
 country is set to Canada in HQ Company Setup (Default Country field).
Select the correct business type for this vendor:

- Individual

- Corporation

- Partnership

## First

(Canada) The First field on the AP Vendors form, Add'l Info tab.
This field displays when the current company's
 country is set to Canada in HQ Company Setup (Default Country field).
Enter the first name of the proprietor.

## Middle Initial

(Canada) The Middle Initial field on the AP Vendors form, Add'l Info tab.
This field displays when the current company's
 country is set to Canada in HQ Company Setup (Default Country field).
Enter the middle initial of the proprietor.

## Last

(Canada) The Last field on the AP Vendors form, Add'l Info tab.
This field displays when the current company's country is set to Canada in HQ Company Setup (Default Country field).
Enter the last name of the proprietor.

## SIN

This field displays when the current company's
 country is set to Canada in HQ Company Setup (Default Country field).
Enter the Social Insurance Number (SIN) for the proprietor.

## Business #

(CA only)The Business # field on the AP Vendors form, Add'l Info tab.
This field only displays for Canadian companies and requires entry when the Subject to T5018 reporting checkbox is selected.
Enter the Goods and Service Tax Account number for this vendor, using the 9-digit + 2 alpha characters + 4-digit format (for example, 123456789AB1234).
Note: The system allows you to enter 9 digits (representing the vendor's business number), but displays a warning. However, it will allow you to save the record.

## Partnership FIN

This field displays when the current company's
 country is set to Canada in HQ Company Setup (Default Country field).
Enter the vendor's partnership filer identification number. The format for this number should be 2 alpha characters + 7 digits (e.g., AB1234567).

## Create a Separate Payment Per Transaction

Check this box to have all transactions entered for this vendor (in AP Transaction Entry, AP Unapproved Invoice Entry, or updated from PR AP Update) automatically flagged for separate payment. When checked, and transactions are entered for this vendor, the “Separate Payment” flag will automatically be set to Y (checked). Default may be overridden at time of entry.
Do not check this box if you do not want transactions entered for this vendor to automatically be flagged for separate payment.

## Override Unique APRef Level

The Override Unique APRef Level field on the AP Vendors form, Add'l Info tab.
Select one of the following options to indicate how to handle validation for duplicate AP Reference numbers (entered in AP Transaction Entry, AP Unapproved Invoice Entry) for this vendor. Validation levels set here override the validation level defined for the company (AP Company Parameters).

- 0-No Override — Do not override validation option specified for the company in AP Company Parameters.Note: If you set the company validation level to 1-By Vendor & Co or 2-By Vendor, Cross-Co, and this vendor is not set up as a master vendor or sub vendor, the validation process will assume this vendor as its own master vendor and include it when checking for duplicate numbers.

- 1-By Vendor & Co — Check for duplicate reference numbers for vendor within the current company. If a duplicate number is entered for this vendor in the current company, display a warning and only allow entry if the Prevent duplicate AP Reference checkbox in AP Company Parameters is unselected.

- 2-By Vendor, Cross-Co — Check for duplicate reference numbers for vendor across companies. If a duplicate number is entered for this vendor in any company sharing this vendor's vendor group, display a warning and only allow entry if the Prevent duplicate AP Reference checkbox in AP Company Parameters is unselected..

- 3-By Master Vendor & Co — Check for duplicate numbers for master vendor/sub vendor and company. If this vendor is a master or sub vendor, and a reference number is entered that already exists for this vendor or any vendor in the master/sub vendor group in the current company, display a warning and only allow entry if the Prevent duplicate AP Reference checkbox in AP Company Parameters is unselected.. This option is only applicable if you are using master vendors and sub vendors.

- 4-By Master Vendor, Cross-Co — Check for duplicate numbers for master vendor/sub vendor and company. If this vendor is a master or sub vendor, and a reference number is entered that already exists for this vendor or any vendor in the master/sub vendor group in any company sharing this vendor's vendor group, display a warning and only allow entry if the Prevent duplicate AP Reference checkbox in AP Company Parameters is unselected. This option is only applicable if you are using master vendors and sub vendors.

## Customer

 If this vendor is also one of your customers, you can cross-reference this by entering a valid AR Customer number in this field.

## Reviewer

 Enter the default reviewer for this vendor. This reviewer defaults for all line type transactions entered in AP Unapproved Invoice Entry referencing this vendor. The reviewer may be overridden during transaction entry.

## Email Address

Enter this vendor’s email address, if
 applicable.
Note: Clicking the Send button (to the right of this field)
 will automatically open up Microsoft Outlook and set up an outgoing message for you using
 the email address specified in this field.
If you elected to update changes to PM (flag
 in PM Company Parameters), changes to this field will be updated to the corresponding field
 in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company
 Parameters), changes to the corresponding field in PM Firms will be updated here.

## Internet Address

Enter this vendor’s Internet address, if applicable. Up to 60 characters allowed. This field is informational only.
Clicking the Go button () to the right of this field will take you directly to the Web site indicated in this field.
Note: If you elected to update changes to PM (flag in PM
 Company Parameters), changes to this field will be updated to the corresponding field in PM
 Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters),
 changes to the corresponding field in PM Firms will be updated here.

## Method of Payment Info Delivery

Select a following delivery option for sending payment information to the vendor by Email (when you use the [AP Email Pay Info](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-email-pay-info-form) form):

- N-None – The vendor will not receive an email after
 you print checks or download EFTs, even if you perform a send action using the AP
 Email Pay Info form.

- A-Email with attachment – The vendor will receive an
 email with the payment information report attached. The type of payment report
 depends on the entries in the Check Print Report Title by Vendor
 and EFT
 Remittance Report Title by Vendor fields in the [AP Company Parameters](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form) form. If you select this
 option, you must enter an email address in the Email Address field. Additionally,
 you must be attaching payment reports to payment history records. For more
 information, see [Setting Payment Information](/en/vista/vista/accounting/accounts-payable/ap-company-setup/set-up-an-ap-company/payment-reporting-information).

- E-Email as notification – The vendor will receive an
 email, but it will not include an attachment. If you select this option, you must
 enter an email address in the Email Address field.

## Sync to ProjectSight

The Sync to ProjectSight checkbox on the AP Vendors form, Add'l Info tab.
Important: Only if you have a legacy integration with ProjectSight, use this checkbox to sync records. If you have the current integration, this checkbox is *not used at this time*. For information about syncing records with the current integration, see [ProjectSight Integration with Vista](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:vista_60033).

Select this checkbox to sync this vendor to ProjectSight . When selected, the system sends the vendor record to ProjectSight as a company.

## Pay Control

Enter the pay control code for this vendor.
Note: Pay control codes group invoices together for
 payment. For example, you could code all loan payments with the same control code. Then,
 when initializing the payment batch, you can select all invoices with that pay control
 code. For subcontract invoices, you might use the owner’s application number to facilitate
 the “pay when paid” process (the SL Worksheet updates this field for that purpose).

## AP Invoice Lines Subject to On-Cost
 Default

Subject to On-Cost -
 Select this checkbox if this subcontractor/vendor is subject to on-cost. When selected, the
 system auto-selects the Subject to On-Cost checkbox for each invoice
 line entered for this vendor in AP Transaction Entry. Once you select this checkbox here, the
 system enables the JC
 Cost Type field.
JC Cost Type - If you
 want to specify a cost type for generating on-cost invoices, enter the cost type in this field
 or press F4 to select from a list of valid cost types. When you enter an invoice line
 for this subcontractor in AP Transaction Entry, the cost type in that form must match the one
 you specify here, or the system automatically deselects the Subject to On-Cost
 checkbox for that line; however, you will be able to re-check the box if necessary.
By entering a cost type here, you can set a
 specific cost type to use for subcontractors whom you are paying burden/on-cost amounts. For
 all other job cost types you enter in AP Transaction Entry, the system will not generate
 on-cost invoices. If you do not enter a cost type here, the system automatically selects the
 Subject to
 On-Cost box in AP Transaction Entry for every invoice line associated with this
 subcontractor.

## Valid Clearance Certificate

Check this box if the vendor/subcontractor has a valid clearance certificate. If you do not check this box, the vendor will display on the AP Worker Comp Liabilities for Subcontractors report. The report allows you to identify the dollars paid to the vendor/subcontractor for actual labor. You can then calculate and pay the worker's compensation liability.

## Clearance Cert #

Enter the workers compensation clearance certificate number for this vendor/subcontractor.

## Effective Date

Enter the effective date for the vendor/subcontractor's clearance certificate.

## Pay Method

The Pay Method field on the AP Vendors form, Payment Method tab

Select a default payment method for the vendor:

- N-ePayments (U.S. only) - If you elect to use this method, you must meet certain setup requirements before you can generate and upload an ePayments file. For more information, see [AP ePayments Export Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-epayments-export-form).

- C-Check

- E-EFT - When selected, the system enables the EFT Info field.

- S-Credit Service - If you elect to use this method, you must specify the credit service to use (Comdata or EFS) in AP Company Parameters, Payment Services tab.

The system uses the method you select here as the default entry in the Pay Method field in all AP transaction forms (AP Transaction Entry, AP Unapproved Invoice Entry, and AP Recurring Invoices).

## PR Co

The PRCo field in the AP Vendors form, Payment Method
 tab.
This field is read-only. It displays the PR Company of the employee that is associated to this AP Vendor record.

## PR Employee

The PR Employee field in the AP Vendors form, Payment Method
 tab.
This field is read-only. It displays the employee that is associated to this AP Vendor record.

## Payment Service Email

The Payment Service Email field on the AP Vendors
 form.
Enter the email address to which Comdata should send remittance notices.
The system enables this field when you select 1-Comdata from the Credit Service field in the AP
 Company Parameters form (Payment Services tab) as well as S-Credit Service from the Pay Method field in the AP Vendors
 form (Payment Method tab).

## EFT Info

None – Check this option if not using EFT (Electronic Funds Transfer) to pay this vendor. All payable transactions posted to this vendor must be paid with a manual or computer-generated check.
Prenote – Check this option if this vendor is in the “prenote” stage of validating data with the bank for EFT. All payable transactions posted to this vendor must be paid with a manual or computer-generated check. Default Payment Method will be “Check”.
Active – Check this option if you are using EFT to pay this vendor. All payable transactions posted to this vendor will default to Payment Method of “EFT”, but may be overridden to “check” or “manual”.

## Routing Transit #

Enter the EFT routing transit number supplied by your bank. Up to
 9 characters allowed; digits only (0-9), no spaces or non-numeric characters (per NACHA
 requirements).

## Bank Account #

Enter the account number of the bank receiving the EFT, up to 35 characters. Alpha, numeric (0-9) and hyphens only; no spaces or other characters allowed (per NACHA requirements).
This number identifies the specific account receiving the funds. All net pay will be deposited into this account unless additional distributions are set up in PR Direct Deposit.

## Account Type

Select the correct radio button. The system
 defaults the Checking radio button when you select the Active option
 from the EFT
 Info field.

- Checking – Select this option if this vendor’s bank account is a
 checking account. This account type will appear as code '22' in the EFT file.

- Savings - Select this option if this vendor’s bank account is a savings account. This
 account type will appear as code '32' in the EFT file.

## Addenda Type

The Addenda Type field in the AP Vendors form, Payment Method tab.
This field is active when the Active radio
 button is selected in the EFT Info section.
For this EFT-paid vendor, specify the addenda type that should be used as a default when entering Payment Info for transactions in the AP Transaction Entry form.
Note: Addenda settings in this form are passed only to
 invoices that are entered in the AP Transaction Entry form, not to invoices entered in the
 AP Unapproved Invoice Entry form. Instructions for adding EFT addenda information to
 already approved, ready-to-post vendor invoices are included in [Posting Approved Invoices](/en/vista/vista/accounting/accounts-payable/invoices/unapproved-invoices/posting-approved-invoices).

- Tax Payment – Select this option if
 this is an IRS vendor and you want payroll withholding automatically paid by EFT.
 The EFT download will include an EFT payment to the IRS with an addenda record
 indicating the tax form code, tax period end date, and amount. Social security,
 medicare and withholding amounts must be input by the user in AP Transaction
 Entry. Other Federal tax payments can be entered manually through AP Transaction
 Entry. Types of Federal tax payments are limited to those outlined in the EFTPS
 Payment Instruction Booklet. Without this option selected, tax payments cannot be
 made via EFT.

- Child Support – Select this option if
 you wish to remit child support payments via EFT. The EFT download will include an
 EFT payment to the state agency with an addenda record containing the employee
 number and amount withheld. When the PR AP Update is run, it will generate a
 payment record for the state agency specified as vendor. The payment can be
 edited/deleted in AP Transaction Entry. Child support payments to state agencies
 can also be manually generated through AP Transaction Entry by selecting the
 vendor and choosing 'Child Support' in the Addenda field and entering the required
 EFT addenda info.

- Stub Detail – Select this option if
 you want to include invoice detail with the vendor's EFT payment. This option can
 be used for any vendor (except for those requiring Tax or Child Support addenda).
 When the EFT Download is run, all vendors in the batch set up for EFT that have
 this addenda type will automatically have CTX format addenda text records created
 in the download. One addenda for each line of detail will include the APRef,
 invoice date, description, gross amount and net amount [gross - (retainage +
 discount)].

Viewpoint does not currently support state EFT tax payments.

## Pay Vendor with International ACH Transaction Format

Check this box to enable the system to create international electronic payments for this vendor.
When you check this box, the system enables all fields in the IAT Information section of the form.
Do not check this box if this vendor’s bank resides in the United States.

## ISO Destination Country Code

Enter the two-character ISO country code for this vendor.
The system enables this field when you check the Pay Vendor with International ACH Transaction Format box.
Note: For a list of ISO country codes, refer to [www.iso.org](http://www.iso.org/).

## Bank Name

 Enter the name of the vendor’s bank.
 The system enables this field when you check the Pay Vendor with International ACH Transaction Format box.

## Branch Country Code

 Enter the two-character ISO country code where the vendor’s bank branch is located.
 The system enables this field when you check the Pay Vendor with International ACH Transaction Format box.

## ID # Qualifier

Select a qualifier for identifying the numbering scheme used by the vendor’s bank. The vendor should provide this information, which comes from its bank.
The following qualifiers are available for selection:

- 1 – National Clearing System #

- 2 – BIC Code

- 3 – IBAN

The system enables this field when you check the Pay Vendor with International ACH Transaction Format box.

## U.S. Gateway Operator ID #

Enter the routing identification number for the U.S. gateway operator that will send the electronic payment. Vendors should provide this information, which comes from their bank.
The system enables this field when you check the Pay Vendor with International ACH Transaction Format box.

## Active

Select this checkbox if you are using EFT to
 pay this vendor. All payable transactions that you post to this vendor default to a payable
 method of “EFT”, which you can override to “Check” or “Manual”.

## BSB #

 The system enables this required field when you select the Active checkbox.
 Enter the Bank/State/Branch number for this account.

## Account #

 The system enables this required field when you select the Active checkbox.
 Enter the account number for this account.

## Reference

 The system enables this optional field when you select the Active checkbox.
 Enter the vendor reference number, up to 18 characters.
 If you leave this field blank, the EFT generates a value using the bank reference and the check number (e.g., Company-25000).

## Address Seq

Enter the existing address sequence to work
 on, or enter “N”, 'New' or '+' to add a new sequence. System will assign the next available
 sequence number once you save the record.
When entering transactions (in AP Transaction
 Entry, AP Unapproved Invoice, AP Recurring Invoices, or PO Purchase Order Entry) where an
 override payment and/or purchase order address is to be specified, entry of this sequence
 number will identify this address for this vendor.

## Address Type

Specify the address type for this additional address.

- 0-Both – Select this option if this address is used for both payment and purchase order transactions.

- 1-Payment – Select this option if this address is only used for payment transactions.

- 2-Purchase – Select this option if this address is only used for purchase order transactions.

## Description

Enter a description for this address to identify what this address is used for. Up to 30 characters allowed.
Note: This description is informational only and will not
 print as part of the address.

## Address

Enter the address for this vendor, up to 60 characters. This address will print on checks paid to this vendor when using an override payment address where this address sequence is specified.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## City

Enter the city name, up to 30 characters.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## State

Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Zip Code

Enter the zip code, up to 12 characters.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Country

Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Add'l Address

Use this field to enter additional address
 information for this vendor (up to 60 characters). For example, if the vendor receives mail
 at a P.O. Box for this address, then you might enter the P.O. Box in the Address field
 above, and use this field to enter the street address.
The address information entered here is not
 used by any of the posting programs, but may be used on certain reports.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## First Name

The First Name field on the AP Vendors form, I.C. Report Info tab.
This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the first name of the contractor, up to 28 characters.
Note: This information is required for all states that
 require independent contractor reporting.

## Middle Initial

The Middle Initial field on the AP Vendors form, I.C. Report Info tab.
This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the contractor's middle initial. Do not include the period.
Note: This information is required for all states that
 require independent contractor reporting.

## Last Name

The Last Name field on the AP Vendors form, I.C. Report Info tab.
This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the last name of the contractor, up to 40 characters.
Note: This information is required for all states that
 require independent contractor reporting.

## SSN#

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the contractor's social security number. Do not use dashes or slashes.
Note:This information is required for all states that require independent contractor reporting.

## Street Number

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the contractor's street number, up to 5 characters.
Note:This information is required for all states that require independent contractor reporting.

## Street Name

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the contractor's street name, up to 40 characters.
Note:This information is required for all states that require independent contractor reporting.

## Unit/Apt #

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the contractor's unit or apartment number, up to 4 characters.
Note: This information is required for all states that
 require independent contractor reporting.

## City

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the contractor's city, up to 40 characters.
Note: This information is required for all states that
 require independent contractor reporting.

## State

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- If you elected to update changes to PM (flag in PM Company Parameters), changes to this field update to the corresponding field in PM Firms. Likewise, if you elected to update changes from PM (flags in AP Company Parameters), changes to the corresponding field in PM Firms will update here.

## Zip Code

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the contractor's zip code, up to 12 characters.
Note: This information is required for all states that
 require independent contractor reporting.

## Country

This field is accessible only if you checked the Independent Contractor Reporting checkbox in AP Company Parameters.
Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

- If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). The selected map site will default the approximate location of
 the specified country and address. If a country is not specified, the map site will
 attempt to locate the address based on the Default Country specified in HQ
 Company Setup.

- This information is required for all states that require independent contractor reporting.

## On-Cost ID

Enter an on-cost type that you want to
 associate with this vendor. Press F4 for a list of valid on-cost types.

## Calc Method

This field defaults from the Calculation Method
 drop-down for the on-cost type from AP On-Cost Types. Accept the default or override the
 setting by choosing one of the two options: A-Amount or R-Rate. If you
 select A-Amount, the system enables the Amount field. If you select R-Rate, the system
 enables the Rate field.

## Rate

This field defaults the percentage rate from the Rate field on AP On-Cost Types. If you did not specify a percentage rate, this field defaults as blank and disabled.
Accept the default or override the percentage rate for calculating this on-cost type.

## Amount

This field defaults the flat amount from the Amount field on AP On-Cost Types. If you did not specify an amount, this field defaults as blank and disabled.
Accept the default or override the flat amount for calculating this on-cost type.

## Pay Type

This field defaults the pay type from the
 Pay
 Type field on AP On-Cost Types. Accept the default or enter a new pay type.
 Press F4 to see a list of available pay types.

## On-Cost Vendor

This field defaults the on-cost vendor from
 the On-Cost
 Vendor field on AP On-Cost Types. Accept the default or enter a new on-cost
 vendor. Press F4 for a list of vendors.

## Fund ID

This field displays only for Australian
 companies (the Default Country field in HQ Company Setup has been set to AU for
 Australia).
The system enables this field if the
 ATO
 Category field is set to either Superannuation or Superannuation-Extra.
Enter the superannuation fund number for the
 subcontractor. Press F4 for a list of superannuation
 funds.

## Membership Number

The system enables this field if the
 ATO
 Category field is set to either Superannuation or Superannuation-Extra.
Enter the subcontractor's superannuation fund number for this on-cost type.
Note: The system displays this field when the Default Country
 field (HQ Company Setup) has been set to AU for Australia.

## Vendor

The Vendor field on the AP Vendors form, Duplicate Vendors
 tab.
Enter the vendor to designate as a duplicate of the current vendor. Press F4 for a list of valid vendors.Note: If open invoices exist for the duplicate vendor, the system displays a message that you cannot merge a vendor with open invoices, and will not save the record. You must close the invoices before you can add the vendor as a duplicate here.

Once you save the record, the system marks this vendor as inactive and displays a message on the vendor's record indicating it is inactive and a duplicate of the specified parent vendor.
