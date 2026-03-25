---
title: "Field Definitions: JC Revenue Projections Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form/field-definitions-jc-revenue-projections-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form/field-definitions-jc-revenue-projections-form"
---

# Field Definitions: JC Revenue Projections Form

The following is a list of field descriptions for the JC
 Revenue Projections form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Actual Date

 Specify the actual date for revenue projections. Once you have initialized projections, this field is disabled and cannot be changed.
Important: Changing projections for a prior month after you have calculated projections for a later month may cause the later projections to be incorrect. If you must recalculate projections for a prior month, make sure you recalculate all subsequent months. Date field shortcuts
T ort
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

##  Contract

 Specify the contract for which to calculate projections. Must be a valid contract with a status of 'Open'. If you allow posting to closed jobs (flag in JC Company Parameters), contracts with a status of ‘Closed’ are also eligible.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

## Sequence

Display only, system-assigned sequence number for this revenue projections line.
Note: Sequence numbers are based on all entries in the batch. 
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

##  Adjusted Units

 Enabled for non-LS items only.
 If projection values (Adjusted Units/Dollars, Projected Units/Dollars) are not 0.00, enter the number of units by which to adjust (increase or decrease) the current projected units. If you initialized projections, units will default based on the projection method specified during initialization (e.g. if projection method is 'Billed Units and Dollars', this amount will be the total billed units through the month and date specified for this contract item).
 If projection values are 0.00, enter the final projected units for this contract item. For example, if current units are 2000.000 and the final projected units are 4000.000, enter 4000.000 here. Remaining projection values will be calculated accordingly.
Note: Once you plug a value, remaining projection values are recalculated accordingly, and a checkmark appears in the P column (right) to indicate the values are plugged.  
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

##  Adjusted Dollars

 If projection values (Adjusted Units/Dollars, Projected Units/Dollars) are not 0.00, enter the dollars by which to adjust (increase or decrease) the current projected dollars. If you initialized projections, dollars will default based on the projection method specified during initialization. For example, if the projection method is 'Billed Units and Dollars', this amount will be the total billed dollars through the month and date specified for this contract item.
 If projection values are 0.00, enter the final projected dollars for this contract item. For example, if your current contract dollars are 15,000.00 and the final projected dollars are 25,000.00, enter 25,000.00 here. Remaining projection values will be calculated accordingly.
Note: Once you plug a value, remaining projection values are recalculated accordingly, and a checkmark appears in the P column (right) to indicate the values are plugged.  
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

## Projected Units

For non-LS items only.
If projection values (Adjusted Units/Dollars, Projected Units/Dollars) are not 0.00, this field defaults the current projected units (previous projected units plus/minus adjusted units) for this contract item. Overriding this value will cause remaining projection values to be recalculated and the system will check the Plugged box.
Note: If you override this field to be 0.00, the system will
 uncheck the Plugged box.
If projection values (Adjust Units, Adjust Dollars, Projected Units, and Projected Dollars) are 0.00, enter the final projected units here.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

## Projected Revenue

If projection values (Adjusted Units/Revenue, Projected Units/Revenue) are not 0.00, this field defaults the current projected dollars (previous projected dollars plus/minus adjusted dollars) for this contract item. Overriding this value will cause remaining projection values to be recalculated and a checkmark to appear in the Plugged column.
Note: If you override this field to be 0.00, the system will
 uncheck the Plugged box.
If projection values (Adjust Units, Adjust Dollars, Projected Units, and Projected Dollars) are 0.00, enter the final projected dollars here.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

## Plugged

Check this box if the projection values for this contract item are plugged (i.e. entered manually). The system will automatically check this box if you enter a value in the adjusted or projected fields. You can also leave the projection and adjusted fields set to zero and check this box to create a zero dollar projection.
If unchecked, indicates projection values for this contract item were initialized using [JC Revenue Calculation ](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-calculation-form).

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections

##  Notes

 Enter any notes specific to this revenue projection and contract item. Notes entered here are stored in the JCCI (Contract Items) table, and will therefore be included in any future revenue projections for this contract item. For tracking and identification purposes, it is recommended that you include the date at the beginning or ending of the note.
 For additional space in which to write more detailed notes, double-click on this field. The JC Notes window displays, allowing you virtually unlimited space for your notes and information. There is however, a maximum allowance of 8k.
 Standard notes (set up in HQ Standard Note) can be added if applicable. Make sure focus is in the Notes field, then move to any gray area on the screen and right mouse click. From the displayed list, select the Add Std Note option, which will bring up the Standard Note Copy window. Enter the note you wish to copy (use F4 for a list of standard notes), and click OK to add the note to this field.
Tip: To use the 'Tab' feature (such as to indent the first line of a paragraph or create columns), you will need to press 'Ctrl + Tab' for each tab increment.  
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-projections-form)JC Revenue Projections
