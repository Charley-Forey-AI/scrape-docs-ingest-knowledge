---
title: "Field Definitions: HQ Company Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form/field-definitions-hq-company-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form/field-definitions-hq-company-setup-form"
---

# Field Definitions: HQ Company Setup Form

The following is a list of field descriptions for the HQ
 Company Setup form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Company

Enter a number (0-255) that will identify this company throughout the system.

##  Business Name

 Enter the name of the company, up to 60 characters. This name will be used as the default for this company throughout the system wherever the company name is used, and will print on all reports. It is also required if you will be using the Independent Contractor Reporting feature (in AP).

## Mail Address

Enter the company address, up to 60 characters. This address, along with the city, state, and zip code specified for this company will be the default address printed on Purchase Orders, Payroll W-2's, Accounts Payable 1099 forms, and job billings. It is also required if you will be using the Independent Contractor Reporting feature (in AP).
Note:If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified below.

##  City

 Enter the city, up to 30 characters. Entry in this field is required if you will be using the Independent Contractor Reporting feature (in AP).
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified below.

##  State

 Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified below for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.
 Entry in this field is required if you will be using the Independent Contractor Reporting feature (in AP).
Note:If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified below.

##  Zip Code

 Enter the zip code, up to 12 digits. Entry in this field is required if you will be using the Independent Contractor Reporting feature (in AP).
Note: If you have Internet access, you can click the Map
 button for direct access to the default map site for your login (as defined in User
 Options, Main Menu). Map will default the approximate location of the specified country and
 address. If a country is not specified, attempts to locate address based on Default Country
 specified below.

##  Country

 Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified (below) for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.
Note:If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified below.

##  Add'l Address

 Use this field to enter additional address information for this company, up to 60 characters. For example, if your place of business receives its mail at a P.O. Box, then you might enter the P.O. Box in the Mail Address field above, and use this field to enter the street address.
 The address information entered here is not used by any of the posting programs, but may be used on certain reports.

##  Phone

 Enter the phone number for this company, up to 20 characters (including area code and dashes). This number will print on several reports, including the PR 941 Federal Form report.

##  Fax

 Enter the fax number for this company, up to 20 characters (including area code and dashes).

## Federal Tax ID / Business Number

United States: Federal Tax ID field on the HQ
 Company Setup form.
Australia: Business Number (ABN) field on the HQ
 Company Setup form.
Canada: Business Number field on the HQ Company
 Setup form.
United States: Federal Tax ID
Enter the federal tax identification number for this company, up to 10 digits. This will be used when processing 1099's (AP) and W-2's and Unemployment Reports (PR, as well as when setting up Federal tax information in PR109 (Federal/State/City Codes). It is also required if you will be using the Independent Contractor Reporting feature (flag in AP Company Parameters).
Australia: Business Number (ABN)
Enter the Australian Business Number (ABN) for your company. This field is used for reporting purposes.
Note:The system displays this field when the current
 company's Default Country is set to AU.

ABNs can be entered as 11 consecutive digits, or as 11 digits with a space separating the 2nd and 3rd digits, the 5th and 6th digits, and 8th and 9th digits (e.g. ## ### ### ###).
Canada: Business Number
Enter the 9-digit business number for your company, as provided by the Canada Revenue Agency.
Note:Entry in this field is not required; however, if you
 will be generating electronic files for Record of Employment reporting (in PR
 Employee ROE Generate), you must enter your business number here. The system will
 not generate electronic ROE files if this number is missing.

 When reporting T5018 payments (in AP T5018
 Payments), the system will generate the Payer's Account Number using this 9-digit number
 and appending the 6-character GST/HST Program Account number
 specified for the AP company in AP Company Parameters (PayTypes/Discounts/ICR tab). The
 Payer's Account Number is included in the generated electronic file, and will print on
 the AP Canada T5018 Summary report and the T5018 slip (if you cleared the Suppress Payer's
 Account Number on T5018 Slip checkbox in AP Electronic File
 Generate).

Related information

- [HQ Company Setup Form](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)

## Corporate Number

Enter the Australian Corporate Number for you company. This field is used for reporting purposes.

## State Employer ID

For use with Independent Contractor reporting only.
Enter the state employer identification number for this company, up to 30 characters. Not all states require this number for independent contractor reporting. You will need to check your state's requirements to determine if entry in this field is required.
Click [here](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form/field-definitions-hq-company-setup-form#ID-00052163--en) to see the field definition for Australian users.

## Quebec Employer ID

This field displays for Canadian companies only.
Enter the company's Quebec Employer ID, up to 10 digits.

## DUNS Number

The DUNS Number field in the HQ Company Setup form, Info tab.
Enter your company's 9-digit DUN and Bradstreet (DUNS) identification number.
Only required for HR VETS-421 reporting.Note: You can override the DUNS number by hiring location in HR Hiring Location Setup.

The system includes this code on the HR Federal Contractor VETS-4212 report (used for exporting data for e-filing) and the HR Federal Contractor VETS Resources report (used for viewing or printing).

Related information

- [About Regulatory Reporting Using Aatrix](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aatrix-reporting/about-regulatory-reporting-using-aatrix)

- [Prepare and Process 1099s](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/prepare-and-process-1099s)

- [Process W-2s](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/w-2s/process-w-2s)

- [Aatrix Tax Type](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form/field-definitions-pr-deductions-liabilities-form#ID-00036b63--en)

## NAICS Code

The NAICS Code field on the HQ Company Setup form, Info tab.
Enter the North American Industry Classification System (NAICS) code (up to 6 digits) for this HQ company.
The system includes this code on the HR Federal Contractor VETS-4212 report (used for exporting data for e-filing) and the HR Federal Contractor VETS Resources report (used for viewing or printing).
Note: You can override this code by hiring location in the HR Hiring Location Setup form.

##  Default Country

 Specify the default country (as defined in HQ Countries) for this company. The system will
 use this country to validate the state or region (e.g. province, territory, etc.) specified
 when entering addresses on forms throughout the software. If the state or region is valid
 for this country, the related form will not require entry of a country code. However, if
 the state or region is not valid for this country, you will need to specify a valid country
 code for the state or region.
Note:The country specified here may affect field display
 and labeling in certain forms (AP and PR). For example, if your workstation regional
 setting (Start à Control Panel à Regional and Language Options à Regional Option tab) is
 set to ‘English (United States)’, but your Default Country is ‘AU’ for the active
 company and you are working in the AP Vendors form, the EFT tab will display Australian
 EFT-related fields.

## Report Date Format

 Specify the date format to use for standard reports.

- 1 - (mm/dd/yy) – This is the most commonly used
 format in the U.S. It is the default when US, NZ, or NL are entered
 in the Default
 Country field.

- 2 - (dd/mm/yy) – This is the most commonly used format worldwide. It is the default when
 AU
 or
 CA
 are entered in the
 Default Country
 field.

- 3 - (yy/mm/dd) – This is the preferred international standard (per ISO 8601).

Note:The format specified here will print in the footer
 of reports (e.g. “Date Format – mm/dd/yy”) to help prevent confusion.

## Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following is a detailed list of the audit options.

- Company Parameters - This audit
 option is display-only and is always checked. Any additions, changes, or deletions
 made to the HQ Company Setup program will be tracked in the Master Audit file.

- Materials - Check this box to
 record additions, changes, and deletions made in HQ Material Categories and HQ
 Materials.

- Tax Codes - Check this box to
 record additions, changes, and deletions made in HQ Tax Codes.

Note:If you are tracking changes to Materials and/or Tax Codes, and multiple companies share the same Material and/or Tax group, HQMA will be updated when additions, changes, or deletions are made to these files in any of the sharing companies. However, only a single record will be generated (per add/change/delete) for the material group/material, material group/category, or tax group/tax code.

- Contacts
 - Check this box to record additions, changes, deletions made in HQ
 Contacts.

##  AR Customers

Specify the group (as defined in HQ Groups)
 whose Customer Master this company will use. Customers set up in AR Customers while this
 company is active will be set up in this group.
Important:DO NOT change the group number once you have begun entering and processing data in this company or any company pointing to this group, as it can seriously affect existing data. If you must change a group, please contact Customer Support; however, be aware that there may be certain situations in which a group cannot be changed.

##  AP Vendors and PM Firm Codes

 Specify the group (as defined in HQ Groups) whose Vendor Master or Firm files (Firm
 Types, Firm Master, Firm Contact Master, and Project Firms) this company will use.
 Vendors set up in AP Vendors or firm information set up in PM (Project Management) while
 this company is active will be set up in this group.
Important:DO NOT change the group number once you have begun entering and processing data in this company or any company pointing to this group, as it can seriously affect existing data. If you must change a group, please contact Customer Support; however, be aware that there may be certain situations in which a group cannot be changed.

##  HQ Material Codes

 Specify the group (as defined in HQ Groups) whose material categories and materials files this company will use. Material categories set up in HQ Material Categories or materials set up in HQ Materials while this company is active will be set up in this group.
Important:DO NOT change the group number once you have begun entering and processing data in this company or any company pointing to this group, as it can seriously affect existing data. If you must change a group, please contact Customer Support; however, be aware that there may be certain situations in which a group cannot be changed.

##  JC Phase and Cost Types

 Specify the group (as defined in HQ Groups)
 whose Phases file this company will use. Phases set up in JC Phases while this company is
 active will be set up in this group.
Important: DO NOT change the group number once you have
 begun entering and processing data in this company or any company pointing to this group,
 as it can seriously affect existing data. If you must change a group, please contact
 Customer Support; however, be aware that there may be certain situations in which a group
 cannot be changed.

##  HQ Tax Codes and Rates

 Specify the group (as defined in HQ Groups) whose Tax Codes file this company will use. Tax codes set up in HQ Tax Codes while this company is active will be set up in this group.
Important:DO NOT change the group number once you have begun entering and processing data in this company or any company pointing to this group, as it can seriously affect existing data. If you must change a group, please contact Customer Support; however, be aware that there may be certain situations in which a group cannot be changed.

##  EM Cost and Revenue Codes

 Specify the group (as defined in HQ Groups) whose revenue codes, cost codes, and cost types files this company will use. Revenue codes set up in EM Revenue Codes, cost codes set up in EM Cost Codes, or cost types set up in EM Cost Types while this company is active will be set up in this group.
Important:DO NOT change the group number once you have begun entering and processing data in this company or any company pointing to this group, as it can seriously affect existing data. If you must change a group, please contact Customer Support; however, be aware that there may be certain situations in which a group cannot be changed.

##  EM Shops

 Specify the group (as defined in HQ Groups) whose shop file this company will use. Shops set up in EM Shops while this company is active will be set up in this group.
Important:DO NOT change the group number once you have begun entering and processing data in this company or any company pointing to this group, as it can seriously affect existing data. If you must change a group, please contact Customer Support; however, be aware that there may be certain situations in which a group cannot be changed.

##  Customer

 This field is only used if you are using the Material Sales module and the 'Create Intercompany Invoices" option in MS Company Parameters is set to Y (checked).
 Specify the customer number (from AR Customers) that identifies this company. This is the customer to which receivable transactions will be posted (in the ‘purchased from’ companies) when materials are sold to this company in Material Sales.
Note: If you are using intercompany invoicing, it is highly
 recommended that you do not assign the same AR customer number to multiple HQ companies.
 During invoicing, the system will determine the tax group to use based on the first
 occurrence of the customer number in HQ Company Setup. This may cause a discrepancy
 between the tax group for the AR company and the tax group for the AP company, especially
 if you do not share tax groups between companies. For more information, see [Intercompany Invoicing](/en/vista/vista/job-resources/material-sales/invoices/intercompany-invoicing).

##  Vendor

This field is only used if you are using the
 Material Sales module and the 'Create Intercompany Invoices" option in MS Company
 Parameters is set to Y (checked).
Specify the Vendor #, (from AP Vendors) that
 identifies this company. This will be the vendor to which payable transactions will be
 posted (in the ‘sold to’ companies) when materials are sold from this company in Material
 Sales. It is suggested that the Vendor # be the same as the HQ Company #.

##  Document Type

The Document Type field on the HQ Company Setup form, Workflow tab.
 Select the type of document to which the workflow applies.

- PO - Purchase Order

- SL - Subcontracts

Note: You can have only one process for each document type.

Note: You can override the workflows defined here for specific modules (EM, GL, IN, JC, and PM), as well as for specific equipment departments, inventory locations, jobs, and projects.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Process

The Process field on the HQ Company Setup form, Workflow tab.
Enter the workflow process to perform for the specified document type or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the same document type specified in the Document Type field or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type (Purchase Order or Subcontract). However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). In this case, you may assign it to either or both document types on this tab.

Note: You can override the workflows defined here for specific modules (EM, GL, IN, JC, and PM), as well as for specific equipment departments, inventory locations, jobs, and projects.

##  Active

The Active checkbox on the HQ Company Setup form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs or Subcontracts (depending on the document type) are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

##  Notes

The Notes field on the HQ Company Setup form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
