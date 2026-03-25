---
title: "Set up Vendors for International Electronic Payments (United States) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-up-vendors-for-international-electronic-payments-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-payment-methods/set-up-vendors-for-international-electronic-payments-united-states"
---

# Set up Vendors for International Electronic Payments (United States)

When processing Electronic Funds Transfers (EFTs) in U.S. companies, the system creates transactions based on Automated Clearing House (ACH) rules and regulations.
In order for you to process EFTs to vendors with banks residing in foreign countries, you must set up the vendors to meet International ACH Transaction (IAT) specifications. First, you must set up information in the system about the country associated with the vendor’s bank, and then you must configure information on the Payment Method tab in AP Vendors. Once you have done this, the system will create transactions for this vendor using IAT specifications, but you will process the payment in the same way as all other transactions.
Prior to setting up a vendors for international payments, obtain the following information:

-  the vendor’s bank name

- the Branch Country Code (which identifies the country where the vendor’s bank branch is located)

- the bank’s numbering scheme

- the payment gateway-operator identification number

Note: You must also make sure that your address in the HQ Company Setup form has a street address (PO boxes are not allowed) and that you enter your country in the Country field.
If you are unsure when to use the IAT format, contact the National Association of Clearing House Administrators (NACHA) for more information.
To set up an international vendor for electronic payments:

1. Create a record for the vendor’s country in the HQ Countries form.

1. If the vendor’s country has provinces/states/territories, set up the applicable province/state/territory in the HQ States form.

1. Set up the vendor as usual in AP Vendors, using the following guidelines for the Payment Address section of the Info tab:

1. The vendor address must be a street address; PO boxes are not allowed.

1. In the State field, enter the province/state/territory you created in step 2.

1. In the Country field, enter the country you created in step 1.

1. On the Payment Method tab in the AP Vendors form, select the Active radio button from the EFT Info section of the form.

1. Enter bank information in the Routing Transit# and Bank Account # fields.

1. Select the Pay Vendor with International Automated Transaction checkbox.The system enables all fields in the IAT Information section of the form.

1. Enter information in all fields in the IAT Information section. For more information, see the F1 help for each field. When processing electronic payments for this vendor, the system automatically applies the required IAT format for this vendor.
Note: If you are paying a U.S. company that has an international bank, you must use this same process. In this case, create an additional record in the AP Vendors form for this vendor, but associate the payment address with the country where the vendor’s bank resides.

Related information

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)

- [Create country codes](/en/vista/vista/administration/headquarters/region-setup/create-country-codes)

- [HQ States Form](/en/vista/vista/administration/headquarters/region-setup/hq-states-form)
