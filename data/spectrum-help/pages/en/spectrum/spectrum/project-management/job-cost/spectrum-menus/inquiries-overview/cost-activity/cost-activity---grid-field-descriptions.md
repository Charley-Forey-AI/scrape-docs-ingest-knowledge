---
title: "Cost Activity - Grid Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/cost-activity/cost-activity---grid-field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/cost-activity/cost-activity---grid-field-descriptions"
---

# Cost Activity - Grid Field Descriptions

Use the table below for reference when completing fields on this screen.
Column type
Description

Cost summary
When all checkboxes in the Job-to-date calculations section in the [Advanced Selections](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/advanced-selections) window are selected, the Cost summary section includes the following:

- Actual job-to-date history: Sum of cost values in the Job Cost History Table through the period-end date associated with the current Job Cost processing date of phases/cost types included in the list box (see calculation HH in the Report Calculations -- Job Analysis Inquiry topic).

- Open commitments: Sum of values displayed in the Open commitments (commit) column (see calculation B).

- Unposted A/P invoice cost: Sum of extensions of all invoice detail lines in the Unapproved Invoice Detail Table assigned to phases/cost types included in the list box (see calculation l).

- Unposted Payroll cost: Sum of extensions of all time card detail lines in the Pre-Time Card Detail Table plus the Burden% designated in the Job Cost Master Table, up to the period-end date associated with the current Job Cost processing date of phases/cost types currently included in the list box. Pre-time cards with work dates later than this period-end date are disregarded. This calculation method is consistent with how time cards are handled in other Job Cost inquiry screens and reports (see calculation m).

- JTD cost: Sum of values displayed in this box: Actual job-to-date history + Open commitments + + Unposted costs + Unapproved invoices + Pre-time cards (see calculation A).

Cost projections
This section includes the following:

- Projected cost: Sum of the values displayed in the Projected cost column (see calculation D)

- Current estimate: Sum of values displayed in the Estimate column (See calculation C)

- Variance: Projected cost total minus Estimate total

- Variance %: Variance total divided by Estimate total times 100; if the Estimate total equals zero, then the variance% will be set to zero.

Job progress
This section includes the following:

- Hours to complete: If the job status is complete, then the progress will be set to zero If the job status is set to active or inactive, then the calculation will be Projected hour total minus Total job-to-date hours; if the difference is negative, then the calculation will be set to zero.

- Cost to complete: If the job status is complete, then the calculation will be set to zero. If the job status is set to active or inactive, then the calculation will be Projected cost total minus Total job-to-date cost; if the difference is negative, then the calculation will be set to zero.

- % complete: If the Job status is set to complete, then the calculation will be set to 100% JOB STATUS = ACTIVE OR INACTIVE ('Projected cost total' minus 'Cost to complete') / 'Projected cost total' x 100; if 'Projected cost total' is zero, set % complete to zero.

Hours summary
When all checkboxes in the Job-to-date calculations section in the [Advanced Selections](/en/spectrum/spectrum/project-management/job-cost/spectrum-menus/inquiries-overview/advanced-selections) window on the main Job Analysis Inquiry screen are selected, the Hours summary section includes the following:

- Actual job-to-date history: Sum of the total hours values in the Job Cost History Table through the period-end date associated with the current Job Cost processing date of phases/cost types included in the list box (see calculation JJ).

- Contract labor hours history: Sum of contract hours values associated with Job Cost History records through the period-end date associated with the current Job Cost processing date of phases/cost types included in the list box (see calculation r).

- Unapproved contract hours: Sum of contract hours associated with all invoice detail lines in the Unapproved Invoice Detail Table for phases/cost types currently included in the list box display (see calculation s).

- Pre-time card hours: Sum of hours of all time card detail lines in the Pre-Time Card Detail Table, up to the period-end date associated with the current Job Cost processing date of phases/cost types currently included in the list box display. Pre-time cards with work dates later than this period-end date are disregarded (see calculation n).

- Total job-to-date hours: Sum of the values displayed in this section: Actual job-to-date history plus Contract labor hours history plus Unapproved contract hours plus Unposted costs plus Pre-time card hours.

Hours projections
The Hours projections section includes the following:

- Projected hours: Sum of values displayed in the Projected hours column (see calculation J).

- Current estimate: Sum of values currently displayed in the 'Estimated hours' column (see calculation G).

- Variance: Projected hours total minus Estimate hours total.

- Variance %: (Projected hours total minus Estimated hours total) / Estimated hours total x 100; if the Estimated hours total is zero, then the set variance% will be set to zero.

Rate / hour analysis
The Rate / hour analysis section includes the following:

-  $/hour: Total job-to-date cost / Total job-to-date hours

-  Projected $/hour: Projected cost / Projected hours total

-  Estimated $/hour: Current estimate / Estimated hours total
