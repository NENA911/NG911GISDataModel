#____________________________________________________________________________________________________________________________________________________
# Creates a file geodatabase to fit the NENA NG9-1-1 Data Model
#
# Python script initially shared with NENA Data Structures on: 2019-02-12 (Melissa Liebert, WA State NG9-1-1 GIS Subcommittee Chair)
# Initially Created:     2015-11-20 (Jason Guthrie, TComm911)
# Recreated:	2019-04-29 (NENA GIS Template Working Group)
# Last Updated:	2019-11-20 (NENA GIS Template Working Group)
#____________________________________________________________________________________________________________________________________________________
# Description:
#              Script creates a File Geodatabase, Domains, adds feature classes, adds fields to each feature class after they are created. 
#              Some fields are optional or conditional so may be commented out with a # if you don't need to use them.
#
#____________________________________________________________________________________________________________________________________________________
# Change Log:
#				11/20/2019 - Added "del" to StreetNamePreTypeSeparator domain
#				11/20/2019 - Added "Grade" to StreetNameType domain
#____________________________________________________________________________________________________________________________________________________

# Import the necessary python modules (only works on a machine with ArcGIS/arcpy)
print ("Importing ArcPy")
import arcpy, datetime
print (datetime.datetime.now().time())

#Make sure that the folder in this variable exists (template_gdb) in the same directory as the script.
FolderPath = ".\\template_gdb"
MetadataPath = ".\\template_gdb"
print
print ("Working Folder set to:          " + FolderPath)
print ("Metadata Folder set to:         " + MetadataPath)
GeodatabaseName = FolderPath + "\\NG911_GIS_20191120.gdb"
arcpy.gp.CreateFileGDB(FolderPath, "NG911_GIS_20191120", "10.0")
#arcpy.gp.CreateFileGDB(FolderPath, "NG911_GIS_20181028", "CURRENT")
print ("Created File Geodatabase:       " + GeodatabaseName)

#____________________________________________________________________________________________________________________________________________________
# Build the Domains.  This needs to be done first so that when creating fields, the domain is already available for association.
#____________________________________________________________________________________________________________________________________________________

print ("Creating Domain AdditionalCode...")
arcpy.CreateDomain_management(GeodatabaseName, "AdditionalCode", "A code that specifies a geographic area. Used in Canada to hold a Standard Geographical Classification code; it differentiates two municipalities with the same name in a province that does not have counties.", "TEXT", "CODED")
# This code applies to Road Centerlines and Site/Structure address points.

print ("Creating Domain AddressNumber...")
arcpy.CreateDomain_management(GeodatabaseName, "AddressNumber", "The numeric identifier of a location along a thoroughfare or within a defined community.", "LONG", "RANGE")
arcpy.SetValueForRangeDomain_management(GeodatabaseName, "AddressNumber", 0, 999999)
# This code applies to Road Centerlines and Site/Structure address points.

print ("Creating Domain AgencyID...")
arcpy.CreateDomain_management(GeodatabaseName, "AgencyID", "A Domain Name System (DNS) domain name which is used to uniquely identify an agency.", "TEXT", "CODED")
# This code applies to PSAP Boundaries and all other layers defined by the Emergency Services Boundary table definition.

print ("Creating Domain LegacyStreetNameDirectional...")
arcpy.CreateDomain_management(GeodatabaseName, "LegacyStreetNameDirectional", "An abbreviation that indicates the direction taken by the road from an arbitrary starting point or line, or the sector where it is located", "TEXT", "CODED")
domDict = {"N":"North", "S": "South", "E": "East", "W": "West", "NE": "Northeast", "NW": "Northwest", "SE": "Southeast", "SW": "Southwest"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "LegacyStreetNameDirectional", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "LegacyStreetNameDirectional", "CODE", "ASCENDING")
domDict = {}
# This domain applies both for the primary legacy street name directionals (pre/post) and the alias legacy street name directionals.

print ("Creating Domain LegacyStreetNameType...")
arcpy.CreateDomain_management(GeodatabaseName, "LegacyStreetNameType", "An abbreviation that follows the Alias Legacy Street Name element and identifies a type of thoroughfare in a complete alias legacy street name.  US Postal Service Publication Number 28, Appendix C1.", "TEXT", "CODED")
domDict = {"ALY": "ALLEY","ANX": "ANEX","ARC": "ARCADE","AVE": "AVENUE","BYU": "BAYOU","BCH": "BEACH","BND": "BEND","BLF": "BLUFF","BLFS": "BLUFFS","BTM": "BOTTOM","BLVD": "BOULEVARD","BR": "BRANCH","BRG": "BRIDGE","BRK": "BROOK","BRKS": "BROOKS","BG": "BURG","BGS": "BURGS","BYP": "BYPASS","CP": "CAMP","CYN": "CANYON","CPE": "CAPE","CSWY": "CAUSEWAY","CTR": "CENTER","CTRS": "CENTERS","CIR": "CIRCLE","CIRS": "CIRCLES","CLF": "CLIFF","CLFS": "CLIFFS","CLB": "CLUB","CMN": "COMMON","CMNS": "COMMONS","COR": "CORNER","CORS": "CORNERS","CRSE": "COURSE","CT": "COURT","CTS": "COURTS","CV": "COVE","CVS": "COVES","CRK": "CREEK","CRES": "CRESCENT","CRST": "CREST","XING": "CROSSING","XRD": "CROSSROAD","XRDS": "CROSSROADS","CURV": "CURVE","DL": "DALE","DM": "DAM","DV": "DIVIDE","DR": "DRIVE","DRS": "DRIVES","EST": "ESTATE","ESTS": "ESTATES","EXPY": "EXPRESSWAY","EXT": "EXTENSION","EXTS": "EXTENSIONS","FALL": "FALL","FLS": "FALLS","FRY": "FERRY","FLD": "FIELD","FLDS": "FIELDS","FLT": "FLAT","FLTS": "FLATS","FRD": "FORD","FRDS": "FORDS","FRST": "FOREST","FRG": "FORGE","FRGS": "FORGES","FRK": "FORK","FRKS": "FORKS","FT": "FORT","FWY": "FREEWAY","GDN": "GARDEN","GDNS": "GARDENS","GTWY": "GATEWAY","GLN": "GLEN","GLNS": "GLENS","GRN": "GREEN","GRNS": "GREENS","GRV": "GROVE","GRVS": "GROVES","HBR": "HARBOR","HBRS": "HARBORS","HVN": "HAVEN","HTS": "HEIGHTS","HWY": "HIGHWAY","HL": "HILL","HLS": "HILLS","HOLW": "HOLLOW","INLT": "INLET","IS": "ISLAND","ISS": "ISLANDS","ISLE": "ISLE","JCT": "JUNCTION","JCTS": "JUNCTIONS","KY": "KEY","KYS": "KEYS","KNL": "KNOLL","KNLS": "KNOLLS","LK": "LAKE","LKS": "LAKES","LAND": "LAND","LNDG": "LANDING","LN": "LANE","LGT": "LIGHT","LGTS": "LIGHTS","LF": "LOAF","LCK": "LOCK","LCKS": "LOCKS","LDG": "LODGE","LOOP": "LOOP","MALL": "MALL","MNR": "MANOR","MNRS": "MANORS","MDW": "MEADOW","MDWS": "MEADOWS","MEWS": "MEWS","ML": "MILL","MLS": "MILLS","MSN": "MISSION","MTWY": "MOTORWAY","MT": "MOUNT","MTN": "MOUNTAIN","MTNS": "MOUNTAINS","NCK": "NECK","ORCH": "ORCHARD","OVAL": "OVAL","OPAS": "OVERPASS","PARK":"PARK(S)","PKWY": "PARKWAY(S)","PASS": "PASS","PSGE": "PASSAGE","PATH": "PATH","PIKE": "PIKE","PNE": "PINE","PNES": "PINES","PL": "PLACE","PLN": "PLAIN","PLNS": "PLAINS","PLZ": "PLAZA","PT": "POINT","PTS": "POINTS","PRT": "PORT","PRTS": "PORTS","PR": "PRAIRIE","RADL": "RADIAL","RAMP": "RAMP","RNCH": "RANCH","RPD": "RAPID","RPDS": "RAPIDS","RST": "REST","RDG": "RIDGE","RDGS": "RIDGES","RIV": "RIVER","RD": "ROAD","RDS": "ROADS","RTE": "ROUTE","ROW": "ROW","RUE": "RUE","RUN": "RUN","SHL": "SHOAL","SHLS": "SHOALS","SHR": "SHORE","SHRS": "SHORES","SKWY": "SKYWAY","SPG": "SPRING","SPGS": "SPRINGS","SPUR": "SPUR(S)","SQ": "SQUARE","SQS": "SQUARES","STA": "STATION","STRA": "STRAVENUE","STRM": "STREAM","ST": "STREET","STS": "STREETS","SMT": "SUMMIT","TER": "TERRACE","TRWY": "THROUGHWAY","TRCE": "TRACE","TRAK": "TRACK","TRFY": "TRAFFICWAY","TRL": "TRAIL","TRLR": "TRAILER","TUNL": "TUNNEL","TPKE": "TURNPIKE","UPAS": "UNDERPASS","UN": "UNION","UNS": "UNIONS","VLY": "VALLEY","VLYS": "VALLEYS","VIA": "VIADUCT","VW": "VIEW","VWS": "VIEWS","VLG": "VILLAGE","VLGS": "VILLAGES","VL": "VILLE","VIS": "VISTA","WALK": "WALK(S)","WALL": "WALL","WAY": "WAY","WAYS": "WAYS","WL": "WELL","WLS": "WELLS"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "LegacyStreetNameType", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "LegacyStreetNameType", "CODE", "ASCENDING")
domDict = {}
# This domain applies both for the primary legacy street name types and the alias legacy street name types.

print ("Creating Domain StreetNameDirectional...")
arcpy.CreateDomain_management(GeodatabaseName, "StreetNameDirectional", "A word preceding or following the Street Name element that indicates the direction taken by the road from an arbitrary starting point or line, or the sector where it is located.", "TEXT", "CODED")
domDict = {"North":"North", "South": "South", "East": "East", "West": "West", "Northeast": "Northeast", "Northwest": "Northwest", "Southeast": "Southeast", "Southwest": "Southwest"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "StreetNameDirectional", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "StreetNameDirectional", "CODE", "ASCENDING")
domDict = {}
# This domain applies both for the primary street name directionals (pre/post) and the alias street name directionals.

print ("Creating Domain StreetNameType...")
arcpy.CreateDomain_management(GeodatabaseName, "StreetNameType", "A word or phrase that precedes or follows the Street Name element and identifies a type of thoroughfare in a complete street name.", "TEXT", "CODED")
domDict = {"Access Road":"Access Road","Acres":"Acres","Alcove":"Alcove","Alley":"Alley","Annex":"Annex","Approach":"Approach","Arcade":"Arcade","Arch":"Arch","Avenida":"Avenida","Avenue":"Avenue","Avenue Court":"Avenue Court","Bank":"Bank","Bay":"Bay","Bayou":"Bayou","Bayway":"Bayway","Beach":"Beach","Bend":"Bend","Bluff":"Bluff","Bluffs":"Bluffs","Bottom":"Bottom","Boardwalk":"Boardwalk","Boulevard":"Boulevard","Branch":"Branch","Bridge":"Bridge","Brook":"Brook","Brooks":"Brooks","Bureau of Indian Affairs Route":"Bureau of Indian Affairs Route","Burg":"Burg","Burgs":"Burgs","Bypass":"Bypass","Calle":"Calle","Camino":"Camino","Camp":"Camp","Canyon":"Canyon","Cape":"Cape","Causeway":"Causeway","Center":"Center","Centers":"Centers","Chase":"Chase","Circle":"Circle","Circles":"Circles","Circus":"Circus","Cliff":"Cliff","Cliffs":"Cliffs","Close":"Close","Club":"Club","Cluster":"Cluster","Common":"Common","Commons":"Commons","Concourse":"Concourse","Connect":"Connect","Connector":"Connector","Corner":"Corner","Corners":"Corners","Corridor":"Corridor","County Forest Road":"County Forest Road","County Highway":"County Highway","County Road":"County Road","County Route":"County Route","Course":"Course","Court":"Court","Courts":"Courts","Cove":"Cove","Coves":"Coves","Creek":"Creek","Crescent":"Crescent","Crest":"Crest","Cross":"Cross","Crossing":"Crossing","Crossroad":"Crossroad","Crossroads":"Crossroads","Crossway":"Crossway","Curve":"Curve","Custer County Road":"Custer County Road","Cutoff":"Cutoff","Cutting":"Cutting","Dale":"Dale","Dam":"Dam","Dawson County Road":"Dawson County Road","Dell":"Dell","Divide":"Divide","Down":"Down","Downs":"Downs","Drift":"Drift","Drive":"Drive","Drives":"Drives","Driveway":"Driveway","End":"End","Esplanade":"Esplanade","Estate":"Estate","Estates":"Estates","Exchange":"Exchange","Exit":"Exit","Expressway":"Expressway","Extension":"Extension","Extensions":"Extensions","Fall":"Fall","Falls":"Falls","Fare":"Fare","Farm":"Farm","Federal-Aid Secondary Highway":"Federal-Aid Secondary Highway","Ferry":"Ferry","Field":"Field","Fields":"Fields","Flat":"Flat","Flats":"Flats","Flyway":"Flyway","Ford":"Ford","Fords":"Fords","Forest":"Forest","Forge":"Forge","Forges":"Forges","Fork":"Fork","Forks":"Forks","Fort":"Fort","Freeway":"Freeway","Front":"Front","Garden":"Garden","Gardens":"Gardens","Garth":"Garth","Gate":"Gate","Gates":"Gates","Gateway":"Gateway","Glade":"Glade","Glen":"Glen","Glens":"Glens","Gorge":"Gorge","Grade":"Grade","Green":"Green","Greens":"Greens","Grove":"Grove","Groves":"Groves","Harbor":"Harbor","Harbors":"Harbors","Harbour":"Harbour","Haven":"Haven","Heights":"Heights","Highway":"Highway","Hill":"Hill","Hills":"Hills","Hollow":"Hollow","Horseshoe":"Horseshoe","Inlet":"Inlet","Interstate":"Interstate","Interval":"Interval","Island":"Island","Islands":"Islands","Isle":"Isle","Junction":"Junction","Junctions":"Junctions","Keep":"Keep","Key":"Key","Keys":"Keys","Knoll":"Knoll","Knolls":"Knolls","Lair":"Lair","Lake":"Lake","Lakes":"Lakes","Land":"Land","Landing":"Landing","Lane":"Lane","Lateral":"Lateral","Ledge":"Ledge","Light":"Light","Lights":"Lights","Loaf":"Loaf","Lock":"Lock","Locks":"Locks","Lodge":"Lodge","Lookout":"Lookout","Loop":"Loop","Mall":"Mall","Manor":"Manor","Manors":"Manors","Market":"Market","Meadow":"Meadow","Meadows":"Meadows","Mews":"Mews","Mill":"Mill","Mills":"Mills","Mission":"Mission","Montana Highway":"Montana Highway","Motorway":"Motorway","Mount":"Mount","Mountain":"Mountain","Mountains":"Mountains","Narrows":"Narrows","National Forest Development Road":"National Forest Development Road","Neck":"Neck","Nook":"Nook","Orchard":"Orchard","Oval":"Oval","Overlook":"Overlook","Overpass":"Overpass","Park":"Park","Parke":"Parke","Parks":"Parks","Parkway":"Parkway","Parkways":"Parkways","Pass":"Pass","Passage":"Passage","Path":"Path","Pathway":"Pathway","Pike":"Pike","Pine":"Pine","Pines":"Pines","Place":"Place","Plain":"Plain","Plains":"Plains","Plaza":"Plaza","Point":"Point","Pointe":"Pointe","Points":"Points","Port":"Port","Ports":"Ports","Prairie":"Prairie","Promenade":"Promenade","Quarter":"Quarter","Quay":"Quay","Ramp":"Ramp","Radial":"Radial","Ranch":"Ranch","Rapid":"Rapid","Rapids":"Rapids","Reach":"Reach","Rest":"Rest","Ridge":"Ridge","Ridges":"Ridges","Rise":"Rise","River":"River","River Road":"River Road","Road":"Road","Roads":"Roads","Round":"Round","Route":"Route","Row":"Row","Rue":"Rue","Run":"Run","Runway":"Runway","Shoal":"Shoal","Shoals":"Shoals","Shore":"Shore","Shores":"Shores","Skyway":"Skyway","Slip":"Slip","Spring":"Spring","Springs":"Springs","Spur":"Spur","Spurs":"Spurs","Square":"Square","Squares":"Squares","State Highway":"State Highway","State Parkway":"State Parkway","State Road":"State Road","State Route":"State Route","State Secondary":"State Secondary","Station":"Station","Strand":"Strand","Strasse":"Strasse","Stravenue":"Stravenue","Stream":"Stream","Street":"Street","Street Court":"Street Court","Streets":"Streets","Strip":"Strip","Summit":"Summit","Taxiway":"Taxiway","Tern":"Tern","Terrace":"Terrace","Throughway":"Throughway","Thruway":"Thruway","Trace":"Trace","Track":"Track","Trafficway":"Trafficway","Trail":"Trail","Trailer":"Trailer","Triangle":"Triangle","Tunnel":"Tunnel","Turn":"Turn","Turnpike":"Turnpike","United States Forest Service Road":"United States Forest Service Road","United States Highway":"United States Highway","Underpass":"Underpass","Union":"Union","Unions":"Unions","Valley":"Valley","Valleys":"Valleys","Via":"Via","Viaduct":"Viaduct","View":"View","Views":"Views","Villa":"Villa","Village":"Village","Villages":"Villages","Ville":"Ville","Vista":"Vista","Walk":"Walk","Walks":"Walks","Wall":"Wall","Way":"Way","Ways":"Ways","Weeg":"Weeg","Well":"Well","Wells":"Wells","Woods":"Woods","Wye":"Wye"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "StreetNameType", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "StreetNameType", "CODE", "ASCENDING")
domDict = {}
# This domain applies both for the primary street name types (pre/post) and the alias street name types.
# As NENA updates the StreetNamePreTypesAndStreetNamePostTypes registry the values in this domain will also need to be updated.

print ("Creating Domain StreetNamePreTypeSeparator...")
arcpy.CreateDomain_management(GeodatabaseName, "StreetNamePreTypeSeparator", "A preposition or prepositional phrase between the Street Name Pre Type and the Street Name.", "TEXT", "CODED")
domDict = {"of the":"of the", "at":"at", "de las":"de las", r'in the':r'in the', "des":"des", "to the":"to the", "of":"of", "on the":"on the", "to":"to", "del":"del"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "StreetNamePreTypeSeparator", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "StreetNamePreTypeSeparator", "CODE", "ASCENDING")
domDict = {}

print ("Creating Domain Country...")
arcpy.CreateDomain_management(GeodatabaseName, "Country", "The name of a country represented by its two-letter ISO 3166-1 English country alpha-2 code elements in capital ASCII letters.", "TEXT", "CODED")
domDict = {"US":"United States", "CA": "Canada", "MX": "Mexico"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "Country", code, domDict[code])
domDict = {}

print ("Creating Domain County...")
arcpy.CreateDomain_management(GeodatabaseName, "County", "The name of a County or County-equivalent where the address is located. The Domain is restricted to the exact listed values as published in ANSI INCITS 31:2009, including casing and use of abbreviations.", "TEXT", "CODED")

print ("Creating Domain ESN...")
arcpy.CreateDomain_management(GeodatabaseName, "ESN", "A 3-5 character alphanumeric string that represents an Emergency Service Zone (ESZ).", "TEXT", "CODED")

print ("Creating Domain LandmarkNamePartOrder...")
arcpy.CreateDomain_management(GeodatabaseName, "LandmarkNamePartOrder", "The order in which to concatenate Landmark Name Parts where 1 is the first (or leftmost) Landmark Name Part, 2 is the second Landmark Name Part, 3 is the third Landmark Name Part, etc.", "SHORT", "RANGE")
arcpy.SetValueForRangeDomain_management(GeodatabaseName, "LandmarkNamePartOrder", 1, 99)

print ("Creating Domain Latitude...")
arcpy.CreateDomain_management(GeodatabaseName, "Latitude", "The angular distance of a location north or south of the equator as defined by the coordinate system, expressed in decimal degrees.", "DOUBLE", "RANGE")
arcpy.SetValueForRangeDomain_management(GeodatabaseName, "Latitude", -90, +90)

print ("Creating Domain Longitude...")
arcpy.CreateDomain_management(GeodatabaseName, "Longitude", "The angular distance of a location north or south of the equator as defined by the coordinate system, expressed in decimal degrees.", "DOUBLE", "RANGE")
arcpy.SetValueForRangeDomain_management(GeodatabaseName, "Longitude", -180, +180)

print ("Creating Domain MilePostIndicator...")
arcpy.CreateDomain_management(GeodatabaseName, "MilePostIndicator", "Indicator of the type of mile post measurement.", "TEXT", "CODED")
domDict = {"P":"Posted", "L": "Logical / Calculated"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "MilePostIndicator", code, domDict[code])
domDict = {}

print ("Creating Domain MilePostUnitOfMeasurement...")
arcpy.CreateDomain_management(GeodatabaseName, "MilePostUnitOfMeasurement", "Unit of measurement used for mile post value.", "TEXT", "CODED")
domDict = {"miles":"miles", "nautical miles":"nautical miles", "feet":"feet", "kilometers":"kilometers", "meters":"meters"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "MilePostUnitOfMeasurement", code, domDict[code])
domDict = {}

print ("Creating Domain OneWay...")
arcpy.CreateDomain_management(GeodatabaseName, "OneWay", "The direction of traffic movement along a road in relation to the FROM node and TO node of the line segment representing the road in the GIS data.", "TEXT", "CODED")
domDict = {"B":"Travel in both directions allowed", "FT":"One-way traveling from FROM node to TO node", "TF":"One-way traveling from TO node to FROM node"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "OneWay", code, domDict[code])
domDict = {}

print ("Creating Domain Parity...")
arcpy.CreateDomain_management(GeodatabaseName, "Parity", "The even or odd property of the address number on the corresponding side of the road segment relative to the FROM Node.", "TEXT", "CODED")
domDict = {"O":"Odd", "E":"Even", "B":"Both", "Z":"Address Range 0-0"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "Parity", code, domDict[code])
domDict = {}
# This domain applies to both Parity Left and Parity Right

print ("Creating Domain PlaceType...")
arcpy.CreateDomain_management(GeodatabaseName, "PlaceType", "The type of feature identified by the address.", "TEXT", "CODED")
domDict = {"airport":"A place from which aircrafts operate, such as an airport or heliport.","arena":"Enclosed area used for sports events.","bank":"Business establishment in which money is kept for saving, commercial purposes, is invested, supplied for loans, or exchanged.","bar":"A bar or saloon.","bus-station":"Terminal that serves bus passengers, such as a bus depot or bus terminal.","cafe":"Usually a small and informal establishment that serves various refreshments (such as coffee); coffee shop.","classroom":"Academic classroom or lecture hall.","club":"Dance club, nightclub, or discotheque.","construction":"Construction site.","convention-center":"Convention center or exhibition hall.","government":"Government building, such as those used by the legislative, executive, or judicial branches of governments, including court houses, police stations, and military installations.","hospital":"Hospital, hospice, medical clinic, mental institution, or doctor's office.","hotel":"Hotel, motel, inn, or other lodging establishment.","industrial":"Industrial setting, such as a manufacturing floor or power plant.","library":"Library or other public place in which literary and artistic materials, such as books, music, periodicals, newspapers, pamphlets, prints, records, and tapes, are kept for reading, reference, or lending.","office":"Business setting, such as an office.","other":"A place without a registered place type representation.","outdoors":"Outside a building, in or into the open air, such as a park or city streets.","parking":"A parking lot or parking garage.","place-of-worship":"A religious site where congregations gather for religious observances, such as a church, chapel, meetinghouse, mosque, shrine, synagogue, or temple.","prison":"Correctional institution where persons are confined while on trial or for punishment, such as a prison, penitentiary, jail, brig.","public":"Public area such as a shopping mall, street, park, public building, train station, or airport or in public conveyance such as a bus, train, plane, or ship. This general description encompasses the more precise descriptors 'street', 'public-transport', 'ai","residence":"A private or residential setting, not necessarily the personal residence of the entity, e.g., including a friend's home.","restaurant":"Restaurant, coffee shop, or other public dining establishment.","school":"School or university property, but not necessarily a classroom or library.","shopping-area":"Shopping mall or shopping area. This area is a large, often enclosed, shopping complex containing various stores, businesses, and restaurants usually accessible by common passageways.","stadium":"Large, usually open structure for sports events, including a racetrack.","store":"Place where merchandise is offered for sale, such as a shop.","street":"A public thoroughfare, such as an avenue, street, alley, lane, or road, including any sidewalks.","theater":"Theater, lecture hall, auditorium, classroom, movie theater, or similar facility designed for presentations, talks, plays, music performances, and other events involving an audience.","train-station":"Terminal where trains load or unload passengers or goods; railway station, railroad station, railroad terminal, train depot.","unknown":"The type of place is unknown.","warehouse":"Place in which goods or merchandise are stored, such as a storehouse or self-storage facility.","water":"In, on, or above bodies of water, such as an ocean, lake, river, canal, or other waterway."}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "PlaceType", code, domDict[code])
domDict = {}

print ("Creating Domain PlacementMethod...")
arcpy.CreateDomain_management(GeodatabaseName, "PlacementMethod", "The methodology used for placement of the address point.", "TEXT", "CODED")
domDict = {"Geocoding":"Placement of an address point to represent an address along a road segment based on the high and low numbers assigned to the road segment using geocoding techniques.", "Parcel":"Placement of an address point to represent an address associated with a parcel.", "Property Access":"Placement of an address point to represent an address based on the location of the primary access to a given property.", "Site":"Placement of an address point to represent an identified, described, or recognized location that may not have a defined boundary or a structure (e.g., campsite, ball field, picnic area, etc.).", "Structure":"Placement of an address point to represent an address associated with a structure.", "Unknown":"Default value when the Site/Structure Address Point placement method is unknown."}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "PlacementMethod", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "PlacementMethod", "CODE", "ASCENDING")
domDict = {}

print ("Creating Domain PostalCode...")
arcpy.CreateDomain_management(GeodatabaseName, "PostalCode", "A system of 5-digit (US) or 7-character codes (Canada) that identify the individual USPS or Canadian Post Office or metropolitan area delivery station associated with an address.", "TEXT", "CODED")

print ("Creating Domain PostalCommunityName...")
arcpy.CreateDomain_management(GeodatabaseName, "PostalCommunityName", "A city name for the ZIP Code of an address, as given in the USPS City State file.", "TEXT", "CODED")

print ("Creating Domain RoadClass...")
arcpy.CreateDomain_management(GeodatabaseName, "RoadClass", "The general description of the type of road.", "TEXT", "CODED")
domDict = {"Primary":"Primary roads are limited-access highways that connect to other roads only at interchanges and not at at-grade intersections", "Secondary":"Secondary roads are main arteries that are not limited access, usually in the U.S. highway, state highway, or county highway systems.", "Local":"Generally a paved non-arterial street, road, or byway that usually has a single lane of traffic in each direction.", "Ramp":"A road that allows controlled access from adjacent roads onto a limited access highway, often in the form of a cloverleaf interchange.", "Service Drive":"A road, usually paralleling a limited access highway, that provides access to structures and/or service facilities along the highway.","Vehicular Trail":"An unpaved dirt trail where a four-wheel drive vehicle is required. These vehicular trails are found almost exclusively in very rural areas.", "Walkway":"A path that is used for walking, being either too narrow for or legally restricted from vehicular traffic.", "Stairway":"A pedestrian passageway from one level to another by a series of steps.", "Alley":"A service road that does not generally have associated addressed structures and is usually unnamed. It is located at the rear of buildings and properties and is used for deliveries.", "Private":"A road within private property that is privately maintained for service, extractive, or other purposes. These roads are often unnamed.", "Parking Lot":"The main travel route for vehicles through a paved parking area. This may include unnamed roads through apartment/condominium/office complexes where pull-in parking spaces line the road.", "Trail":"(Ski, Bike, Walking/Hikding Trail) is generally a path used by human powered modes of transportation.", "Bridle Path":"A path that is used for horses, being either too narrow for or legally restricted from vehicular traffic.", "Other":"Any road or path type that does not fit into the above categories"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "RoadClass", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "RoadClass", "CODE", "ASCENDING")
domDict = {}

print ("Creating Domain ServiceURI...")
arcpy.CreateDomain_management(GeodatabaseName, "ServiceURI", "URI for routing.  This attribute is contained in the Emergency Service Boundary layer and will define the Service URI of the service.", "TEXT", "CODED")

print ("Creating Domain ServiceURN...")
arcpy.CreateDomain_management(GeodatabaseName, "ServiceURN", "The URN used to select the service for which a route is desired.", "TEXT", "CODED")
domDict = {"urn:service:sos":"The generic 'sos' service reaches a public safety answering point (PSAP), which in turn dispatches aid appropriate to the emergency.","urn:service:sos.ambulance":"This service identifier reaches an ambulance service that provides emergency medical assistance and transportation.","urn:service:sos.animal-control":"Animal control typically enforces laws and ordinances pertaining to animal control and management, investigates cases of animal abuse, educates the community in responsible pet ownership and wildlife care, and provides for the housing and care of homeless animals, among other animal-related services.","urn:service:sos.fire":"The 'fire' service identifier summons the fire service, also known as the fire brigade or fire department.","urn:service:sos.gas":"The 'gas' service allows the reporting of natural gas (and other flammable gas) leaks or other natural gas emergencies.","urn:service:sos.marine":"The 'marine' service refers to maritime search and rescue services such as those offered by the coast guard, lifeboat, or surf lifesavers.","urn:service:sos.mountain":"The 'mountain' service refers to mountain rescue services (i.e., search and rescue activities that occur in a mountainous environment), although the term is sometimes also used to apply to search and rescue in other wilderness environments.","urn:service:sos.physician":"The 'physician' emergency service connects the caller to a physician referral service.","urn:service:sos.poison":"The 'poison' service refers to special information centers set up to inform citizens about how to respond to potential poisoning.","urn:service:sos.police":"The 'police' service refers to the police department or other law enforcement authorities.","urn:nena:service:sos.psap":"Route calls to primary PSAP.","urn:nena:service:sos.level_2_esrp":"Route calls to a second level ESRP (for an example, a state ESRP routing towards a county ESRP).","urn:nena:service:sos.level_3_esrp":"Route calls to a third level ESRP (for example, a regional ESRP that received a call from a state ESRP and in turn routes towards a county ESRP).","urn:nena:service:sos.call_taker":"Route calls to a call taker within a PSAP.","urn:nena:service:responder.police":"Police Agency","urn:nena:service:responder.fire":"Fire Department","urn:nena:service:responder.ems":"Emergency Medical Service","urn:nena:service:responder.poison_control":"Poison Control Center","urn:nena:service:responder.mountain_rescue":"Mountain Rescue Service","urn:nena:service:responder.sheriff":"Sheriff's office, when both a police and Sheriff dispattch may be possible","urn:nena:service:responder.stateProvincial_police":"State or provincial police office","urn:nena:service:responder.coast_guard":"Coast Guard Station","urn:nena:service:responder.psap":"Other purposes beyond use for dispatch via ECRF","urn:nena:service:responder.federal_police.fbi":"Federal Bureau of Investigation","urn:nena:service:responder.federal_police.rcmp":"Royal Canadian Mounted Police","urn:nena:service:responder.federal_police.usss":"U.S. Secret Service","urn:nena:service:responder.federal_police.dea":"Drug Enforcement Agency","urn:nena:service:responder.federal_police.marshal":"Marshals Service","urn:nena:service:responder.federal_police.cbp":"Customs and Border Protection","urn:nena:service:responder.federal_police.ice":"Immigration and Customs Enforcement","urn:nena:service:responder.federal_police.atf":"Bureau of Alcohol, Tobacco, Fire Arms and Explosives","urn:nena:service:responder.federal_police.pp":"U.S. Park Police","urn:nena:service:responder.federal_police.dss":"Diplomatic Security Service","urn:nena:service:responder.federal_police.fps":"Federal Protective Service","urn:nena:service:additionalData":"Return a URI to an Additional Data structure as defined in NENA-STA-012.2.","urn:nena:policy":"Route Policy"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "ServiceURN", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "ServiceURN", "CODE", "ASCENDING")
domDict = {}

print ("Creating Domain SpeedLimit...")
arcpy.CreateDomain_management(GeodatabaseName, "SpeedLimit", "Posted Speed Limit in MPH in US or Km/h in Canada", "SHORT", "RANGE")
arcpy.SetValueForRangeDomain_management(GeodatabaseName, "SpeedLimit", 1, 999)

print ("Creating Domain State...")
arcpy.CreateDomain_management(GeodatabaseName, "State", "The name of a state or state equivalent, represented by the two-letter abbreviation given in USPS Publication 28 [14], Appendix B.", "TEXT", "CODED")
domDict = {"AL":"Alabama","AK":"Alaska","AS":"American Samoa","AZ":"Arizona","AR":"Arkansas","CA":"California","CO":"Colorado","CT":"Connecticut","DE":"Delaware","DC":"District of Columbia","FM":"Federated States of Micronesia","FL":"Florida","GA":"Georgia","GU":"Guam","HI":"Hawaii","ID":"Idaho","IL":"Illinois","IN":"Indiana","IA":"Iowa","KS":"Kansas","KY":"Kentucky","LA":"Louisiana","ME":"Maine","MH":"Marshall Islands","MD":"Maryland","MA":"Massachusetts","MI":"Michigan","MN":"Minnesota","MS":"Mississippi","MO":"Missouri","MT":"Montana","NE":"Nebraska","NV":"Nevada","NH":"New Hampshire","NJ":"New Jersey","NM":"New Mexico","NY":"New York","NC":"North Carolina","ND":"North Dakota","MP":"Northern Mariana Islands","OH":"Ohio","OK":"Oklahoma","OR":"Oregon","PW":"Palau","PA":"Pennsylvania","PR":"Puerto Rico","RI":"Rhode Island","SC":"South Carolina","SD":"South Dakota","TN":"Tennessee","TX":"Texas","UT":"Utah","VT":"Vermont","UM":"United States Minor Outlying Islands","VI":"Virgin Islands","VA":"Virginia","WA":"Washington","WV":"West Virginia","WI":"Wisconsin","WY":"Wyoming"}
for code in domDict:   
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "State", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "State", "CODE", "ASCENDING")
domDict = {}

print ("Creating Domain Validation...")
arcpy.CreateDomain_management(GeodatabaseName, "Validation", "Indicates if the address range on the corresponding side of the road segment should be used for civic location validation.", "TEXT", "CODED")
domDict = {"Y":"Yes", "N": "No"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "Validation", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "Validation", "CODE", "ASCENDING")
domDict = {}
# This domain applies to both the Valid_L and Valid_R fields

#____________________________________________________________________________________________________________________________________________________
# Create the layers and assign fields
#____________________________________________________________________________________________________________________________________________________

FeatureClassLabel = "RoadCenterlines"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RCL_NGUID", "TEXT", "", "", "254", "Road Centerline NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AdNumPre_L", "TEXT", "", "", "15", "Left Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AdNumPre_R", "TEXT", "", "", "15", "Right Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "FromAddr_L", "LONG", "", "", "", "Left FROM Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "ToAddr_L", "LONG", "", "", "", "Left TO Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "FromAddr_R", "LONG", "", "", "", "Right FROM Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "ToAddr_R", "LONG", "", "", "", "Right TO Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "Parity_L", "TEXT", "", "", "1", "Parity Left", "NON_NULLABLE", "REQUIRED", "Parity")
arcpy.gp.AddField(FeatureClassName, "Parity_R", "TEXT", "", "", "1", "Parity Right", "NON_NULLABLE", "REQUIRED", "Parity")
arcpy.gp.AddField(FeatureClassName, "St_PreMod", "TEXT", "", "", "15", "Street Name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreDir", "TEXT", "", "", "9", "Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PreTyp", "TEXT", "", "", "50", "Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PreSep", "TEXT", "", "", "20", "Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "StreetNamePreTypeSeparator")
arcpy.gp.AddField(FeatureClassName, "St_Name", "TEXT", "", "", "60", "Street Name", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosTyp", "TEXT", "", "", "50", "Street Name Post Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PosDir", "TEXT", "", "", "9", "Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PosMod", "TEXT", "", "", "25", "Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_PreDir", "TEXT", "", "", "2", "Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "LSt_Name", "TEXT", "", "", "75", "Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Type", "TEXT", "", "", "4", "Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameType")
arcpy.gp.AddField(FeatureClassName, "LSt_PosDir", "TEXT", "", "", "2", "Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ESN_L", "TEXT", "", "", "5", "ESN Left", "NULLABLE", "NON_REQUIRED", "ESN")
arcpy.gp.AddField(FeatureClassName, "ESN_R", "TEXT", "", "", "5", "ESN Right", "NULLABLE", "NON_REQUIRED", "ESN")
arcpy.gp.AddField(FeatureClassName, "MSAGComm_L", "TEXT", "", "", "30", "MSAG Community Name Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MSAGComm_R", "TEXT", "", "", "30", "MSAG Community Name Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country_L", "TEXT", "", "", "2", "Country Left", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "Country_R", "TEXT", "", "", "2", "Country Right", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State_L", "TEXT", "", "", "2", "State Left", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "State_R", "TEXT", "", "", "2", "State Right", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County_L", "TEXT", "", "", "40", "County Left", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "County_R", "TEXT", "", "", "40", "County Right", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode_L", "TEXT", "", "", "6", "Additional Code Left", "NULLABLE", "NON_REQUIRED", "AdditionalCode")
arcpy.gp.AddField(FeatureClassName, "AddCode_R", "TEXT", "", "", "6", "Additional Code Right", "NULLABLE", "NON_REQUIRED", "AdditionalCode")
arcpy.gp.AddField(FeatureClassName, "IncMuni_L", "TEXT", "", "", "100", "Incorporated Municipality Left", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "IncMuni_R", "TEXT", "", "", "100", "Incorporated Municipality Right", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincCom_L", "TEXT", "", "", "100", "Unincorporated Community Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincCom_R", "TEXT", "", "", "100", "Unincorporated Community Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdCom_L", "TEXT", "", "", "100", "Neighborhood Community Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdCom_R", "TEXT", "", "", "100", "Neighborhood Community Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "PostCode_L", "TEXT", "", "", "7", "Postal Code Left", "NULLABLE", "NON_REQUIRED", "PostalCode")
arcpy.gp.AddField(FeatureClassName, "PostCode_R", "TEXT", "", "", "7", "Postal Code Right", "NULLABLE", "NON_REQUIRED", "PostalCode")
arcpy.gp.AddField(FeatureClassName, "PostComm_L", "TEXT", "", "", "40", "Postal Community Name Left", "NULLABLE", "NON_REQUIRED", "PostalCommunityName")
arcpy.gp.AddField(FeatureClassName, "PostComm_R", "TEXT", "", "", "40", "Postal Community Name Right", "NULLABLE", "NON_REQUIRED", "PostalCommunityName")
arcpy.gp.AddField(FeatureClassName, "RoadClass", "TEXT", "", "", "15", "Road Class", "NULLABLE", "NON_REQUIRED", "RoadClass")
arcpy.gp.AddField(FeatureClassName, "OneWay", "TEXT", "", "", "2", "One-Way", "NULLABLE", "NON_REQUIRED", "OneWay")
arcpy.gp.AddField(FeatureClassName, "SpeedLimit", "SHORT", "", "", "", "Speed Limit", "NULLABLE", "NON_REQUIRED", "SpeedLimit")
arcpy.gp.AddField(FeatureClassName, "Valid_L", "TEXT", "", "", "1", "Validation Left", "NULLABLE", "NON_REQUIRED", "Validation")
arcpy.gp.AddField(FeatureClassName, "Valid_R", "TEXT", "", "", "1", "Validation Right", "NULLABLE", "NON_REQUIRED", "Validation")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "SiteStructureAddressPoints"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_NGUID", "TEXT", "", "", "254", "Site NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "40", "County", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "AdditionalCode")
arcpy.gp.AddField(FeatureClassName, "AddDataURI", "TEXT", "", "", "254", "Additional Data URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Nbrhd_Comm", "TEXT", "", "", "100", "Neighborhood Community", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddNum_Pre", "TEXT", "", "", "15", "Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Add_Number", "LONG", "", "", "", "Address Number", "NULLABLE", "NON_REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "AddNum_Suf", "TEXT", "", "", "15", "Address Number Suffix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreMod", "TEXT", "", "", "15", "Street name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreDir", "TEXT", "", "", "9", "Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PreTyp", "TEXT", "", "", "50", "Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PreSep", "TEXT", "", "", "20", "Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "StreetNamePreTypeSeparator")
arcpy.gp.AddField(FeatureClassName, "St_Name", "TEXT", "", "", "60", "Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosTyp", "TEXT", "", "", "50", "Street Name Post Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PosDir", "TEXT", "", "", "9", "Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PosMod", "TEXT", "", "", "25", "Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_PreDir", "TEXT", "", "", "2", "Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "LSt_Name", "TEXT", "", "", "75", "Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Type", "TEXT", "", "", "4", "Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameType")
arcpy.gp.AddField(FeatureClassName, "LSt_PosDir", "TEXT", "", "", "2", "Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ESN", "TEXT", "", "", "5", "ESN", "NULLABLE", "NON_REQUIRED", "ESN")
arcpy.gp.AddField(FeatureClassName, "MSAGComm", "TEXT", "", "", "30", "MSAG Community Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Post_Comm", "TEXT", "", "", "40", "Postal Community Name", "NULLABLE", "NON_REQUIRED", "PostalCommunityName")
arcpy.gp.AddField(FeatureClassName, "Post_Code", "TEXT", "", "", "7", "Postal Code", "NULLABLE", "NON_REQUIRED", "PostalCode")
arcpy.gp.AddField(FeatureClassName, "Post_Code4", "TEXT", "", "", "4", "ZIP Plus 4", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Building", "TEXT", "", "", "75", "Building", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Floor", "TEXT", "", "", "75", "Floor", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Unit", "TEXT", "", "", "75", "Unit", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Room", "TEXT", "", "", "75", "Room", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Seat", "TEXT", "", "", "75", "Seat", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Addtl_Loc", "TEXT", "", "", "225", "Additional Location Information", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LandmkName", "TEXT", "", "", "150", "Complete Landmark Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Mile_Post", "TEXT", "", "", "150", "Milepost", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Place_Type", "TEXT", "", "", "50", "Place Type", "NULLABLE", "NON_REQUIRED", "PlaceType")
arcpy.gp.AddField(FeatureClassName, "Placement", "TEXT", "", "", "25", "Placement Method", "NULLABLE", "NON_REQUIRED", "PlacementMethod")
arcpy.gp.AddField(FeatureClassName, "Long", "DOUBLE", "", "", "", "Longitude", "NULLABLE", "NON_REQUIRED", "Longitude")
arcpy.gp.AddField(FeatureClassName, "Lat", "DOUBLE", "", "", "", "Latitude", "NULLABLE", "NON_REQUIRED", "Latitude")
arcpy.gp.AddField(FeatureClassName, "Elev", "SHORT", "", "", "", "Elevation", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PSAPBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "254", "Emergency Service Boundary NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "LawEnforcementBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "254", "Emergency Service Boundary NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "FireBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "254", "Emergency Service Boundary NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "EmergencyMedicalServicesBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ES_NGUID", "TEXT", "", "", "254", "Emergency Service Boundary NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency ID", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "ProvisioningBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "PB_NGUID", "TEXT", "", "", "254", "Provisioning Boundary NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "StreetNameAliasTable"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_NGUID", "TEXT", "", "", "254", "Alias Street Name Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RCL_NGUID", "TEXT", "", "", "254", "Road Centerline NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PreMod", "TEXT", "", "", "15", "Alias Street Name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PreDir", "TEXT", "", "", "9", "Alias Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ASt_PreTyp", "TEXT", "", "", "50", "Alias Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "ASt_PreSep", "TEXT", "", "", "20", "Alias Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "StreetNamePreTypeSeparator")
arcpy.gp.AddField(FeatureClassName, "ASt_Name", "TEXT", "", "", "60", "Alias Street Name", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PosTyp", "TEXT", "", "", "50", "Alias Street Name Post Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "ASt_PosDir", "TEXT", "", "", "9", "Alias Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ASt_PosMod", "TEXT", "", "", "25", "Alias Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ALStPreDir", "TEXT", "", "", "2", "Alias Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ALStName", "TEXT", "", "", "75", "Alias Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ALStTyp", "TEXT", "", "", "4", "Alias Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameType")
arcpy.gp.AddField(FeatureClassName, "ALStPosDir", "TEXT", "", "", "2", "Alias Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "LandmarkNamePartTable"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNP_NGUID", "TEXT", "", "", "254", "Landmark Name Part NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_NGUID", "TEXT", "", "", "254", "Site NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ACLMNNGUID", "TEXT", "", "", "254", "Alias Complete Landmark Name NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNamePart", "TEXT", "", "", "150", "Landmark Name Part", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNP_Order", "SHORT", "", "", "", "Landmark Name Part Order", "NON_NULLABLE", "REQUIRED", "LandmarkNamePartOrder")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "CompleteLandmarkNameAliasTable"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ACLMNNGUID", "TEXT", "", "", "254", "Alias Complete Landmark Name NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_NGUID", "TEXT", "", "", "254", "Site Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ACLandmark", "TEXT", "", "", "150", "Alias Complete Landmark Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "StateOrEquivalentBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel  #This should be provided by the state, not a local jurisdiction.
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "StateNGUID", "TEXT", "", "", "254", "State Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "CountyOrEquivalentBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CntyNGUID", "TEXT", "", "", "254", "County Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NON_NULLABLE", "REQUIRED", "County")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "IncorporatedMunicipalityBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "IncM_NGUID", "TEXT", "", "", "254", "Incorporated Municipality NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "UnincorporatedCommunityBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincNGUID", "TEXT", "", "", "254", "Unincorporated NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "NeighborhoodCommunityBoundary"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdNGUID", "TEXT", "", "", "254", "Neighborhood NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Nbrhd_Comm", "TEXT", "", "", "100", "Neighborhood Community", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "RailroadCenterlines"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RS_NGUID", "TEXT", "", "", "254", "Rail Segment NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RLOwn", "TEXT", "", "", "100", "Rail Line Owner", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RLOp", "TEXT", "", "", "100", "Rail Line Operator", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RLName", "TEXT", "", "", "100", "Rail Line Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RMPL", "FLOAT", "", "", "", "Rail Mile Post Low", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RMPH", "FLOAT", "", "", "", "Rail Mile Post High", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "HydrologyLine"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HS_NGUID", "TEXT", "", "", "254", "Hydrology Segment NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HS_Type", "TEXT", "", "", "100", "Hydrology Segment Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HS_Name", "TEXT", "", "", "100", "Hydrology Segment Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "HydrologyPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_NGUID", "TEXT", "", "", "254", "Hydrology Polygon NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_Type", "TEXT", "", "", "100", "Hydrology Polygon Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_Name", "TEXT", "", "", "100", "Hydrology Polygon Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "CellSectorLocation"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "Cell_NGUID", "TEXT", "", "", "254", "Cell NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_ID", "TEXT", "", "", "10", "Site ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Sector_ID", "TEXT", "", "", "4", "Sector ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Switch_ID", "TEXT", "", "", "10", "Switch ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CMarket_ID", "TEXT", "", "", "10", "Market ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CSite_Name", "TEXT", "", "", "10", "Cell Site ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESRD_ESRK", "LONG", "", "", "", "ESRD or First ESRK", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESRK_Last", "LONG", "", "", "", "Last ESRK", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CSctr_Ornt", "TEXT", "", "", "4", "Sector Orientation", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Technology", "TEXT", "", "", "10", "Technology", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_NGUID", "TEXT", "", "", "254", "Site NENA Globally Unique ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Long", "DOUBLE", "", "", "", "Longitude", "NULLABLE", "NON_REQUIRED", "Longitude")
arcpy.gp.AddField(FeatureClassName, "Lat", "DOUBLE", "", "", "", "Latitude", "NULLABLE", "NON_REQUIRED", "Latitude")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "MileMarkerLocation"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "75", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileMNGUID", "TEXT", "", "", "254", "Mile Post NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Unit", "TEXT", "", "", "15", "Mile Post Unit of Measurement", "NULLABLE", "NON_REQUIRED", "MilePostUnitOfMeasurement")
arcpy.gp.AddField(FeatureClassName, "MileMValue", "FLOAT", "", "", "", "Mile Post Measurement Value", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Rte", "TEXT", "", "", "100", "Mile Post Route Name", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Type", "TEXT", "", "", "15", "Mile Post Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MileM_Ind", "TEXT", "", "", "1", "Mile Post Indicator", "NON_NULLABLE", "REQUIRED", "MilePostIndicator")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
print
#____________________________________________________________________________________________________________________________________________________



#____________________________________________________________________________________________________________________________________________________
# Now that the feature classes and tables have been created, create relationship classes
#____________________________________________________________________________________________________________________________________________________
# First, the Alias Street Name relationship
rcs = GeodatabaseName + "/" + "RoadCenterlines"
sn_alias = GeodatabaseName + "/" + "StreetNameAliasTable"
print ("Creating Relationship Class between:          " + rcs)
print ("and...")
print (sn_alias)
print
relClass = GeodatabaseName + "/" + "RoadCenterline_Has_StreetNameAliases"
forLabel = "StreetNameAliasTable"
backLabel = "RoadCenterlines"
primaryKey = "RCL_NGUID"
foreignKey = "RCL_NGUID"
arcpy.CreateRelationshipClass_management(rcs,
                                         sn_alias,
                                         relClass,
                                         "SIMPLE",
                                         forLabel,
                                         backLabel,
                                         "NONE",
                                         "ONE_TO_MANY",
                                         "NONE",
                                         primaryKey,
                                         foreignKey)

# Next, the Landmark Name Part relationships
# First the relationship between the SiteStructureAddressPoints
ssap = GeodatabaseName + "/" + "SiteStructureAddressPoints"
lmnp_table = GeodatabaseName + "/" + "LandmarkNamePartTable"
print ("Creating Relationship Class between:          " + ssap)
print ("and...")
print (lmnp_table)
print
relClass = GeodatabaseName + "/" + "SiteStructureAddressPoint_Has_LandmarkNameParts"
forLabel = "LandmarkNamePartTable"
backLabel = "SiteStructureAddressPoints"
primaryKey = "Site_NGUID"
foreignKey = "Site_NGUID"
arcpy.CreateRelationshipClass_management(ssap,
                                         lmnp_table,
                                         relClass,
                                         "SIMPLE",
                                         forLabel,
                                         backLabel,
                                         "NONE",
                                         "ONE_TO_MANY",
                                         "NONE",
                                         primaryKey,
                                         foreignKey)

# Next the relationship between the SiteStructureAddressPoints and the CompleteLandmarkNameAliasTable
clmn_table = GeodatabaseName + "/" + "CompleteLandmarkNameAliasTable"
print ("Creating Relationship Class between:          " + ssap)
print ("and...")
print (clmn_table)
print
relClass = GeodatabaseName + "/" + "SiteStructureAddressPoint_Has_CompleteLandmarkNameAliases"
forLabel = "CompleteLandmarkNameAliasTable"
backLabel = "SiteStructureAddressPoints"
primaryKey = "Site_NGUID"
foreignKey = "Site_NGUID"
arcpy.CreateRelationshipClass_management(ssap,
                                         clmn_table,
                                         relClass,
                                         "SIMPLE",
                                         forLabel,
                                         backLabel,
                                         "NONE",
                                         "ONE_TO_MANY",
                                         "NONE",
                                         primaryKey,
                                         foreignKey)

# Lastly the relationship between CompleteLandmarkNameAliasTable and the LandmarkNamePartTable
print ("Creating Relationship Class between:          " + clmn_table)
print ("and...")
print (lmnp_table)
print
relClass = GeodatabaseName + "/" + "CompleteLandmarkNameAlias_Has_LandmarkNameParts"
forLabel = "LandmarkNamePartTable"
backLabel = "CompleteLandmarkNameAliasTable"
primaryKey = "ACLMNNGUID"
foreignKey = "ACLMNNGUID"
arcpy.CreateRelationshipClass_management(clmn_table,
                                         lmnp_table,
                                         relClass,
                                         "SIMPLE",
                                         forLabel,
                                         backLabel,
                                         "NONE",
                                         "ONE_TO_MANY",
                                         "NONE",
                                         primaryKey,
                                         foreignKey)
#____________________________________________________________________________________________________________________________________________________



print
print ("The script is now COMPLETE.")
print (datetime.datetime.now().time())
wait = raw_input('Press <ENTER> to close.')
