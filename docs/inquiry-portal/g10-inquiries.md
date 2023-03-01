# Health IT Feedback and Inquiry Portal: Standardized API Certification Criterion at § 170.315(g)(10)

This section contains anonymized feedback and inquiries, related to the standardized API certification criterion at (g)(10), that ONC has handled through the ONC <a target = "_blank" href = "https://www.healthit.gov/feedback">Health IT Feedback Portal</a>. The inquiries are organized by date under headers that mirror the organization of paragraphs in the Code of Federal Regulations at 45 CFR § 170.315(g)(10). A section is also included for inquiries related to (g)(10) Standardized API Test Kit in the Inferno Framework.

!!! attention

    The date headers provide important context as some information may have changed since the time of an inquiry and response.

## Applies to Entire Criterion
### January 2023
**Stakeholder Inquiry**: We have a question about this text in the US Core Server CapabilityStatement:
!!! note ""

    The US Core Server SHALL:

    1. Support the US Core Patient resource profile.
    1. Support at least one additional resource profile from the list of US Core Profiles.
    1. etc...

Does this imply that we need to certify only the Patient resource, and one other resource, such as Medication? How is this tested in Inferno?

**ONC Response**: Health IT Modules being certified to the § 170.315(g)(10) criterion must support US Core profiles (or FHIR core profiles if no corresponding US Core profile exists) for each of the data in the United States Core Data for Interoperability (USCDI) standard. <a target = "_blank" href = "https://www.healthit.gov/isa/united-states-core-data-interoperability-uscdi">USCDI</a> includes more data than Patient Demographics/Information, so more US Core profiles than US Core Patient must be supported for § 170.315(g)(10) certification. US Core includes <a target = "_blank" href = "https://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#us-core-data-for-interoperability-and-2015-edition-common-clinical-data-set">guidance</a> for how USCDI data can map to FHIR Core and US Core profiles.

Please see the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services">§ 170.315(g)(10) Certification Companion Guide</a> for additional details and guidance regarding requirements for supporting US Core.

The Inferno <a target = "_blank" href = "https://github.com/onc-healthit/onc-certification-g10-test-kit">ONC Certification (g)(10) Standardized API Test Kit</a> implements tests according to the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#test_procedure">§ 170.315(g)(10) Test Procedure</a>. This Test Procedure defines tests to verify conformance to § 170.315(g)(10) requirements to support US Core profiles (or FHIR core profiles if no corresponding US Core profile exists) for each of the data in USCDI. Therefore, the Inferno ONC Certification (g)(10) Standardized API Test Kit includes tests for US Core profiles beyond the US Core Patient profile.

### November 2022
**Stakeholder Inquiry**: We have some questions regarding the consent requirements for § 170.315(g)(10) Standardized API for patient and population services.

- If a patient is accessing data, are providers required to obtain a separate consent from the patient?
- Is patient consent required for Multiple Patient Population Bulk Export?
- Are there documented standards for consent and § 170.315(g)(10) Standardized API for patient and population services?

**ONC Response**: For information on the technical requirements and standards for the § 170.315(g)(10) criterion, please see the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services">§ 170.315(g)(10) Certification Companion Guide</a> (CCG). The § 170.315(g)(10) CCG includes ONC guidance including technical clarifications for the requirements regarding responding to requests for a single patient’s data and requests for multiple patients’ data.

For information on ONC Certification Program requirements on actions and behaviors of Certified API Developers, please see the <a target = "_blank" href = "https://www.healthit.gov/condition-ccg/application-programming-interfaces">§ 170.404 API Conditions and Maintenance of Certification</a> CCG.

<a target = "_blank" href = "https://www.hhs.gov/hipaa/index.html">HIPAA</a> (specifically the <a target = "_blank" href = "https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html">HIPAA Privacy Rule</a>) defines the circumstances in which a Covered Entity (individuals, organizations, and agencies that meet the definition of a Covered Entity under HIPAA) may use or disclose an individual’s Protected Health Information (PHI). HIPAA provides many pathways for permissibly exchanging PHI, which are commonly referred to as HIPAA Permitted Uses and Disclosures.

Permitted Uses and Disclosures are situations in which a Covered Entity is permitted, but not required, to use and disclose PHI without first having to obtain a written authorization from the patient. The circumstances for which this information may be shared must meet specific criteria, and the <a target = "_blank" href = "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/minimum-necessary-requirement/index.html">minimum necessary rule</a> applies. Instances when a patient’s authorization is not required would be listed in the provider’s HIPAA Notice of Privacy Practices.

In general, a Covered Entity may only use or disclose PHI if either (1) the HIPAA Privacy Rule specifically permits or requires it; or (2) the individual who is the subject of the information provides a written authorization. Please see the ONC webpage “<a target = "_blank" href = "https://www.healthit.gov/topic/interoperability/how-hipaa-supports-data-sharing">How HIPAA Supports Data Sharing</a>” for more details.

The ONC website HealthIT.gov provides many additional resources for learning more about patient consent, including the “<a target = "_blank" href = "https://www.healthit.gov/topic/interoperability/patient-consent-electronic-health-information-exchange-and-interoperability">Patient Consent and Interoperability</a>” topics webpage.

Patients have a right under HIPAA to access their health records. Health insurers and providers who are covered entities must comply with a patient’s right to ask to see and get a copy of their health records. Except in certain circumstances, individuals have the right to review and obtain a copy of their protected health information in a covered entity's designated record set. Please see the “<a target = "_blank" href = "https://www.healthit.gov/sites/default/files/YourHealthInformationYourRights_Infographic-Web.pdf">Your Health Information, Your Rights</a>” fact sheet, and the “<a target = "_blank" href = "https://www.hhs.gov/hipaa/for-individuals/guidance-materials-for-consumers/index.html">Your Rights Under HIPAA</a>” webpage for more information regarding a patient’s rights under HIPAA. Additionally, the “<a target = "_blank" href = "https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/access-right-health-apps-apis/index.html">The access right, health apps, & APIs</a>” webpage provides guidance regarding the patient’s access right in the context of health apps and APIs.

For an overview of key elements of the HIPPA Privacy Rule including who is covered, what information is protected, and how protected health information can be used and disclosed, please see the “<a target = "_blank" href = "https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html">Summary of the HIPAA Privacy Rule</a>” resource. Another resource is the <a target = "_blank" href = "https://www.hhs.gov/hipaa/for-professionals/faq/health-information-technology/index.html">HHS HIPAA Health Information Technology FAQ for professionals</a>, which includes responses to frequently asked questions about HIPAA regarding health IT.

The Office for Civil Rights (OCR) enforces the HIPAA Privacy, Security, and Breach Notification Rules. For questions related to Health Information Privacy, please email <a target = "_blank" href = "mailto:OCRPrivacy@hhs.gov">OCRPrivacy@hhs.gov</a>.

### October 2022
**Stakeholder Inquiry**: Can you confirm that the requirements of the 2015 Edition Cures Update Base EHR Definition (specifically the requirement to satisfy 170.315(g)(10)) can be met using one Certified Health IT Module or a combination of Certified Health IT Modules?

**ONC Response**: You are correct that the requirements of the <a target = "_blank" href = "https://www.healthit.gov/topic/certification-ehrs/2015-edition-test-method/2015-edition-cures-update-base-electronic-health-record-definition">2015 Edition Cures Update Base EHR Definition</a> can be met using one Certified Health IT Module or a combination of Certified Health IT Modules.

### July 2022
**Stakeholder Inquiry**: Are there any (g)(10) requirements around patient data retention?

**ONC Response**: Neither the § 170.315(g)(10) "Standardized API for patient and population services" certification criterion nor the § 170.315 (b)(10) "Electronic Health Information export" criterion have any data retention requirement. However, most states have laws and regulations governing the retention of patient medical records. As such, historical data should be maintained by the organization in accordance with all applicable state laws, and once those requirements have been met, managing historical data in a consistent manner as business needs dictate. Organizations must follow all HIPAA requirements for the destruction of protected health information. And, in addition, they should review the Office of Civil Rights guidance on data destruction to ensure their policies and practices align to it.

### June 2022
**Stakeholder Inquiry**: If a Health IT Developer is providing a FHIR Server and FHIR API for patient access, but not the authorization server (e.g. OAuth 2 + OIDC) or the App registration portal, can such a solution be certified? Some organizations already have an authorization server, so providing the Patient Access API involves integrating the FHIR API with the existing authorization server. It seems from a (g)(10) perspective that demonstration or live testing must include authorization, authentication, etc. As such is it accurate to assume that each fully integrated solution comprised of multiple vendor components needs to be certified, but that some of the individual components such as a FHIR API + FHIR Server cannot be certified alone?

**ONC Response**: Health IT developers are permitted to use “<a target = "_blank" href = "https://www.healthit.gov/sites/default/files/relieduponsoftwareguidance.pdf">relied upon software</a>” to demonstrate compliance with certification criteria in ONC's Health IT Certification Program. Relied upon software is typically 3rd party software that is not developed by the health IT developer presenting its health IT for testing and certification. Relied upon software may be used to demonstrate compliance with a portion of an adopted certification criterion or an entire certification criterion.

A developer must present its own health IT for certification, and  may also use other software (“relied upon software”) to meet certification requirements. When a health IT developer relies upon software to demonstrate compliance with a certification criterion, such relied upon software must be included in the scope of the certification issued to the Health IT Module.

In the provided example, the health IT developer could use "relied upon software" in the form of an authorization server to fulfill authentication and authorization requirements in the § 170.315(g)(10) "Standardized API for patient and population services" criterion. However, a Health IT Module cannot be certified to the § 170.315(g)(10) "Standardized API for patient and population services" criterion without fulfilling all of its specified requirements, including authentication and authorization requirements.
For more information about "relied upon software", please see the <a target = "_blank" href = "https://www.healthit.gov/sites/default/files/relieduponsoftwareguidance.pdf">Relied Upon Software Program Guidance document</a>.

### December 2021
**Stakeholder Inquiry**: If we certify to 170.315(g)(10), does that cover all of the API requirements specified in this PDF? <a target = "_blank" href = "https://www.healthit.gov/cures/sites/default/files/cures/2020-03/APICertificationCriterion.pdf">https://www.healthit.gov/cures/sites/default/files/cures/2020-03/APICertificationCriterion.pdf</a>

Are there any other criteria in that PDF not covered in the (g)(10) criterion?

**ONC Response**: The requirements for the certification criterion at <a target = "_blank" href = "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-C#p-170.315(g)(10)">45 CFR 170.315(g)(10) can be found at the electronic code of federal regulations page</a>. We also provide a Certification Companion Guide (CCG) and Test Procedure for each of the criteria under the ONC Health IT Certification Program, including a <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">CCG</a> and <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#test_procedure">Test Procedure</a> for 170.315(g)(10).

The (g)(10) CCG is a quick reference for the regulatory requirements of the criterion, and includes a list of clarifications organized by regulation text paragraph (e.g. clarifications that apply to Paragraph (g)(10)(i )(A), etc.). The (g)(10) CCG clarifications include clarifications that were part of preamble text from the <a target = "_blank" href = "https://www.federalregister.gov/documents/2020/05/01/2020-07419/21st-century-cures-act-interoperability-information-blocking-and-the-onc-health-it-certification">ONC Cures Act Final Rule</a> and the <a target = "_blank" href = "https://www.federalregister.gov/documents/2020/11/04/2020-24376/information-blocking-and-the-onc-health-it-certification-program-extension-of-compliance-dates-and">ONC Interim Final Rule</a>.

The (g)(10) Test Procedure specifies a list of capabilities required by Health IT Modules that need to be demonstrated by health IT developers during certification testing. These tests are implemented by the <a target = "_blank" href = "https://inferno.healthit.gov/suites/g10_certification">Inferno testing tool for (g)(10) certification testing</a>. We provide a <a target = "_blank" href = "https://inferno.healthit.gov/reference-server">(g)(10)-compliant reference server</a> which can be used for reference to understand the tests required for certification.

We have also published an <a target = "_blank" href = "https://onc-healthit.github.io/api-resource-guide/g10-criterion/">API Resource Guide</a> which can be used to help navigate the API testing criteria in the ONC Health IT Certification Program. This interactive document includes all the information from the (g)(10) CCG and additional examples and context.

### September 2021
**Stakeholder Inquiry**: Is it sufficient for Certified API Technology to include at least one method of documenting and accessing data via an API for each data class for certification to (g)(10)? We are uncertain about how to handle ambiguities in the underlying standard(s).

**ONC Response**: Health IT developers certified to the criterion at <a target = "_blank" href = "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-C#p-170.315(g)(10)">45 CFR 170.315(g)(10)</a> are required to support standardized API access to electronic health information according to the adopted standards and implementation specifications referenced in the criterion for all applicable information (e.g. USCDI and US Core IG “mandatory” and “must support” data elements) that have been incorporated into certified EHR technology. For example, some health organizations may choose to incorporate only a portion of a HL7 CDA document received from an external setting into their clinical record; (g)(10)-certified Health IT Modules would need to support access to the portion of incorporated information via a standardized FHIR-based API. Similarly, if a patient were to supply health information that was incorporated into the clinical record, (g)(10)-certified Health IT Modules would need to support access to the incorporated patient-supplied health information via a standardized FHIR-based API.

Any missing information from historical or externally sourced records incorporated into certified EHR technology should be represented as not available according to applicable standards and implementation specifications (e.g. <a target = "_blank" href = "http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#missing-data">US Core IG section 2.1.1.6: Missing Data</a>).

The requirements at 45 CFR 170.315(g)(10) do not currently address methods developers use to import, map, or store health information. Health IT developers should refer to the standards and implementation specifications required as part of the certification criterion to enable access to information that has been incorporated into certified EHR technology via a standardized API.

In regard to ambiguities in the underlying standard(s) that present challenges for mapping health information to HL7 FHIR and the HL7 US Core IG, ONC suggests working with the HL7 FHIR developer community to help resolve any ambiguities in this or future versions of the adopted standards.

Any missing information made available via the (g)(10) standardized API should be represented as not available according to applicable standards and implementation specifications (e.g. US Core IG section 2.1.1.6: Missing Data). 

### April 2021
**Stakeholder Inquiry**: Does the Cures Act mandate the use of FHIR for eCQM's? Also, if it is mandatory, from which performance year will this be applicable?

**ONC Response**: The 21st Century Cures Act adopts a new API certification criterion §  170.315(g)(10) Standardized API for patient and population services.  This API certification criterion requires the use of Health Level 7 (HL7®) Fast Healthcare Interoperability Resources (FHIR®) standard Release 4 and references several standards and implementation specifications including FHIR US Core Implementation Guide STU V3.1.1, and HL7 FHIR Bulk Data Access (Flat FHIR)(V1.0.0:STU 1).

The ONC Certification criteria for eCQMs does not require any FHIR standards. For additional information on CMS regulations, please reference CMS sources or contact CMS if you have questions about specific requirements. The CMS.gov website is a great place to start for information about the requirements of any particular CMS program that may be of interest to health care providers and those who support them with health IT solutions. For one example, the Quality Payment Program overview page (<a target = "_blank" href = "https://qpp.cms.gov/about/qpp-overview">https://qpp.cms.gov/about/qpp-overview</a>) offers links to educational resources and information how to contact CMS. Similarly, the CMS.gov Promoting Interoperability Programs page (<a target = "_blank" href = "https://www.cms.gov/Regulations-and-Guidance/Legislation/EHRIncentivePrograms">https://www.cms.gov/Regulations-and-Guidance/Legislation/EHRIncentivePrograms</a>) currently indicates that Medicare and dually eligible hospitals participating in the Medicare and Medicaid Promoting Interoperability Programs may contact the QualityNet help desk for assistance.

## Paragraph (g)(10)(i)(A): Data Response (Single Patient)
### October 2022
**Stakeholder Inquiry**: Two FHIR® DocumentReference resource related questions:

1. The Inferno (g)(10) Standardized API Test Kit test 4.31.01 requires a system under test to demonstrate support for the Discharge Summary note type (18842-5). Are ambulatory vendors expected to demonstrate support for this note type for the purposes of (g)(10) certification?
1. For the purposes of certification, what are the FHIR search requirements around `DocumentReference` note types?

**ONC Response**: Answers to question #1 and #2 respectively:

1. The § 170.315(g)(10) "Standardized API for patient and population services" certification criterion requires the Health IT Module respond to requests for single and multiple patient's data according to the USCDI standard and the US Core implementation guide. Using the base regulatory standards for reference, the USCDI v1 standard requires support for the "<a target = "_blank" href = "https://www.healthit.gov/isa/taxonomy/term/606/uscdi-v1">Discharge Summary Note</a>" data element and its corresponding LOINC code. Similarly, the US Core 3.1.1 implementation guide section <a target = "_blank" href = "https://hl7.org/fhir/us/core/STU3.1.1/clinical-notes-guidance.html#clinical-notes">2.2.1 Clinical Notes Guidance</a> requires support for the Discharge Summary clinical note and its corresponding LOINC code. Therefore, the Inferno testing tool tests for support for the Discharge Summary clinical note and its corresponding LOINC code.
1. To certify to the § 170.315(g)(10) criterion, a Health IT Module must respond to requests and searches for single and multiple patient's data according to the USCDI standard and the US Core implementation guide. This includes support for the USCDI Clinical Notes data class and the corresponding SHALL and Must Support requirements in the US Core clinical notes guidance and FHIR profiles (e.g., DocumentReference). The US Core 3.1.1 implementation guide includes a shall requirement in the <a target = "_blank" href = "https://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-documentreference.html">DocumentReference</a> profile to "support searching using the combination of the patient and type search parameters" and specifies "The DocumentReference.type binding must support at a minimum the <a target = "_blank" href = "https://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-clinical-note-type.html">5 Common Clinical Notes</a> and may extend to the full US Core DocumentReference Type Value Set". Thus, while the <a target = "_blank" href = "https://hl7.org/fhir/us/core/STU3.1.1/ValueSet-us-core-clinical-note-type.html">FHIR 4.0.1</a> specification provides flexibility to the server to determine which resources meet the search parameter criteria and provide additional search results if they are deemed relevant, the server should provide meaningful search results for searches regarding the 5 Common Clinical note types specified in the US Core implantation guide. Also, while the § 170.315(g)(10) criterion does not specify how patient data storage must be implemented, patient data should be stored in such a manner that permits the Health IT Module's single patient FHIR API to return relevant search results to FHIR searches. In the context of this inquiry, this includes providing appropriate search results to searches regarding the 5 Common Clinical note types specified in the US Core implementation guide. 

### August 2022
**Stakeholder Inquiry**: The US Core IG requires support for the $docref operation. Can you clarify what the (g)(10) requirements regarding the $docref operation are?

**ONC Response**: The § 170.315(g)(10) "Standardized API for patient and population services" certification criterion does not require support for the US Core <a target = "_blank" href = "http://hl7.org/fhir/us/core/STU3.1.1/OperationDefinition-docref.html">$docref operation</a>.

### December 2021
**Stakeholder Inquiry**: US Core 3.1.1 requires Procedure.performed. For (g)(10) certification how are we expected to accommodate cancelled or not done procedures where a date or period does not exist? 

**ONC Response**: Health IT modules certified to the Standardized API for patient and population services (45 CFR 170.315(g)(10)) must "Respond to requests for a single patient’s data according to the standard adopted in § 170.215(a)(1) and implementation specification adopted in § 170.215(a)(2), including the mandatory capabilities described in “US Core Server CapabilityStatement,” for each of the data included in the standard adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported."

Through the ONC Health IT Certification Program, ONC implements required standards and functionalities that must be supported by certified products. In general, the Program requires the electronic standards in which available data is stored and/or shared by certified health IT but not how much data or when specific data must be recorded or shared. Certified Health IT Developers should reach out to the appropriate standards development organization (in this case HL7) when the standard is not clear.

To accommodate “cancelled or not done” procedures where a “date or period does not exist,” health IT developers should follow the <a target = "_blank" href = "http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#missing-data">“Missing Data” section</a> of the US Core implementation guide (IG) for additional guidance. Test data used in Inferno (g)(10) certification testing can include "Missing Data" handled according to the US Core IG.

The requirements at 45 CFR 170.315(g)(10) do not currently address methods developers use to import, map, or store health information. Health IT developers should refer to the standards and implementation specifications required as part of the certification criterion to enable access to information that has been incorporated into certified EHR technology via a standardized API. Regarding your specific inquiry on missing data for the Procedure resource for use cases where the Procedure is “cancelled” or “not done” and a date or period does not exist, the adopted US Core version 3.1.1 IG provides guidance in section 2.1.1.6: Missing Data for supporting required and must support data elements that cannot be populated.

During the HL7 Connectathon, we discussed how the US Core version 3.1.1 IG does not satisfactorily address some of these Procedure use cases as described above, and observed efforts underway by HL7 to create a process in the US Core IG to better accommodate corrections to sections of prior standards (e.g. labeling certain updates as "patch" fixes). Unfortunately, we do not have a process in place to accommodate the updated conformance rules of `Procedure.performed[x]` in US Core 4.0.1 and later versions as a “patch” at this time, but we will monitor this effort over the next several months and provide any updates on the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">(g)(10) Certification Companion Guide</a> when available.

### August 2021
**Stakeholder Inquiry**: US Core 3.1.1 requires that a server demonstrate support for the "composite OR" search for the CareTeam.status search parameter (US Core 3.1.1 CareTeam Mandatory Search Parameters). However, neither US Core, nor USCDI require that multiple CareTeam resource be supported. Can you clarify what is required here?

**ONC Response**: According to the regulation text for the 170.315(g)(10) certification criterion at 45 CFR 170.315(g)(10)(i)(A), health IT developers must demonstrate the ability of Health IT Modules to:

*"Respond to requests for a single patient’s data according to the standard adopted in § 170.215(a)(1) and implementation specification adopted in § 170.215(a)(2), including the mandatory capabilities described in 'US Core Server CapabilityStatement,' for each of the data included in the standard adopted in § 170.213."*

In <a target = "_blank" href = "http://hl7.org/fhir/us/core/STU3.1.1/StructureDefinition-us-core-careteam.html#mandatory-search-parameters">section 3.19.1.4.1</a> of the US Core Implementation Guide (v3.1.1: STU 3) (US Core IG) adopted at § 170.215(a)(2), there is a requirement for US Core IG CareTeam resources that servers "SHALL support searching using the combination of the patient and status search parameters: including support for composite OR search on status…"

Given that the “composite OR search on status” is a “SHALL” requirement, Health IT Modules must support this search functionality. However, given that there is not a requirement that multiple CareTeam.status values must be supported, we will update the Inferno testing tool to permit demonstration of the “composite OR search on status” using a minimum of one CareTeam.status value. We will issue a clarification on the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">§ 170.315(g)(10) Certification Companion Guide</a>, and this update will be included in the next release of Inferno.

***

**Stakeholder Inquiry**: Can you provide guidance on how we are expected to demonstrate support for “must support” “dataAbsentReason” elements in US Core?

**ONC Response**: According to the ONC Cures Act Final Rule, Health IT Modules must “Respond to requests for a single patient’s data according to the standard adopted in § 170.215(a)(1) and implementation specification adopted in § 170.215(a)(2), including the mandatory capabilities described in “US Core Server CapabilityStatement,” for each of the data included in the standard adopted in § 170.213. All data elements indicated as “mandatory” and “must support” by the standards and implementation specifications must be supported” (<a target = "_blank" href = "https://www.federalregister.gov/d/2020-07419/p-3457">85 FR 25945</a>).

However, for purposes of testing and certification for the ONC Health IT Certification Program, health IT developers with Health IT Modules that never provide an observation without a value do not need to demonstrate Health IT Module support for the “dataAbsentReason” elements contained in the the US Core IG profiles and FHIR Vital Sign profiles that build on the HL7 FHIR "observation", HL7 FHIR "observation-vitalsigns", or HL7 FHIR "observation-oxygensat" profiles, including "component.dataAbsentReason" elements. As a reminder, health IT developers are still required to adhere to and demonstrate Health IT Module support for the <a target = "_blank" href = "http://hl7.org/fhir/us/core/STU3.1.1/general-guidance.html#missing-data">“Missing Data” section</a> of the US Core IG.

We will issue a clarification on the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">§ 170.315(g)(10) Standardized API for patient and population services Certification Companion Guide</a> regarding this issue, and the Inferno testing tool will be updated in the next regular release, which occurs at least monthly, to accommodate this clarification.

## Paragraph (g)(10)(i)(B): Data Response (Multiple Patients)
### August 2022
**Stakeholder Inquiry**: We are working on the Multi-Patient API Certification requirements, what are the requirements around group ids?

**ONC Response**: The § 170.315(g)(10) "Standardized API for patient and population services" certification criterion requires the Health IT Module support requests for multiple patients’ data as a group using the “group-export” operation as detailed in the Bulk Data Access implementation guide. The `group-export` operation allows authorized clients to obtain FHIR resources pertaining to all patients in a specified Group. The client uses the Group ID to specify which Group is to be exported.

The § 170.315(g)(10) criterion does not specify how the health IT developer creates groups, how many groups must be supported, nor how patients are organized into groups. The health IT developer is expected to work with its customers to define the appropriate groups for export via the Health IT Module.

<a target = "_blank" href = "https://hl7.org/fhir/uv/bulkdata/STU1.0.1/export/index.html#endpoint---group-of-patients">Bulk Data Access 1.0.1 section 5.1.2 Endpoint - Group of Patients</a> includes the following note regarding group definitions:

*How these Groups are defined is specific to each FHIR system’s implementation. For example, a payer may send a healthcare institution a roster file that can be imported into their EHR to create or update a FHIR group. Group membership could be based upon explicit attributes of the patient, such as age, sex or a particular condition such as PTSD or Chronic Opioid use, or on more complex attributes, such as a recent inpatient discharge or membership in the population used to calculate a quality measure. FHIR-based group management is out of scope for the current version of this implementation guide.*

Additionally, health IT developers may choose to implement the Standards Version Advancement Process (SVAP) approved standard of <a target = "_blank" href = "http://hl7.org/fhir/uv/bulkdata/STU2/index.html">Bulk Data Access 2.0.0</a> instead of Bulk Data Access 1.0.1. Bulk Data Access 2.0.0 defines an experimental, optional "patient" parameter for the <a target = "_blank" href = "http://hl7.org/fhir/uv/bulkdata/STU2/OperationDefinition-group-export.html#grouplevelexport">"group-export" operation</a> which restricts the returned resources to the Patient Compartments associated with the patients specified within the parameter.

### June 2022
**Stakeholder Inquiry**: ONC (g)(10) Certification requirements and the Inferno Test Tool indicate that we are to demonstrate support for bulk FHIR requests with Group IDs (e.g. `[base url]/Group/[id]/$export`). Is there any minimum requirement in the upcoming 2022 (g)(10) certification for EHRs on how many different types of groups should be supported by the EHR? Can you give more guidance on what groups we need?

**ONC Response**: The § 170.315(g)(10) "Standardized API for patient and population services" certification criterion requires the Health IT Module support requests for multiple patients’ data as a group using the “group-export” operation as detailed in the Bulk Data Access 1.0.1 implementation guide. The § 170.315(g)(10) criterion does not specify how the health IT developer creates groups nor how many groups must be supported. The health IT developer is expected to work with its customers to define the appropriate groups for export via the Health IT Module.
 
Bulk Data Access 1.0.1 section 5.1.2 Endpoint - Group of Patients includes the following note regarding group definitions:

*How these Groups are defined is specific to each FHIR system’s implementation. For example, a payer may send a healthcare institution a roster file that can be imported into their EHR to create or update a FHIR group. Group membership could be based upon explicit attributes of the patient, such as age, sex or a particular condition such as PTSD or Chronic Opioid use, or on more complex attributes, such as a recent inpatient discharge or membership in the population used to calculate a quality measure. FHIR-based group management is out of scope for the current version of this implementation guide.*

### February 2022
**Stakeholder Inquiry**: We are seeking some further confirmation in relation to the [1] new clarification published to the (g)(10) Certification Companion Guide (CCG) on the use of capability URLs. Can our Health IT Module require clients to re-direct to a capability URL with an authorization header?

[1] *Health IT Modules may use access control schemes other than OAuth 2.0 for controlling access to the file server, such as capability URLs. The HL7 FHIR-I Work Group has documented expectations for the use of capability URLs with the Bulk Data Access IG on the HL7 confluence website. For purposes of Certification testing, Health IT Modules will be tested for the ability to share bulk data files either using OAuth 2.0 bearer tokens or via capability URLs accessible without preconditions or additional steps.*

**ONC Response**: The § 170.315(g)(10) "Standardized API for patient and population services" certification criterion requires (§ 170.315(g)(10)(i)(B)) that a Health IT Module respond to requests for multiple patients’ data as a group in a standardized manner. One of the standards for this requirement is the FHIR Bulk Data Access (Flat FHIR) (v1.0.1: STU 1) implementation guide, which specifies how bulk patient data is exported to a bulk data client.

As specified in Bulk Data Access 1.0.1 <a target = "_blank" href = "http://hl7.org/fhir/uv/bulkdata/STU1.0.1/export/index.html#response---complete-status">"5.3.4 Response - Complete Status"</a>, the Health IT Module provides a manifest to the client containing URLs to access the bulk data files. The Bulk Data Access 1.0.1 implementation guide provides flexibility to the server in implementing how these URLs eventually provide access to the bulk data files. Given this flexibility, Health IT Modules may require clients to re-direct to a capability URL without an authorization header when resolving the file URLs provided in the manifest. To address this flexibility, the Inferno testing tool was updated in the April release (4/11/2022).

Requirements imposed on clients to access multiple patients' data using this flexibility must be completely and appropriately documented as per the documentation requirements at § 170.315(g)(10)(viii).

### September 2021
**Stakeholder Inquiry**: For the Inferno Multi-Patient API tests, there is mention of the server providing the resources that are referenced as must support elements in other required resources. Also in this test, the location resource is called out as optional.

Can you clarify the intent here?

**ONC Response**: Regarding the “Location” HL7 FHIR resource, we provided the following clarification in the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">Certification Companion Guide (CCG) for § 170.315(g)(10)</a>:

*“Health IT Modules must demonstrate support for “Location” FHIR resources by providing this resource as part of the multiple patient services response, or by including it as a contained resource as part of the multiple patient services response.”*

Thus, “Location” FHIR resources do not need to be presented as independent FHIR resources but can be *contained within* other applicable FHIR resources.

Regarding “Organization” HL7 FHIR resources, we provided the following clarification in the CCG for § 170.315(g)(10):

*“During testing and certification for multiple patient services, Health IT Modules must demonstrate support for “Encounter,” “Organization,” and “Practitioner” US Core IG FHIR Profiles.”*

Health IT developers must include all the resources necessary via the multiple patient services API responses to fully resolve references contained in HL7 FHIR resources, including “Organization” resources.

## Paragraph (g)(10)(iii): Application Registration
### March 2021
**Stakeholder Inquiry**: Can you clarify how we are expected to scope US Core IG resources that do not exists in USCDI or the FHIR Patient Compartment?

**ONC Response**: We have provided a clarification in the Certification Companion Guide for § 170.315(g)(10) to address this ambiguity:

*"For demonstration of the SMART IG "Standalone Launch" steps, health IT developers are permitted to scope US Core IG resources that do not exist in either the standard adopted at § 170.213 (USCDI version 1) or the "Compartment Patient" section of the standard adopted at § 170.215(a)(1) (HL7 FHIR Release 4.0.1) as either patient/[Resource] or user/[Resource]. These resources include “Encounter,” “Device,” “Location,” “Medication,” “Organization,” “Practitioner,” and “PractitionerRole.” Health IT developers must document their supported scopes according to the technical documentation requirements at § 170.315(g)(10)(viii)(A) and § 170.404(a)(2)."*

The <a target = "_blank" href = "https://inferno.healthit.gov/suites/g10_certification">Inferno testing tool ONC Health IT Certification Program tests for § 170.315(g)(10)</a> will be updated to accommodate this change in the coming weeks.

## Paragraph (g)(10)(iv): Secure Connection
### July 2022
**Stakeholder Inquiry**: We are failing the Inferno (g)(10) Standardized API Test Kit test “5.3.01 Bulk Data Server is secured by transport layer security Server did not permit/deny the connections with the correct TLS versions.” Our implementation enforces TLS connections at the application layer and not the network layer. Is this allowable for certification to (g)(10)?

**ONC Response**: ONC has issued the following clarification in the § 170.315(g)(10) "Standardized API for patient and population services" Certification Companion Guide regarding the requirements at § 170.315(g)(10)(iv) “Secure connection”.

*Health IT developers are encouraged but not required to follow TLS Best Current Practice (BCP 195) for TLS version enforcement, referenced in section 6.1.0.3 of the HL7 4.0.1 Fast Healthcare Interoperability Resources Specification (FHIR) Release 4, October 30, 2019, which recommends TLS 1.2 or higher to be used for all production data exchange and limits support for lower versions of TLS. To meet ONC Certification requirements, Health IT developers must document how the Health IT Module enforces TLS version 1.2 or above to meet the API documentation requirements at § 170.315(g)(10)(viii) and API Transparency Conditions at 45 CFR 170.404(a)(2).*

The Inferno testing tool will be updated to align with this clarification. However, until the Inferno testing tool is updated, ONC grants an exception for the ONC Certification (g)(10) Standardized API Test Kit test 5.3.01 "Bulk Data Server is secured by transport layer security", wherein for the purposes of certification and testing it is sufficient for the health IT developer to document how the Health IT Module enforces TLS version 1.2 or above for the Bulk Data file server.

## Paragraph (g)(10)(v)(A)(1): First Time Authentication / Authorization for Single Patients
### February 2023
**Stakeholder Inquiry**: Can ONC please clarify requirements around patient ability to authorize an application to receive their EHI based on FHIR resource level scopes? Is it required that the patient be given the ability to select or deselect individual FHIR resources? We’ve seen examples of other deployed systems not providing the ability for a patient to select or deselect individual FHIR resources.

**ONC Response**: As part of the “permission-patient” “SMART on FHIR® Core Capability” in § 170.215(a)(3), Health IT Modules presented for § 170.315(g)(10) testing and certification must include the ability for patients to authorize an application to receive their electronic health information (EHI) based on FHIR® resource-level scopes. Specifically, this means patients would need to have the ability to authorize access to their EHI at the individual FHIR resource level, from one specific FHIR resource (e.g., “Immunization”) up to all FHIR resources necessary to implement the standard adopted in § 170.213 and implementation specification adopted in § 170.215(a)(2).

Although Health IT Modules presented for testing and certification must include the ability for patients to authorize an application to receive their EHI based on FHIR resource-level scopes, Health IT Modules are not prohibited from presenting authorization scopes in a more user-friendly format (e.g. grouping resources under categories, renaming the scopes for easier comprehension by the end-user, using more granular scopes), as long as the ability for patients to authorize applications based on resource-level scopes is available, if requested by the patient.

Please note that the information above is specific and limited in scope to the requirements and potential limitations of certification criteria. A Certified Health IT Developer and their Certified Health IT Modules must comply with all applicable requirements of the ONC Certification program. For Health IT Modules certified to the § 170.315(g)(10) criterion, this includes the aforementioned capability for patients to authorize an application to receive their EHI based on FHIR resource-level scopes. Choices made by users of certified health IT as to if, when, or how they may deploy particular functionalities of the health IT are outside the scope of the Certification Program, although other regulations may apply, such as <a target = "_blank" href = "https://www.healthit.gov/topic/information-blocking">information blocking regulations</a> or requirements for successful participation in CMS programs such as the <a target = "_blank" href = "https://www.cms.gov/regulations-and-guidance/legislation/ehrincentiveprograms">Promoting Interoperability Program</a>.

### February 2022
**Stakeholder Inquiry**: Can you provide some more clarification on what is required in (g)(10)(v)(A)(1) where systems are expected to support refresh tokens for “no less than 3 months.”

**ONC Response**: The § 170.315(g)(10) "Standardized API for patient and population services" certification criterion includes requirements for first time connections at § 170.315(g)(10)(v)(A)(1) that a Health IT Module’s authorization server must issue a refresh token valid for a period of no less than three months to applications capable of storing a client secret and native applications capable of securing a refresh token. A requirement for subsequent connections is also included under § 170.315(g)(10)(v)(A)(2) that a Health IT Module’s authorization server must issue a refresh token valid for a new period of no less than three months to applications capable of storing a client secret. These refresh token requirements are intended to enable a patient's persistent access to their electronic health information without special effort.

In fulfillment of the aforementioned § 170.315(g)(10) requirements, health IT developers are not prohibited from allowing patients to express their persistent access preferences and from configuring the duration of persistent access according to patient preferences. When patients are presented with options for the duration of persistent access, an option of at least three months must be included.

### December 2021
**Stakeholder Inquiry**: What is a permissible method of allowing patients to authorize access to individual FHIR resources, and if this means that the FHIR server must be able to support requests from client applications for one to all USCDI resources; or if it means the FHIR server must allow the user at the time of authorization to pick/choose which resources are granted access?

Client applications are often designed to request access for their full list and then be granted/denied for the full list and don’t necessarily support this individual selection option at the authorization level. Meaning, they say they need all requested items, and the user can accept that or deny it.

The final rule states that “patients would need to have the ability to authorize access to their EHI at the individual FHIR resource level, from one specific FHIR resource (e.g., “Immunization”) up to all FHIR resources necessary to implement the standard adopted in § 170.213 and implementation specification adopted in § 170.215(a)(2).”

As an example, the client application presents the Immunization, Allergies, Medications, and Problems as the scope of resources they are requesting to access to the server, and this list is then shown to the user for authorization. In light of the requirement above, is it permissible for the FHIR Server to have the user accept the list as a whole (i.e., grant access to Immunization, Allergies, Medications, and Problems) or reject the list as a whole (i.e., denying the client application access to ALL of the resources) but not allow the user to pick/choose which resource they want to be given access?

Or, does the requirement mean the server MUST allow the user to choose which of the specific resources they want to grant access to (e.g., grant access to Immunization, Allergies, and Medications, but don’t grant access to Problems) and the client application must either accept that or deny that?

**ONC Response**: A clarification has been issued to the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">Certification Companion Guide for § 170.315(g)(10)</a> which states:

 *Although Health IT Modules presented for testing and certification must include the ability for patients to authorize an application to receive their EHI based on FHIR® resource-level scopes, Health IT Modules are not prohibited from presenting authorization scopes in a more user-friendly format (e.g. grouping resources under categories, renaming the scopes for easier comprehension by the end-user, using more granular scopes), as long as the ability for patients to authorize applications based on resource-level scopes is available, if requested by the patient.”*

In the example you provided, it would be acceptable “for the FHIR Server to have the user accept the list as a whole … or reject the list as a whole” as long as the patient has the ability to authorize the application based on resource-level scopes, if requested by the patient. For example, the patient could be presented a “request list for the user to blanket request/deny access” accompanied with a hyperlink that could direct them to choose individual resources, if they desired.

### May 2021
**Stakeholder Inquiry**: Can you clarify what is required of OAuth 2.0 in the Patient Access API?

**ONC Response**: The § 170.315(g)(10) Standardized API for patient and population services certification criterion requires the following for authentication and authorization for patient and user scopes for first time connections:

- Authentication and authorization must occur during the process of granting access to patient data in accordance with the HL7® SMART Application Launch Framework Implementation Guide (incorporated by reference at § 170.215(a)(3)) and OpenID Connect Core 1.0 incorporating errata set 1 (incorporated by reference at § 170.215(b)). 
- A Health IT Module’s authorization server must issue a refresh token valid for a period of no less than three months to applications capable of storing a client secret.
- A Health IT Module’s authorization server must issue a refresh token for a period of no less than three months to native applications capable of securing a refresh token.

and for subsequent connections:

- Access must be granted to patient data in accordance with the implementation specification adopted in the HL7® SMART Application Launch Framework Implementation Guide (incorporated by reference at § 170.215(a)(3)) without requiring re-authorization and re-authentication when a valid refresh token is supplied by the application.
- A Health IT Module’s authorization server must issue a refresh token valid for a new period of no less than three months to applications capable of storing a client secret. 
Beyond the certification criteria requirements, health IT developers are not required to support all methods that third-party application developers seek to use. Additional information and clarifications regarding this criterion can be found on the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">Certification Companion Guide for § 170.315(g)(10)</a>.

## Paragraph (g)(10)(v)(B): Authentication / Authorization for Multiple Patient Services
### October 2021
**Stakeholder Inquiry**: There is a requirement that clients downloading the bulk data use the same access token as they did to make the original request. Does it permit other equivalently secure means of authorization as well?

The  FHIR specification says that there should be alternatives: <a target = "_blank" href = "https://hl7.org/fhir/uv/bulkdata/export/index.html#response---complete-status">https://hl7.org/fhir/uv/bulkdata/export/index.html#response---complete-status</a>

*[requiresAccessToken] Value SHALL be true if both the file server and the FHIR API server control access using OAuth 2.0 bearer tokens. Value MAY be false for file servers that use access-control schemes other than OAuth 2.0, such as downloads from Amazon S3 bucket URLs or verifiable file servers within an organization's firewall.*

**ONC Response**: We recently provided a clarification to a question we received via the Centralized Feedback System regarding this topic, and are planning to publish the clarification to the § 170.315(g)(10) Certification Companion Guide shortly.

The § 170.315(g)(10) "Standardized API for patient and population services" certification criterion regulation text states in paragraph <a target = "_blank" href = "https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-D/part-170/subpart-C#p-170.315(g)(10)(v)(B)">§ 170.315(g)(10)(v)(B)</a>:

*Authentication and authorization must occur during the process of granting an application access to patient data in accordance with the “SMART Backend Services: Authorization Guide” section of the implementation specification adopted in § 170.215(a)(4) and the application must be issued a valid access token.*

According to the requirements in § 170.315(g)(10)(v)(B), Health IT Modules must issue an application a valid access token during authentication and authorization as per the “SMART Backend Services: Authorization Guide” section of the "FHIR Bulk Data Access (Flat FHIR) (v1.0.1: STU 1)" implementation guide (Bulk FHIR IG). In order for the aforementioned access token to be valid, the application must also be able to access patient data via the access token. The “SMART Backend Services: Authorization Guide” section of the Bulk FHIR IG requires the use of OAuth 2.0 bearer tokens for access control. According to <a target = "_blank" href = "https://hl7.org/fhir/uv/bulkdata/export/index.html#response---complete-status">section 5.3.4</a> of the Bulk FHIR IG, the “requiresAccessToken” element be set to “true” if “both the file server and the FHIR API server control access using OAuth 2.0 bearer tokens.” Therefore, the Inferno testing tool requires the "requiresAccessToken" parameter be set to "true" as part of the test to check if the granted access token is valid for accessing patient data.

At a minimum for the ONC Health IT Certification Program, Health IT Modules certified to the § 170.315(g)(10) criterion must support the issuance of a valid access token to an application during authentication and authorization as per the “SMART Backend Services: Authorization Guide” section of the Bulk FHIR IG. However, if the minimum requirements are met, health IT developers may support additional access-control schemes beyond OAuth 2.0 bearer tokens.

## Paragraph (g)(10)(vi): Patient Auhtorization Revocation
### October 2021
**Stakeholder Inquiry**: To satisfy the “Patient authorization revocation” requirements can short-lived access tokens be allowed to expire in lieu of immediate access token revocation?

**ONC Response**: The § 170.315(g)(10) "Standardized API for patient and population services" Certification Companion Guide will be updated with the following clarification:

*For authorization revocation, Health IT Modules presented for certification are permitted to allow short-lived access tokens to expire in lieu of immediate access token revocation. ONC recommends health IT developers limit the lifetime of access tokens to one hour or less as recommended in the standard adopted at § 170.215(a)(3), HL7® <a target = "_blank" href = "https://hl7.org/fhir/smart-app-launch/1.0.0/">SMART Application Launch Framework Implementation Guide Release 1.0.0.</a> For purposes of testing and certification, Health IT Modules will be tested for patient authorization revocation occurring within one hour of the request.*

## Inferno
### July 2022
**Stakeholder Inquiry**: In Inferno test 4.2.04 (and others) patient data is included in the URL of the HTTP GET request. Is this a Privacy and Security concern?

**Stakeholder Inquiry**: The Inferno testing tool acts as a demanding client to test the conformance of servers to health IT standards. In particular, the ONC Certification (g)(10) Standardized API Test Kit, which uses Inferno, tests a health IT developer's APIs' conformance to the requirements of the § 170.315(g)(10) "Standardized API for patient and population services" certification criterion. The Inferno implementation provided by ONC on healthit.gov includes a banner indicating it is for demonstration purposes only and must not be used to access sensitive data or Protected Health Information (PHI).

Regarding the privacy and security of the FHIR APIs certified to the § 170.315(g)(10) "Standardized API for patient and population services" certification criterion, there are numerous privacy and security requirements to protect patient data. The ONC Certification (g)(10) Standardized API Test Kit includes tests for conformance to authentication and authorization requirements, such as those detailed in the <a target = "_blank" href = "https://hl7.org/fhir/smart-app-launch/1.0.0/">SMART App Launch Framework</a> and <a target = "_blank" href = "http://hl7.org/fhir/uv/bulkdata/STU1.0.1/authorization/index.html">SMART Backend Services: Authorization Guide</a>, which require that only authorized clients can access data. Additionally, there are requirements that the connections for data responses for single and multiple patients' data are appropriately secured using Transport Layer Security (TLS) 1.2 or above. When used to secure HTTP connections via <a target = "_blank" href = "https://https.cio.gov/faq/#what-does-https-do">HTTPS</a>, TLS protects the confidentiality of the data included in the HTTP URL via encryption, including the URL path and query string parameters (e.g. name and birthdate).

### June 2022
**Stakeholder Inquiry**: We are testing our FHIR Server using the Inferno (g)(10) Standardized API Test Kit. We are failing some Pulse Oximetry Tests. Specifically, in one of our Observation resources, we use dataAbsentReason for 'Inhaled oxygen flow rate'. But Inferno is failing the test mentioning that 'component.value[x].code' is not present in the Observation. Can you provide some clarity on why this is failing?

**ONC Response**: The Inferno <a target = "_blank" href = "https://github.com/onc-healthit/onc-certification-g10-test-kit/wiki/FAQ#q-how-does-inferno-test-mustsupport-flag-on-an-element">ONC Certification (g)(10) Standardized API Test Kit FAQ</a> includes the following guidance regarding how Inferno tests the "MustSupport" flag on an element.

*Inferno follows guidance provided by HL7 FHIR Conformance Rules and US Core IG General Guidance. Inferno checks that a server implementation SHALL demonstrate that it supports the "MustSupport" element in a meaningful way. In general, Inferno "MustSupport" tests check that each "MustSupport" element is present in at least one resource from all resources returned from the server. It is not necessary that one resource contain all MustSupport elements. Inferno does not consider using a "Data Absent Reason" (DAR) extension on a "MustSupport" element as supporting the element "in a meaningful way," so Inferno ignores elements with DAR extensions when looking for "MustSupport" elements.*

For the Inferno Pulse Oximetry Tests (4.18), the Health IT Module must provide FHIR resources conforming to the US Core Pulse Oximetry Profile as specified in the US Core Implementation Guide. The US Core Pulse Oximetry Profile contains elements marked as "MustSupport". As part of the Inferno Pulse Oximetry Tests, the Health IT Module must provide each of these "MustSupport" elements at least once. If at least one cannot be found, the Health IT Module will not pass these tests. Inferno ignores elements with Data Absent Reason extensions when looking for "MustSupport" elements.

***
**Stakeholder Inquiry**: Our FHIR API returns additional resource types in search responses and Inferno ((g)(10) Standardized API Test Kit) is failing us for this. Is this intended to not be allowed? The FHIR specification provides flexibility for server search responses.

**ONC Response**: The Inferno <a target = "_blank" href = "https://github.com/onc-healthit/onc-certification-g10-test-kit/releases/tag/v2.2.2">ONC Certification (g)(10) Standardized API Test Kit v2.2.2</a>, released on 7/11/2022, includes the following update which should resolve the technical concern raised. If your implementation continues to experience this issue, please submit another ticket through the Health IT Feedback and Inquiry Portal.

*Relaxes constraint that prevented systems from returning additional resource types in search responses. Systems may return other resource types if they believe them to be relevant, and tests now provide informational messages in this case.*

### April 2022
**Stakeholder Inquiry**: Does ONC have a published list of IP addresses we can whitelist for the (g)(10) Standardized API Test Kit hosted at <a target = "_blank" href = "https://inferno.healthit.gov/onc-certification-g10-test-kit">https://inferno.healthit.gov/onc-certification-g10-test-kit</a>?

**ONC Response**: The IP addresses for ONC's hosted instance of Inferno are as follows:

- The latest Inferno release (inferno.healthit.gov): 52.20.119.0
- The development build of Inferno (inferno-dev.healthit.gov): 34.225.213.213

### March 2022
**Stakeholder Inquiry**: Do we need to register Inferno as EHR Practitioner App to test ONC certification criteria or we can use SMART Apps like Cardiac Risk to test the criteria? If it’s the Inferno that we need to register for EHR Practitioner App criteria testing, can you please guide me on the workflow on which the EHR practitioner app criteria works for testing in Inferno tool?

**ONC Response**: Response to Question 1: *Do we need to register Inferno as EHR Practitioner App to test the specific criteria or we can use SMART APPS like Cardiac Risk to test the criteria?*

Only ONC-approved test methods can be used to test products intended for certification in the Certification Program. Currently, Inferno is the only ONC-approved testing tool for testing compliance to the § 170.315(g)(10) "Standardized API for patient and population services" certification criterion. When using Inferno to test compliance to the § 170.315(g)(10) criterion, Inferno must be registered with the Health IT Module so that the "EHR Practitioner App" tests in Inferno can be completed.

Response to Question 2: *If it’s the Inferno that we need to register for EHR Practitioner App criteria testing, can you please guide me on the workflow on which the EHR practitioner app criteria works for testing in Inferno tool?*

The "EHR Practitioner App" tests in Inferno require the Health IT Module demonstrate the ability to perform an EHR launch to a SMART on FHIR confidential client with patient context, refresh token, and OpenID Connect identity token. After launch, Inferno performs a simple Patient resource read on the patient in context. Inferno then refreshes the access token and reads the Patient resource using the new access token to ensure that the refresh was successful. Finally, Inferno decodes and validates the authentication information provided by OpenID Connect.

Additional detail regarding the "EHR Practitioner App" tests in Inferno is available in the ONC Certification (g)(10) Matrix provided with each Inferno release. The ONC Certification (g)(10) Matrix for the current version of Inferno is available via the <a target = "_blank" href = "https://github.com/onc-healthit/onc-certification-g10-test-kit">onc-certification-g10-test-kit</a> repository on GitHub.

### August 2021
**Stakeholder Inquiry**: What are the test data requirements for testing to (g)(10) using Inferno?

**ONC Response**: The Inferno (g)(10) Standardized API Test Kit does not currently require a specific set of data to be entered into the system under test prior to testing. Instead, it leverages HL7 FHIR's built-in conformance rules to ensure that data returned is valid, conforms to required profiles, and contains all elements that must be supported. This allows systems to use either their own sample data or supplied sample data.

If needed, Inferno supplies multiple synthetic data sets suitable for testing. These data sets are ideal for testing because they provide coverage of all HL7 US Core IG profiles and support for all "Must Support" data elements without requiring a large set of patients or sacrificing realism. These synthetic data can be generated using the <a target = "_blank" href = "https://github.com/inferno-framework/uscore-data-script">uscore-data-script on GitHub</a>.

Otherwise, a health IT developer can supply their own sample data loaded into the system under test for certification, but the sample data must be able to demonstrate all the conformance requirements for certification according to the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#test_procedure">Test Procedure for 170.315(g)(10)</a>. We also encourage health IT developers read the clarifications provided on the <a target = "_blank" href = "https://www.healthit.gov/test-method/standardized-api-patient-and-population-services#ccg">Certification Companion Guide for 170.315(g)(10)</a>.

### April 2021
**Stakeholder Inquiry**: Can Inferno be used for Provider Directory testing? We have been able to use this tool for Patient Access API testing.

**ONC Response**: The Inferno (g)(10) Standardized API Test Kit is designed to support the Standardized API for Patient and Population Services certification criterion (§ 170.315(g)(10)) for the ONC Health IT Certification Program. Since a provider directory is not part of the § 170.315(g)(10) certification criterion, the Inferno (g)(10) Standardized API Test Kit does not support provider directory testing.

However, the <a target = "_blank" href = "https://inferno.healthit.gov/validator/">Inferno FHIR Validator</a> tool can be used to validate FHIR resources against implementation guides, including provider directory FHIR implementation guides, like the <a target = "_blank" href = "http://hl7.org/fhir/uv/vhdir/2018Jan/index.html">HL7 FHIR® Validated Healthcare Directory Implementation Guide STU 1</a>. Additionally, Inferno is currently being updated to allow for greater extensibility and testing capabilities with a broad array of implementation guides. Support for fully-featured provider directory implementation guide testing may also be added in the future.

--8<-- "includes/abbreviations.md"