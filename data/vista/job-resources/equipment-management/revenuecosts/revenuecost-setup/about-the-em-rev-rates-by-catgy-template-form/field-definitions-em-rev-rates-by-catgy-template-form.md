---
title: "Field Definitions: EM Rev Rates by Catgy Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-rev-rates-by-catgy-template-form/field-definitions-em-rev-rates-by-catgy-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-rev-rates-by-catgy-template-form/field-definitions-em-rev-rates-by-catgy-template-form"
---

# Field Definitions: EM Rev Rates by Catgy Template Form

The following is a list of field descriptions for the EM Rev
 Rates by Catgy Template form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Category

 Specify the category for which you are setting up override or percent of standard rates. All rates entered for this category will apply to all equipment within this category.

##  Revenue Code

 Enter the revenue code to which the override or percent of standard rates apply for this category.

##  Rate

 Used for ‘Rate Override’ templates only.
 Enter the override rate to use when posting usage to this category/revenue code on a job using this Revenue Template.

##  % of Rate

 Used for ‘Percent of Standard Rate’ templates only.
 Enter the percentage of the standard revenue rate to use when posting usage to this category/revenue code on a job using this Revenue Template.

##  Allow Posting Override

 This option is only accessible if the ‘Allow Rate Change’ option in EM Company Parameters (Usage tab) is checked.
 Check this box to allow overriding the revenue rate for this category/revenue code when posting usage to jobs using this revenue template.
 Leave this box unchecked if not allowing overrides to the revenue rate for this category/revenue code when posting usage to jobs using this revenue template.

##  Revenue Breakdown Code

 This field is only accessible if using the ‘Rate Override’ template type.
 Initially defaults the revenue breakdown code specified in EM Company Parameters. If the default code is not applicable to this template/category/revenue code, delete it and then add new breakdown codes as necessary.
Note: If the total breakdown rate does not match the
 override rate and you attempt to move off the tab, a message displays indicating that the
 breakdown total does not equal the revenue rate total, and asking if you would like to
 automatically update the revenue rate. Select ‘Yes’ to have the override rate adjusted to
 equal the total breakdown rate. If you select No, you cannot exit this tab until you
 manually adjust the rates to match the override rate.

##  Amount

 This field is only accessible if using the ‘Rate Override’ template type.
 Initially defaults the total amount of the revenue rate for the specified revenue code. If multiple breakdown codes exist, enter the applicable amount for this breakdown code. Make sure the total of all breakdown rates equals the total override revenue rate.
Note: If the total breakdown rate does not match the
 override rate and you attempt to move off the tab, a message displays indicating that the
 breakdown total does not equal the revenue rate total, and asking if you would like to
 automatically update the revenue rate. Select ‘Yes’ to have the override rate adjusted to
 equal the total breakdown rate. If you select No, you cannot exit this tab until you
 manually adjust the rates to match the override rate.
