# ==============================================================================
# Section: 5 Detailed Description of Field Names and associated attribute data
# Purpose:
# Format:  Dictionary
#           "<Field Name>": {
#               "section": "<Section # from 006.x>",
#               "title": "<Descriptive Name>",
#               "description":
#                   """
#                   <Description from Section 5>
#                   """,
#               "definition": {
#                   "type": '<Field Type>',
#                   "width": <Field Type>,
#                   "null": <Required (Yes=true, No/Conditional=false)>
#               },
#               "domain": <true/false>,
#               "rules": {
#                   <TBD>
#               },
#               "example": [<List of examples from Section 5>]
#           }
# ==============================================================================

FIELDS = {
    "AddCode": {
        "section": '5.1',
        "title": "Additional Code",
        "description":
            """
            A code that specifies a geographic area. Used in Canada to hold a 
            Standard Geographical Classification code; it differentiates two municipalities with 
            the same name in a province that does not have counties.

            Domain: Statistics Canada, Standard Geographical Classification 2011, Volume I, 
            Statistical Area Classification by Province and Territory – Variant of SGC 2016 at 
            https://www.statcan.gc.ca/eng/subjects/standard/sgc/2016/index
            
            Example: 3318013; 5926005
            """,
        "definition": {
            "type": 'P',
            "width": 6,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "https://www.statcan.gc.ca/en/subjects/standard/sgc/2016/index"
        },
        "example": ['3318013', '5926005']
    },
    "AddCode_L": {
        "section": "5.2",
        "title": "Additional Code Left",
        "description":
            """
            The Additional Code on the Left side of the road segment relative 
            to the FROM Node.
            
            Domain: See Additional Code
            
            Example: 4611040; 6106023
            """,
        "definition": {
            "type": 'P',
            "width": 6,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "https://www.statcan.gc.ca/en/subjects/standard/sgc/2016/index"
        },
        "example": ['4611040', '6106023']
    },
    "AddCode_R": {
        "section": "5.3",
        "title": "Additional Code Right",
        "description":
            """
            The Additional Code on the Right side of the road segment relative 
            to the FROM Node.
            
            Domain: See Additional Code
            
            Example: 5926005; 4711066
            """,
        "definition": {
            "type": 'P',
            "width": 6,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "https://www.statcan.gc.ca/en/subjects/standard/sgc/2016/index"
        },
        "example": ['5926005', '4711066']
    },
    "AddDataURI": {
        "section": "5.4",
        "title": "Additional Data URI",
        "description":
            """
            URI(s) for additional data associated with the address point. This 
            attribute is contained in the SiteStructureAddressPoint layer and will define the 
            Service URI of additional information about a location, including building 
            information (blueprints, contact info, floor plans, etc.).
            
            Domain: List of one or more URIs
            
            Example: https://addl68603.example.com
            """,
        "definition": {
            "type": 'U',
            "width": 254,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "re",
            "re": None
        },
        "example": ['https://addl68603.example.com']
    },
    "Addtl_Loc": {
        "section": "5.5",
        "title": "Additional Location Information",
        "description":
            """
            A part of a sub-address that is not a Building, Floor, Unit, Room, or 
            Seat.
            
            Domain: None
            
            Example: Pediatric Wing; Loading Dock; Concourse B; Gate B27; Corridor 5
            """,
        "definition": {
            "type": 'P',
            "width": 225,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['Pediatric Wing', 'Loading Dock', 'Concourse B', 'Gate B27', 'Corridor 5']
    },
    "Add_Number": {
        "section": "5.6",
        "title": "Address Number",
        "description":
            """
            The numeric identifier of a location along a thoroughfare or within a 
            defined community.
            
            Domain: Whole numbers from 0 to 999999
            
            Example: “1600” in “1600 Pennsylvania Avenue”
                        
            Note: The Address Number MUST be a whole number. This element is a 
            conditional element. For more details, please see the CLDXF Standard, 
            NENA-STA-004.
            """,
        "definition": {
            "type": 'N',
            "width": 6,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "range",
            "range": [0, 999999]
        },
        "example": [0, 999999]
    },
    "AddNum_Pre": {
        "section": "5.7",
        "title": "Address Number Prefix",
        "description":
            """
            An extension of the Address Number that precedes it and further 
            identifies a location along a thoroughfare or within a defined area.
            
            Domain: None
            
            Example: “75-” in “75-6214 Kailua Place”; “3W2N-” in “3W2N-4551” 
            
            Note: The Address Number Prefix contains any alphanumeric characters, 
            punctuation, and spaces preceding the Address Number. This element is a 
            conditional element. For more details, please see the CLDXF Standard, 
            NENA-STA-004 [4].
            """,
        "definition": {
            "type": 'P',
            "width": 15,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['75-', '3W2N-']
    },
    "AddNum_Suf": {
        "section": "5.8",
        "title": "Address Number Suffix",
        "description":
            """
            An extension of the Address number that follows it and further 
            identifies a location along a thoroughfare or within a defined area.
            
            Domain: None

            Example: “B” in “223B Jay Avenue”; “½” in 119½ Elm Street” 
            
            Note: This element is a conditional element. For more details, please see the 
            CLDXF Standard, NENA-STA-004.
            """,
        "definition": {
            "type": 'P',
            "width": 15,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['B', '1/2', '½']
    },
    "Agency_ID": {
        "section": "5.9",
        "title": "Agency Identifier",
        "description":
            """
            A Domain Name System (DNS) domain name which is used to 
            uniquely identify an agency. An agency is represented by a fully qualified domain 
            name as defined in NENA-STA-010 [3]. In order to correlate actions across a wide 
            range of calls and incidents, each agency MUST use one domain name 
            consistently. Any domain name in the public DNS is acceptable so long as each 
            distinct agency uses a different domain name. This ensures that each agency 
            identifier is globally unique.
            
            Domain: Fully qualified domain name
            
            Example: psap.harriscounty.tx.us; police.allegheny.pa.us; newbrunswick.ca;
            flctnecd.gov
            
            Note: The Agency Identifier is a field in service boundary layers which identifies 
            the agency the boundary defines. It is also used in the Emergency Incident Data 
            Object, the Service/Agency Locator, and MUST be used in constructing NGUIDs.
            """,
        "definition": {
            "type": 'P',
            "width": 100,
            "null": True
        },
        "domain": True,
        "rules": {
         "type": "re",
         "re": r'^(?!.*?_.*?)(?!(?:[\w]+?\.)?\-[\w\.\-]*?)(?![\w]+?\-\.(?:[\w\.\-]+?))(?=[\w])(?=[\w\.\-]*?\.+[\w\.\-]*?)(?![\w\.\-]{254})(?!(?:\.?[\w\-\.]*?[\w\-]{64,}\.)+?)[\w\.\-]+?(?<![\w\-\.]*?\.[\d]+?)(?<=[\w\-]{2,})(?<![\w\-]{25})$'
        },
        "example": ['psap.harriscounty.tx.us', 'police.allegheny.pa.us',
                    'newbrunswick.ca', 'flctnecd.gov']
    },
    "AVcard_URI": {
        "section": "5.10",
        "title": "Agency vCard URI",
        "description":
            """
            A vCard is a file format standard for electronic business cards. The 
            Agency vCard URI is the internet address of JavaScript Object Notation (JSON)
            data structure which contains contact information (Name of Agency, Contact 
            phone numbers, etc.) in the form of a jCard (RFC 7095). The vCard URI is used in 
            the service boundary layers to provide contact information for that agency. The 
            Agency Locator (see NENA-STA-010 [3]) provides these URIs for Agencies listed 
            in it.
            
            Domain: None
            
            Example: https://vcard.psap.allegheny.pa.us; https://jcard.houstontx.gov/fire
            
            Note: This field will be considered for deletion in a future version of this 
            document to align with future changes in NENA-STA-010.
            """,
        "definition": {
            "type": 'U',
            "width": 254,
            "null": True
        },
        "domain": False,
        "rules": {
            "type": "re",
            "re": r'^(https:|http:|www\.)\S*'
        },
        "example": ['https://vcard.psap.allegheny.pa.us/', 'https://jcard.houstontx.gov/fire']
    },
    "ASt_Name": {
        "section": "5.11",
        "title": "Alias Street Name",
        "description":
            """
            An alias street name associated with the road centerline segment in 
            the RoadCenterLine layer. The alias street name does not include any street 
            types, directionals, or modifiers. If an alias street name is used in the 
            StreetNameAliasTable this field MUST be populated.
            
            Domain: None
            
            Example: “Scenic” in the Alias Street Name “Scenic Boulevard”
            """,
        "definition": {
            "type": 'P',
            "width": 254,
            "null": True
        },
        "domain": False,
        "rules": {},
        "example": ['Scenic']
    },
    "ASt_PosDir": {
        "section": "5.12",
        "title": "Alias Street Name Post Directional",
        "description":
            """
            A word following the Street Name element that indicates the 
            direction taken by the road from an arbitrary starting point or line, or the sector 
            where it is located.
            
            Domain: North; South; East; West; Northeast; Northwest; Southeast;
            Southwest; Nord; Sud; Est; Ouest; Nord-Est; Nord-Ouest; Sud-Est; Sud-Ouest; or 
            equivalent words in other languages.

            Example: “West” in the Alias Street Name “Foley Street West”; “Ouest” in 
            “Boulevard Jean-Talon Ouest”
            """,
        "definition": {
            "type": 'P',
            "width": 10,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "domain",
            "domain": ['North', 'South', 'East', 'West', 'Northeast',
                       'Northwest', 'Southeast', 'Southwest', 'Nord', 'Sud',
                       'Est', 'Ouest', 'Nord-Est', 'Nord-Ouest', 'Sud-Ouest']
        },
        "example": ['West', 'Ouest']
    },
    "ASt_PosMod": {
        "section": "5.13",
        "title": "Alias Street Name Post Modifier",
        "description":
            """
            A word or phrase that follows and modifies the Alias Street Name 
            element, but is separated from it by an Alias Street Name Post Type or an Alias 
            Street Name Post Directional or both.
            
            Domain: None
            
            Example: “Bypass” in the Alias Street Name “Loop 601 North Bypass”
            """,
        "definition": {
            "type": 'P',
            "width": 25,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['Bypass']
    },
    "ASt_PosTyp": {
        "section": "5.14",
        "title": "Alias Street Name Post Type",
        "description":
            """
            A word or phrase that follows the Alias Street Name element and 
            identifies a type of thoroughfare in a complete alias street name.
            
            Domain: Restricted to values found in the “NENA Registry of Street Name Pre 
            Types and Street Name Post Types” or combinations thereof at: 
            http://technet.nena.org/nrs/registry/StreetNamePreTypesAndStreetNamePostTypes.xml
            
            Example: “Avenue” in the Alias Street Name “Fashion Avenue”; “Rue” in “48e 
            Rue Ouest”
            """,
        "definition": {
            "type": 'P',
            "width": 25,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": 'http://technet.nena.org/nrs/registry/StreetNamePreTypesAndStreetNamePostTypes.xml'
        },
        "example": ['Avenue', 'Rue']
    },
    "ASt_PreDir": {
        "section": "5.15",
        "title": "Alias Street Name Pre Directional",
        "description":
            """
            A word preceding the Alias Street Name element that indicates the 
            direction taken by the road from an arbitrary starting point or line, or the sector 
            where it is located.
            
            Domain: North; South; East; West; Northeast; Northwest; Southeast; 
            Southwest; Nord; Sud; Est; Ouest; Nord-Est; Nord-Ouest; Sud-Est; Sud-Ouest; or 
            equivalent words in other languages.
            
            Example: “North” in the Alias Street Name “North Commerce Street”
            """,
        "definition": {
            "type": 'P',
            "width": 10,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "domain",
            "domain": ['North', 'South', 'East', 'West', 'Northeast',
                       'Northwest', 'Southeast', 'Southwest', 'Nord', 'Sud',
                       'Est', 'Ouest', 'Nord-Est', 'Nord-Ouest', 'Sud-Ouest']
        },
        "example": ['North']
    },
    "ASt_PreMod": {
        "section": "5.16",
        "title": "Alias Street Name Pre Modifier",
        "description":
            """
            A word or phrase that precedes and modifies the Alias Street Name 
            element but is separated from it by an Alias Street Name Pre Type or an Alias 
            Street Name Pre Directional or both.
            
            Domain: None
            
            Example: "Alternate" in the Alias Street Name “Alternate Route 8”
            """,
        "definition": {
            "type": 'P',
            "width": 15,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['Alternate']
    },
    "ASt_PreTyp": {
        "section": "5.17",
        "title": "Alias Street Name Pre Type",
        "description":
            """
            A word or phrase that precedes the Alias Street Name element and 
            identifies a type of thoroughfare in a complete street name.
            
            Domain: Restricted to values found in the “NENA Registry of Street Name Pre 
            Types and Street Name Post Types” or combinations thereof at: 
            http://technet.nena.org/nrs/registry/StreetNamePreTypesAndStreetNamePostTypes.xml
            
            Example: “Avenue” in the Alias Street Name “Avenue C”;
            “County Road” in the Alias Street Name “County Road 12”;
            “Avenue” in the Alias Street Name “Avenue of the Americas”;
            “Chemin” in “Chemin de la Canardière”;
            "Rue" in "Rue Principale"
            """,
        "definition": {
            "type": 'P',
            "width": 25,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": 'http://technet.nena.org/nrs/registry/StreetNamePreTypesAndStreetNamePostTypes.xml'
        },
        "example": ['Avenue', 'County Road', 'Chemin', 'Rue']
    },
    "ASt_PreSep": {
        "section": "5.18",
        "title": "Alias Street Name Pre Type Separator",
        "description":
            """
            A preposition or prepositional phrase between the Alias Street 
            Name Pre Type and the Alias Street Name. This element is defined in the CLDXF 
            Standard, NENA-STA-004 [4], as a US specific extension of PIDF-LO per RFC 6848 
            [7].
            
            Domain: Restricted to values found in the “NENA Registry of Street Name Pre
            Type Separators” at: 
            http://technet.nena.org/nrs/registry/StreetNamePreTypeSeparators.xml
            
            Example: “in the” in the Alias Street Name “Circle in the Woods”; “du” in “Rue 
            du Petit-Champlain”
            """,
        "definition": {
            "type": 'P',
            "width": 20,
            "null": False
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "http://technet.nena.org/nrs/registry/StreetNamePreTypeSeparators.xml"
        },
        "example": ['in the', 'du']
    },
    "Building": {
        "section": "5.19",
        "title": "Building",
        "description":
            """
            One among a group of buildings that have the same address 
            number and complete street name.
            
            Domain: None
            
            Example: Building A; Building 4
            """,
        "definition": {
            "type": 'p',
            "width": 75,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['Building A', 'Building 4']
    },
    "CSite_Name": {
        "section": "5.20",
        "title": "Cell Site ID",
        "description":
            """
            Description: Name provided by the wireless service provider on the wireless 
            routing sheet, usually unique to the cell site.
            
            Domain: None
            
            Example: 234-1; HX0441-4412
            """,
        "definition": {
            "type": 'P',
            "width": 10,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['234-1', 'HX0441-4412']
    },
    "LandmkName": {
        "section": "5.21",
        "title": "Complete Landmark Name",
        "description":
            """
            The name by which a prominent site/structure is publicly known.
             
            Domain: None
            
            Example: Empire State Building; The Alamo; South Central High School; Kirkwood 
            Mall; James A Haley Veterans Hospital; University of South Florida Sun Dome
            
            Note: Landmarks may or may not be associated with a civic address. There are 
            two landmark name elements: Landmark Name Part and Complete Landmark 
            Name. Within a record, Landmark Name Part MAY occur multiple times, while 
            Complete Landmark Name MAY occur only once. When a landmark is denoted by 
            multiple names in a series (such as “University of South Florida” and “Sun Dome,” 
            an arena on the university campus), the Landmark Name Part element holds the 
            separate individual names, and the Complete Landmark Name holds the complete 
            combination. The Landmark Name Part element also allows specification of the 
            order in which the separate names SHOULD be combined into the complete 
            name. This element is a conditional element. For more details, please see the 
            CLDXF Standard, NENA-STA-004.
            """,
        "definition": {
            "type": 'P',
            "width": 150,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['Empire State Building', '; The Alamo', 'South Central High School',
                    'Kirkwood Mall', 'James A Haley Veterans Hospital', 'University of South Florida Sun Dome']
    },
    "CLNAlias": {
        "section": "5.22",
        "title": "Complete Landmark Name Alias",
        "description":
            """
            Description: An alias or alternate name by which a prominent site/structure is 
            publicly known.
            
            Domain: None
            
            Example: JFK Library; SUNY Buffalo; Veterans Hospital; VA Hospital; USF Sun 
            Dome; Sun Dome
            
            Note: Landmarks may or may not be associated with a civic address.
            """,
        "definition": {
            "type": 'P',
            "width": 150,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['JFK Library', 'SUNY Buffalo', 'Veterans Hospital',
                    'VA Hospital', 'USF Sun Dome', 'Sun Dome']
    },
    "CLNA_NGUID": {
        "section": "5.23",
        "title": "Complete Landmark Name Alias NENA Globally Unique ID (Foreign Key)",
        "description":
            """
            The Complete Landmark Name Alias NENA Globally Unique ID 
            (CLNA_NGUID) is used in the LandmarkNamePartTable as a foreign key 
            relationship between the LandmarkNamePartTable and the 
            LandmarkNameCompleteAliasTable. A foreign key acts as a cross-reference 
            between the CLNA_NGUID field in the LandmarkNamePartTable because it 
            references the NGUID field primary key in the LandmarkNameCompleteAliasTable, 
            thereby establishing a link between them. A record in the 
            LandmarkNameCompleteAliasTable may have one to many (1:M) 
            LandmarkNamePartTable records. Without this relationship, it would not be 
            possible to identify any landmark name parts associated with a 
            LandmarkNameCompleteAliasTable record. The values in the CLNA_NGUID field 
            MUST exist in the values of the NGUID field in the 
            LandmarkNameCompleteAliasTable layer.
            
            Domain: None
            
            Example: “urn:emergency:uid:gis:clna:1:city911.fl.us” value in the 
            LandmarkNameCompleteAliasTable NGUID would appear in all related alias 
            records in the CLNA_NGUID field of the LandmarkNamePartTable.
            """,
        "definition": {
            "type": 'P',
            "width": 254,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['urn:emergency:uid:gis:clna:1:city911.fl.us']
    },
    "Country": {
        "section": "5.24",
        "title": "Country",
        "description":
            """
            The name of a country represented by its two-letter ISO 3166-1 
            English country alpha-2 code elements in UPPER CASE letters.
            
            Domain: Restricted to the two-letter designations provided in ISO 3166-1.
            
            Example: "US" for the United States of America; "CA" for Canada
            """,
        "definition": {
            "type": 'P',
            "width": 2,
            "null": True
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['US', 'CA']
    },
    "Country_L": {
        "section": "5.25",
        "title": "Country Left",
        "description":
            """
            The name of the Country on the Left side of the road segment 
            relative to the FROM Node, represented by its two-letter ISO 3166-1 English 
            country alpha-2 code elements in UPPER CASE letters.
            
            Domain: Restricted to the two-letter designations provided in ISO 3166-1.
            
            Example: "US" for the United States of America; "CA" for Canada
            """,
        "definition": {
            "type": 'P',
            "width": 2,
            "null": True
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['US', 'CA']
    },
    "Country_R": {
        "section": "5.26",
        "title": "Country Right",
        "description":
            """
            The name of the Country on the Right side of the road segment 
            relative to the FROM Node, represented by its two-letter ISO 3166-1 English 
            country alpha-2 code elements in UPPER CASE letters.
            
            Domain: Restricted to the two-letter designations provided in ISO 3166-1.
            
            Example: "US" for the United States of America; "CA" for Canada
            """,
        "definition": {
            "type": 'P',
            "width": 2,
            "null": True
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['US', 'CA']
    },
    "County": {
        "section": "5.27",
        "title": "County or Equivalent (A2)",
        "description":
            """
            The name of a County or County-equivalent where the address is 
            located. A county (or its equivalent) is the primary legal division of a state or 
            territory.
            
            Domain: Restricted to the names of counties and county equivalents. For the US, 
            a complete list is maintained by the US Census Bureau as ANSI INCITS 31:2009 
            [17] (Formerly FIPS 6-4) and the Domain is restricted to the exact listed values as 
            published in ANSI INCITS 31:2009 [17], including casing and use of 
            abbreviations.
            
            Example: Washington County; Kenai Peninsula Borough; Jefferson Parish; Carson 
            City; Falls Church city; District of Columbia
            
            Note: The following clarifications are provided directly from the CLDXF Standard,
            NENA-STA-004 [4]:
            • County equivalents include parishes (LA), boroughs and census areas (AK), 
            federal district (DC), independent cities (VA, MD, MO, NV), municipios (PR), 
            and districts (AS, GU, MP, VI). 
            • The county name or county equivalent name indicates location, not 
            jurisdiction. Many counties include federal, state, tribal, and other lands 
            within which county government powers, including powers to name roads 
            and assign address numbers, may be limited or superseded by other 
            government bodies. Indicating who has what jurisdiction at a given 
            address is well beyond the scope or intent of this standard.
            • FIPS Codes have been superseded, renamed, and updated by the 
            InterNational Committee for Information Technology Standards (INCITS) 
            and can be found at: 
            https://www.census.gov/library/reference/code-lists/ansi.html.
            """,
        "definition": {
            "type": 'P',
            "width": 100,
            "null": True
        },
        "domain": False,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['Washington County' 'Kenai Peninsula Borough', 'Jefferson Parish',
                    'Carson City', 'Falls Church city' 'District of Columbia']
    },
    "County_L": {
        "section": "5.28",
        "title": " County or Equivalent Left (A2)",
        "description":
            """
            The name of a County or County-equivalent on the Left side of the 
            road segment relative to the FROM Node. A county (or its equivalent) is the 
            primary legal division of a state or territory.
            
            Domain: See County
            
            Example: St. Louis County; Adams County
            """,
        "definition": {
            "type": 'P',
            "width": 100,
            "null": True
        },
        "domain": False,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['St. Louis County' 'Adams County']
    },
    "County_R": {
        "section": "5.29",
        "title": " County or Equivalent Right (A2)",
        "description":
            """
            The name of a County or County-equivalent on the Right side of 
            the road segment relative to the FROM Node. A county (or its equivalent) is the 
            primary legal division of a state or territory.
            
            Domain: See County
            
            Example: St. Johns County; DeSoto County; Doña Ana County
            """,
        "definition": {
            "type": 'P',
            "width": 100,
            "null": True
        },
        "domain": False,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['St. Johns County', 'DeSoto County', 'Doña Ana County']
    },
    "DateUpdate": {
        "section": "5.30",
        "title": "Date Updated",
        "description":
            """
            The date and time that the record was created or last modified. 
            This value MUST be populated upon modifications to attributes, geometry, or 
            both.
            
            Domain: Date and Time may be stored in the local database date/time format 
            with the proviso that local time zone MUST be recorded and time MUST be 
            recorded to a precision of at least 1 second and MAY be recorded to a precision of 
            0.1 second. If the local database date/time format does not meet these 
            specifications, the database SHOULD record both the local date/time format and a 
            string conforming to W3C dateTime format as described in XML Schema Part 2: 
            Datatypes Second Edition [15].
            
            Example: (of a W3C dateTime with optional precision of .1 second)
            2017-12-21T17:58.03.1-05:00 (representing a record updated on December 21, 
            2017 at 5:58 and 3.1 seconds PM US Eastern Standard Time); 
            2017-07-11T08:31:15.2-04:00 (representing a record updated on July 11, 2017 at 
            8:31 and 15.2 seconds AM US Eastern Daylight Time)
            """,
        "definition": {
            "type": 'D',
            "null": True
        },
        "domain": True,
        "rules": {
            "type": "timestamp",
        },
        "example": ['2017-07-11T08:31:15.2-04:00', '2017-12-21T17:58.03.1-05:00']
    },
    "DiscrpAgID": {
        "section": "5.31",
        "title": "Discrepancy Agency ID",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['Vermont911.vt.us.gov', 'nct911.dst.tx.us']
    },
    "DsplayName": {
        "section": "5.32",
        "title": "Display Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Effective": {
        "section": "5.33",
        "title": "Effective Date",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Elevation": {
        "section": "5.34",
        "title": "Elevation",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESN": {
        "section": "5.35",
        "title": "ESN",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESN_L": {
        "section": "5.36",
        "title": "ESN Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESN_R": {
        "section": "5.37",
        "title": "ESN Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESRD_ESRK": {
        "section": "5.38",
        "title": "ESRD or first ESRK",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Expire": {
        "section": "5.39",
        "title": "Expiration Date",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Floor": {
        "section": "5.40",
        "title": "Floor",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HP_Name": {
        "section": "5.41",
        "title": "Hydrology Polygon Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HP_Type": {
        "section": "5.42",
        "title": "Hydrology Polygon Type",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HS_Name": {
        "section": "5.43",
        "title": "Hydrology Segment Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HS_Type": {
        "section": "5.44",
        "title": "Hydrology Segment Type",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Inc_Muni": {
        "section": "5.45",
        "title": "Incorporated Municipality",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "IncMuni_L": {
        "section": "5.46",
        "title": "Incorporated Municipality Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "IncMuni_R": {
        "section": "5.47",
        "title": "Incorporated Municipality Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LMNamePart": {
        "section": "5.48",
        "title": "Landmark Name Part",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LMNP_Order": {
        "section": "5.49",
        "title": "Landmark Name Part Order",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESRK_Last": {
        "section": "5.50",
        "title": "Last ESRK",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Latitude": {
        "section": "5.51",
        "title": "Latitude",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "AdNumPre_L": {
        "section": "5.52",
        "title": "Left Address Number Prefix",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "FromAddr_L": {
        "section": "5.53",
        "title": "Left FROM Address",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ToAddr_L": {
        "section": "5.54",
        "title": "Left TO Address",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LSt_Name": {
        "section": "5.55",
        "title": "Legacy Street Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LSt_PosDir": {
        "section": "5.56",
        "title": "Legacy Street Name Post Directional",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LSt_PreDir": {
        "section": "5.57",
        "title": "Legacy Street Name Pre Directional",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LSt_Typ": {
        "section": "5.58",
        "title": "Legacy Street Name Type",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Ind": {
        "section": "5.59",
        "title": "Location Marker Indicator",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Label": {
        "section": "5.60",
        "title": "Location Marker Label",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Value": {
        "section": "5.61",
        "title": "Location Marker Measurement Value",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Rte": {
        "section": "5.62",
        "title": "Location Marker Route Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Type": {
        "section": "5.63",
        "title": "Location Marker Type",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Unit": {
        "section": "5.64",
        "title": "Location Marker Unit of Measurement",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Longitude": {
        "section": "5.65",
        "title": "Longitude",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "CMarket_ID": {
        "section": "5.66",
        "title": "Market ID",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Milepost": {
        "section": "5.67",
        "title": "Milepost",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "MSAGComm": {
        "section": "5.68",
        "title": "MSAG Community Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "MSAGComm_L": {
        "section": "5.69",
        "title": "MSAG Community Name Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "MSAGComm_R": {
        "section": "5.70",
        "title": "MSAG Community Name Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "NbrhdComm": {
        "section": "5.71",
        "title": "Neighborhood Community",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "NbrhdCom_L": {
        "section": "5.72",
        "title": "Neighborhood Community Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "NbrhdCom_R": {
        "section": "5.73",
        "title": "Neighborhood Community Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "NGUID": {
        "section": "5.74",
        "title": "NENA Globally Unique ID",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "OneWay": {
        "section": "5.75",
        "title": "One-Way",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Parity_L": {
        "section": "5.76",
        "title": "Parity Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Parity_R": {
        "section": "5.77",
        "title": "Parity Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Place_Type": {
        "section": "5.78",
        "title": "Place Type",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Placement": {
        "section": "5.79",
        "title": "Placement",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Post_Code": {
        "section": "5.80",
        "title": "Postal Code",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "PostCodeEx": {
        "section": "5.81",
        "title": "Postal Code Extension",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "PostCode_L": {
        "section": "5.82",
        "title": "Postal Code Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "PostCode_R": {
        "section": "5.83",
        "title": "Postal Code Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Post_Comm": {
        "section": "5.84",
        "title": "Postal Community Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "PostComm_L": {
        "section": "5.85",
        "title": "Postal Community Name Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "PostComm_R": {
        "section": "5.86",
        "title": "Postal Community Name Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RLName": {
        "section": "5.87",
        "title": "Rail Line Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RLOwn": {
        "section": "5.88",
        "title": "Rail Line Operator",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RLOp": {
        "section": "5.89",
        "title": "Rail Line Owner",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RMPH": {
        "section": "5.90",
        "title": "Rail Mile Post High",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RMPL": {
        "section": "5.91",
        "title": "Rail Mile Post Low",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "AdNumPre_R": {
        "section": "5.92",
        "title": "Right Address Number Prefix",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "FromAddr_R": {
        "section": "5.93",
        "title": "Right FROM Address",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ToAddr_R": {
        "section": "5.94",
        "title": "Right TO Address",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RCL_NGUID": {
        "section": "5.95",
        "title": "Road Centerline NENA Globally Unique ID (Foreign Key)",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RoadClass": {
        "section": "5.96",
        "title": "Road Class",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Room": {
        "section": "5.97",
        "title": "Room",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Seat": {
        "section": "5.98",
        "title": "Seat",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Sector_ID": {
        "section": "5.99",
        "title": "Sector ID",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "CSctr_Ornt": {
        "section": "5.100",
        "title": "Sector Orientation",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ServiceNum": {
        "section": "5.101",
        "title": "Service Number",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ServiceURI": {
        "section": "5.102",
        "title": "Service URI",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ServiceURN": {
        "section": "5.103",
        "title": "Service URN",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Site_ID": {
        "section": "5.104",
        "title": "Site ID",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "SSAP_NGUID": {
        "section": "5.105",
        "title": "Site NENA Globally Unique ID (Foreign Key)",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "SpeedLimit": {
        "section": "5.106",
        "title": "Speed Limit",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "State": {
        "section": "5.107",
        "title": "State or Equivalent (A1)",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "State_L": {
        "section": "5.108",
        "title": "State or Equivalent Left (A1)",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "State_R": {
        "section": "5.109",
        "title": "State or Equivalent Right (A1)",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_Name": {
        "section": "5.110",
        "title": "Street Name",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PosDir": {
        "section": "5.111",
        "title": "Street Name Post Directional",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PosMod": {
        "section": "5.112",
        "title": "Street Name Post Modifier",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PosTyp": {
        "section": "5.113",
        "title": "Street Name Post Type",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PreDir": {
        "section": "5.114",
        "title": "Street Name Pre Directional",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PreMod": {
        "section": "5.115",
        "title": "Street Name Pre Modifier",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PreTyp": {
        "section": "5.116",
        "title": "Street Name Pre Type",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PreSep": {
        "section": "5.117",
        "title": "Street Name Pre Type Separator",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Switch_ID": {
        "section": "5.118",
        "title": "Switch ID",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Technology": {
        "section": "5.119",
        "title": "Technology",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Uninc_Comm": {
        "section": "5.120",
        "title": "Unincorporated Community",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "UnincCom_L": {
        "section": "5.121",
        "title": "Unincorporated Community Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "UnincCom_R": {
        "section": "5.122",
        "title": "Unincorporated Community Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Unit": {
        "section": "5.123",
        "title": "Unit",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Valid_L": {
        "section": "5.124",
        "title": "Validation Left",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Valid_R": {
        "section": "5.125",
        "title": "Validation Right",
        "description":
            """
            """,
        "definition": {
            "type": 'X',
            "width": 0,
            "null": False
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    }
}


# ==============================================================================
# Section:  7.2 "GIS Data Layers" Registry
# Purpose:  Dictionary representation of Section 7.2 "GIS Data Layers" Registry
#           used in tests to verify NENA GIS Data Layer names and Layer
#           Indicators are documented and implemented correctly.
# Format:   <Name>: <Layer Indicator>
# ==============================================================================

GIS_DATA_LAYERS_REGISTRY = {
    "RoadCenterLine": "RCL",
    "SiteStructureAddressPoint": "SSAP",
    "PsapPolygon": "Psap",
    "PolicePolygon": "Pol",
    "FirePolygon": "Fire",
    "FireForestPolygon": "FireFor",
    "FireAirportPolygon": "FireAir",
    "FireMilitaryPolygon": "FireMil",
    "FirePrivatePolygon": "FirePrivt",
    "EmsPolygon": "Ems",
    "EmsPrivatePolygon": "EmsPrivt",
    "EmsAirPolygon": "EmsAir",
    "EmsMilitaryPolygon": "EmsMil",
    "PoisonControlPolygon": "PoisonCntl",
    "MountainRescuePolygon": "MntnResc",
    "CoastGuardPolygon": "CoastG",
    "PoliceCountyPolygon": "PolCnty",
    "PoliceStateProvincialPolygon": "PolStProvl",
    "PoliceFederalPolygon": "PolFed",
    "PoliceFederalFbiPolygon": "PolFedFbi",
    "PoliceFederalRcmpPolygon": "PolFedRcmp",
    "PoliceFederalSecretServicePolygon": "PolFedScrtSrv",
    "PoliceFederalDeaPolygon": "PolFedDea",
    "PoliceFederalMarshalPolygon": "PolFedMars",
    "PoliceFederalCustomsBorderProtectionPolygon": "PolFedCustBPrtcn",
    "PoliceFederalImmigrationCustomsPolygon": "PolFedImmCust",
    "PoliceFederalAtfPolygon": "PolFedAtf",
    "PoliceFederalParkPolygon": "PolFedPark",
    "PoliceFederalDiplomaticSecurityPolygon": "PolFedDipScrty",
    "PoliceFederalProtectiveServicePolygon": "PolFedPrttvSrv",
    "PoliceSheriffPolygon": "PolSheriff",
    "PoliceMilitaryPolygon": "PolMil",
    "PoliceCampusPolygon": "PolCamp",
    "PolicePrivatePolygon": "PolPrivt",
    "PoliceAirportPolygon": "PolAir",
    "PoliceHousingPolygon": "PolHous",
    "PoliceParkPolygon": "PolPark",
    "StreetNameAliasTable": "StNA",
    "LandmarkNameParkTable": "LnmkNamePart",
    "LandmarkNameCompleteAliasTable": "LnmkNameCompA",
    "A1Polygon": "A1",
    "A2Polygon": "A2",
    "A3Polygon": "A3",
    "A4Polygon": "A4",
    "A5Polygon": "A5",
    "RailroadCenterLine": "RrCL",
    "HydrologyLine": "HydL",
    "HydrologyPolygon": "HydPgn",
    "CellSectorPoint": "CellSect",
    "LocationMarkerPoint": "LocMark"
}
