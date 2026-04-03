---
title: "Non-Payroll Year-end Processing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/non-payroll-year-end-processing"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/year-end/year-end-for-u.s.-payrolls/processing/non-payroll-year-end-processing"
---

# Non-Payroll Year-end Processing

This topic covers year-end processing steps for the following modules:

- [General Ledger](#ID-0000061f--en__section_ev3_rmv_1tb)

- [Accounts Payable](#ID-0000061f--en__section_yjq_qmv_1tb)

- [Equipment Control](#ID-0000061f--en__section_qfl_nmv_1tb)

- [Fixed Assets](#ID-0000061f--en__section_pkv_nmv_1tb)

- [Materials Management](#ID-0000061f--en__section_n1l_mmv_1tb)

## General Ledger

## Open Forward Balance Update

The Opening Forward Balance Update carries all asset, liability, and equity General Ledger balances forward from one year to the next. All changes are reflected in current balances. Income and expense accounts will be closed to the Retained Earnings account defined in the G/L Installation screen. This update may be run frequently as the company progresses into a new fiscal year. This step should be repeated if changes have been made to the previous year.
Important: When using this function, all balance records for the next year will be affected.

- If any of these account types have year-end balances of $0.00 and a status of Not used, the account code is not rolled forward to the New Year:

- Asset

- Liability

- Capital

- All income account codes are closed to Retained Earnings regardless of the account's status.

## Fiscal Calendar Maintenance

The Fiscal Calendar Maintenance screen displays all fiscal years presently set up in the current company. Use this screen to set and maintain Journal Entry sequence numbers and ending dates for each fiscal period. Entries you make here control certain defaults and virtually every transaction updated to the General Ledger.
While changes are rarely required in this screen, the end of your fiscal year is a good time to check whether there need to be any additional years added to the fiscal calendar. If changes are made, the dates on historical transactions aren't changed.

To update the Fiscal Calendar

1. Go to General Ledger > Period End > Fiscal Calendar Maintenance.

1. Select the New Year button. The Add New Fiscal Year window displays.

1. Press Enter until all periods display, and then select OK.Note: Use the Add New Fiscal Year window to add years to your fiscal calendar. After entering the number of periods, press Enter. The dates and period labels for the next future year default, and you are able to edit the period labels. Next, the Auto-Create Additional Fiscal Years window displays, allowing you to create up to nine additional years based on the established settings.

1. Display the new Fiscal Calendar. Review the new dates to verify the update.

1. Select the checkmark to save and exit the calendar.

## Processing Dates Maintenance

At the end of each fiscal year, your system's maximum dates in all modules must fall in the new year.
When you open the Change Processing Dates screen, date-based changes are disallowed for all other users. Anyone else making entries in that company must wait until you close the screen to process date-based transactions.

1. Go to System Installation > Processing Dates.

1. Make any necessary changes.

1. To save changes, select Save and/or the checkmark in the upper right hand corner until the screen has returned to the Site Map.

## Accounts Payable

## Managing Vendors with 1099s

The IRS requires that if you make payments in excess of $600 to certain groups, you must prepare 1099-MISC/NEC forms and send copies of the forms to the IRS and vendor(s). Complete the following steps to ensure that your vendor and their 1099 information are set up properly within Spectrum.

## Set up the Vendor

1. Go to Accounts Payable > Vendors.

1. Select the Properties button and complete the Payment due, Discount due, Insurance, Status, and Invoice defaults sections.

1. In the 1099-Misc section of the Properties window, select the 1099-Applicable checkbox and then complete the Alternative name field.Note: It is suggested that you complete the Alternative name field in case the vendor uses multiple names when filing.

1. In the Amount indicator field, use the drop-down menu to select the 1099 form's payment indicator.

1. Complete the Social Security # field or the Payer Tax ID number field. Important: Do not wait to until a later time or date to complete this step.

1. Complete the remaining fields and then select OK until you return to the Site Map.

## Vendor Year-end Processing

1. Go to Accounts Payable > Period End > 1099 MISC/NEC Form, or go to System Administration > Year End > Year End Processing > Accounts Payable > 1099 MISC/NEC Maintenance.

1. Select the Build button to open the Build 1099-MISC/NEC Forms screen.

1. In the Vendor field, enter the vendor code, press F4 to select a valid vendor code, or press Enter to accept the default of all vendors.

1. In the From date field, enter the first payment date to be processed. Normally, this is 01/01/YY.

1. In the Through date field, enter the final payment date to be processed. Normally, this is 12/31/YY.

1. In the Minimum amount field, enter the minimum year-to-date payment amount for the vendor 1099s. Vendors with total payment amounts less than the amount entered in this field will not be updated to 1099 processing.

1. Select Continue and then select Save until you return to the Site Map.

## 1099-MISC/NEC Maintenance

The 1099-MISC/NEC Form Maintenance screen displays a list of all the vendors currently receiving a 1099. You can also use this screen to update and print 1099-Misc forms for vendors.

1. Select New to create add a new 1099-Misc recipient, or select a record and select Edit to make changes.

1. This screen provides vendor status protection. Entry is prevented when the vendor status is Not Used. A warning displays when the status is Inactive.

## Build 1099-MISC/NEC Forms

This update is used prior to printing 1099-MISC/NEC forms to collect necessary information from throughout the software. In order for 1099-Misc forms to be accurate, it must be run prior to the Vendor History Purge.
To support tax law guidelines requiring companies to omit payments made by a "third party network" (for example, credit card processor) from this form, the Build 1099-MISC/NEC Forms exclude payments made from Cash Management credit card accounts and any payments made via Comdata. The Vendor 1099 report also excludes these payments.

## Print 1099-MISC/NEC Forms

Use this screen to print 1099-MISC/NEC forms. Form 1099 information is generated either through 1099-MISC/NEC Form Update or through 1099-MISC/NEC Form Maintenance. The payer name, address, and telephone number shown on the 1099-MISC/NEC form are printed based on information stored in the Company Installation screen.Note: About Address 2

- If you want to see the entry of your company's Address 2 line, go to System Administration > Installation > Company > Properties tab.

- For the Recipient, if you want to include any data that is on Line 2, enter it manually on Line 1.

.

## Export 1099-MISC/NEC File

Use this screen to export 1099-MISC/NEC forms. Only 1099s that are filed electronically display in this screen.

1. All entries must be capitalized per Internal Revenue Service (IRS) specifications.

1. The transmitter is the party preparing the 1099-MISC/NEC file. The contact name is the party the IRS will contact should there be a problem. These may be the same.

1. If 'Entity tracking' is enabled in Enterprise Installation, this export segregates forms by Entity. In these cases, the Export file contains the 'entity' name and address, when applicable, in place of the Company Installation information. Whereas the 'payer tax ID number' for the 'main company entity' is entered as the forms are built, the entity-specific 'payer tax ID numbers' are derived from the Entity setup.Note: While entering tax ID and address information, do not include punctuation characters.

## Viewpoint Partners with Nelco to Support 1099-MISC/NEC Filing

Your Spectrum application can create a comma delimited (.csv) file for uploading to the Nelco site to process Forms 1099-MISC/NEC.
If you want to file using Nelco, and if you haven't already, you'll need to [Create an account at our partner site](https://spectrum.nelcoportal.com/Account/CreateUser) where you'll be prompted to enter general info (name, address, email) about your company.
Complete and review the screen select ions, paying special attention to the tax year select ion.

1. Select the Nelco CSV button. The Export to Nelco CSV Format information window displays.

1. Select Continue.

1. A second information window displays letting you know if the export was successful and listing any exceptions (records containing errors) if they exist.

1. Open the [Nelco partner site](https://spectrum.nelcoportal.com/import/gwximport).

1. Select the Import Data link and select the 'Federal Information Reporting' Form Type and select the File to Import.

1. Upload your .CSV file to the Nelco site from your Downloads folder.

1. Select the Import button.

1. On the Forms In Progress screen, choose the filing services you wish to use, related to electronic filing and delivery of forms to employees.

1. Make sure all the employees for your companies are select ed on this screen and select Next.

1. If you select ed the 'Recipient Mail & Online Retrieval' service, enter recipient email addresses.

1. Review the recipients in your cart and select the Next button.

1. On the Payment Details screen, enter credit card information.

1. Select the Pay & Submit button to complete processing.

Important: Iowa filers:When filing 1099's electronically with Nelco, the state of Iowa requires an additional electronic filing number. To support this Business eFile Number (aka 'BEN'), a new field titled 'Electronic filing #' has been added to the Export 1099NEC/MISC File page.

## Equipment Control

## Open Forward Balance Update

The Open Forward Balance Update screen resets the opening revenue and cost balances for a new fiscal year from the previous year for each piece of equipment. This is a necessary update when moving from one year to the next, and may be run numerous times.

This function is available at Equipment Control > Period End > Open Forward Balance Update or System Administration > Year End > Year End Processing.

1. Select Equipment Control.

1. Select Open Forward Balance.

1. Enter the fiscal year most recently completed.

1. Select Continue.

## Fixed Assets

For Fixed Assets year-end processing, often companies are required to report on assets that they acquire or dispose of that year, and report on YTD depreciation.

## YTD Depreciation

YTD depreciation can be reported by going to Fixed Assets > Period End > Depreciation History Report, running the Depreciation History Report for the 01/01/YY through 12/31/YY dates (and then canceling out of the optional Purge step which appears on another screen).

## Disposal

To dispose of an asset without deleting it and to report on the disposal at year-end, perform the following steps:

1. Create a Department at Fixed Assets > Maintenance > Department for all assets that are disposed of in the current year.

1. When an asset is retired, sold, disposed of, and so on, set the asset to Inactive status at Fixed Assets > Maintenance > Fixed Assets Master, to stop depreciation calculation.

1. Enter the date retired and sales price (if applicable) on the asset, and change the department on the asset to the department created in step 1.

1. These changes are not recorded in the general ledger. If you have sold the asset, create a journal entry to reduce the asset, accumulated depreciation amount, and gain/loss on sale, and more.

1. To report on asset disposal for the year, run a fixed asset listing (go to Fixed Assets > Maintenance > Fixed Assets Master, select the Listing button), using the department created in step 1.

## Deletion

If you choose to delete an asset entirely from Fixed Assets, you can report on disposed assets with the Deletions Report, at Fixed Assets > Reports > Fixed Assets Deletions. Only deleted assets appear in the Deletions report.
Note: Once viewed, the Fixed Assets Deletions report prompts you to purge the data (it purges the retirement activity). If you've never run these reports before, or opted not to purge, you may see several years of data.

1. Go to Fixed Assets > Maintenance > Fixed Assets Master.

1. Press Enter to see all your assets.

1. Locate and select the asset you have sold.

1. Select the Delete button.

1. Select OK to confirm.

## Addition

When you run this report, please retain it as a permanent record of the company, as it cannot be recreated.
To report an asset addition to Spectrum, go to Fixed Assets > Reports > Fixed Assets Additions and select Preview. All assets that have ever been added and not yet purged from this listing appear in this report.
Note: Once viewed, the Fixed Assets Addition report prompts you to purge the data (it purges the addition activity only, not the asset or depreciation records). If you've never run this report before, you will likely see several years of data.

## History Consolidation

The Fixed Assets History Consolidation is an optional function and used only if you have purged General Ledger depreciation records in General Ledger for prior years.

This function is available at Fixed Assets > Period End > History Consolidation, or at System Administration > Year End > Year End Processing.

1. Select Fixed Assets.

1. Select History Consolidation.

## Materials Management

## Open Forward Balance Update

The Open Forward Balance Update function rolls the totals of the plant production file from one year to the next.

This function is available at Materials Management > Period End > Open Forward Balance Update or at System Administration > Year End > Year End Processing.

1. Select Materials Management.

1. Select Open Forward Balance.

1. In the From fiscal year field, choose a year from the drop-down. The ending balance of that year will roll to the opening balance of the next year.

1. Select Continue.

1. Select OK to confirm.
