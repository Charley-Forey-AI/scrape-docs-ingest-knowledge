---
title: "Field Definitions: EM Categories Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-categories-form/field-definitions-em-categories-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-categories-form/field-definitions-em-categories-form"
---

# Field Definitions: EM Categories Form

The following is a list of field descriptions for the EM
 Categories form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Category

 Enter a code, up to 10 characters, that identifies this category.

##  Description

 Enter a description of this category, up to 30 characters.

## PR Class

For each category you set up, you have the option to specify the default PR Class to use when posting equipment usage in PR Timecard Entry. However, timecards will only default this class when you have specified to enter the equipment before the craft/class (i.e. you have checked the Equipment Class Override option in PR Timecard Entry, Options menu). If you enter the equipment after the craft/class (i.e. the Equipment Class Override option is unchecked), the class will default as specified for the employee in PR Employees.

##  PR Class

 Enter the PR Class to use when posting usage to equipment in this category in PR Timecard Entry. You will only need to make an entry in this field if the equipment operator's pay rate is based on the type of equipment operated. It will only be used if timecards are set up to allow input of the equipment before the craft and class (i.e. the Equipment Class Override option is checked in PR Timecard Entry, Options menu) and will be the default class when entering timecards, if it is a valid class for the specified craft. It will then determine the pay rate for the operator of the equipment.
 Any class may be entered and no validation is provided. An F4 will be available only if you specified a PR Company in EM Company Parameters, and will display all classes, regardless of craft, from that company. However, since multiple PR companies could post to this company's equipment, no company-specific validation is provided.

##  Restrict Usage to Current Job

 Check this box to restrict posting of
 equipment usage (in EM and PR) to the current job for a piece of equipment (i.e., the job
 to which the equipment is currently assigned).
You can view the job that a piece of equipment
 is assigned to using the Job field on the Info tab of the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form.
 Leave this box unchecked if allowing
 equipment usage to be posted to any valid job in EM and PR.

## Restrict Usage to Current Job

This option allows you to restrict posting of equipment usage to the current job for the equipment, thus reducing incorrect usage entries. However, in order for this option to be useful, you must be actively using the EM Location Transfers form.
