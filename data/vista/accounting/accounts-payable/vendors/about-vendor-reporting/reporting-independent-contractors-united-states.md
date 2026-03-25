---
title: "Reporting Independent Contractors (United States) | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/reporting-independent-contractors-united-states"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-payable/vendors/about-vendor-reporting/reporting-independent-contractors-united-states"
---

# Reporting Independent Contractors (United States)

If your state requires businesses to report independent
 contractors, you can have the system automatically generate a report for all contractors
 meeting reporting requirements when posting payments in Accounts Payable.
To enable independent
 contractor reporting, you must set up information in AP Company Parameters, as
 well as required reporting information for each applicable vendor in AP
 Vendors.

1. In AP Company Parameters (Pay Types/Discounts/ICR tab), select the Independent Contractor Reporting checkbox. When selected, the system triggers a search function during payment processing to locate vendors meeting reporting requirements. The system enables the Threshold Payment Amount and Report Title fields.

1. In the Threshold Payment Amount field, enter the threshold amount. The payment threshold may differ by state, ranging from $0 to $2,500; however, it will typically be $600. Contractors meeting or exceeding this amount (and meeting other reporting requirements) are included when printing the AP Independent Contractors Report.

1. If you are using a custom report for independent contractor reporting, use the Report
 Title field to enter the custom report title. If you are not using a custom report, leave this field blank. The system will automatically use the standard report (AP Independent Contractors Report). Note: The standard report follows California's reporting requirements. However, because reporting requirements may vary from state to state, you may choose to create your own report.

1. In AP Vendors,
 enter the reporting information on the I.C. Report Info tab. The
 information on this tab is required for all states that require
 independent contractor reporting. Note: You must fill out this information for
 vendors you have hired who are independent contractors and:

- for whom you are required to file
 a 1099-MISC form for their services,

- to whom you pay $600 or more or
 enter into a contract for $600 or more and,

- who are individuals or sole
 proprietorships

 You are now set up for independent contractor
 reporting. When you process a payment batch (in AP Payment Posting), the system
 searches the batch for invoices for qualifying contractors. If an invoice is
 found, you will be given the option to run the AP Independent Contractor Report.When you run the report, the system updates the
 Last Reported Activity
 display field in AP Vendors (I.C. Report Info tab) with the date on which
 the contractor was last reported. It is updated each time the Independent
 Contractors report is run for the vendor and is used to determine whether or
 not a contractor has been reported for the calendar year.
For more
 information about independent contractor reporting, see [AP Independent Contractor Rpt ](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-independent-contractor-rpt-form).

Related information

- [AP Independent Contractor Rpt Form](/en/vista/vista/accounting/accounts-payable/year-end-reporting/1099s/ap-1099-forms/ap-independent-contractor-rpt-form)

- [AP Payment Posting Form](/en/vista/vista/accounting/accounts-payable/payments/ap-payment-forms/ap-payment-posting-form)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)
