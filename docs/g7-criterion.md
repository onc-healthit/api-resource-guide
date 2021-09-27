<!-- $criterion-endpoint{"test-method/application-access-patient-selection"} -->

# Non-standarized Data Request API Criterion § 170.315(g)(7)

## Information and Clarifications

### Entire Criterion

<!-- $ref{g-7:CCG["Applies to entire criterion"], tabbed} -->
??? quote "*Clarifications included in the (g)(7) CCG that apply to the entire criterion*"
	- While no standard is required for this criterion, we intend to adopt a standards-based approach for certification in a future rulemaking. We encourage the use of the Fast Healthcare Interoperability Resources (FHIR) specification.
	- Security:
		- For the purposes of certification there is no conformance requirement related to the registration of third party applications that use the APIs. If a Health IT module requires registration as a pre-condition for accessing the APIs, then, the process must be clearly specified in the API documentation as required by the criterion. We strongly believe that registration should not be used as a means to block information sharing via APIs.
		- This criterion does not currently include any security requirements beyond the privacy and security approach detailed above, but we encourage organizations to follow security best practices and implement security controls, such as penetration testing, encryption, audits, and monitoring as appropriate. We expect health IT developers to include information on how to securely use their APIs in the public documentation required by the certification criteria and follow industry best practices. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1072" target="_blank">80 FR 62676</a>]
		- We strongly encourage developers to build security into their APIs following best practice guidance, such as the <a href="https://us-cert.cisa.gov/bsi" target="_blank">Department of Homeland Security’s Build Security In</a> initiative. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1084" target="_blank">80 FR 62677</a>]
		- A “trusted connection” means the link is encrypted/integrity protected according to § 170.210(a)(2) or (c)(2). As such, we do not believe it is necessary to specifically name HTTPS and/or SSL/TLS as this standard already covers encryption and integrity protection for data in motion. [see also <a href="https://www.federalregister.gov/d/2015-25597/p-1072" target="_blank">80 FR 6267</a>]
		- APIs could be used when consent or authorization by an individual is required. In circumstances where there is a requirement to document a patient’s request or particular preferences, APIs can enable compliance with documentation requirements. The HIPAA Privacy Rule (45 CFR Part 160 and Part 164, Subparts A and E) permits the use of electronic documents to qualify as writings for the purpose of proving signature, e.g., electronic signatures. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1094" target="_blank">80 FR 62677</a>]
	- By requiring that documentation and terms of use be open and transparent to the public by requiring a hyperlink to such documentation to be published with the product on the ONC Certified Health IT Product List, we hope to encourage an open ecosystem of diverse and innovative applications that can successfully and easily interact with different Health IT Modules’ APIs. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1112" target="_blank">80 FR 62679</a>]
	- A health IT developer must demonstrate that its API functionality properly performs consistent with this certification criterion’s requirements. How this is done is up to the health IT developer. Doing so could include, but is not limited to, the health IT developer using existing tools or creating its own app or “client” to interact with the API as well as using a third-party application.
	- Health IT developers are able to update/upgrade/improve functionality that’s within the scope of certification, provided that certain rules and conditions are followed. The “API criteria” § 170.315(g)(7), § 170.315(g)(8), and § 170.315(g)(9) are treated no different under this regulatory structure. If a developer seeks to update their API functionality post-certification a developer will need to consider the following:
		- If their ONC-ACB requires notification or updated documentation associated with the functionality they changed. This procedure is at the discretion of the ONC-ACB and may result in an additional CHPL listing.
		- Pursuant to the certification criteria, there is a documentation portion in each. Which would include (publicly available) technical specs, configuration requirements, and terms of use. Insofar as a developer updates their API post-certification, they are expected to keep all of this documentation up-to-date. Similarly, ONC-ACBs are expected to oversee/enforce/surveil that this action is taken and could find a non-conformity if those updates are not made.
		- If any of their changes would require updates to the developer’s 170.523(k)(1) disclosures (the broader product transparency disclosures).

### Functional Requirement

???+ quote "**Regulation text at § 170.315(g)(7)(i)**"
	Functional requirement. The technology must be able to receive a request with sufficient information to uniquely identify a patient and return an ID or other token that can be used by an application to subsequently execute requests for that patient's data.

<!-- $ref{g-7:CCG["Paragraph (g)(7)(i)"], tabbed} -->
??? quote "*Clarifications included in the (g)(7) CCG that apply to paragraph § 170.315(g)(7)(i)*"
	- The developer can determine the method and the amount of data by which the health IT uniquely identifies a patient. [see also <a href="http://www.federalregister.gov/a/2015-25597/p-1101" target="_blank">80 FR 62678</a>]
	- The term “token” is not to be interpreted as the token in the OAuth2 workflow, but simply as an identifier for something that would uniquely identify a patient.

### Documentation Requirements (API Interface)

???+ quote "**Regulation text at § 170.315(g)(7)(ii)(A)(1)**"
	(A) The API must include accompanying documentation that contains, at a minimum: (1) API syntax, function names, required and optional parameters and their data types, return variables and their types/structures, exceptions and exception handling methods and their returns.

<!-- $ref{g-7:CCG["Paragraph (g)(7)(ii)(A)(1)"], tabbed} -->
??? quote "*Clarifications included in the (g)(7) CCG that apply to paragraph § 170.315(g)(7)(ii)(A)(1)*"
	- No additional clarifications available.

### Documentation Requirements (API Interaction)

???+ quote "**Regulation text at § 170.315(g)(7)(ii)(A)(2)**"
	(2) The software components and configurations that would be necessary for an application to implement in order to be able to successfully interact with the API and process its response(s).

<!-- $ref{g-7:CCG["Paragraph (g)(7)(ii)(A)(2)"], tabbed} -->
??? quote "*Clarifications included in the (g)(7) CCG that apply to paragraph § 170.315(g)(7)(ii)(A)(2)*"
	- No additional clarifications available.

### Documentation Requirements (API Terms of Use)

???+ quote "**Regulation text at § 170.315(g)(7)(ii)(A)(2)**"
	(3) Terms of use. The terms of use for the API must be provided, including, at a minimum, any associated developer policies and required developer agreements.

<!-- $ref{g-7:CCG["Paragraph (g)(7)(ii)(A)(3)"], tabbed} -->
??? quote "*Clarifications included in the (g)(7) CCG that apply to paragraph § 170.315(g)(7)(ii)(A)(3)*"
	- Health IT developers must be clear and transparent about the general terms of agreements or contracts that will typically apply to all prospective third-party applications.
	- Health IT developers that typically execute unique agreements or contracts with interested third-party applications using their API must disclose this practice as part of their terms of use.
	- For the purposes of certification, a health IT developer is accountable for documenting and making public the provisions of its API’s terms of use. If, post-certification, a health IT developer permits its customers to deploy and integrate its API in ways where the customer would be able to layer on its own specific terms of use unique to that organization, the health IT developer would need to disclose this business practice in its terms of use. A health IT developer is NOT expected to change or factor instances into its terms of use where its customers establish additional, organizational-specific terms for the API’s use.
	- Pursuant to the certification criterion’s documentation requirement, health IT developers are required to make their API documentation publicly available, including terms of use (and its associated policies and required developer agreements). Developers’ enforcement of their terms of use is beyond the scope of conformance to this certification criterion. This criterion focuses on the technical API capabilities with which a Health IT Module must be in compliance and documentation requirements as specified. For example, this certification criterion does not require health IT developers to evaluate app developers or prohibit such activity (though such activities may implicate other requirements of the Program). We also note that CMS, <a href="https://www.cms.gov/Regulations-and-Guidance/Legislation/EHRIncentivePrograms/Downloads/MedicaidEPStage3_Obj5.pdf" target="_blank">specifically in the patient access context</a>, states that “[p]roviders may not prohibit patients from using any application, including third-party applications, which meet the technical specifications of the API, including the security requirements of the API.”

### Documentation Requirements (Availability)

???+ quote "**Regulation text at § 170.315(g)(7)(ii)(A)(2)**"
	(B) The documentation used to meet paragraph (g)(7)(ii)(A) of this section must be available via a publicly accessible hyperlink.

<!-- $ref{g-7:CCG["Paragraph (g)(7)(ii)(B)"], tabbed} -->
??? quote "*Clarifications included in the (g)(7) CCG that apply to paragraph § 170.315(g)(7)(ii)(B)*"
	- The hyperlink provided for all of the documentation referenced by provision (g)(7)(ii)(A) must reflect the most current version of the Health IT developer’s documentation.
	- All of the documentation referenced by provision (g)(7)(ii)(A) must be accessible to the public via a hyperlink without additional access requirements, including, without limitation, any form of registration, account creation, “click-through” agreements, or requirement to provide contact details or other information prior to accessing the documentation.

--8<-- "includes/abbreviations.md"