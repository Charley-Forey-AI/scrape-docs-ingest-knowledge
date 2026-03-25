---
title: "Set Vendors Subject to 1099 Reporting (United States) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/set-vendors-subject-to-1099-reporting-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/set-vendors-subject-to-1099-reporting-united-states"
---

# Set Vendors Subject to 1099 Reporting (United States)

You can set a vendor to be subject to 1099 Reporting in the AP
 Vendors form, even if you are not completely certain whether the vendor is subject to
 reporting.
 If you are unsure of whether a vendor is subject to 1099 reporting, you should set them as subject. This ensures that all transactions posted to this vendor are automatically flagged to be included in the vendor's 1099 totals. If you later learn that this vendor is not subject to 1099 reporting, you can reverse the action and 1099's will not print - you will not need to change any transactions. They will show on the AP 1099 Report, but will include a message stating that 'transactions subject to 1099 report exist, but no 1099 forms will print'.To set a vendor subject to 1099 reporting:

1. Open the AP Vendors form and enter the vendor to update.

1. Click on the Add'l Info tab.

1. In the 1099 Info section, select the Subject
 to 1099 reporting checkbox.The system enables the 1099
 Type, Box#, Proprietor, Include in 1099 Processing, and Mailing
 Address Seq fields.

1. If the vendor will receive a printed copy of 1099s and you need to use an address other than the payment address specified for the vendor (Info tab), use the Mailing Address Seq field to specify the address sequence or press
 F4 to see a list of
 sequences.Note: Address sequences are maintained on the Add'l Addresses tab of the AP
 Vendors form. If you enter a sequence in this field, the system uses the
 associated address when printing 1099s or when electronically filing Federal 1099s via Aatrix (initiated via AP 1099 Download).

1. In the 1099 Type field, enter the 1099 type that the system will use to track payable amounts subject to 1099 reporting for this vendor. Press F4 for a list of 1099 types.

1. In the Box# field, press F4 to select from a list of valid boxes on the 1099 form where 1099 amounts will accumulate and print for this vendor.

1. In the Tax ID# field, enter the vendor’s federal tax identification number. This number prints on the 1099 form.

1. In the EIN/SSN drop-down, specify whether the tax ID is the vendor's EIN or SSN number.If you select SSN, the system enables the First Name, Middle Initial, and Last Name fields.

1. In the Proprietor field, enter the proprietor (owner) name, if any. You must enter the name as "Last Name, First Name" to enable proper 1099 electronic filing.Note: This field is only used when the EIN/SIN drop-down is set to EIN. If set to SSN, you must enter the proprietor's name using the First Name, Middle Initial, and Last Name fields.

1. If you selected SSN as the tax ID type, use the First Name, Middle Initial, and Last Name fields to enter the proprietor's name.Note: You are not required to enter a middle initial, but for reporting purposes, you must enter a first and last name.

1. Select the Include in 1099 Processing (ignore minimum) checkbox if the system should include a vendor's totals when processing (downloading or printing) 1099s, regardless of whether the vendor's payment is less than the specified minimum payment amount.Note: If you do not select this checkbox, the system only prints a
 1099 for the vendor if the vendor's payment is equal to or greater than the value
 in the Minimum Payment Amount field in the AP 1099 Download form.

1. If the vendor has consented to receive 1099s electronically (via email), select the 1099 Email Consent checkbox. If this checkbox is not selected, the vendor will receive printed 1099s.

1. Save the record.

Related information

- [Prepare and Process 1099s](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/prepare-and-process-1099s)

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)

- [AP 1099 Download Form](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-download-form)
