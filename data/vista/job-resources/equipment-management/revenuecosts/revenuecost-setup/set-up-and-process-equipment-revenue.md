---
title: "Set Up and Process Equipment Revenue | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/set-up-and-process-equipment-revenue"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/set-up-and-process-equipment-revenue"
---

# Set Up and Process Equipment Revenue

The following are the basic steps for setting up and processing equipment revenue.

1. EM Company Parameters – Define the default options for usage processing. Some of the options include specifying the PR Co#; defining whether automatic GL posting will occur whenever posting usage entries; and whether to allow the override of usage rates during usage posting.

1. EM Departments – Define the GL accounts for revenue posting.

1. EM Categories – Define codes that categorize your equipment by similar capabilities so that you can establish standard usage rates by category. Thereafter, all equipment assigned a category will be given that category’s rate as default (which can be overridden if needed). If you want usage posted only to the current job for a piece of equipment, check the Restrict Usage to Current Job option for the equipment category.

1. EM Revenue Codes – Create a code for each of the time increments in which you bill out equipment to jobs differently (for example, an hourly, daily, monthly, and hourly standby code). You will be able to set up a separate usage rate for each of these revenue codes in EM Revenue Rates by Category.

1. EM Revenue Rates by Category – For each equipment category and revenue code combination, define its default usage rates (such as daily and weekly usage rates for backhoes and weekly and monthly usage rates for pickup trucks). When rate changes occur, you will be able to enter them here by category and have the system update the rates for all pieces of equipment in that category except those you override.

1. EM Equipment – Set up each piece of equipment and assign a category. You should also designate its Usage Cost Type (the JC cost type to interface usage cost to in Job Cost).For example, if you have a cost type ‘4’ set up in Job Cost for equipment usage, you should designate ‘4’ as the Usage Cost Type for each piece of equipment so that all direct costs to the job for equipment usage will be posted to cost type ‘4’ in Job Cost.
The Usage Cost Type you specify in the Equipment Master may be overridden, if needed, during usage posting. However, usage posting in PR Timecard Entry does NOT provide the opportunity to override the Usage Cost Type. Therefore, if you will be posting any usage through Payroll, you MUST identify the Usage Cost Type in EM Equipment (even though the screen will allow you to bypass it) or you will get an Invalid Cost Type message when entering timecards.

1. EM Revenue Rates by Equipment — Use to set up override rates by equipment. For each piece of equipment, define the revenue rate that will be used when posting usage. This rate overrides the standard rate defined for the category.
