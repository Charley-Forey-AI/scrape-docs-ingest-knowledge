---
title: "Copy Union Codes | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-union-codes"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/copy-union-codes"
---

# Copy Union Codes

This screen is used to copy information from one union file
 to another.
Caution should be exercised when performing this function. Any date-sensitive wage code,
 union deduction, fringe, benefit tier, rate information and standard labor rates will be
 automatically included in the copy.
This feature uses the processing date less one day. This is because when copying an existing union to a new union the goal is to create the union so that edits can be made using today's date. For example, if you have a union contract with several rate structures, you will need to set up multiple union codes, each with different rates, and it usually makes the first three characters of the code the same (the Payroll calculation has to be different for the trainees and journeymen but it is really one union to report to at the end of the month). Because these (sub)unions are very similar, you will need to set up one and then copy it to the other (sub)unions, and then go into the copied one and change the pay rates, deduction rate, fringe rate and/or inactivate deductions/fringes. Also, because there is usually editing to be done after creating the new union, Spectrum saves today's date for the actual new rates and status setting; otherwise you would receive an error stating that a revision already exists for this date.
