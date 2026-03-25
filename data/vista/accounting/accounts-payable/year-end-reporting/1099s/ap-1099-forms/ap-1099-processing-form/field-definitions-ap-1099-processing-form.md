---
title: "Field Definitions: AP 1099 Processing Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-processing-form/field-definitions-ap-1099-processing-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-1099-processing-form/field-definitions-ap-1099-processing-form"
---

# Field Definitions: AP 1099 Processing Form

The following is a list of field descriptions for the AP 1099 Processing form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Year Ending

The Year Ending field on the AP 1099 Processing form.

Enter the calendar year-ending month for which to view and/or adjust 1099 totals for the specified vendor.

## Vendor

The Vendor field on the AP 1099 Processing form.
Specify the vendor whose 1099s you want to view and/or adjust.

## 1099 Type

The 1099 Type field on the AP 1099 Processing form.
Enter the 1099 form type for which to view and/or adjust totals.

## Box 1 Total - Box 18 Total

The Box 1 Total through Box 18 Total fields on the AP 1099 Processing form, Info tab.

Field labels change and boxes are enabled or disabled depending on the selected 1099 Type.
Each box shows the total accumulated year-to-date 1099 amounts that will print in that box for the specified vendor and form. Totals are accumulated as transactions are paid, and include the actual paid amount (less actual discounts taken). Adjust totals as needed.
Note: If you need to enter data that will print in Box 7 of
 the 1099-DIV and 1099-Int forms (Copy B and Copy C), use the Div or Int Box
 7 field. (The Box 7 Total field is disabled for both
 DIV and INT 1099 types.)

## DIV or INT Box 7 - Foreign Country or U.S. Possession

The DIV or INT Box 7 - Foreign Country or U.S. Possession field on the AP 1099 Processing form, Info tab.

This field is enabled for 1099 types 'DIV' and 'INT' only.
Enter the name of the foreign country or US possession to which the withheld tax in Box 6 applies; up to 30 characters allowed. The data entered here prints in Box 7 of the 1099-DIV or 1099-INT forms (Copy B and Copy C).

## Other Data

The Other Data field on the AP 1099 Processing form, Info tab.

Use this field to record information for state or local governmental reporting or for your own filing purposes. Contact your state or local revenue department for filing requirements. You may enter your routing and transit number (RTN) here.
Leave this field blank if you are not required to use it.
This field allows up to 60 characters.

## 2nd TIN Notification

The 2nd TIN Notification checkbox on the AP 1099 Processing form, Info tab.

Select this checkbox if you were notified by the IRS twice within three calendar years that this vendor provided an incorrect TIN (Taxpayer Identification Number). If selected, the 2nd TIN not. box is checked on Copy A of the 1099 form or a '2' printed in position 544 of the B record for electronic downloads. No further notifications will be sent by the IRS.
Leave this checkbox unselected if you did not receive notification by the IRS that this vendor provided an incorrect TIN or, if:

- you have not received more than one notification within three calendar years

- you received both notices in the same year

- you received both notices in different years, but they both related to information returns filed for the same year

## 1099 Email Consent

(United States only) The 1099 Email Consent checkbox on the AP 1099 Processing form, Info tab.

This checkbox defaults based on how you set the 1099 Email Consent checkbox for the Vendor in AP Vendors.
Select this checkbox if this vendor has consented to receive 1099s electronically (via email) for this Tax Year and 1099 Type. If selected, the vendor must have an email address defined in AP Vendors.
Leave this checkbox unselected if the vendor has not consented to receive 1099s electronically for the selected Tax Year and 1099 Type. Instead, the vendor will receive printed 1099s.
When you launch Aatrix (via the AP 1099 Processing form), the setting defined here is sent to Aatrix and determines how Aatrix will handle delivery of 1099s for the vendor.

## Corrected Filing

The Corrected Filing checkbox on the AP 1099 Processing form, Corrected Filing tab.

Note: Corrected 1099s must be handled directly in Aatrix, regardless of whether you filed via Aatrix or downloaded your 1099-NEC via Vista. Therefore, this checkbox is no longer used and is disabled. However, to preserve historical data, this field remains visible. For information about correcting 1099s via Aatrix, see [Make Corrections to Regulatory Filings via Aatrix](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/make-corrections-to-regulatory-filings-via-aatrix). For information on correcting 1099s downloaded in Vista, see [Correct 1099-NECs Generated in Vista](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/correct-1099-necs-generated-in-vista).

Display only, indicating whether this is a corrected filing for the selected vendor/tax year/1099 type.

## Error Type

The Error Type field on the AP 1099 Processing form, Corrected Filing tab.

Note: Corrected 1099s must be handled directly in Aatrix, regardless of whether you filed via Aatrix or downloaded your 1099-NEC via Vista. Therefore, this checkbox is no longer used and is disabled. However, to preserve historical data, this field remains visible. For information about correcting 1099s via Aatrix, see [Make Corrections to Regulatory Filings via Aatrix](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/make-corrections-to-regulatory-filings-via-aatrix). For information on correcting 1099s downloaded in Vista, see [Correct 1099-NECs Generated in Vista](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/correct-1099-necs-generated-in-vista).

Display only, the error type for corrected filings (that is, the Corrected Filing checkbox is selected for the tax year).
Indicates what information was included in the generated electronic file:

- 1099 Info - Corrected filing included 1099s with updated totals only.

- Vendor/1099 Info - Corrected filing included 1099s with updated totals and updated vendor information.
