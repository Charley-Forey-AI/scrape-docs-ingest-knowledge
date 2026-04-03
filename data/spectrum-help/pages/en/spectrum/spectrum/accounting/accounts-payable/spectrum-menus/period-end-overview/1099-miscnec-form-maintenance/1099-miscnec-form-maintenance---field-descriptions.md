---
title: "1099-MISC/NEC Form Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/period-end-overview/1099-miscnec-form-maintenance/1099-miscnec-form-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/period-end-overview/1099-miscnec-form-maintenance/1099-miscnec-form-maintenance---field-descriptions"
---

# 1099-MISC/NEC Form Maintenance - Field Descriptions

Use this table for reference when completing the fields on this screen.
FieldsDescriptions
EntityNote: This field displays only if cost centers are being used and entity tracking is also enabled in the current company.
After entering or selecting an Entity, all records will be shown on the main screen for tax review purposes, and cost center security prevents editing vendors that the operator does not have authorization to access.
If the Entity is left blank, the company name displays.

1099 typeSelect the type of 1099: Vendor, Customer, or Other.
Vendor/cust codeEnter the vendor or customer code. The system will read the Vendors screen for the entered (V)endor code, or the Customer screen for the entered (C)ustomer code, and complete the name, address, and ID information.
It is not necessary to enter a valid customer code. This is particularly helpful for first-year users that may need to send a 1099-MISC/NEC to an individual paid prior to conversion to Spectrum.
Note: If you select a vendor with a status of Not used, you will not be allowed to proceed. If you select a vendor with a status of Inactive, the software displays a warning.

Payer tax ID numberThe payer tax ID defaults from the Build 1099-MISC/NEC Form screen; no changes are allowed.
Vendor totalThe total payment made to this vendor displays.
Recipient
Recipient nameThe name of the vendor/customer displays.
Alternate nameAny alternate name stored in the software for the selected vendor will default. Enter an alternate name that you want printed on the 1099-MISC/NEC form, which will print in the Name box.
Address, City, StateThe full address of the 1099 recipient displays.
Recipient properties
Federal ID#If federal income tax was manually withheld from vendor payments, enter the company's federal tax ID in this field.
Payer state codeEnter the company's two-digit state ID to display on the form and update to the Nelco export file.
State/payer #If state income tax was manually withheld from vendor payments, enter the company's state tax ID in this field. Tip: Kansas and Wisconsin require longer Tax ID numbers than can be entered in this field. For these states, enter REPLACEME in this field, export the file, and then open the file with a text editor and replace the text with the appropriate 15-digit State Tax ID. Alabama, Georgia, Hawaii, Nebraska, New Jersey, and New Mexico do not require a State ID for 1099-MISC filing, so this field should be left blank in these states.

FIT withheldIf you manually withheld federal income tax from vendor payments, enter that amount in this field. The system will generate a dollar amount for this field if the "amount indicator" is "4" in the Vendors.
SIT withheldIf you manually withheld state income tax from vendor payments, enter that amount in this field.
State incomeEnter the amount of earned income for the state for Form 1099-MISC (Box 17) and Form 1099-NEC (Box 7).
2nd TIN notice?Select the checkbox if notified twice within the past three years that the vendor or customer's taxpayer identification number is incorrect.
Products for resale?Select the checkbox if $5,000 or more of resellable goods were sold to this customer.
If this 1099-MISC/NEC is for a customer rather than a vendor, the remaining fields are irrelevant.

Form 1099-MISC amount paid
RentsEnter the rent amount paid. The system will generate a dollar amount for this field if the "amount indicator" is "1" in the Vendors.
RoyaltiesEnter the royalties paid. The system will generate a dollar amount for this field if the "amount indicator" is "2" in the Vendors.
Other incomeEnter the amount paid for other income (for example, prizes or awards). The system will generate a dollar amount for this field if the "amount indicator" is "3" in the Vendors.
Med paymentsEnter the medical payments amount. The system will generate a dollar amount for this field if the "amount indicator" is "6" in the Vendors.
Non-emp compEnter the non-employee compensation amount . The system will generate a dollar amount for this field if the "amount indicator" is "7" in the Vendors (or if the "amount indicator" is blank).
Int/div substituteIf a partial payment was made in lieu of money owed for interest or dividends, enter the amount paid.
Golden parachuteEnter the amount paid as excess golden parachute payments.
Paid to attorneyEnter the gross proceeds paid to an attorney.
Total 1099-MISC amountThe total of all 1099-MISC amounts entered above will display in this field.
Form 1099-NEC amount paid
Non-employee compensationEnter the non-employee compensation amount. The system will generate a dollar amount for this field if the "amount indicator" is "7" in the Vendors (or if the "amount indicator" is blank).
