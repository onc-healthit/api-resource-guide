<!-- $criterion-endpoint{"test-method/application-access-data-category-request"} -->

# Non-standarized Data Request API Criterion § 170.315(g)(8)

## Information and Clarifications

### Entire Criterion

<!-- $ref{g-8:CCG["Applies to entire criterion"], tabbed} -->
??? quote "*Clarifications included in the (g)(8) CCG that apply to the entire criterion*"
	***Clarifications:***
	
	
	* While no content exchange standard is required for this criterion, ONC intend to adopt a standards-based approach for certification in a future rulemaking. We encourage the use of the Fast Healthcare Interoperability Resources (FHIR®) specification.
	* *Security:*
		+ For the purposes of certification there is no conformance requirement related to the registration of third party applications that use the APIs. If a Health IT Module requires registration as a pre-condition for accessing the APIs, then, the process must be clearly specified in the API documentation as required by the criterion. ONC strongly believes that registration should not be used as a means to block information sharing via APIs.
		+ This criterion does not currently include any security requirements beyond the privacy and security approach detailed above, but we encourage organizations to follow security best practices and implement security controls, such as penetration testing, encryption, audits, and monitoring as appropriate. ONC expects health IT developers to include information on how to securely use their APIs in the public documentation required by the certification criteria and follow industry best practices. [see also [80 FR 62676](http://www.federalregister.gov/a/2015-25597/p-1072)]
		+ ONC strongly encourages developers to build security into their APIs following industry best practices. [see also [80 FR 62677](http://www.federalregister.gov/a/2015-25597/p-1084)]
		+ A “trusted connection” means the link is encrypted/integrity protected according to § 170.210(a)(2) or (c)(2). As such, ONC does not believe it is necessary to specifically name HTTPS and/or SSL/TLS as this standard already covers encryption and integrity protection for data in motion. [see also [80 FR 62676](https://www.federalregister.gov/d/2015-25597/p-1072)]
		+ APIs could be used when consent or authorization by an individual is required. In circumstances where there is a requirement to document a patient’s request or particular preferences, APIs can enable compliance with documentation requirements. The HIPAA Privacy Rule (45 CFR Part 160 and Part 164, Subparts A and E ) permits the use of electronic documents to qualify as writings for the purpose of proving signature, e.g., electronic signatures. [see also [80 FR 62677](http://www.federalregister.gov/a/2015-25597/p-1094)]
	* The audit record should be able to distinguish the specific user who accessed the data using a third-party application through the certified API in order to meet the requirements of § 170.315(d)(2) or (d)(10).
	* A health IT developer must demonstrate that its API functionality properly performs consistent with this certification criterion’s requirements. How this is done is up to the health IT developer. Doing so could include, but is not limited to, the health IT developer using existing tools or creating its own app or “client” to interact with the API as well as using a third-party application.
	* By requiring that documentation and terms of use be open and transparent to the public by requiring a hyperlink to such documentation to be published with the product on the ONC Certified Health IT Product List (CHPL), ONC hopes to encourage an open ecosystem of diverse and innovative applications that can successfully and easily interact with different Health IT Modules’ APIs. [see also [80 FR 62679](http://www.federalregister.gov/a/2015-25597/p-1112)]
	* Health IT developers are able to update/upgrade/improve functionality that’s within the scope of certification, provided that certain rules and conditions are followed. The “API criteria” § 170.315(g)(7), § 170.315(g)(8), and § 170.315(g)(9) are treated no different under this regulatory structure. If a developer seeks to update their API functionality post-certification, a developer will need to consider the following:
		+ If their ONC-ACB requires notification or updated documentation associated with the functionality they changed. This procedure is at the discretion of the ONC-ACB and may result in an additional CHPL listing.
		+ Pursuant to the certification criteria, there is a documentation portion in each, which would include (publicly available) technical specifications, configuration requirements, and terms of use. Insofar as a developer updates their API post-certification, they are expected to keep all of this documentation up-to-date. Similarly, ONC-ACBs are expected to oversee/enforce/surveil that this action is taken and could find a non-conformity if those updates are not made.
		+ If any of their changes would require updates to the developer’s § 170.523(k)(1) disclosures (the broader product transparency disclosures).
	* § 170.315(g)(10) will replace § 170.315(g)(8). ONC–ACBs can issue certificates for § 170.315(g)(8) until December 31, 2022 during the transition period to § 170.315(g)(10). We have included a provision in § 170.550(m)(3) to only allow ONC-ACBs to issue certificates for this criterion until December 31, 2022.
	* A Certified API Developer with certified API technology previously certified to the certification criterion in § 170.315(g)(8) must provide all API Information Sources with such certified API technology deployed with certified API technology certified to the certification criterion in § 170.315(g)(10) by no later than December 31 2022. [see also [85 FR 70064]](https://www.federalregister.gov/d/2020-24376/p-300)
	* A Certified API Developer with Health IT Module(s) certified to the certification criteria in § 170.315(g)(8) must comply with the requirements finalized in § 170.404(a) “Compliance for existing certified API technology”, including revisions to their existing business and technical API documentation and make such documentation available via a publicly accessible hyperlink that allows any person to directly access the information by no later than April 5, 2021. [see also [85 FR 70064](https://www.federalregister.gov/d/2020-24376/p-301)]
	
### Functional Requirements (Data Categories)

???+ quote "**Regulation text at § 170.315(g)(8)(i)(A)**"
	(i) Functional requirements. (A) Respond to requests for patient data (based on an ID or other token) for each of the individual data categories specified in the Common Clinical Data Set and return the full set of data for that data category (according to the specified standards, where applicable) in a computable format.

<!-- $ref{g-8:CCG["Paragraph (g)(8)(i)(A)"], tabbed} -->
??? quote "*Clarifications included in the (g)(8) CCG that apply to paragraph § 170.315(g)(8)(i)(A)*"
	Technical outcome – The API must be able to respond to requests for patient data (using an ID or other token) for each of the individual categories listed in the Common Clinical Data Set (CCDS) and return the full set of data for that category, according to the required data standards in a computable format.
	
	
	***Clarifications:***
	
	
	* Please refer to the 2015 Edition CCDS for the data standards that are required.
	* There is no standard required for the format of the data category request, as long as the data returned are in a computable format (machine-readable format). [see also [80 FR 62678](http://www.federalregister.gov/a/2015-25597/p-1105)]
	* The technology specifications should be designed and implemented in such a way as to return meaningful responses to queries, particularly with regard to exceptions and exception handling, and should make it easy for applications to discover what data exists for the patient. [see also [80 FR 62678](http://www.federalregister.gov/a/2015-25597/p-1109)]
	* The term “token” as used here is not to be interpreted as the token in the OAuth2 workflow, but simply as something that would uniquely identify a patient.
	* The developer can determine the method and the amount of data by which the health IT uniquely identifies a patient. [see also [80 FR 62678](http://www.federalregister.gov/a/2015-25597/p-1101)]
	* The CCDS definition lists a set of data. It does not, however, specify a set of “data categories” or prescribe a predefined grouping for API responses as may be implied by the regulatory text.
	* Consistent with the intent expressed for this functionality in the proposed rule [[80 FR 16861](http://www.federalregister.gov/a/2015-06612/p-959)], which conveyed that we intended to “allow for but not require, health IT developers to implement the Fast Health Interoperability Resource (FHIR®)” and which we carried forward with the final rule, a health IT developer is permitted and has the flexibility to group the data specified in the CCDS in its API responses in a manner that it sees fit. This could be in manner following a particular industry standard, such as FHIR, or other documented means.
		+ In doing so, a health IT developer must ensure:
			- That the “API response groupings” it uses ultimately cover all of the data specified in the CCDS. For example, if a health IT developer had 10 API response groupings, all of data specified by the CCDS definition would need to be covered by those 10 API responses.
			- The technical documentation it discloses clearly specifies how all of the data specified CCDS is met by its API response groupings.
	
### Functional Requirements (Date & Date Range)

???+ quote "**Regulation text at § 170.315(g)(8)(i)(B)**"
	(B) Respond to requests for patient data associated with a specific date as well as requests for patient data within a specified date range.

<!-- $ref{g-8:CCG["Paragraph (g)(8)(i)(B)"], tabbed} -->
??? quote "*Clarifications included in the (g)(8) CCG that apply to paragraph § 170.315(g)(8)(i)(B)*"
	Technical outcome – The API must be able to respond to requests for patient data associated with a specific date as well as requests for patient data with a specific date range.
	
	
	***Clarifications:***
	
	
	* Health IT returning an entire patient record that does not reflect the specific date or date range requested is not permissible when a specific date or date range is requested. [see also [80 FR 62678](http://www.federalregister.gov/a/2015-25597/p-1109)]
	* The API must be able to send, at a minimum all required data for a specified date range(s). ONC acknowledges that there will be organizational policies and/or safety best practices that will dictate additional data to be sent and when data are considered complete and/or ready for being sent. This should be appropriately described in the API documentation. However, returning no data on receipt of a valid date or date range, or sending an error message (which is equivalent to no data) is not permissible.
	
### Documentation Requirements (API Interface)

???+ quote "**Regulation text at § 170.315(g)(8)(ii)(A)(1)**"
	(A) The API must include accompanying documentation that contains, at a minimum: (1) API syntax, function names, required and optional parameters and their data types, return variables and their types/structures, exceptions and exception handling methods and their returns.

<!-- $ref{g-8:CCG["Paragraph (g)(8)(ii)(A)(1)"], tabbed} -->
??? quote "*Clarifications included in the (g)(8) CCG that apply to paragraph § 170.315(g)(8)(ii)(A)(1)*"
	Technical outcome – The API must include accompanying documentation that contains API syntax, function names, required and optional parameters and their data types, return variables and their types/structures, exceptions and exception handling methods and their returns.
	
	
	***Clarifications:***
	
	
	* API documentation must include information for requesting patient data using date and date ranges.
	
### Documentation Requirements (API Interaction)

???+ quote "**Regulation text at § 170.315(g)(8)(ii)(A)(2)**"
	(2) The software components and configurations that would be necessary for an application to implement in order to be able to successfully interact with the API and process its response(s).

<!-- $ref{g-8:CCG["Paragraph (g)(8)(ii)(A)(2)"], tabbed} -->
??? quote "*Clarifications included in the (g)(8) CCG that apply to paragraph § 170.315(g)(8)(ii)(A)(2)*"
	Technical outcome – The API must include accompanying documentation, which contains software components and configurations that would be necessary for an application to implement in order to be able to successfully interact with the API and process its response(s).
	
	
	***Clarifications:***
	
	
	* No additional clarifications.
	
### Documentation Requirements (API Terms of Use)

???+ quote "**Regulation text at § 170.315(g)(8)(ii)(A)(3)**"
	(3) Terms of use. The terms of use for the API must be provided, including, at a minimum, any associated developer policies and required developer agreements.

<!-- $ref{g-8:CCG["Paragraph (g)(8)(ii)(A)(3)"], tabbed} -->
??? quote "*Clarifications included in the (g)(8) CCG that apply to paragraph § 170.315(g)(8)(ii)(A)(3)*"
	Technical outcome – The API must include the terms of use for the API including, at a minimum, any associated developer policies and required developer agreements.
	
	
	***Clarifications:***
	
	
	* Health IT developers must be clear and transparent about the general terms of agreements or contracts that will typically apply to all prospective third party applications.
	* Health IT developers that typically execute unique agreements or contracts with interested third party applications using their API must disclose this practice as part of their terms of use.
	* For the purposes of certification, a health IT developer is accountable for documenting and making public the provisions of its API’s terms of use. If, post-certification, a developer permits its customers to deploy and integrate its API in ways where the customer would be able to layer on its own specific terms of use unique to that organization, the developer would need to disclose this business practice in its terms of use. A Certified Health IT Developer is not expected to change or factor instances into its terms of use where its customers establish additional, organizational-specific terms for the API’s use.
	* Pursuant to the certification criterion’s documentation requirement, health IT developers are required to make their API documentation publicly available, including the terms of use (and its associated policies and required developer agreements). Developers’ enforcement of their terms of use is beyond the scope of conformance to this certification criterion. This criterion focuses on the technical API capabilities with which a Health IT Module must be in compliance and documentation requirements as specified. For example, this certification criterion does not require health IT developers to evaluate app developers or prohibit such activity (though such activities may implicate other requirements of the Certification Program). ONC also notes that CMS, [specifically in the patient access context](https://www.cms.gov/Regulations-and-Guidance/Legislation/EHRIncentivePrograms/Downloads/MedicaidEPStage3_Obj5.pdf), states that “[p]roviders may not prohibit patients from using any application, including third-party applications, which meet the technical specifications of the API, including the security requirements of the API.”
	
	 
	
	
	
### Documentation Requirements (Availability)

???+ quote "**Regulation text at § 170.315(g)(8)(ii)(B)**"
	(B) The documentation used to meet paragraph (g)(8)(ii)(A) of this section must be available via a publicly accessible hyperlink.

<!-- $ref{g-8:CCG["Paragraph (g)(8)(ii)(B)"], tabbed} -->
??? quote "*Clarifications included in the (g)(8) CCG that apply to paragraph § 170.315(g)(8)(ii)(B)*"
	Technical outcome – The documentation used to meet the provisions in (g)(8)(ii)(A)(*1*)-(*3*) must be available through a publicly accessible hyperlink.
	
	
	***Clarifications:***
	
	
	* The hyperlink provided for all of the documentation referenced by provision (g)(8)(ii)(A) must reflect the most current version of the developer’s documentation.
	* All of the documentation referenced by provision (g)(8)(ii)(A) must be accessible to the public via a hyperlink without additional access requirements, including, without limitation, any form of registration, account creation, “click-through” agreements, or requirement to provide contact details or other information prior to accessing the documentation.
	
--8<-- "includes/abbreviations.md"