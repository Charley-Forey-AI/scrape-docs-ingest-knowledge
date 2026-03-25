---
title: "Field Definitions: EM Process Cost Allocations Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-process-cost-allocations-form/field-definitions-em-process-cost-allocations-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-process-cost-allocations-form/field-definitions-em-process-cost-allocations-form"
---

# Field Definitions: EM Process Cost Allocations Form

The following is a list of field descriptions for the EM
 Process Cost Allocations form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Allocation Date

 Specify the allocation date for all transactions in the batch. This date will become the Actual date in the EM Cost Detail table (EMCD).

##  Reversal

 Check this box if you will be reversing these cost allocation transactions in a later month. If checked, all transactions in the batch will be flagged with a reversal status of ‘1-Auto Reverse’.
 Leave this box unchecked if you will not be reversing the cost allocation transactions in this batch. All transactions will be flagged with a reversal status of ‘0-Regular’.
Note: You may override the reversal status by transaction in
 EM Cost Adjustments.

##  Allocation Code

 Specify the allocation code (from EM Allocation Codes) to process. After you enter the allocation code, the section below displays the specifications for this allocation. Some fields on this form may or may not be available for input based on how this allocation code was set up.

##  Equipment

 This field is only accessible if ‘Equipment to Allocate’ option in EM Allocation Codes is set to ‘Prompt for Equipment’.
 Enter the equipment (from EM Equipment) to which you are applying this allocation.

##  Department

 This field is only accessible if ‘Departments to Allocate’ option in EM Allocation Codes is set to ‘Prompt for Departments’.
 Indicate the department (from EM Departments) to which you are applying this allocation.

## Category

Enter a category code or press F4 to select
 one from a list. Category codes are created and maintained using the [EM Categories ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-categories-form) form and they are associated with equipment
 using the Category field on the Info tab of the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form)
 form.
 This field is only enabled when Prompt for
 Categories is selected in the Categories to Allocate field in the [EM Allocation Codes ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-allocation-codes-form)form.

##  Begin Date

 This field is only accessible if date option in EM Allocation Codes is set to ‘By Date Range’.
 Enter the date from which to begin calculating the basis. (Not available if allocations are calculated based on a specific month rather than a date range.

##  End Date

 This field is only accessible if date option in EM Allocation Codes is set to ‘By Date Range’.
 Enter the date from at which to end calculating the basis. (Not available if allocations are calculated based on a specific month rather than a date range.

##  Amount to Allocate

 Initially defaults the allocation amount from EM Allocation Codes, which may be overridden. If no default, specify the amount to allocate for this batch. May be a positive or negative amount (e.g. if you received a refund of a previous allocation, you would enter a negative amount).

Related information

- [Show Basis](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-process-cost-allocations-form/field-definitions-em-process-cost-allocations-form#ID-0000c8ea--en)

## Rate to Allocate

Initially defaults the allocation rate from EM Allocation Codes, which may be overridden. If no default, specify the rate to use for this allocation. May be a positive or negative rate (e.g. if you received a refund of a previous allocation, you would enter a negative rate).

Related information

- [Show Basis](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-process-cost-allocations-form/field-definitions-em-process-cost-allocations-form#ID-0000c8ea--en)

##  Show Basis

 Once you have entered the necessary allocation criteria, click the Show Basis button to show the basis amount. This is the amount used as the basis for calculating the allocation amount. If the basis amount (for the allocation code) is ‘Cost’, the basis amount will be the total costs posted for the equipment, departments, and categories specified.
Process Allocations
 Click the Process button to begin the allocation process. Once processed, a message displays indicating that allocations have been successfully added to your batch and that you can edit the entries in the cost adjustments program. When you close the window, focus returns to the form, allowing you to process additional allocations as necessary. If the allocations could not be processed, a message displays giving you the reason(s) why.
