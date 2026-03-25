---
title: "MS Oil Price Escalation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/reports-catalog/material-sales-reports/material-sales-united-states-specific-reports/ms-oil-price-escalation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/reports-catalog/material-sales-reports/material-sales-united-states-specific-reports/ms-oil-price-escalation"
---

# MS Oil Price Escalation

You can use the MS Oil Price Escalation report to print
 monthly material price adjustments for jobs or customers that have agreements to correct
 billings due to increases or decreases in the price of oil by selecting Material Sales > Reports > MS Oil Price Escalation.
The purpose of this report is to print monthly material price adjustments for jobs or customers that have agreements to correct billings due to increases or decreases in the price of oil. These price adjustments are applied to the components of finished materials sold in MS Ticket Entry (job and customer type sales) and are based on monthly indexes (supplied by the State where the sale occurred) entered in the HQ Escalation Index Form. Other required setup includes the following. JC Job Master (Apply Price Escalators checkbox), MS Quotes (for customer sales), IN Bill of Materials (or Bill of Materials Overrides) with % Weight of oil to the Finished Good.
The report lists Finish Material, the Component Material, and the associated Price Index name. Mixed tons is the number tons sold (from MS Ticket Detail) whereas Liquid Tons is Mix Tons X %Weight (from IN Bill of Materials).
The Bid Index represents the English price amount listed in the HQ escalation form. For Job sales, the Bid Index used is where the Job's start month is between the From/End Date on the Monthly Index tab in the HQ Escalation form. For customer type sales, the Bid Index used is based on the Bid Index Date from the MS Quotes form. The Placing Index is based on the date of the MS ticket sale.
The Price Adjustment is as follows. (Placing Index / Bid Index - (1 + factor)) * (Bid Index * %Weight / 100) * Mix Tons
Sales that do not meet Min days and Min Amounts from the HQ Escalation Index are excluded from the report. Also, either a single customer and/or job may be entered. If only a customer is entered, job type sales will print for that customer assigned to the contract.
When determining which state the sale occurred in, the report looks in various places depending on the type of sale. For Job Type Sales, the report uses Ship State from JC Job Master. For Customer Type Sales, the report looks at State from MS Quotes first, but if empty, uses the Bill State from AR Customers.
The report takes eight parameters, but not all are used depending upon the Sale Type parameter.
If the Sale Type parameter = ‘C’ for Customer is selected, then the report uses MS Company, Customer #, Customer Job, Begin Date and End Date. JC Company and Job are ignored.
 If the Sale Type parameter = ‘J’ for Job is selected, then the report uses MS Company, JC Company, Job, Begin Date, and End Date. Customer # and Customer Job are ignored.
Report Parameters
Description
Company
Accept the default, or press F4 to select a company.

Customer
Select the Field Lookup button or press F4 to select the Customer or leave blank for All

Sale Type (C)ustomer or (J)ob
Enter C or J.

Job (Blank for All)
Click the Field Lookup
 button or press F4 to select the job or leave blank for
 all.

JC Company
Click the Field Lookup
 button or press F4 to select the job cost company.

Customer Job (Blank for All)
Enter customer job or leave blank for all.

Begin Date
Enter beginning date or leave blank for all.

End Date
Enter ending date or leave blank for all.
