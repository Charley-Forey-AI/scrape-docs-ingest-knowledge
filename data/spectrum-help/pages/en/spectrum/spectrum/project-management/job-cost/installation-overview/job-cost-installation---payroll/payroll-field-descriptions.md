---
title: "Payroll Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---payroll/payroll-field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/installation-overview/job-cost-installation---payroll/payroll-field-descriptions"
---

# Payroll Field Descriptions

A reference table of field descriptions.
Fields
 Descriptions

Default overhead

Calculation method
 Select Percent overhead
 at this prompt to specify that you want to have an additional
 payroll burden added to job cost based on the percentage method.
 This would add an additional percentage amount calculated on the
 total burdened payroll dollars. The next prompt then asks for the
 actual percentage you want for the overhead calculation. Enter the
 percentage as follows: 5% would be entered as 5.00 (the system
 converts it to a percentage for calculation). The payroll overhead
 feature is used for adding additional overhead to your jobs (for
 example, small tools expense) over and above your normal payroll
 burdens. If this option is selected, the Default percent
 field displays on this screen. In the Default percent
 field, enter the default payroll overhead percentage amount.
 Select Amount per hour
 at this prompt to calculate the payroll overhead as an amount per
 hour instead of a percentage of payroll dollars. This gives you
 another method for calculating your overhead rate; some contractors
 like to use hours as their basis for allocation because it is more
 constant and doesn't fluctuate like payroll dollars. The next prompt
 then asks for the rate, which is the rate per hour for your overhead
 calculation. This rate is entered as a rate per hour (for example,
 $1.50 per hour) and is calculated based on total payroll hours not
 adjusted for overtime (one overtime hour is counted as 1 overhead
 hour, not 1.5 hours). If this option is selected, the Default
 amount/hour field displays on this screen. In the
 Default
 amount/hour field, enter the default payroll
 overhead amount per hour.
Select No overhead if
 you want to calculate the payroll without any overhead.

Default percent
 If the Calculation
 method was Amount per hour
 or left blank, this prompt will not display.
 If the Calculation
 method is Percent overhead,
 then enter the default
 percent to be used for overhead calculation.
OR If the preceding field was Percent overhead
 or left blank, this prompt will not display.
If the payroll overhead type is Amount per hour,
 then enter the dollar amount per hour to be used for overhead
 calculation.

Phase
 Decide which phase code you will typically use, if
 any, when the system posts Payroll overhead to Job Cost. If this
 field is left clear, then when adding new jobs the system will
 default all overhead to post to the same phase as the earnings
 specified in Time Card Entry. Instead, if a phase code is
 designated, then the default when adding new jobs will be for
 overhead amounts to post to this phase exclusively. This entry will
 serve as a default only when jobs are added, and can be overwritten
 as needed.
 Your response in this field will serve as a
 default when future jobs are added. Any entry in this field has no
 effect on existing jobs; desired changes to existing jobs must be
 done in Jobs.

Cost type
 Decide which cost type you will typically use, if
 any, when the system posts Payroll overhead to Job Cost. Press
 F4 or
 double-click on this field to select from a list of valid cost
 types. If this field is left blank, then the default when adding new
 jobs will be for any overhead to post to the same cost type as the
 earnings specified in Time Card Entry. Instead, if a cost type is
 designated, then the default when adding new jobs will be for
 overhead amounts to post to this cost type instead of the labor cost
 type specified in Time Card Entry. This entry will serve as a
 default only when jobs are added, and can be overwritten as
 needed.
 Your response in this field will serve as a
 default when future jobs are added. Any entry in this field has no
 effect on existing jobs; changes to existing jobs must be
 done in Jobs.

Default burden

Actual payroll burdens?
 This checkbox determines whether you will want to
 post actual payroll burden or a percentage to job cost when the
 payroll cycle is updated.
 Select this checkbox if you want actual burden
 from payroll to job cost to default when adding new jobs. Leave this
 checkbox clear if you want the percentage burden to default when
 adding new jobs. If this checkbox is left clear, you will be
 prompted to specify the default percentage for burden when new jobs
 are added. For example, you should enter 30 if the desired burden
 percentage will be 30%. This entry will serve as a default only when
 jobs are added and can be overwritten as needed.
Your selection will serve as a default when future jobs are added.
 Whether or not you select this checkbox has no bearing on existing
 jobs; changed to existing jobs must be done in Job Master File
 Maintenance.

Pre-time card burden%
 If the Actual payroll
 burden checkbox is left clear, this prompt will not
 display.
 If you selected the Actual payroll
 burden checkbox, then this prompt will display.
 Enter the pre-time card percentage burden that will be used if you
 have specified that Pre-Time Card Entry information is included on
 some of the job cost inquiries. When you include Pre-Time Card Entry
 hours and dollars on a report or inquiry screen, the system will add
 an additional amount for burden. It will use the percentage that you
 specify here for that burden calculation. This is an estimated
 burden and is used only at the time of reporting or inquiring.
If you left this checkbox clear, then the Default burden %
 prompt will display. In this case, you are using a burden percent
 for all your postings to job cost and that same percentage will be
 used for pre-time card burdens as well.

Phase
 Enter the phase code you will want to use, if any,
 when the system posts payroll burden to job cost. If this field is
 left blank, then the default when adding new jobs will be for burden
 to post to the same phase as the earnings specified in Time Card
 Entry. Instead, if a phase code is designated, then the default when
 adding new jobs will be for burden amounts to post to this phase
 exclusively. This entry will serve as a default only when jobs are
 added, and can be overwritten, as needed.
 Your response in this field will serve as a
 default when future jobs are added. Any entry in this field has no
 effect on existing jobs; desired changes to existing jobs must be
 done in Jobs.

Cost type
 The software is prompting for the cost type you
 will typically want used, if any, when the system posts payroll
 burden to job cost. Press F4 or
 double-click on this field to select from a list of valid cost
 types. If this field is left blank, then the default when adding new
 jobs will be for burden to post to the same cost type as the
 earnings specified in Time Card Entry. Instead, if a cost type is
 designated, then the default when adding new jobs will be for burden
 amounts to post to this cost type instead of the labor cost type
 specified in Time Card Entry. This entry will serve as a default
 only when jobs are added, and can be overwritten, as needed.
 Your response in this field will serve as a
 default when future jobs are added. Any entry in this field has no
 effect on existing jobs; changes to existing jobs must be
 done in Jobs.

Note:About Non-cash Add-onsPayroll Burden does not include any Non-Cash Add-ons appearing on the Properties tab of union setup. Non-Cash Add-ons burden costs are always attributed to the Labor Phase Code, regardless of the values in the Phase and Cost Type fields.
