---
title: "Field Definitions: HR ACA Coverage Offer Init Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form/field-definitions-hr-aca-coverage-offer-init-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form/field-definitions-hr-aca-coverage-offer-init-form"
---

# Field Definitions: HR ACA Coverage Offer Init Form

The following is a list of field descriptions for the HR ACA
 Coverage Offer Init form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Offer Date

Offer Date field on the HR ACA Coverage Offer Init form
 Enter the coverage offer date in MM/DD/YYYY format.
If the date specified here matches the
 Activity
 Date of any existing history sequence for an employee, initialization will
 handle the coverage offer as follows:

- If you selected the Overwrite Existing
 Data checkbox and the existing record is for a coverage offer (series
 one code), the system will update the existing coverage record with any changed data
 (i.e. expiration date or offer code).

- If you selected the Overwrite Existing
 Data checkbox and the existing record is for an acceptance event
 (series two code), no coverage offer record will be added.

- If you do not select the Overwrite Existing
 Data checkbox, no coverage offer record will be added.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

## Offer Expire Date

 Enter coverage offer expiration date in MM/DD/YYYY format.
Offer Date field on the HR ACA Coverage Offer Init form

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

## Offer Code

Offer Code field on the HR ACA Coverage Offer Init form
Select an IRS Series 1 coverage offer code.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

## Overwrite Existing Data

Overwrite Existing Data checkbox on the HR ACA Coverage Offer Init form
 Select this checkbox to overwrite existing
 data during initialization. The system will overwrite any existing coverage offer sequence
 where the Activity
 Date matches the Offer Date specified for initialization.
 If the Offer
 Date does not match the Activity Date of any existing coverage
 offer sequence, the system will add a new sequence.
If you do not select this checkbox, the system will add a new coverage offer sequence as long as the Offer Date does not match the Activity Date of an existing coverage offer sequence. If a match is found, no new sequence will be created.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

## Look Back Group

Look Back Group field on the HR ACA Coverage Offer Init form
To restrict initialization to resources within
 only a certain ACA look back group, enter that look-back group in this field. Press
 F4
 for a list of look-back groups.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)

- [About the HR ACA Look Back Group Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-look-back-group-form)

## ACA Employment Status

ACA Employment Status field on the HR ACA Coverage Offer Init form
To restrict initialization to resources with only a certain employment status, select the IRS employment status from the list. This list is specific to ACA employment statuses, and is not related to the Employment Status field on the Info tab.

Related information

- [Initializing ACA Monthly Coverage Offer Dates](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/initializing-aca-monthly-coverage-offer-dates)

- [About the HR ACA Coverage Offer Init Form](/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-aca-coverage-offer-init-form)
