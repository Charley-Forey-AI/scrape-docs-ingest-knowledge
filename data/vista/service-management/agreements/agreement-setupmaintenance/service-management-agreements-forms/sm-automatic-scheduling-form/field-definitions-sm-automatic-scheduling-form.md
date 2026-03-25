---
title: "Field Definitions: SM Automatic Scheduling Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-automatic-scheduling-form/field-definitions-sm-automatic-scheduling-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-automatic-scheduling-form/field-definitions-sm-automatic-scheduling-form"
---

# Field Definitions: SM Automatic Scheduling Form

The following is a list of field descriptions for the SM
 Automatic Scheduling form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Frequency

Automatic Bill Scheduling
Select the frequency at which to schedule billings. The system will use the frequency in conjunction with the start date and agreement term to generate a billing schedule.

- A - Annual: Select this option to set up a single billing sequence on the specified date for each year in the agreement term.

- M - Monthly: Select this option to set up one billing sequence per month for the term of the agreement.

- Q - Quarterly: Select this option to set up one billing sequence per quarter for the term of the agreement. Quarters will be based on the Start Date, so may not occur in the standard calendar year quarters.

- B - Bi-Monthly: Select this option to set up billing sequences every two months for the term of the agreement. For example, if the first billing sequence is 7/1/15, the next billing sequence will be on 9/1/15, then 11/1/15, and so forth.

- S - Semi-Annual: Select this option to set up billing sequences twice a year (every six months) for the term of the agreement. For example, if the first billing sequence is 1/1/15, the next billing sequence will be on 7/1/15, then 1/1/16, and so forth.

- T - Three Per Year: Select this option to set up billing sequences three times a year (every four months) for the term of the agreement. For example, if the first billing sequence is 7/1/15, the next billing sequence will be 11/1/15, then 3/1/16, and so forth.

Automatic Amortization Scheduling
Select the frequency at which to schedule revenue deferrals. The system will use the frequency in conjunction with the start date and agreement term to generate an amortization schedule.

- A - Annual: Select this option to set up a single deferral sequence on the specified date for each year in the agreement term.

- M - Monthly: Select this option to set up one deferral sequence per month for the term of the agreement.

- Q - Quarterly: Select this option to set up one deferral sequence per quarter for the term of the agreement. Quarters will be based on the Billing Start Date, so may not occur in the standard calendar year quarters.

- B - Bi-Monthly: Select this option to set up deferral sequences every two months for the term of the agreement. For example, if the first deferral sequence is 7/1/15, the next deferral sequence will be on 9/1/15, then 11/1/15, and so forth.

- S - Semi-Annual: Select this option to set up deferral sequences twice a year (every six months) for the term of the agreement. For example, if the first deferral sequence is 1/1/15, the next deferral sequence will be on 7/1/15, then 1/1/16, and so forth.

- T - Three Per Year: Select this option to set up deferral sequences three times a year (every four months) for the term of the agreement. For example, if the first deferral sequence is 7/1/15, the next deferral sequence will be 11/1/15, then 3/1/16, and so forth.

## Start Date

Automatic Bill Scheduling
Enter the date on which the first billing will occur or select the start date using the pop-up calendar. Initially defaults the agreement's effective date.
The date specified here will become the default date for each billing entry in the schedule. For example, if you select 6/15/15 as the start date, the billing date for each billing sequence will be the 15th. You can override the billing date once the schedule has been generated.
Automatic Amortization Scheduling
Enter the date on which the first revenue deferral will occur or select the start date using the pop-up calendar. Initially defaults the agreement's effective date.
The date specified here will become the default date for each deferral entry in the schedule. For example, if you select 6/15/15 as the start date, the date for each deferral sequence will be the 15th. You can override the deferral date once the schedule has been generated.

## Tax Type

This field is only available if auto-generating billing schedules.
Enter the tax type to use when billing the agreement. Leave blank if taxes are not applicable.

- 1 - Sales

- 2 - Use

- 3 - VAT

## Tax Code

This field is only available if auto-generating billing schedules.
Enter the tax code to use when billing the
 agreement. Press F4 for a list of valid tax codes.

## Tax Basis Percent

This field is only available if auto-generating billing schedules.
Enter the tax basis percent to use when calculating the tax basis for each sequence in the billing schedule.
When generating the billing schedule, the system first calculates the billing amount for each sequence. It then uses the billing amount and the tax basis percent to determine the tax basis amount for each bill sequence.
