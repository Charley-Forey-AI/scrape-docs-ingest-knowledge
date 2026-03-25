---
title: "Initializing ACA Monthly Coverage Offer Dates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates"
---

# Initializing ACA Monthly Coverage Offer Dates

Use the HR ACA Coverage Offer Init form to initialize monthly
 coverage offer dates data for resources into the ACA History tab of the HR Resources form.

This automates data entry of ACA information. This information is then used to populate data required in the Payroll module for Affordable Care Act compliance.
Note: Users should be familiar with IRS definitions and
 requirements for ACA reporting before using Vista to enter ACA data and
 generate reports. For more information, visit the Internal Revenue Service website
 at [www.irs.gov](http://www.irs.gov/) and search for
 "Instructions for Forms 1094-C and 1095-C".
Before starting this procedure, ACA Look Back groups must already have been created. For more information, see [HR ACA Look Back Group](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-look-back-group-form).

To initialize monthly coverage offer dates data for
 all resources into the ACA History tab of HR Resources:

1. In HR Resources, press
 F4 in the Resource # field to select
 form a list of existing resources. If the resource you want does not yet exist,
 you must create it first.

1. Select Initialize
 HR ACA Coverage Offer from the Tasks pull-down list.The HR ACA Coverage Offer Init form
 displays.

1. In the Offer Date field, enter the offer date (in MM/DD/YYYY format). For information about how the system handles an Offer Date that matches the Activity Date of an existing coverage offer sequence, see [Offer Date](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form/field-definitions-hr-aca-coverage-offer-init-form#ID-0001182f--en).

1. In the Offer Expire Date field, enter the offer expiration date (in MM/DD/YYYY format).

1. From the Offer Code drop-down, select the IRS offer code.

1. If you want to overwrite
 existing data in the ACA History tab for the selected resource, select the
 Overwrite Existing Data checkbox. For information about how
 the system handles this during initialization, see the [Overwrite Existing Data](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form/field-definitions-hr-aca-coverage-offer-init-form#ID-0001185b--en) F1 help. If you want to
 restrict initialization to resources within a specific look back group, enter
 the look-back group in the Look Back Group field. Press
 F4 for a list of look-back groups. To restrict initialization to
 resources with a specific employment status, select the IRS employment
 status from the ACA Employment Status
 drop-down. Options are:

- F – Full Time

- P – Part Time

- V – Variable

- S – Seasonal

1. Click Initialize.  The initialization process creates the appropriate
 coverage offers (1094-C and 1095-C data) to the ACA History tab (in HR
 Resources) for all specified resources. Resources with a termination date
 (Term Date field, Payroll Info tab) are excluded from
 initialization.
Once initialization is complete, you can edit the records as needed in the ACA History tab.

Related concepts

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [PR ACA 1095-C Employee Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/pr-aca-1095-c-employee-form)

Related tasks

- [Set Up Employee Information for ACA 1095-C Processing](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/set-up-employee-information-for-aca-1095-c-processing)

Related information

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

- [About the HR ACA Look Back Group Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-look-back-group-form)

- [About the HR Resources Form](/en/vista/vista/hr-and-payroll/human-resources/applicantsresources/resource-setupmaintenance/about-the-hr-resources-form)

- [Set up Earnings Codes: United States](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states)

- [Set Up Employer Information for ACA 1094-C Processing](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/set-up-employer-information-for-aca-1094-c-processing)

- [Set Up Employee Information for ACA 1095-C Processing](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/aca-reporting/set-up-and-process-data-for-aca-1094s-and-1095s/set-up-employee-information-for-aca-1095-c-processing)
