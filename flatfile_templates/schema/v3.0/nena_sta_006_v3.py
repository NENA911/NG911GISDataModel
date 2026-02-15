# ==============================================================================
# Section: 5 Detailed Description of Field Names and associated attribute data
#
# Purpose: Each of the Field Names given in the tables in Section 4, GIS Data
#          Model Layers, are listed in alphabetical order below. Each Field
#          Name has a description, attribute data domain, and an example. Some
#          Field Names include a conditional business rule that controls the
#          presence of a value in the data field. For details on case
#          sensitivity, please refer to Section 3.5 Case Sensitivity of
#          NENA-STA-006.
#
#          An attribute data domain defines the set of all valid values that
#          are allowed in the attribute data field. If the domain is none,
#          then any value that matches the data type and description MAY be
#          used for the attribute field. Those with a given data domain MUST
#          use only those values with the domain given. Web links in the
#          examples are for illustrative purposes.
#
# Format:  Dictionary
#           "<Field Name>": {
#               "section": "<Section # from 006.x>",
#               "title": "<Descriptive Name>",
#               "description":
#                   """
#                   <Description from Section 5>
#                   """,
#               "definition": {
#                   "type": '<Field Type>', ('TEXT', 'DATETIME', 'INTEGER', 'REAL')
#                   "width": <Field Type>,
#                   "required": <Required (Yes=true, No/Conditional=false)>
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
Description: A case-sensitive alphanumeric code of up to six characters used to disambiguate addresses in Canada when the combination of Administrative Level 2, Administrative Level 3, Administrative Level 4 (if used), and Street Name may not be unique within a province or territory.

Domain: None 

Example: 3h12jk; 100232; AREQUF

Business Rules: CLDXF-US: Not Applicable; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 6,
            "required": "No"
        },
        "domain": False,
        "rules": {
        },
        "example": ['3h12jk', '100232', 'AREQUF']
    },
    "AddCode_L": {
        "section": "5.2",
        "title": "Additional Code Left",
        "description":
            """
Description: The Additional Code on the left side of the road segment relative to the FROM Node.

Domain: None 

Example: 3h12jk; 100232; AREQUF

Business Rules: CLDXF-US: Not Applicable; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 6,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['3h12jk', '100232', 'AREQUF']
    },
    "AddCode_R": {
        "section": "5.3",
        "title": "Additional Code Right",
        "description":
            """
Description: The Additional Code on the right side of the road segment relative to the FROM Node.

Domain: None 

Example: 3h12jk; 100232; AREQUF

Business Rules: CLDXF-US: Not Applicable; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 6,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['3h12jk', '100232', 'AREQUF']
    },
    "AddDataURI": {
        "section": "5.4",
        "title": "Additional Data URI",
        "description":
            """
Description: URI(s) for additional data associated with the address. This attribute is contained in the SiteStructureAddressPoint and SiteStructureAddressPolygon layers and will define the URI of additional information about a location, including building information (blueprints, contact info, floor plans, etc.).

Domain: None

Example: https://addl68603.example.com
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": True,
        "rules": {
            "type": "regex",
            "re": r"/^[a-z](?:[-a-z0-9\+\.])*:(?:\/\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:])*@)?(?:\[(?:(?:(?:[0-9a-f]{1,4}:){6}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|::(?:[0-9a-f]{1,4}:){5}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){4}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,1}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){3}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,2}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:){2}(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,3}[0-9a-f]{1,4})?::[0-9a-f]{1,4}:(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,4}[0-9a-f]{1,4})?::(?:[0-9a-f]{1,4}:[0-9a-f]{1,4}|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3})|(?:(?:[0-9a-f]{1,4}:){0,5}[0-9a-f]{1,4})?::[0-9a-f]{1,4}|(?:(?:[0-9a-f]{1,4}:){0,6}[0-9a-f]{1,4})?::)|v[0-9a-f]+\.[-a-z0-9\._~!\$&'\(\)\*\+,;=:]+)\]|(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(?:\.(?:[0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])){3}|(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=])*)(?::[0-9]*)?(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@]))*)*|\/(?:(?:(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@]))+)(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@]))*)*)?|(?:(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@]))+)(?:\/(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@]))*)*|(?!(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@])))(?:\?(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@])|[\x{E000}-\x{F8FF}\x{F0000}-\x{FFFFD}\x{100000}-\x{10FFFD}\/\?])*)?(?:\#(?:(?:%[0-9a-f][0-9a-f]|[-a-z0-9\._~\x{A0}-\x{D7FF}\x{F900}-\x{FDCF}\x{FDF0}-\x{FFEF}\x{10000}-\x{1FFFD}\x{20000}-\x{2FFFD}\x{30000}-\x{3FFFD}\x{40000}-\x{4FFFD}\x{50000}-\x{5FFFD}\x{60000}-\x{6FFFD}\x{70000}-\x{7FFFD}\x{80000}-\x{8FFFD}\x{90000}-\x{9FFFD}\x{A0000}-\x{AFFFD}\x{B0000}-\x{BFFFD}\x{C0000}-\x{CFFFD}\x{D0000}-\x{DFFFD}\x{E1000}-\x{EFFFD}!\$&'\(\)\*\+,;=:@])|[\/\?])*)?$/i"
        },
        "example": ['https://addl68603.example.com']
    },
    "Addtl_Loc": {
        "section": "5.5",
        "title": "Additional Location Information",
        "description":
            """
Description: Information that relates to location but does not meet the definition of any other named location elements.

Domain: None

Example: Main Loading Dock; Stairwell C; Elevator Bank 14-21

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 225,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['Main Loading Dock', 'Stairwell C', 'Elevator Bank 14-21']
    },
    "Add_Number": {
        "section": "5.6",
        "title": "Address Number",
        "description":
            """
Description: The integer identifier of a location along a thoroughfare or within a defined community.

Domain: None 

Example: “1600” in “1600 Pennsylvania Avenue”; “24” in “24 Sussex Drive”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes

            """,
        "definition": {
            "type": 'INTEGER',
            "width": 6,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": [1600, 24]
    },
    "AddNum_Cmp": {
        "section": "5.7",
        "title": "Address Number Complete",
        "description":
            """
Description: The Address Number Complete includes the Address Number Prefix (if any), the Address Number, Address Number Suffix (if any), and any formatting or separator characters needed to display the official version of the complete address number. The Address Number Complete precedes the complete street name to identify a location along a thoroughfare or within a defined area.

Domain: None

Example: A19; 194-03½; N89W16758

Business Rules: CLDXF-US: Yes; CLDXF-CA: Not Applicable
            """,
        "definition": {
            "type": 'TEXT',
            "width": 42,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['A19', '194-03½', 'N89W16758']
    },
    "AddNum_Pre": {
        "section": "5.8",
        "title": "Address Number Prefix",
        "description":
            """
Description: An identifier that precedes the Address Number and further identifies a location along a thoroughfare, or within a defined area.

Domain: None

Example: “A” in “A19 route 117”; “75” in “75 6214 Kailua Place” (CLDXF-US only);  “75-” in “75-6214 Kailua Place” (CLDXF-CA only)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['A', '75 ', '75-']
    },
    "AddNum_Suf": {
        "section": "5.9",
        "title": "Address Number Suffix",
        "description":
            """
Description: An extension of the Address Number that follows it and further identifies a location along a thoroughfare or within a defined area.

Domain: None

Example: “B” in “223B Jay Avenue”; “½” in 119½ Elm Street” (CLDXF-US only); “1/2” in “119 1/2 Elm Street” (CLDXF-CA only)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['B', '1/2', '½']
    },
    "A1": {
        "section": "5.10",
        "title": "Administrative Level 1",
        "description":
            """
Description: The name of a state, province, or territory represented by the two letter UPPERCASE abbreviation given in ISO 3166-2.

Domain: ISO 3166-2 or USPS Publication 28 (for the United States)

Example: TN; NS; YT; PR

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "Yes"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "A1_L": {
        "section": "5.11",
        "title": "Administrative Level 1 Left",

        "description":
            """
Description: The Administrative Level 1 value on the left side of the road segment relative to the FROM Node.

Domain: ISO 3166-2 or USPS Publication 28 (for the United States)

Example: LA; NB

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "Yes"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "A1_R": {
        "section": "5.12",
        "title": "Administrative Level 1 Right",

        "description":
            """
Description: The Administrative Level 1 value on the right side of the road segment relative to the FROM Node.

Domain: ISO 3166-2 or USPS Publication 28 (for the United States)

Example: PA; NU

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "Yes"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "A2": {
        "section": "5.13",
        "title": "Administrative Level 2",
        "description":
            """
Description: The name of the primary subdivision of a state, province, or territory.

Domain: CLDXF-US: A complete list is maintained by the US Census Bureau as ANSI INCITS 31:2009 (Formerly FIPS 6 4) and the Domain is restricted to the exact listed values as published in ANSI INCITS 31:2009, including casing and use of abbreviations.

CLDXF-CA: None

Example: Washington County; District of Columbia; Capitale-Nationale; Region of Peel

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['Washington County' 'Kenai Peninsula Borough', 'Jefferson Parish',
                    'Carson City', 'Falls Church city' 'District of Columbia']
    },
    "A2_L": {
        "section": "5.14",
        "title": "Administrative Level 2 Left",
        "description":
            """
Description: The Administrative Level 2 value on the left side of the road segment relative to the FROM Node. 

Domain: CLDXF-US: A complete list is maintained by the US Census Bureau as ANSI INCITS 31:2009 (Formerly FIPS 6 4) and the Domain is restricted to the exact listed values as published in ANSI INCITS 31:2009, including casing and use of abbreviations.
CLDXF-CA: None

Example: St. Louis County; Adams County; Northumberland; Central Kootenay

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['St. Louis County' 'Adams County']
    },
    "A2_R": {
        "section": "5.15",
        "title": "Administrative Level 2 Right",
        "description":
            """
Description: The Administrative Level 2 value on the right side of the road segment relative to the FROM Node. 

Domain: CLDXF-US: A complete list is maintained by the US Census Bureau as ANSI INCITS 31:2009 (Formerly FIPS 6 4) and the Domain is restricted to the exact listed values as published in ANSI INCITS 31:2009, including casing and use of abbreviations.
CLDXF-CA: None

Example: St. Johns County; DeSoto County; Doña Ana County; Guysborough

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['St. Johns County', 'DeSoto County', 'Doña Ana County']
    },
    "A3": {
        "section": "5.16",
        "title": "Administrative Level 3",

        "description":
            """
Description: The name of the secondary division of a state, province, or territory. In Canada, where no Administrative Level 2 exists, it can be the name of the primary division of the province or territory.

Domain: None

Example: Southlake; Alpine; Yellowknife

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A3_L": {
        "section": "5.17",
        "title": "Administrative Level 3 Left",

        "description":
            """
Description: The Administrative Level 3 value on the left side of the road segment relative to the FROM Node.

Domain: None

Example: Lexington; Columbus; Mont Saint Grégoire

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A3_R": {
        "section": "5.18",
        "title": "Administrative Level 3 Right",

        "description":
            """
Description: The Administrative Level 3 value on the right side of the road segment relative to the FROM Node.

Domain: None

Example: Tampa; Yonkers; Toronto

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A4": {
        "section": "5.19",
        "title": "Administrative Level 4",

        "description":
            """
Description: The name of the subdivision of the most granular preceding administrative level.

Domain: None

Example: Cypress; Bowen; Mont Élie

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A4_L": {
        "section": "5.20",
        "title": "Administrative Level 4 Left",

        "description":
            """
Description: The Administrative Level 4 value on the left side of the road segment relative to the FROM Node.

Domain: None

Example: Latham; Moose; Sherwood Park

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A4_R": {
        "section": "5.21",
        "title": "Administrative Level 4 Right",

        "description":
            """
Description: The Administrative Level 4 value on the right side of the road segment relative to the FROM Node.

Domain: None

Example: Mountain View; Palmer; Picard

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A5": {
        "section": "5.22",
        "title": "Administrative Level 5",

        "description":
            """
Description: The name of the most granular administrative level supported by this standard. It is typically an unincorporated portion of a preceding administrative level.

Domain: None

Example: Copperfield; University Heights; Shady Oaks Mobile Home Park; Sutton

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A5_L": {
        "section": "5.23",
        "title": "Administrative Level 5 Left",

        "description":
            """
Description: The Administrative Level 5 value on the left side of the road segment relative to the FROM Node.

Domain: None

Example: East Harlem; Cypress Meadows Subdivision

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "A5_R": {
        "section": "5.24",
        "title": "Administrative Level 5 Right",

        "description":
            """
Description: The Administrative Level 5 value on the right side of the road segment relative to the FROM Node.

Domain: None

Example: Edgewater Park; The Meadows

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Agency_ID": {
        "section": "5.25",
        "title": "Agency Identifier",
        "description":
            """
Description: A Domain Name System (DNS) domain name which is used to uniquely identify an agency. An agency is represented by a fully qualified domain name as defined in NENA-STA-010. In order to correlate actions across a wide range of calls and incidents, each agency MUST use one domain name consistently. Any domain name in the public DNS is acceptable so long as each distinct agency uses a different domain name. This ensures that each agency identifier is globally unique.

Domain: Fully qualified domain name

Example: psap.harriscounty.tx.us; police.allegheny.pa.us; newbrunswick.ca; flctnecd.gov

Note: The Agency Identifier is a field in service boundary layers that identifies the agency the boundary defines. It is also used in the Emergency Incident Data Object, the Service/Agency Locator, and MUST be used in constructing NGUIDs.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "Yes"
        },
        "domain": True,
        "rules": {
         "type": "regex",
         "re": r'^(?!.*?_.*?)(?!(?:[\w]+?\.)?\-[\w\.\-]*?)(?![\w]+?\-\.(?:[\w\.\-]+?))(?=[\w])(?=[\w\.\-]*?\.+[\w\.\-]*?)(?![\w\.\-]{254})(?!(?:\.?[\w\-\.]*?[\w\-]{64,}\.)+?)[\w\.\-]+?(?<![\w\-\.]*?\.[\d]+?)(?<=[\w\-]{2,})(?<![\w\-]{25})$'
        },
        "example": ['psap.harriscounty.tx.us', 'police.allegheny.pa.us',
                    'newbrunswick.ca', 'flctnecd.gov']
    },
    "AVcard_URI": {
        "section": "5.26",
        "title": "Agency vCard URI",
        "description":
            """
Description: A vCard is a file format standard for electronic business cards. The Agency vCard URI is the internet address of a JavaScript Object Notation (JSON) data structure which contains contact information (Name of Agency, Contact phone numbers, etc.) in the form of a jCard (RFC 7095). The vCard URI is used in the service boundary layers to provide contact information for that agency. The Agency Locator (see NENA-STA-010) provides the URIs for Agencies listed in it.

Domain: None

Example: https://vcard.psap.allegheny.pa.us; https://jcard.houstontx.gov/fire

Note: This field will be considered for deletion in a future version of this document to align with future changes in NENA-STA-010.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "Yes"
        },
        "domain": False,
        "rules": {
            "type": "regex",
            "re": r'^(https:|http:|www\.)\S*'
        },
        "example": ['https://vcard.psap.allegheny.pa.us/', 'https://jcard.houstontx.gov/fire']
    },
    "Altitude": {
        "section": "5.27",
        "title": "Altitude",
        "description":
            """
Description: The measure of the orthogonal distance from the WGS84 ellipsoid, given in meters. For Site/Structure Address Points, Altitude measures the orthogonal distance from the WGS84 ellipsoid to the surface (such as a floor or ground).

Domain: Restricted to a double-precision floating point number with a precision of nine and a scale of three (e.g., REAL (9,3)).

Example: “75.000” representing the altitude (in meters) associated with the address “123 Main Street, Suite 401”

Note: WGS84 (GPS) altitude, also known as the Z Coordinate, is measured as distance above or below the ellipsoid, which varies significantly from the geoid (approximately mean sea level). For more information, see NENA Requirements for 3D Location Data for E9-1-1 and NG9-1-1, .
            """,
        "definition": {
            "type": 'REAL',
            "precision": 9,
            "scale": 3,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Country": {
        "section": "5.28",
        "title": "Country",
        "description":
            """
Description: The name of a country represented by its two letter ISO 3166-1 English country alpha 2 code elements in UPPERCASE letters.

Domain: Restricted to the two letter designations provided in .

Example: "US" for the United States of America; "CA" for Canada

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "Yes"
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['US', 'CA']
    },
    "Country_L": {
        "section": "5.29",
        "title": "Country Left",
        "description":
            """
Description: The name of the Country on the left side of the road segment relative to the FROM Node, represented by its two letter ISO 3166-1 English country alpha 2 code elements in UPPERCASE letters.

Domain: Restricted to the two letter designations provided in ISO 3166-1.

Example: "US" for the United States of America; "CA" for Canada

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "Yes"
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['US', 'CA']
    },
    "Country_R": {
        "section": "5.30",
        "title": "Country Right",

        "description":
            """
Description: The name of the Country on the right side of the road segment relative to the FROM Node, represented by its two letter ISO 3166-1 English country alpha 2 code elements in UPPERCASE letters.

Domain: Restricted to the two letter designations provided in ISO 3166-1.

Example: "US" for the United States of America; "MX" for Mexico

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "Yes"
        },
        "domain": True,
        "rules": {
            "type": "url",
            "url": "TBD"
        },
        "example": ['US', 'CA']
    },
    "DateUpdate": {
        "section": "5.31",
        "title": "Date Updated",
        "description":
            """
Description: The date and time that the record was created or last modified. This value MUST be populated upon modifications to attributes, geometry, or both.

Domain: None

Example: (of a W3C dateTime with optional precision of .1 second)
2017 12 21T17:58.03.1 05:00 (representing a record updated on December 21, 2017 at 5:58 and 3.1 seconds PM US Eastern Standard Time); 2017 07 11T08:31:15.2 04:00 (representing a record updated on July 11, 2017 at 8:31 and 15.2 seconds AM US Eastern Daylight Time)
            """,
        "definition": {
            "type": 'DATETIME',
            "required": "Yes"
        },
        "domain": True,
        "rules": {
            "type": "timestamp",
        },
        "example": ['2017-07-11T08:31:15.2-04:00', '2017-12-21T17:58.03.1-05:00']
    },
    "Dir_Travel": {
        "section": "5.32",
        "title": "Direction of Travel",
        "description":
            """
Description: A word which follows all other street name elements and is used only as needed to indicate direction of travel on a divided roadway and associated frontage roads.

Domain: None

Example: northbound; eastbound

Business Rules: CLDXF-US: Yes; CLDXF-CA: Not Applicable
            """,
        "definition": {
            "type": 'TEXT',
            "width": 10,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "DiscrpAgID": {
        "section": "5.33",
        "title": "Discrepancy Agency ID",
        "description":
            """
Description: Agency that receives a Discrepancy Report (DR), should a discrepancy be discovered, and will take responsibility for ensuring discrepancy resolution. This may or may not be the same as the 9 1 1 Authority. This MUST be represented by a domain name that is an Agency Identifier as defined in the NENA Knowledge Base Glossary.

Domain: None

Example: Vermont911.vt.us.gov; nct911.dst.tx.us
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "Yes"
        },
        "domain": False,
        "rules": {},
        "example": ['Vermont911.vt.us.gov', 'nct911.dst.tx.us']
    },
    "DsplayName": {
        "section": "5.34",
        "title": "Display Name",
        "description":
            """
Description: A description or "name" of the service provider that offers services within the area of a Service Boundary. This value MUST be suitable for display.

Domain: None

Example: New York Police Department; Med Life Ambulance Services
            """,
        "definition": {
            "type": 'TEXT',
            "width": 60,
            "required": "Yes"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "DistMarker": {
        "section": "5.35",
        "title": "Distance Marker",

        "description":
            """
Description: A physical marker labeled with the distance from or to a given point along a route such as a trail, a waterway, a road, or a highway. 

Domain: None

Example: Milepost 13; Mile Marker 327.5; Station 101 North; Kilometre 10

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 150,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "DM_Ind": {
        "section": "5.36",
        "title": "Distance Marker Indicator",
        "description":
            """
Description: A physical marker labeled with the distance from or to a given point along a route such as a trail, a waterway, a road, or a highway. 

Domain: None

Example: Milepost 13; Mile Marker 327.5; Station 101 North; Kilometre 10

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 1,
            "required": "Yes"
        },
        "domain": True,
        "rules": {
            "type": "domain",
            "domain": ['P', 'L']
        },
        "example": ['P', 'L']
    },
    "DM_Label": {
        "section": "5.37",
        "title": "Distance Marker Label",

        "description":
            """
Description: The label or text on a physical distance marker. Note that the posted label may be different from the actual measure.

Domain: None

Example: MM 3.5; HWY 102 SOUTH 19 KM; 14

Business Rules: If the Distance Marker Indicator value is "P" and the physical distance marker is labeled, the Distance Marker Label MUST be populated. If the Distance Marker Indicator value is "P" and the physical distance marker is not physically labeled, the Distance Marker Label MAY be populated with a description.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "DM_Value": {
        "section": "5.38",
        "title": "Distance Marker Measurement Value",
        "description":
            """
Description: Linear distance from a reference point, or the actual value of the distance measurement.

Domain: Restricted to a double-precision floating point number with a precision of nine and a scale of three (e.g., REAL (9,3)).

Example: 357.44; 10.0
            """,
        "definition": {
            "type": 'REAL',
            "precision": 9,
            "scale": 3,
            "required": "Yes"
        },
        "domain": False,
        "rules": {
            "type": "domain",
            "domain": ['P', 'L']
        },
        "example": ['P', 'L']
    },
    "DM_Rte": {
        "section": "5.39",
        "title": "Distance Marker Route Name",
        "description":
            """
Description: The primary route name the distance marker is associated with.

Domain: None

Example: I 90; US 66; St. Lawrence River; South Beaver Creek Trail; CSX Railroad Blue Island to Utica
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "Yes"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "DM_Type": {
        "section": "5.40",
        "title": "Distance Marker Route Type",
        "description":
            """
Description: The type of route the distance marker refers to.

Domain: None

Example: Road; Waterway; Beach; Trail; Railroad
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "DM_Unit": {
        "section": "5.41",
        "title": "Distance Marker Unit of Measurement",
        "description":
            """
Description: Unit of measurement used for the distance marker.

Domain: Standardized units of measure

Example: miles; nautical miles; feet; meters; kilometers
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "Effective": {
        "section": "5.42",
        "title": "Effective Date",
        "description":
            """
Description: The date and time that the record is scheduled to take effect.

Domain: None

Example: (of a W3C dateTime with optional precision of .1 second)
2017 02 18T02:30:00.1 05:00 (representing a record that will become active on February 18, 2017 at 2:30 and 0.1 seconds AM US Eastern Standard Time); 2017 10 09T13:01:35.2 04:00 (representing a record that will become active on October 9, 2017 at 1:01 and 35.2 seconds PM US Eastern Daylight Time)

Note: This field is used when time and date of a change is known. For example, the time and date an annexation takes effect.
            """,
        "definition": {
            "type": 'DATETIME',
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Elevation": {
        "section": "5.43",
        "title": "Elevation",

        "description":
            """
Description:  The orthogonal distance of the Earth’s surface from the WGS84 ellipsoid at the Site/Structure Address Point’s latitude and longitude; also, the Altitude of the ground level. Within a structure, this is “the zero floor level”.

Domain: Restricted to a double-precision floating point number with a precision of nine and a scale of three (e.g., REAL (9,3)).

Example: “68.000” representing the elevation (in meters) associated with ground level.

Note: WGS84 (GPS) elevation is measured as distance from the ellipsoid, which varies significantly from the geoid (approximately mean sea level). For more information, see NENA Requirements for 3D Location Data for E9-1-1 and NG9-1-1, NENA-REQ-003.
            """,
        "definition": {
            "type": 'REAL',
            "precision": 9,
            "scale": 3,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESN": {
        "section": "5.44",
        "title": "ESN",
        "description":
            """
Description: A 3-5 character numeric string that represents one or more Emergency Service Zones (ESZ).

Domain: Characters from 000 to 99999

Example: 54321; 120; 001

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 5,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESN_L": {
        "section": "5.45",
        "title": "ESN Left",

        "description":
            """
Description: The Emergency Service Number (ESN) on the left side of the road segment relative to the FROM Node.

Domain: Characters from 000 to 99999

Example: 5422; 124; 005

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 5,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ESN_R": {
        "section": "5.46",
        "title": "ESN Right",

        "description":
            """
Description: The Emergency Service Number (ESN) on the right side of the road segment relative to the FROM Node.

Domain: Characters from 000 to 99999

Example: 5423; 125; 007

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 5,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Expire": {
        "section": "5.47",
        "title": "Expiration Date",

        "description":
            """
Description: The date and time when the information in the record is no longer considered valid.

Domain: None

Example: (of a W3C dateTime with optional precision of .1 second)
2017 02 18T02:30:00.1 05:00 (representing a record that will expire and no longer be valid on February 18, 2017 at 2:30 and 0.1 seconds AM US Eastern Standard Time);
2017 10 09T13:01:35.2 04:00 (representing a record that will expire and no longer be valid on October 9, 2017 at 1:01 and 35.2 seconds PM US Eastern Daylight Time)

Note: This field is used when the time and date of a change is known. For example, the time and date an annexation takes effect and the previous boundary is retired.
            """,
        "definition": {
            "type": 'DATETIME',
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "FloorIndex": {
        "section": "5.48",
        "title": "Floor Index",

        "description":
            """
Description: An internal counter or index of floor, story, or level within a building stored as an integer to convey the range and relationships between floors. Having a floor integer independent of the floor label provides an absolute measure that can be used to convey and operationalize vertical uncertainty and will assist first responders in arriving at the location of the emergency.

The level of an addressed main entrance is “0.” Each floor or partial floor is sequentially incremented by 1 above or below 0. This is not intended for user display. It is intended to be used for internal processing or calculations.

Domain: Integers

Example: -2; -1; 0; 1; 2; 3; 4; 5; 6. 
            """,
        "definition": {
            "type": 'INTEGER',
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Floor": {
        "section": "5.49",
        "title": "Floor Label",

        "description":
            """
Description: A description of floor, story, or level within a building stored as text. This may be considered part of a “dispatchable location”.

Domain: None

Example: Floor 5; 5th Floor; Mezzanine. 
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Height": {
        "section": "5.50",
        "title": "Height",

        "description":
            """
Description: Height is the difference between Elevation and Altitude for a Site/Structure Address Point; often referred to as “Height Above Ground Level” (AGL).

Domain: Restricted to a double-precision floating point number with a precision of nine and a scale of three (e.g., REAL (9,3)).

Example: -3.3 meters; 15.5 meters; 21 meters

Note: For more information about Height, see NENA Requirements for 3D Location Data for E9-1-1 and NG9-1-1, NENA-REQ-003.
            """,
        "definition": {
            "type": 'REAL',
            "precision": 9,
            "scale": 3,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HP_Name": {
        "section": "5.51",
        "title": "Hydrology Polygon Name",

        "description":
            """
Description: Name of a lake, pond, waterway, or similar body of water.

Domain: None

Example: Mirror Lake; intracoastal waterway
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HP_Type": {
        "section": "5.52",
        "title": "Hydrology Polygon Type",

        "description":
            """
Description: Type of water body.

Domain: None

Example: lake; pond; stream; river
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HS_Name": {
        "section": "5.53",
        "title": "Hydrology Segment Name",

        "description":
            """
Description: The name of a creek, stream, river, or similar linear water feature.

Domain: None

Example: Willow Creek; Red River
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "HS_Type": {
        "section": "5.54",
        "title": "Hydrology Segment Type",

        "description":
            """
Description: The type of surface water.

Domain: None

Example: stream; river
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Latitude": {
        "section": "5.55",
        "title": "Latitude",

        "description":
            """
Description: The angular distance of a location north or south of the equator as defined by the coordinate system, expressed in decimal degrees.

Domain: Restricted to a double-precision floating point number, between +90 degrees to  90 degrees, with a precision of ten and a scale of seven (e.g., REAL (10,7)).

Example: 40.8686865
            """,
        "definition": {
            "type": 'REAL',
            "precision": 10,
            "scale": 7,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "AdNumPre_L": {
        "section": "5.56",
        "title": "Left Address Number Prefix",

        "description":
            """
Description: An identifier that precedes the Address Number, applying to all address numbers on the left side of the road segment relative to the FROM Node, and further identifies a location along a thoroughfare or within a defined area.

Domain: None

Example: “A” in “A19 route 117”; “75” in “75 6214 Kailua Place” (CLDXF-US only); “75-” in “75-6214 Kailua Place” (CLDXF-CA only)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "FromAddr_L": {
        "section": "5.57",
        "title": "Left FROM Address Number",

        "description":
            """
Description: In the RoadCenterLine layer, each feature has a begin point and an endpoint. The FROM Node is the begin point while the TO Node is the endpoint. Each has a left side and a right side relative to a begin node and an end node. The Left FROM address is the address number on the left side of the road segment relative to the FROM Node.

Domain: None

Example: See Figure 5-2 in NENA-STA-006

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'INTEGER',
            "required": "Yes"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ToAddr_L": {
        "section": "5.58",
        "title": "Left TO Address Number",

        "description":
            """
Description: In the RoadCenterLine layer, each feature has a begin point and an endpoint. The FROM Node is the begin point while the TO Node is the endpoint. Each has a left side and a right side relative to a begin node and an end node. The Left TO address is the address number on the left side of the road segment relative to the TO Node.

Domain: None

Example: See Figure 5-2 in NENA-STA-006

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'INTEGER',
            "required": "Yes"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LCountyID": {
        "section": "5.59",
        "title": "Legacy County ID",

        "description":
            """
Description: The existing County ID as found in the MSAG for the corresponding MSAG record with which the address point is associated. This is typically the same County ID value found on the corresponding Road Centerline segment.

Domain: None

Example: 021; FRKL

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 5,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LCntyID_L": {
        "section": "5.60",
        "title": "Legacy County ID Left",

        "description":
            """
Description: The existing County ID as found in the MSAG on the left side of the road segment relative to the FROM Node.

Domain: None

Example: 021; FRKL

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 5,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LCntyID_R": {
        "section": "5.61",
        "title": "Legacy County ID Right",

        "description":
            """
Description: The existing County ID as found in the MSAG on the right side of the road segment relative to the FROM Node.

Domain: None

Example: 021; FRKL

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 5,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LSt_Name": {
        "section": "5.62",
        "title": "Legacy Street Name",

        "description":
            """
Description: The street name as it currently exists in the MSAG. Ideally, this is the name as assigned by the local addressing authority. However, it is imperative that the content of the “Legacy Street Name” field in the GIS data and the content of the “Street Name” field in the MSAG MUST be identical. If there are discrepancies, one of these two databases (GIS and/or MSAG) MUST be updated to match the other.

Domain: None

Example: “STATE” in “STATE ST”; “ELMWOOD” in “N ELMWOOD AVE”

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LSt_PosDir": {
        "section": "5.63",
        "title": "Legacy Street Name Post Directional",

        "description":
            """
Description: The trailing street direction suffix as it currently exists in the MSAG. Ideally, this is the street name post directional as assigned by the local addressing authority. However, it is imperative that the content of the “Legacy Street Name Post Directional” field in the GIS data and the “Post Directional” field in the MSAG MUST be identical. If there are discrepancies, one of these two databases (GIS and/or MSAG) MUST be updated to match the other.

Domain: N; S; E; W; NE; NW; SE; SW; O; NO; SO; or equivalent abbreviations in other languages

Example: “E” in “CHURCH ST E”; “O” in “JEAN TALON BD O”

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Notes:
•	The domain values “O,” “NO,” and “SO” are the French equivalent abbreviations for “West,” “Northwest,” and “Southwest.”
•	The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LSt_PreDir": {
        "section": "5.64",
        "title": "Legacy Street Name Pre Directional",

        "description":
            """
Description: The leading street direction prefix as it currently exists in the MSAG. Ideally, this is the street name pre directional as assigned by the local addressing authority. However, it is imperative that the “Legacy Street Name Pre Directional” field in the GIS data and the “Prefix Directional” field in the MSAG MUST be identical. If there are discrepancies, one of these two databases (GIS and/or MSAG) MUST be updated to match the other.

Domain: N; S; E; W; NE; NW; SE; SW; O; NO; SO; or equivalent abbreviations in other languages

Example: “S” in “S PINE AVE”

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Notes:
•	The domain values “O,” “NO,” and “SO” are the French equivalent abbreviations for “West,” “Northwest,” and “Southwest.”
•	The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.

            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "LSt_Typ": {
        "section": "5.65",
        "title": "Legacy Street Name Type",

        "description":
            """
Description: The valid street abbreviation as it currently exists in the MSAG. Ideally, this is the street name type as assigned by the local addressing authority. However, it is imperative that the “Legacy Street Name Type” in the GIS data and the “Street Suffix” field in the MSAG MUST be identical. If there are discrepancies, one of these two databases (GIS and/or MSAG) MUST be updated to match the other.

Domain: None

Example: “ST” for “STREET”; “STR” for “STREET”; “BLVD” for “BOULEVARD”; “AVE” for “AVENUE”; “TRCE” for “TRACE”; “RU” in “48 RU O”; “BD” in “JEAN TALON BD O”

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 4,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LocMarker": {
        "section": "5.66",
        "title": "Location Marker",

        "description":
            """
Description: A uniquely identified and indivisible infrastructure component, smaller than a structure, which exists either within a structure or exterior to any structure, such as an alarm box, a utility pole, a callbox, or other similar feature.

Domain: None

Example: Callbox AB-12-34; Pole 12; Low Water Crossing #12

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Ind": {
        "section": "5.67",
        "title": "Location Marker Indicator",

        "description":
            """
Description: Indicates whether the location marker is identified by a physical sign.

Domain: P (for Posted); U (for Unposted)

Example: P; U
            """,
        "definition": {
            "type": 'TEXT',
            "width": 1,
            "required": "Yes"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "LM_Label": {
        "section": "5.68",
        "title": "Location Marker Label",

        "description":
            """
Description: The label or text on a physical marker, or if unposted, the description of an unposted  marker.

Domain: None

Example: Call Box CC-680-21; Standpipe; Pole 12; Low Water Crossing #21; Trail Intersection 15; Blue Blaze
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "LM_Type": {
        "section": "5.69",
        "title": "Location Marker Type",

        "description":
            """
Description: The type of feature the location marker represents.

Domain: None

Example: Call Box; Utility Pole; Water Crossing; Trail Intersection; Standpipe
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Longitude": {
        "section": "5.70",
        "title": "Longitude",

        "description":
            """
Description: The angular distance of a location east or west of the prime meridian of the coordinate system, expressed in decimal degrees.

Domain: Restricted to a double-precision floating point number, between  180 degrees to +180 degrees, with a precision of eleven and a scale of seven (e.g., REAL (11,7)).

Example:  112.9458335
            """,
        "definition": {
            "type": 'REAL',
            "precision": 11,
            "scale": 7,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "MSAGComm": {
        "section": "5.71",
        "title": "MSAG Community Name",

        "description":
            """
Description: The Community name associated with an address as given in the MSAG and may or may not be the same as the Community Name used by the postal service.

Domain: None

Example: Cypress; Spring; Austin; ALBANY; VERSAILLES; WICHITA COUNTY

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 30,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "MSAGComm_L": {
        "section": "5.72",
        "title": "MSAG Community Name Left",

        "description":
            """
Description: The existing MSAG Community Name on the left side of the road segment relative to the FROM Node.

Domain: None

Example: Harris County; SALEM; MATSU BOROUGH

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 30,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "MSAGComm_R": {
        "section": "5.73",
        "title": "MSAG Community Name Right",

        "description":
            """
Description: The existing MSAG Community Name on the right side of the road segment relative to the FROM Node.

Domain: None

Example: Crystal City; BROWN TWP; FRONTIER SHORES

Conditional Business Rule: All Legacy fields MUST be populated with the exact matching value from the corresponding MSAG record (including space characters and casing) if and only if a value exists. If no value exists, the field shall remain empty. Any new entries MUST be consistent between the GIS and MSAG systems of record. Service provider-specific legacy deployments should be taken into consideration.

Note: The legacy fields are used primarily for the MSAG Conversion Service to ensure that PIDF-LO records are able to return an MSAG-valid address and/or MSAG-valid address records are able to return a PIDF-LO record. The legacy fields may also provide backward compatibility with legacy map display and Computer Aided Dispatch (CAD) systems.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 30,
            "required": "No"
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
Description: The NENA Globally Unique ID (Primary Key) for each record in a GIS data layer. Each record in the GIS data layer MUST have a globally unique ID. When coalescing data from other local 9 1 1 Authorities into the ECRF and LVF, this unique ID MUST continue to have only one occurrence. Additional details on how to construct the NGUID can be found in Section 3.6 NENA Globally Unique ID (NGUID).

Domain: None

Example:
•	urn:emergency:uid:gis:SSAP:3458:caloes.ca.gov
•	urn:emergency:uid:gis:SSAPoly:3458:caloes.ca.gov
•	urn:emergency:uid:gis:RCL:987364:lincoln911.gov
•	urn:emergency:uid:gis:Psap:84274599:newbrunswick.ca
•	urn:emergency:uid:gis:Pol:3184974 8:coronado.ca.us
•	urn:emergency:uid:gis:Fire:{123e4567 e89b 12d3 a456 426652340000}:hanovercounty.gov
•	urn:emergency:uid:gis:Ems:6ee38f8e 20e4 4e5e aa37 a22b7a42d9b4:alleghany.pa.us
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "Yes"
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
Description: The direction of traffic movement along a road in relation to the FROM node and TO node of the line segment representing the road in the GIS data. The One Way field has three possible designations: B (Both), FT (From To), and TF (To From).
B – Travel in both directions allowed
FT – One way traveling from the FROM node to the TO node
TF – One way traveling from the TO node to the FROM node

Domain: B; FT; TF

Example: See Figure 5-3 in NENA-STA-006
            """,
        "definition": {
            "type": 'TEXT',
            "width": 2,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "Parity_L": {
        "section": "5.76",
        "title": "Parity Left",

        "description":
            """
Description: The even or odd property of the address number range on the left side of the road segment relative to the FROM Node.

Domain: O=Odd; E=Even; B=Both; Z=Address Range 0 0

Example: O; E; B; Z
            """,
        "definition": {
            "type": 'TEXT',
            "width": 1,
            "required": "Yes"
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
Description: The even or odd property of the address number range on the right side of the road segment relative to the FROM Node.

Domain: O=Odd; E=Even; B=Both; Z=Address Range 0 0

Example: O; E; B; Z
            """,
        "definition": {
            "type": 'TEXT',
            "width": 1,
            "required": "Yes"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "Place_Type": {
        "section": "5.78",
        "title": "Place Type",

        "description":
            """
Description: The type of feature identified by the address.

Domain: CLDXF-US: https://www.iana.org/assignments/location-type-registry/location-type-registry.xml
CLDXF-CA: None

Example: airport; bank; cafe; aéroport; usine; cinéma

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 50,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Placement": {
        "section": "5.79",
        "title": "Placement Method",

        "description":
            """
Description: The methodology used for placement of the address point or defining the extent of an address polygon.

Domain (Address Point): Address point values are restricted to values found in the “NENA Site/Structure Address Point Placement Method Registry” at: http://technet.nena.org/nrs/registry/SiteStructureAddressPointPlacementMethod.xml

Example (Address Point): Structure; Site; Parcel; Geocoding; ExteriorAccess; InteriorAccess; InteriorCentroid; PropertyAccess; Unknown

Domain (Address Polygon): Address polygon values are restricted to values found in the “NENA Site/Structure Address Polygon Extent Method Registry” at: http://technet.nena.org/nrs/registry/SiteStructureAddressPolygonExtentMethod.xml

Example (Address Polygon): Structure; Site; Parcel; Interior; Other
            """,
        "definition": {
            "type": 'TEXT',
            "width": 25,
            "required": "No"
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
Description: A system of codes that identifies an individual Post Office or metropolitan area delivery station associated with an address.

Domain: As defined by each country’s postal authority (i.e., USPS, Canada Post)

Example: 02109 (Postal Code in Boston, MA); M4E 2V4 (Postal Code in Toronto, ON)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 7,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "PostCodeEx": {
        "section": "5.81",
        "title": "Postal Code Extension",
        "usage": ['US'],
        "description":
            """
Description: A system of 4-digit codes that are used after the US Postal Code to specify a range of USPS delivery addresses.

Domain: Defined by the USPS

Example: “0001” in “02109 0001” (Postal Code Extension in Boston, MA)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Not Applicable
            """,
        "definition": {
            "type": 'TEXT',
            "width": 4,
            "required": "No"
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
Description: The Postal Code on the left side of the road segment relative to the FROM Node.

Domain: As defined by each country’s postal authority (i.e., USPS, Canada Post) 

Example: 44114 (Postal Code in Cleveland, OH); H3B 3B0 (Postal Code in Montreal, QC)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 7,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "PostCode_R": {
        "section": "5.86",
        "title": "Postal Code Right",

        "description":
            """
Description: The Postal Code on the right side of the road segment relative to the FROM Node.

Domain: As defined by each country’s postal authority (i.e., USPS, Canada Post) 

Example: 84101 (Postal Code in Salt Lake City, UT); R3C 3Z0 (Postal Code in Winnipeg, MB)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 7,
            "required": "No"
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
Description: A mailing place name for the Postal Code of an address.

Domain: CLDXF-US: Restricted to city names given in the USPS City State file for a given Postal Code.
CLDXF-CA: None

Example: Bowen; Cypress; Sarnia

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 40,
            "required": "No"
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
Description: A mailing place name for the Postal Code of an address on the left side of the road segment relative to the FROM Node.

Domain: CLDXF-US: Restricted to city names given in the USPS City State file for a given Postal code.
CLDXF-CA: None

Example: Dublin; Magnolia; Sainte Agathe des Monts

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 40,
            "required": "No"
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
Description: A mailing place name for the Postal Code of an address on the right side of the road segment relative to the FROM Node.

Domain: CLDXF-US: Restricted to city names given in the USPS City State file for a given Postal code.
CLDXF-CA: None

Example: Wicket; Zanesville; Yellowknife

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 40,
            "required": "No"
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
Description: The word or phrase that constitutes the distinctive designation of the rail line.

Domain: None

Example: Chester to Rock Hill; Florence to Kingstree to Charleston; Portage la Prairie; Prince Rupert; Winnipeg Terminal
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RLOp": {
        "section": "5.88",
        "title": "Rail Line Operator",

        "description":
            """
Description: The name of the operator of the rail line or the primary rail company with rights to use the rail line.

Domain: None

Example: UP; CSX; Abilene & Smoky Valley Railroad; VIA Rail; Canadian National
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RLOwn": {
        "section": "5.89",
        "title": "Rail Line Owner",

        "description":
            """
Description: The name of the owner of the rail right of way.

Domain: None

Example: CSX; South Carolina Central Railroad; Canadian Pacific; Canadian National
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "No"
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
Description: The ending linear reference of the named rail line.

Domain:  Restricted to a double-precision floating point number with a precision of seven and a scale of three (e.g., REAL (7,3)).

Example: 120.000; 257.330.
            """,
        "definition": {
            "type": 'REAL',
            "precision": 7,
            "scale": 3,
            "required": "No"
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
Description: The beginning linear reference of the named rail line.

Domain:  Restricted to a double-precision floating point number with a precision of seven and a scale of three (e.g., REAL (7,3)).

Example: 5.680; 14.000.
            """,
        "definition": {
            "type": 'REAL',
            "precision": 7,
            "scale": 3,
            "required": "No"
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
Description: An identifier that precedes the Address Number, applying to all address numbers on the right side of the road segment relative to the FROM Node, and further identifies a location along a thoroughfare or within a defined area. 

Domain: None

Example: “A” in “A19 route 117”; “75” in “75 6214 Kailua Place” (CLDXF-US only); “75-” in “75-6214 Kailua Place” (CLDXF-CA only)

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "FromAddr_R": {
        "section": "5.93",
        "title": "Right FROM Address Number",

        "description":
            """
Description: In the RoadCenterLine layer, each feature has a begin point and an endpoint. The FROM Node is the begin point while the TO node is the endpoint. Each has a left side and a right side relative to a begin node and an end node. The Right FROM address number is the address number on the right side of the road segment relative to the FROM Node.

Domain: None

Example: See Figure 5-4 in NENA-STA-006

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'INTEGER',
            "required": "Yes"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ToAddr_R": {
        "section": "5.94",
        "title": "Right TO Address Number",

        "description":
            """
Description: In the RoadCenterLine layer, each feature has a begin point and an endpoint. The FROM Node is the begin point while the TO node is the endpoint. Each has a left side and a right side relative to a begin node and an end node. The Right TO address number is the address number on the right side of the road segment relative to the TO Node.

Domain: None

Example: See Figure 5-4 in NENA-STA-006

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'INTEGER',
            "required": "Yes"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "RoadClass": {
        "section": "5.95",
        "title": "Road Class",

        "description":
            """
Description: The general description of the type of road. The Road Classifications used in this document are derived from the US Census MAF/TIGER Feature Classification Codes (MTFCC), which is an update to the now deprecated Census Feature Class Codes (CFCC).

Domain: Primary; Secondary; Local; Ramp; Service Drive; Vehicular Trail; Walkway/Pedestrian Trail; Stairway; Alley; Private; Parking Lot; Bike Path or Trail; Bridle Path; Other

Example: Ramp

Note: The Road Class is completely spelled out in the attribute fields. Road Classification is based on the Census road classification found in the MAF/TIGER Feature Class Code (MTFCC) Definitions. The values are taken from the S series information in this document which provided the classification scheme for surface roads and can be found at: https://www2.census.gov/geo/pdfs/reference/mtfccs2019.pdf
•	Primary roads are generally divided, limited access highways within the interstate highway system or under state management, and are distinguished by the presence of interchanges. These highways are accessible by ramps and may include some toll highways.
•	Secondary roads are main arteries, usually in the US Highway, State Highway, or County Highway system. These roads have one or more lanes of traffic in each direction, may or may not be divided, and usually have at grade intersections with many other roads and driveways.
•	Local roads are generally a paved non arterial street, road, or byway that usually has a single lane of traffic in each direction. Roads in this classification include neighborhood, rural roads, and city streets.
•	Ramp designates a road that allows controlled access from adjacent roads onto a limited access highway, often in the form of a cloverleaf interchange. Ramps typically do not have address ranges.
•	Service Drive provides access to structures along the highway, usually parallel to a limited access highway. If these roads are named and addressed, they may be considered local roads.
•	Vehicular Trail (4WD, snowmobile) is an unpaved trail or path where a four wheel drive vehicle, snowmobile, or similar vehicle is required.
•	Walkway/Pedestrian Trail is a path that is used for walking, being either too narrow for or legally restricted from vehicular traffic.
•	Stairway is a pedestrian passageway from one level to another by a series of steps.
•	Alley is generally a service road that does not generally have associated addressed structures and is usually unnamed. It is located at the rear of buildings and properties.
•	Private (service vehicles, logging, oil fields, ranches, etc.) is a road within private property that is privately maintained for service, extractive, or other purposes. These roads are often unnamed.
•	Parking Lot is the main travel route for vehicles through a paved parking area.
•	Bike Path or Trail is a path that is used for manual or small, motorized bicycles, being either too narrow for or legally restricted from vehicular traffic.
•	Bridle Path is a path that is used for horses, being either too narrow for or legally restricted from vehicular traffic.
•	Other is any road or path type that does not fit into the above categories.
            """,
        "definition": {
            "type": 'TEXT',
            "width": 24,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "Room": {
        "section": "5.96",
        "title": "Room",

        "description":
            """
Description: A single, distinctly identified, enclosed space within a structure.

Domain: None

Example: Room 137; Lobby

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {
            "type": "none"
        },
        "example": ['', '']
    },
    "Row": {
        "section": "5.97",
        "title": "Row",
        "description":
            """
Description: An identified linear feature, such as a linear arrangement of seats, workstations, equipment, or storage, within a structure, wing, unit, room, or section.

Domain: None

Example: Aisle 4; B-Line Assembly; ligne 5

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {
            "type": "none"
        },
        "example": ['', '']
    },
    "Seat": {
        "section": "5.98",
        "title": "Seat",

        "description":
            """
Description: An identified seat, desk, workstation, cubicle, or similar precise location within a structure, wing, unit, room, section, or row.

Domain: None

Example: Cubicle 5A; 5A; Desk 11; 1

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Section": {
        "section": "5.99",
        "title": "Section",

        "description":
            """
Description: An identified, unenclosed area within a structure, wing, unit, or room.

Domain: None

Example: Section 241; Customer Seating; Waiting Area; pont supérieur

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ServiceNum": {
        "section": "5.100",
        "title": "Service Number",

        "description":
            """
Description: The numbers that would be dialed on a 12 digit keypad to reach the service appropriate for the location. This is not the same as an Emergency Service Number (ESN) in Legacy E9 1 1 systems. This field is used for all service boundary layers including PsapPolygon, PolicePolygon, FirePolygon, EmsPolygon, and others such as PoisonControlPolygon. Within North America, the Service Number for most services is 9 1 1; however, there may be service boundaries that have a different number that may be associated with them such as Poison Control. Additionally, in some countries, different numbers may be used for Police, Fire, and EMS – this field would be used to denote those numbers.

Domain: A dialable number or dial string

Example: 911; 18002221222
            """,
        "definition": {
            "type": 'TEXT',
            "width": 15,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "ServiceURI": {
        "section": "5.101",
        "title": "Service URI",

        "description":
            """
Description: URI for call routing. This attribute is contained in the service boundary layers and will define the URI of the service. The URI is usually a Session Initiation Protocol (e.g., SIP or SIPs) URI that defines the initial route or path the call will take towards the PSAP or agency represented by the boundary.

Domain: Registered domain name

Example:	sips:sos.psap@eoc.houston.tx.us
sip:cambriaallianceems.com
sip:dispatch@harriscountyso.org
sip:22444032@ohiocountywv.gov:5061
sip:wexford fire@psap.allegheny.pa.us
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "Yes"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "ServiceURN": {
        "section": "5.102",
        "title": "Service URN",

        "description":
            """
Description: The URN used to select the service for which a route is desired. The ECRF is queried with a location and a Service URN that returns the URI of the appropriate service.

Domain: RFC 5031 defines the Service URN; NENA-STA-010 defines the domain of allowable values. PSAP boundaries SHOULD only contain features with Service URN values of "urn:emergency:service:sos.psap." Values to be used for service boundaries for other responding agencies are found in the IANA urn:emergency:service:responder registry.

Example:	urn:emergency:service:sos.psap
urn:emergency:service:responder.police
urn:emergency:service:responder.fire
urn:emergency:service:responder.ems
            """,
        "definition": {
            "type": 'TEXT',
            "width": 100,
            "required": "Yes"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "Site": {
        "section": "5.103",
        "title": "Site",

        "description":
            """
Description: The name of an exterior area which is publicly known and unique within a given place. A site may contain one or more structures and/or subsites. Domain: None

Example: Jack Perry Plaza; Tiburon Golf Club; San Marcos Premium Outlets; State University of New York at Buffalo North Campus; Parliament Hill; Toronto Pearson International Airport; Prince Edward Island National Park

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "SpeedLimit": {
        "section": "5.104",
        "title": "Speed Limit",

        "description":
            """
Description: Posted Speed Limit in MPH or Km/h.

Domain: Whole numbers from 1 to 999

Example: 35; 55; 70
            """,
        "definition": {
            "type": 'INTEGER',
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "St_Name": {
        "section": "5.105",
        "title": "Street Name",

        "description":
            """
Description: The element of the official complete street name that identifies the particular thoroughfare (as opposed to any street types, directionals, and modifiers).

Domain: None

Example: “Hastings” in “East Hastings Street”; “101” in “Highway 101”; “Lionel-Groulx” in “Avenue Lionel-Groulx”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PosDir": {
        "section": "5.106",
        "title": "Street Name Post Directional",

        "description":
            """
Description: A word following the Street Name element that indicates the direction taken by the thoroughfare from an arbitrary starting point or line, or the sector where it is located.

Domain: North; South; East; West; Northeast; Northwest; Southeast; Southwest; Nord; Sud; Est; Ouest; Nord Est; Nord Ouest; Sud Est; Sud Ouest; or equivalent words in other languages

Example: “North” in “Elm Avenue North”; “Ouest” in “Boulevard Jean Talon Ouest”; “South” in “Pharr Court South Northwest”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 10,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "St_PosMod": {
        "section": "5.107",
        "title": "Street Name Post Modifier",

        "description":
            """
Description: A word or phrase that follows and modifies the Street Name element but is separated from it by a Street Name Post Type or a Street Name Post Directional or both.

Domain: None

Example: “Number 5” in “Fire Road Number 5”; “Extension” in “Main Street North Extension”; “Northwest” in “Pharr Court South Northwest”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 25,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PosTyp": {
        "section": "5.108",
        "title": "Street Name Post Type",

        "description":
            """
Description: A word or phrase that follows the Street Name element and identifies a type of thoroughfare in a complete street name.

Domain: Restricted to values found in the “NENA Registry of Street Name Pre Types and Street Name Post Types” or combinations thereof at:
http://technet.nena.org/nrs/registry/StreetNamePreTypesAndStreetNamePostTypes.xml

Example: “Parkway” in “Ocean Parkway”; “Street” in “A Street”; “Rue” in “48e Rue Ouest”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 50,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "St_PreDir": {
        "section": "5.109",
        "title": "Street Name Pre Directional",

        "description":
            """
Description: A word preceding the Street Name element that indicates the direction taken by the thoroughfare from an arbitrary starting point or line, or the sector where it is located.

Domain: North; South; East; West; Northeast; Northwest; Southeast; Southwest; Nord; Sud; Est; Ouest; Nord Est; Nord Ouest; Sud Est; Sud Ouest; or equivalent words in other languages

Example: “South” in “South Congress Avenue”; "North" in "Southwest North Globe Avenue"

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 10,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "St_PreMod": {
        "section": "5.110",
        "title": "Street Name Pre Modifier",

        "description":
            """
Description: A word or phrase that precedes and modifies the Street Name element but is separated from it by a Street Name Pre Type or a Street Name Pre Directional or both.

Domain: None

Example:  “Alternate” in “Alternate Route 8”; “Old” in “Old North Church Street”; “Southwest” in “Southwest North Globe Avenue”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 25,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "St_PreTyp": {
        "section": "5.111",
        "title": "Street Name Pre Type",

        "description":
            """
Description: A word or phrase that precedes the Street Name element and identifies a type of thoroughfare in a complete street name.

Domain: Restricted to values found in the “NENA Registry of Street Name Pre Types and Street Name Post Types” or combinations thereof at: http://technet.nena.org/nrs/registry/StreetNamePreTypesAndStreetNamePostTypes.xml

Example: “Avenue” in “Avenue A”; “Highway” in “Highway 443”; “Bypass Highway” in “Bypass Highway 22”; “Boulevard” in “Boulevard of the Allies”; “Chemin” in “Chemin de la Canardière”; “Rue” in "Rue Principale”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 50,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "St_PreSep": {
        "section": "5.112",
        "title": "Street Name Pre Type Separator",

        "description":
            """
Description: A preposition or prepositional phrase between the Street Name Pre Type and the Street Name.

Domain: Restricted to values found in the “NENA Registry of Street Name Pre

Type Separators” at: http://technet.nena.org/nrs/registry/StreetNamePreTypeSeparators.xml

Example: “of the” in “Avenue of the Stars”; “du” in “Rue du Petit Champlain”; “in the” in “Circle in the Woods”; “at” in “Avenue at Port Imperial”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 20,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['', '']
    },
    "Structure": {
        "section": "5.113",
        "title": "Structure",
        "description":
            """
Description: A built feature with a vertical dimension, including both conventional buildings with walls, doors, and a roof, and other kinds of infrastructure such as cell towers, transformer stations, and fuel tanks.

Domain: None

Example: Fuel Storage Shed; Welcome Center; Confederation Bridge; Core Sciences Building; Tower C

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['234-1', 'HX0441-4412']
    },
    "SubSite": {
        "section": "5.114",
        "title": "SubSite",

        "description":
            """
Description: The name of a sub-area within a larger area specified either by a site name, a thoroughfare address, or both.

Domain: None

Example: South Cell Phone Lot; Tennis Courts; les plaines d’Abraham

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 254,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['', '']
    },
    "Unit": {
        "section": "5.115",
        "title": "Unit",
        "usage": ['CA'],
        "description":
            """
Description: A group or suite of rooms within a building, under common ownership or tenancy, typically having a common primary entrance.

Domain: None

Example: Apartment C2; Suite 3103; unité B

Business Rules: CLDXF-US: Not Applicable; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['Apartment 12', 'Suite 1338', 'unité B']
    },
    "UnitPreType": {
        "section": "5.116",
        "title": "Unit Pre Type",
        "usage": ['US'],
        "description":
            """
Description: Part of the complete unit identifier that precedes the Unit Value and indicates the kind of unit.

Domain: None

Example: “Apartment” in “Apartment C2”; “Suite” in “Suite 3103”

Business Rules: CLDXF-US: Yes; CLDXF-CA: Not Applicable
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['Apartment', 'Suite']
    },
    "UnitValue": {
        "section": "5.117",
        "title": "Unit Value",
        "usage": ['US'],
        "description":
            """
Description: Part of the complete unit identifier that uniquely identifies a particular unit.

Domain: None

Example: “C2” in “Apartment C2”; “3103” in “Suite 3103”; Penthouse

Business Rules: CLDXF-US: Yes; CLDXF-CA: Not Applicable
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {},
        "example": ['C2', '3103', 'Penthouse']
    },
    "Valid_L": {
        "section": "5.118",
        "title": "Validation Left",

        "description":
            """
Description: Indicates if the address range on the left side of the road segment, relative to the FROM node, should be used for civic location validation. A value of “Y” MAY be entered if any Address Number within the address range on the left side of the road segment should be considered by the LVF to be valid. A value of “N” MAY be entered if the Address Number should only be validated using the SiteStructureAddressPoint layer. If not present, a value of “Y” is assumed.

Domain: Y; N

Example: Y; N
            """,
        "definition": {
            "type": 'TEXT',
            "width": 1,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['Y', 'N']
    },
    "Valid_R": {
        "section": "5.119",
        "title": "Validation Right",

        "description":
            """
Description: Indicates if the address range on the right side of the road segment, relative to the FROM node, should be used for civic location validation. A value of “Y” MAY be entered if any Address Number within the address range on the right side of the road segment should be considered by the LVF to be valid. A value of “N” MAY be entered if the Address Number should only be validated using the SiteStructureAddressPoint layer. If not present, a value of “Y” is assumed.

Domain: Y; N

Example: Y; N
            """,
        "definition": {
            "type": 'TEXT',
            "width": 1,
            "required": "No"
        },
        "domain": True,
        "rules": {},
        "example": ['Y', 'N']
    },
    "Wing": {
        "section": "5.120",
        "title": "Wing",

        "description":
            """
Description: A designated part of a structure that spans one or more floors, typically including more than one unit or room and representing a significant portion of the structure’s floor area.

Domain: None

Example: Concourse A; North Quadrant; East Wing; Zone Publique – Niveau des Départs

Business Rules: CLDXF-US: Yes; CLDXF-CA: Yes
            """,
        "definition": {
            "type": 'TEXT',
            "width": 75,
            "required": "No"
        },
        "domain": False,
        "rules": {
            "usage": ['US', 'CA'],
        },
        "example": ['Concourse A', 'North Quadrant', 'East Wing', 'Zone Publique']
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
    "SiteStructureAddressPolygon": "SSAPoly",
    "ProvisioningPolygon": "Provisioning",
    "A1Polygon": "A1",
    "A2Polygon": "A2",
    "A3Polygon": "A3",
    "A4Polygon": "A4",
    "A5Polygon": "A5",
    "RailroadCenterLine": "RrCL",
    "HydrologyLine": "HydL",
    "HydrologyPolygon": "HydPgn",
    "LocationMarkerPoint": "LocMark",
    "DistanceMarkerPoint": "DistMark",

    "CoastGuardPolygon": "CoastG",
    "EmsPolygon": "Ems",
    "FirePolygon": "Fire",
    "MountainRescuePolygon": "MntnResc",
    "PoisonControlPolygon": "PoisonCntl",
    "PolicePolygon": "Pol",
    "PsapPolygon": "Psap",

    "PoliceFederalPolygon": "PolFed",
    "PoliceStateProvincialPolygon": "PolStProvl",
    "PoliceTribalPolygon": "PolTribal",
    "PoliceCountyParishPolygon": "PolCntyPar",
    "PoliceSheriffPolygon": "PolSheriff",
    "PoliceLocalPolygon": "PolLocal",
    "PoliceCampusPolygon": "PolCamp",
    "PolicePrivatePolygon": "PolPrivt",
    "PoliceAirportPolygon": "PolAir",
    "PoliceHousingPolygon": "PolHous",
    "PoliceParkPolygon": "PolPark",
    "PoliceMilitaryPolygon": "PolMil",

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

    "FireForestPolygon": "FireFor",
    "FireAirportPolygon": "FireAir",
    "FireMilitaryPolygon": "FireMil",
    "FirePrivatePolygon": "FirePrivt",

    "EmsTribalPolygon": "EmsTribal",
    "EmsCountyParishPolygon": "EmsCntyPar",
    "EmsLocalPolygon": "EmsLocal",
    "EmsPrivatePolygon": "EmsPrivt",
    "EmsMilitaryPolygon": "EmsMil",
    "EmsAirPolygon": "EmsAir",
}

import yaml
yaml_string = yaml.dump(FIELDS, sort_keys=False)
print(yaml_string)