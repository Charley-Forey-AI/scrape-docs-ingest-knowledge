---
title: "MS Oil Price Escalation Setup | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/material-sales-reports/material-sales-united-states-specific-reports/ms-oil-price-escalation-setup"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/material-sales-reports/material-sales-united-states-specific-reports/ms-oil-price-escalation-setup"
---

# MS Oil Price Escalation Setup

You can use the MS Oil Price Escalation Setup report to
 show Material, Job and Quote data related to MS Oil Price Escalation report and calculations
 by selecting Material Sales > Reports > MS Oil Price Escalation Setup.
The MS Oil Price Escalation Setup Report shows Material, Job and Quote data related to MS Oil Price Escalation report and calculations. It is intended to help assure data is set up properly. The report is grouped by State.
The Material Setup section lists materials associated with a Price Index, in either the HQ Escalation Index form or the HQ Materials form. It shows the Finished Material, Component Material and % Weight from IN Bill of Materials and IN Bill of Materials Override. The associated Price Index and most recent, monthly "Min Days" value (from HQ Escalation Index form, Monthly Index tab) make up the final three columns of the section. The Material section falls into a State group, based on State field in HQ Materials.
The Job Setup section is for Job Sales. It list Job's properly set up for Oil Price Escalation. In the JC Job Master form, Add'l Info tab the "Apply Escalators" is checked. The "Ship State" is the associated State. In JC Contract Master, info tab under the associated contract, the "Contract Start Month" is the basis for the Bid Index Date. Days since Bid Index is the number of days past as of the report run date.
The Quote section is for Customer sales. It list Quotes with "Apply Escalators" checked on the MS Quotes, Info tab. The Bid Index date is also found on this tab. Days since Bid Index is the number of days past as of the report run date. State is the "Ship To" state on the Invoices tab; if this field is empty the Billing Address state from AR Customers is used.
Report Parameters
Description
JC Company
Click the Field Lookup
 button or press F4 to select the job cost company.

MS Company
Click the Field Lookup
 button or press F4 to select the material sales company.
