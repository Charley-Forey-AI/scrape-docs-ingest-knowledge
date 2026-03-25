---
title: "Field Definitions: HQ Escalation Index Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form/field-definitions-hq-escalation-index-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/about-the-hq-escalation-index-form/field-definitions-hq-escalation-index-form"
---

# Field Definitions: HQ Escalation Index Form

The following is a list of field descriptions for the HQ
 Escalation Index form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Country

 Enter the country (from HQ Countries) to which this pricing index applies.

##  State

 Enter the state (from HQ States) to which this pricing index applies (must be a valid state for the specified country).

##  Price Index

 Enter the price index code, up to 20 characters.

##  Description

 Enter a description of this pricing index, up to 120 characters.

## Factor

Enter the default escalation factor for this pricing index (e.g. 5% as .05), as defined by the specified state. This is the amount by which pricing must increase/decrease before an adjustment will be applied.
Note:You may override this factor at the month level (Monthly Index tab) or by quote (in MS Quotes, Info tab).

##  Minimum Days

 Enter the minimum number of days from the contract start date (jobs) or bid index date (customer jobs) before price escalation will be applied.
Note: You may override the minimum days at the monthly index
 level as necessary.

##  Minimum Amount

 Enter the minimum amount that the price escalation adjustment must meet to be applied. This value will be used in conjunction with the factor.
 For example, say the factor is 5%, the minimum amount is $50.00, the bid index amount is $632.00, and the current month’s index is $668.00. Although the adjustment (36.00) meets the 5% factor requirement, it is less than the $50.00 minimum and would therefore, not be applied.
Note: You may override the minimum amount at the monthly
 index level as necessary.

##  Notes

 Use this tab to enter any miscellaneous notes about this pricing index. The space allowance is virtually unlimited.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

##  Seq

 Display only, the sequence number assigned to this index once the record is saved.

##  From Date

 Enter the first day that this price escalation
 adjustment begins. Date must be unique for this pricing index (i.e. cannot exist in another
 date range for this index).
Note:You must set up a ‘bid index’ for each applicable
 job and customer job (i.e. jobs/customer jobs to which price escalation will be
 applied). The bid index is the monthly index entry used as the ‘starting point’ for
 price escalation. The from/end date range defined for the bid index must include the
 job/customer job’s Bid Index Date in MS Quotes (jobs or customer jobs) or the contract
 start month in JC Jobs/PM Projects (if no quote exists for the job). For example, if
 setting up a bid index for a job with a Bid Index Date of 01/15/09 (in MS Quotes), you
 might enter ‘01/01/09’ as the From Date and ‘01/31/09’ as the End Date.

##  End Date

 Enter
 the last day that this price escalation adjustment applies. Date must be unique for this
 pricing index (i.e. cannot exist in another date range for this index). Initially defaults
 the last day of the month specified in the From Date field.
Note:You must set up a ‘bid index’ for each applicable
 job and customer job (i.e. jobs/customer jobs to which price escalation will be
 applied). The bid index is the monthly index entry used as the ‘starting point’ for
 price escalation. The from/end date range defined for the bid index must include the
 job/customer job’s Bid Index Date in MS Quotes (jobs or customer jobs) or the contract
 start month in JC Jobs/PM Project Master (if no quote exists for the job). For example,
 if setting up a bid index for a job with a Bid Index Date of 01/15/09 (in MS Quotes),
 you might enter ‘01/01/09’ as the From Date and ‘01/31/09’ as the End Date.

##  English Price

 Enter the price escalation adjustment, in English dollars.

##  Metric Price

 Enter the price escalation adjustment, in metric dollars.

##  Factor

 Enter the override factor for this price escalation adjustment (e.g. 5% as .05) as defined by the specified state, if applicable. This is the amount by which pricing must increase/decrease before this adjustment will be applied.

##  Min Days

 Enter the override minimum number of days from the contract start date (jobs) or bid index date (customer jobs) before price escalation will be applied, if applicable. Initially defaults from the price index (Info tab).

##  Min Amount

 Enter the override minimum amount that the price escalation adjustment must meet to be applied, if applicable. This value will be used in conjunction with the factor.
 For example, say the factor is 5%, the minimum amount is $50.00, the bid index amount is $632.00, and the current month’s index is $668.00. Although the adjustment (36.00) meets the 5% factor requirement, it is less than the $50.00 minimum and would therefore, not be applied.

##  Notes

 Enter any notes pertaining to this price escalation entry. For additional space in which to write detailed notes, double-click on this field. The Grid Notes window displays, allowing virtually unlimited space for your notes and information.

##  Matl Group

 Enter the material group (from HQ Groups) of the finish and component material to which this price escalation adjustment applies.

## Finish Material

Enter the finished good material that represents the mix design formula for this price escalation adjustment. Material must be set up as a finished good in IN Bill of Materials or IN Bill of Materials Override.
Note:Material may be set up multiple times for a country/state/price index as long as the Material Group differs.

##  Component Matl

 Enter the component material to which the price escalation adjustment applies. Material must be set up as a component for the finished good material in IN Bill of Materials or IN Bill of Materials Override.
Note: Component material may be set up multiple times for a
 country/state/price index as long as the Material Group differs

##  Notes

 Enter any notes pertaining to this finish material/component material entry. Space is virtually unlimited.
