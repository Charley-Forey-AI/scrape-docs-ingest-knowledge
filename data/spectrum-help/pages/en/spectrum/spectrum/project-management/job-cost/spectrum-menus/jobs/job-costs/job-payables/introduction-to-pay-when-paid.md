---
title: "Introduction to Pay-When-Paid | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-costs/job-payables/introduction-to-pay-when-paid"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/jobs/job-costs/job-payables/introduction-to-pay-when-paid"
---

# Introduction to Pay-When-Paid

Pay-when-paid is a payment term that states that the vendor or subcontractor will get paid by the general contractor only when the customer pays the general contractor for that vendor's or subcontractor's work. This document explains how to set up and manage pay-when-paid vendor invoices in Spectrum.

## Requirements

At a minimum, the Core modules are required to use pay-when-paid processing. The Core includes Accounts Payable, Accounts Receivable, Cash Management, General Ledger, Job Cost, and Payroll.
Document Imaging is recommended.

## Key Terms and Definitions

Pay-When-Paid
A payment term that states that the vendor or subcontractor will get paid by the general contractor only if the customer pays the general contractor for that vendor's or subcontractor's work.
Pay-When-Paid Policy
The specific rules that govern how vendors and subcontractors will be paid on this job.
Payment Status: Waiting
This vendor invoice is waiting for customer payment and therefor will not be paid at this time.
Payment Status: Review
This invoice is flagged for review as customer payment has been received. Here, the decision to release the item has not yet been made, though cash from the customer has been received.
Payment Status: Released
This vendor invoice is ready for payment as payment from the customer has been received. This occurs when the PM releases the invoice or the system has been set to auto-release it.
*Only vendor invoices that are released may be selected for payment in Accounts Payable*. The exception to this rule includes invoices that are on hold or that are not allowed to be selected due to Document Tracking / Compliance issues.
Auto-Release
When set up, the system will automatically release vendor invoices when the appropriate amount of customer payment has been recorded in Cash Receipts Entry.

## Setting Up Pay-When-Paid

Important: Only when the job and vendor are set to pay-when-paid will these payment terms be used.
Vendor Maintenance
For all vendors eligible to be paid with pay-when-paid terms, select the Pay job invoices based on customer payment checkbox found on the Vendor Defaults page.
Just because this vendor accepts pay-when-paid terms does not automatically mean this is how they will be paid. Remember that this setting along with the setting on the job is used to default the flag on the vendor invoice.
Subcontract Maintenance
As needed, the subcontract can be set to override the vendor's standard payment terms.
The pay-when-paid terms checkbox will default to the vendor's setting. Select the Override standard vendor payment terms checkbox to enable or disable the pay-when-paid terms for this subcontract.
Regardless of whether or not the Override standard vendor payment terms checkbox is selected, the current policy Will be visible on the Subcontract Defaults page.
Job Maintenance
Because state law controls whether or not pay-when-paid terms can be used, each job can be configured to use pay-when-paid terms or not. This is controlled on the Job Setup page by the Pay When-Paid button.
Select the Pay-When-Paid button will open the Pay-When-Paid Policy window. Only when the job and vendor/subcontract are set to pay-when-paid will these payment terms be used.
Auto-release A/P Invoices
Invoices can be released automatically once the contract invoice has been paid. When set to Auto release, the window prompts for the percentage of the non-retention portion of the invoice that must be paid before the invoice will be released. For example, if you set the percentage to 100, the system will automatically release the vendor invoice once the entire non-retention portion of the contract invoice has been paid.Note: The payment applied date AND the G/L date must be on or before today's date in order for the A/P invoice(s) to be auto-released.

Flag A/P Invoices for Review
Invoices can be flagged to be reviewed when a certain portion of the customer invoice has been paid. The status will automatically change during the Cash Receipt Update.
Quick Job Setup
Quick Job Setup templates provide the ability to copy the pay-when-paid policy settings.
Master Jobs
When creating a sub-job based off of the master job, the sub-job will inherit the pay-when-paid policies of the master job.
Accounts Receivable Installation
Disable the Pay-When-Paid Subcontractor Worksheets in Cash Receipts Entry
In earlier versions of the system, a worksheet could be printed to assist the operator in making the decision to release subcontractor payments. As this new feature takes the place of this worksheet process, it is recommended that you disable it on the Accounts Receivables Installation | Properties page.
Clear the checkboxes on all three Print pay-when-paid subcontract worksheets options.
Processing Invoices
In Vendor Invoice Entry, the system will evaluate whether or not the vendor and the job use the pay when-paid terms.
In Vendor Invoice Entry, the system looks to the purchase order or subcontract to determine the job number. For non-purchase order and non-subcontract invoices, the system looks for the job entered on the first distribution row. Once the job number has been determined, the Pay-When-Paid policy will then be determined.
When Pay-when-paid? is selected, the Payment due date field is blank. By rule, all pay-when-paid invoices are considered current and thus no payment due date appears. This checkbox can be changed during data entry. It is important to note that the Payment due date will default to the current date when clearing the checkbox.
The Pay-when-paid? checkbox is only applicable for job invoices. When no job number is found, this field will be shaded and not available.
The operator can also change the pay-when-paid terms using the Change Invoice Due Dates screen or in an open Vendor Invoice Inquiry window.Note: Clearing the checkbox will set the Payment Due date to the current date.

## Processing Cash Receipts

Applying cash receipts to customer invoices will be performed as usual.
During the Cash Receipts Update, the system will look to see whether or not pay-when-paid processing is applicable on each Payment transaction. By rule, only the primary customer is reviewed and transaction codes set as an Adjustment are not included.
When pay-when-paid is applicable, the system then determines if the vendor invoices shall be auto released or set to Review based on the job's pay-when-paid policy. Here the percentage paid is compared to the policy and vendor invoices are flagged accordingly.
The percentage paid is calculated as the amount of the 'current portion' paid divided by the total amount of the current portion. Said another way, the percentage is based on non-retention values of the customer invoice.

## Using Job Payables

The purpose of the Job Payables page is to explain all vendor and subcontractor invoices along with their corresponding customer invoices. It is located in the COSTS category of the Job Info Bar. This interactive screen lets the Project Manager review and release vendor invoices with pay-when-paid terms.
The Job Payables screen can also be used for organizations that do not use pay-when-paid processing. In this situation, the screen presents a handy list of all open payables, including those that are currently being routed for approval.
The Pay-When-Paid Policy displays at the top of the page. Provided that the operator has edit security to the Job Setup page, they will also see the Pay-When-Paid Policy button. The operator can select it to modify the settings.
The Total current payables displays the total non-retention amounts for the current job that use the pay-when-paid terms. While it excludes credit memos, it includes open, unapproved and unposted invoices.
The Total unreleased amount is a subset of Total current payables. This represents the sum of all invoices that do not have a payment status of Released.
In addition to the Job Info Bar, this page also provides the Vendor and Contract Info Bars for convenience.Note: By design, the operator can set an invoice to any status as desired, regardless of whether or not cash has been received from the customer.
Invoice
Depending on where it is in the process, this button will open the highlighted vendor invoice:

- Unposted or Unapproved: Displays in a new Spectrum tab.

- Posted: Displays in the Vendor Invoice Inquiry window.

Release
Use the Release button to manually release the invoice for payment. Only vendor invoices with a Release status may be selected for payment in Accounts Payable.
Selecting this button will store the operator code and date in the Pay-When-Paid Release Note window. Also, the Pay-when-paid? checkbox is cleared on the invoice and the Payment due date is set to the current date. Only the first operator and release date are stored.
Review
Use this button to override the Payment Status of the invoice. Setting it to Flagged for review indicates that the decision to release the invoice has not yet been made, yet some customer cash has been received.
The operator code and date that was stored in the Pay-When-Paid Release Note window are cleared when this status is used.
Waiting
Select to set the Payment Status to Waiting for payment. This is useful when an invoice is moved forward in the process in error and needs to be pushed back.
Any operator code and date that was stored in the Pay-When-Paid Release Note window are also cleared.
Note
Select to open the Pay-When-Paid Release Note window. The operator who released the invoice and the date is also stored here. When system-released, the invoice will state Auto-released during Cash Receipt Update.
Refresh
Select to update the pay-when-paid policy and the totals on the screen.
Status
Select to change the status filters to include items:

- Flagged for review

- Waiting for payment

- Released

## Understanding how A/R Invoices are assigned to Vendor Invoices

The rules for associating customer invoices with vendor invoices depends on the Job Type.
Fixed Price / Unit Price Job Type
The system will read for the customer on the primary contract looking for the first invoice dated later than the vendor invoice on the current row. All vendor invoices that fall into this group will be associated to the customer invoice.
All A/R credit memos are skipped as are A/R invoices dated exactly the same as the vendor invoice.
T+M / Cost Plus Job Type
The system will read the T+M Billing History Table for the vendor and A/P invoice number referenced on the current row. If found, it will then read for the A/R invoice generated by this transaction and determine whether or not it has been paid.
Vendor Information
Key vendor information includes the Vendor, AP invoice #, AP current balance and Days old.
The AP company column indicates the Spectrum company where the invoice's payable is booked. The final two columns on the list box indicate whether or not the invoice is on hold and where the invoice is in the update process (unapproved, unposted or open).
Additional vendor information can be obtained by using the Vendor Info Bar.
Customer Information
Key customer information is provided in the list box, including Customer, Customer invoice #, Customer invoice date and Customer paid date columns.
The AR % paid column is calculated by taking the Customer current paid divided by the Customer original current columns.
The Customer current paid column includes all cash receipts performed on the Customer invoice #. For more information, use the Contract Info Bar to navigate to Payment History.

## Impact to A/P Payment Selection

Accounting will not be able to select any invoice with the Pay-when-paid? checkbox selected. If it is deemed that the invoice should be paid, the operator must go to the Change Vendor Due Dates page to release it. Alternatively, they can use the Job Payables page as well.
Notice that the status of this invoice is Pay-when-paid and it cannot be selected for payment.
Remember that the invoice still may be on an accounting hold once it has been cleared for payment after it has left the Job Payables page.

## Dashboard Apps

Dashboard apps are provided to alert the operator of pay-when-paid invoices in need of review.
Vendor Pay-When-Paid Invoices
The Vendor version displays pay-when-paid transactions for all jobs. Selecting a job will take the user to the Job Payables screen for the job in context.
My Jobs Pay-When-Paid Review
The My Jobs version displays all pay-when-paid invoices for the user's jobs only.
Selecting on a job will take the user to the Job Payables screen for the job in context.

## A/P Vendor Aging Reports

Remember that pay-when-paid invoices have an invoice due date of today. This means that they will always appear in the Not Yet Due section of the pie chart.
Reports
By rule, vendor invoices that use pay-when-paid terms will always appear as Current.
Aged Payables Report
All formats of the Aged Payables Report portray all pay-when-paid invoices are Current. The report will display an asterisk indicating that the item uses pay-when-paid terms and not the payment due date.
Cash Requirements Report
The Cash Requirements Report provides options to include or exclude items based on their pay-when paid status.
Because we do not know when pay-when-paid invoices become eligible for payment, the report now portrays them using a cash requirement date of Pay-When-Paid and Beyond. Like the Aged Payables Report, an asterisk will indicate these pay-when-paid terms and the payment due date will be blank.

## Key Security Settings

Job Payables
Access to the Job Payables page requires a JC level 2.
To process and release invoices on the screen, a JC level 4 security is required. Security is provided to grant or revoke security access to the Release, Review, Waiting, and Note action buttons. In Function Security, this is titled Job Payables – Release Processing.
When the operator does not have the appropriate security, they will only see Invoice, and Refresh action buttons. This is also how the job will appear when there is no pay-when-paid policy.
Job Payables - Pay-When-Paid Policy Button
When operators have security to the Job Setup page (JC level 4), they will also have access to the Pay When-Paid button on the Job Payables screen. The rationale is simple: if you don’t have security to set it up on the job, you don’t have security to change it here.
Job Payables - Invoice Button
The Invoice button will function as it does over in Accounts Payable. Unapproved or unposted invoices will open to Vendor Invoice Entry in a new Spectrum tab provided the operators have security access. Open (posted) invoices will display in the Vendor Invoice Inquiry window.
Vendor Invoice Entry – Edit Ability
The operator must have security access to edit the heading of an unapproved or unposted vendor invoice to be able to modify the Pay-when-paid checkbox.

## Out of Scope

Recurring Vendor Invoice Update
The Pay-when-paid checkbox always defaults to not selected (clear) for non-PO and non-Sub invoices. In the event that a recurring invoice is job related, it will still default as unchecked when it updates to Vendor Invoice Entry. However, once the invoice is in Vendor Invoice Entry, the operator can manually set the flag.
