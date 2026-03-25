---
title: "About Revenue Recognition for SM Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-recognition-for-sm-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-recognition-for-sm-work-orders"
---

# About Revenue Recognition for SM Work Orders

When setting up agreements and work orders in Service Management, you can specify whether to recognize revenue during the billing process or at the time you incur costs.
The system determines revenue amounts and updates to General Ledger
 differently for each revenue recognition method.
Revenue recognition methods are as follows:

- B-As Billed - With this method, revenue is recognized during the work order billing process. Once you create the invoice, you must process the invoice (that is, post the batch that sends it to AR) to initiate revenue recognition. The recognized revenue amount will be the total invoiced amount.

- C-As Cost Incurred - With this method, the system recognizes revenue using the costs posted to a work order via work completed lines. However, the work complete lines must be associated with work order scopes using the 'As Cost Incurred' revenue recognition method. In addition, revenue recognition is not automatic; it must be processed using the SM Revenue Recognition form.

Note: For work order scopes generated from agreements, the revenue recognition method defaults from the agreement and cannot be changed.

## Revenue Recognition Process for As Billed

With the 'as billed' revenue recognition method, the system recognizes revenue using the billed amount for each work completed line. When you process the invoice, the system updates the appropriate Revenue account or Revenue WIP account (if tracking WIP for the scope's call type) based on the department or division associated with the work order scope and the cost type specified for the work completed line. If you do not specify a cost type for the work completed line, the system uses the Revenue account for the line type category.
For example, say you enter a work completed miscellaneous line and you specify a subcontract cost type with a cost type category of S-Subcontracts. When you process the work order invoice, the recognized revenue amount for the work completed line is posted to the Subcontract Revenue account for the service center department or work order scope division (if one is specified). If you had not specified a cost type for the work completed line, the system would have updated the Other Revenue account, since that is the revenue account used for miscellaneous work completed lines that don't reference a cost type.
In addition to updating the Revenue or Revenue WIP account for the cost type category or line type category, the system also posts an offsetting entry to the Revenue GL account defined for the invoice's receivable type in AR Receivable Types.

## Revenue Recognition Process for As Cost Incurred

For 'as costs incurred' revenue recognition, the process is a little different. With this type, you must run the SM Revenue Recognition process to recognize revenue. Once you specify a through date and month, the system creates a revenue recognition batch, pulling in all applicable work completed lines where the work completed line's date is on or before the through date/month. The amount of revenue recognized for these lines is determined as follows:

- If the work completed line is posted to a T&M work order scope (customer or agreement work order), the recognized revenue amount is the line's Total Billable amount.

- If the work completed line is posted to a Flat Price scope (customer or agreement work order), the system recognizes a revenue amount equal to the work completed line's actual cost amount plus the Margin percentage specified for the work order scope (ex: $100 cost + 10% margin = $110 recognized revenue). However, the work completed line's cost type category must match a cost type category defined in the split revenue entries for the flat price scope. If there is no match, no revenue recognition occurs. The system cannot determine a revenue recognition limit without a split revenue entry amount.
If the Margin percentage is 0.00, the system recognizes a revenue amount equal to the line's actual cost.Note: When recognizing revenue, the system will never exceed the split revenue entry amount. If the line's amount will exceed the limit, the system will recognize revenue up to the limit amount only. If the limit has already been met, no revenue recognition will occur for that work completed line.

- If the work completed line is posted to a non-billable scope (agreement work orders only), the recognized revenue is the line's actual cost plus the Margin percentage specified for the work order scope (which defaults from the Agreement). However, recognized revenue will never exceed the agreement price. If you post a work completed line and have already met the agreement price, no revenue is recognized for that work completed line.
Note: For customer work orders only, work completed lines posted to non-billable scopes are not considered in the revenue recognition process.

The update to GL for revenue recognition is handled differently for 'as cost
 incurred' revenue than it is for 'as billed' revenue. For more information, see
 [GL Updates for 'As Cost Incurred' Revenue on SM Work Orders](/en/vista/vista/service-management/agreements/revenue-recognition/about-revenue-recognition-for-agreements/about-revenue-recognition-for-sm-work-orders/gl-updates-for-as-cost-incurred-revenue-on-sm-work-orders).
