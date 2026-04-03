---
title: "Change Request Entry - Costs | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---costs"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/accounts-receivable/spectrum-menus/data-entry-overview/change-request-entry/change-request-entry---costs"
---

# Change Request Entry - Costs

Use this tab to enter contractor and subcontractor pricing changes. The sum of these cost changes will display on the Take off total in the header.
Field/Button
Description

Line
The system automatically assigns a sequential line number to the prices listed. Entry is allowed when adding a change request.

Phase
Enter a phase number for each pricing change. Leaving this field blank is allowed if the action type is set to 4-No recognition of revenue or cost, no billing, but if a valid subcontract is entered on this worksheet, the Phase and Ct fields are must-enter.
Note: Data entry is prevented if the phase status is set to Complete. A warning displays if the status is set to Inactive.
If this is a sub-job transaction set up on a master job, double-click on this field to search phases for the sub-job. This will allow you to easily select a phase set up on a master job, but not present on the sub-job. Spectrum will add a new phase to the sub job if the current job is a sub-job of a valid master job, the phase lengths of both jobs match, and the Phase + Cost type combination for the current job is valid and not 'Complete'.

Ct
Enter a cost type for each pricing change. Leaving this field blank is allowed if the action type is set to 4-No recognition of revenue or cost, no billing, but if a valid subcontract is entered on this worksheet, the Phase and Ct fields are must-enter.
If the job/phase/cost type combination does not exist in the phase file, and error message will prompt you to either create a new phase or clear the preceding fields and start again.

Description
The phase description will display in this field.

Um
The unit of measure will default from the phase.

Quantity
Enter a quantity for the pricing change in this field. Positive, negative, and blank values are allowed.

Hours
Enter the number of hours for each pricing change in this field. Positive, negative, and blank values are allowed.

Estimate amount
Enter the dollar amount for each pricing change in this field. Positive, negative, and blank values are allowed.
If a valid subcontract is entered, this amount will be defined as subcontractor pricing.

Subcontractor
The vendor code specified for this job displays in this field.

- If an invalid vendor code was entered, the field will allow you to search for vendors.

- If no valid vendor code was specified for this job, the subcontract fields will be skipped.
Note: This field will not be available if the Phase is blank.

Subcontract #
Enter the subcontract number for this change request.
If the vendor code + subcontract # does not exist, an error message will alert you that the subcontract is not set up. Click Add New subcontract to create a new subcontract based on the job and vendor code.

Sub CO amount
When a valid subcontract # is entered, the estimate amount will default in this field.

Sub bill item
Enter a subcontract bill item for the current phase in this field.
If the subcontract bill item does not exist, an error message will alert you that the bill code is not set up. Click OK to specify a bill group, bill item, and description.

Sub status
Select a subcontract status: Executed, Proposed, or Rejected
A blank status indicates that this line is not assigned to a subcontract.

Sub CO #
Enter a subcontract change order #.

Sub CO date
Enter a date for the subcontract change order. The date entered here will appear in the same field on the Subcontract Change Order Log, and when changed on that screen the updated date will appear on this screen.
Note: The date entered here must be within the minimum/ maximum period date range specified for this company.

Sub signed date
Enter a subcontract signed date. The date entered here will appear in the same field on the Subcontract Change Order Log, and when changed on that screen the updated date will appear on this screen.

Sub CR description
Enter a subcontract change request description. This description will also appear on the Subcontract Change Order Log.

Sub CR type
Enter a subcontract change request type in this field.

Sub proposal date
Enter a subcontract proposal date. The date entered here will appear in the same field on the Subcontract Change Order Log, and when changed on that screen the updated date will appear on this screen.

Sub sent date
Enter a subcontract sent date. The date entered here will appear in the same field on the Subcontract Change Order Log, and when changed on that screen the updated date will appear on this screen.

Sub due date
Enter a subcontract due date. The date entered here will appear in the same field on the Subcontract Change Order Log, and when changed on that screen the updated date will appear on this screen.

Comments
Enter any notes related to the change request in this field.
