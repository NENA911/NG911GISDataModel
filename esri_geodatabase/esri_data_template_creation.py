#____________________________________________________________________________________________________________________________________________________
# Creates a file geodatabase to fit the NENA NG9-1-1 Data Model V2
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
##              11/09/2022 - Added all StreetNamePreTypesAndStreetNamePostTypes added to NENA registry since V1
##                          - Added all StreetNamePreType separators added to NENA registry since V1
##____________________________________________________________________________________________________________________________________________________

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
GeodatabaseName = FolderPath + "\\NG911_GIS_20221021.gdb"
arcpy.gp.CreateFileGDB(FolderPath, "NG911_GIS_20221021", "10.0")
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
domDict = {"N":"North/Nord", "S": "South/Sud", "E": "East/Est", "W": "West", "NE": "Northeast/Nord-Est", "NW": "Northwest", "SE": "Southeast/Sud-Est", "SW": "Southwest", "O": "Ouest", "NO": "Nord-Ouest", "SO": "Sud-Ouest"}
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
domDict = {"North":"North", "South": "South", "East": "East", "West": "West", "Northeast": "Northeast", "Northwest": "Northwest", "Southeast": "Southeast", "Southwest": "Southwest", "Nord":"Nord", "Sud":"Sud", "Est":"Est", "Ouest":"Ouest", "Nord-Est":"Nord-Est", "Nord-Ouest":"Nord-Ouest", "Sud-Est":"Sud-Est", "Sud-Ouest":"Sud-Ouest"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "StreetNameDirectional", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "StreetNameDirectional", "CODE", "ASCENDING")
domDict = {}
# This domain applies both for the primary street name directionals (pre/post) and the alias street name directionals.

print ("Creating Domain StreetNameType...")
arcpy.CreateDomain_management(GeodatabaseName, "StreetNameType", "A word or phrase that precedes or follows the Street Name element and identifies a type of thoroughfare in a complete street name.", "TEXT", "CODED")
domDict = {"Abbey":"Abbey","Access Road":"Access Road","Acres":"Acres","Airport":"Airport","Alcove":"Alcove","Alle":"Alle","Alley":"Alley","Annex":"Annex","Approach":"Approach","Arc":"Arc","Arcade":"Arcade","Arch":"Arch","Avenida":"Avenida","Avenue":"Avenue","Avenue Circle":"Avenue Circle","Avenue Court":"Avenue Court","Avenue Loop":"Avenue Loop","Avenue Path":"Avenue Path","Avenue Place":"Avenue Place","Avenue Way":"Avenue Way","Bank":"Bank","Bay":"Bay","Bayou":"Bayou","Bayway":"Bayway","Beach":"Beach","Bend":"Bend","Bluff":"Bluff","Bluffs":"Bluffs","Bottom":"Bottom","Boardwalk":"Boardwalk","Boulevard":"Boulevard","Branch":"Branch","Bridge":"Bridge","Brook":"Brook","Brooks":"Brooks","Bureau of Indian Affairs Route":"Bureau of Indian Affairs Route","Burg":"Burg","Burgs":"Burgs","Bypass":"Bypass","Calle":"Calle","Camino":"Camino","Camp":"Camp","Canyon":"Canyon","Cape":"Cape","Cartway":"Cartway","Causeway":"Causeway","Center":"Center","Centers":"Centers","Centre":"Centre","Channel":"Channel","Chase":"Chase","Chemin":"Chemin","Circle":"Circle","Circles":"Circles","Circus":"Circus","Cliff":"Cliff","Cliffs":"Cliffs","Close":"Close","Club":"Club","Cluster":"Cluster","Coast Highway":"Coast Highway","Common":"Common","Commons":"Commons","Concourse":"Concourse","Connect":"Connect","Connector":"Connector","Corner":"Corner","Corners":"Corners","Corridor":"Corridor","Corso":"Corso","Corte":"Corte","County Forest Road":"County Forest Road","County Highway":"County Highway","County Road":"County Road","County Route":"County Route","County State Aid Highway":"County State Aid Highway","Cours":"Cours","Course":"Course","Court":"Court","Courts":"Courts","Cove":"Cove","Coves":"Coves","Creek":"Creek","Crescent":"Crescent","Crest":"Crest","Cross":"Cross","Crossing":"Crossing","Crossings":"Crossings","Crossover":"Crossover","Crossroad":"Crossroad","Crossroads":"Crossroads","Crossway":"Crossway","Curve":"Curve","Custer County Road":"Custer County Road","Cutoff":"Cutoff","Cutting":"Cutting","Dale":"Dale","Dam":"Dam","Dawson County Road":"Dawson County Road","Dell":"Dell","Divide":"Divide","Dock":"Dock","Down":"Down","Downs":"Downs","Draw":"Draw","Drift":"Drift","Drive":"Drive","Drives":"Drives","Driveway":"Driveway","Echo":"Echo","Edge":"Edge","End":"End","Entrance":"Entrance","Entry":"Entry","Esplanade":"Esplanade","Estate":"Estate","Estates":"Estates","Exchange":"Exchange","Exit":"Exit","Expressway":"Expressway","Extension":"Extension","Extensions":"Extensions","Fall":"Fall","Falls":"Falls","Fare":"Fare","Farm":"Farm","Farm to Market":"Farm to Market","Federal-Aid Secondary Highway":"Federal-Aid Secondary Highway","Ferry":"Ferry","Field":"Field","Fields":"Fields","Flat":"Flat","Flats":"Flats","Flowage":"Flowage","Flyway":"Flyway","Ford":"Ford","Fords":"Fords","Forest":"Forest","Forest Highway":"Forest Highway","Forest Road":"Forest Road","Forge":"Forge","Forges":"Forges","Fork":"Fork","Forks":"Forks","Fort":"Fort","Freeway":"Freeway","Front":"Front","Frontage Road":"Frontage Road","Gables":"Gables","Garden":"Garden","Gardens":"Gardens","Garth":"Garth","Gate":"Gate","Gates":"Gates","Gateway":"Gateway","Glade":"Glade","Glen":"Glen","Glens":"Glens","Gorge":"Gorge","Grade":"Grade","Green":"Green","Greens":"Greens","Greenway":"Greenway","Grove":"Grove","Groves":"Groves","Harbor":"Harbor","Harbors":"Harbors","Harbour":"Harbour","Haul Road":"Haul Road","Haven":"Haven","Heath":"Heath","Heights":"Heights","Highway":"Highway","Hill":"Hill","Hills":"Hills","Hollow":"Hollow","Horn":"Horn","Horseshoe":"Horseshoe","Indian Service Road":"Indian Service Road","Inlet":"Inlet","Interstate":"Interstate","Interval":"Interval","Island":"Island","Islands":"Islands","Isle":"Isle","Isles":"Isles","J-Turn":"J-Turn","Junction":"Junction","Junctions":"Junctions","Keep":"Keep","Key":"Key","Keys":"Keys","Knoll":"Knoll","Knolls":"Knolls","Lair":"Lair","Lake":"Lake","Lakes":"Lakes","Land":"Land","Landing":"Landing","Lane":"Lane","Lane Circle":"Lane Circle","Lane Court":"Lane Court","Lane Road":"Lane Road","Lateral":"Lateral","Ledge":"Ledge","Light":"Light","Lights":"Lights","Line":"Line","Loaf":"Loaf","Lock":"Lock","Locks":"Locks","Lodge":"Lodge","Lookout":"Lookout","Loop":"Loop","Loop Road":"Loop Road","Mall":"Mall","Manor":"Manor","Manors":"Manors","Market":"Market","Meadow":"Meadow","Meadows":"Meadows","Mews":"Mews","Mill":"Mill","Mills":"Mills","Mission":"Mission","Montana Highway":"Montana Highway","Motorway":"Motorway","Mount":"Mount","Mountain":"Mountain","Mountains":"Mountains","Narrows":"Narrows","National Forest Development Road":"National Forest Development Road","Neck":"Neck","Nook":"Nook","North Carolina Highway":"North Carolina Highway","Old County Road":"Old County Road","Orchard":"Orchard","Oval":"Oval","Overlook":"Overlook","Overpass":"Overpass","Park":"Park","Parke":"Parke","Parks":"Parks","Parkway":"Parkway","Parkways":"Parkways","Paseo":"Paseo","Pass":"Pass","Passage":"Passage","Path":"Path","Pathway":"Pathway","Piazza":"Piazza","Pike":"Pike","Pine":"Pine","Pines":"Pines","Place":"Place","Plain":"Plain","Plains":"Plains","Platz":"Platz","Plaza":"Plaza","Point":"Point","Pointe":"Pointe","Points":"Points","Port":"Port","Ports":"Ports","Prairie":"Prairie","Private Road":"Private Road","Promenade":"Promenade","Quarter":"Quarter","Quay":"Quay","Ramp":"Ramp","Radial":"Radial","Ranch":"Ranch","Rapid":"Rapid","Rapids":"Rapids","Reach":"Reach","Recreational Road":"Recreational Road","Rest":"Rest","Retreat":"Retreat","Ridge":"Ridge","Ridges":"Ridges","Rise":"Rise","River":"River","River Road":"River Road","Road":"Road","Roads":"Roads","Round":"Round","Route":"Route","Row":"Row","Rue":"Rue","Run":"Run","Runway":"Runway","Shoal":"Shoal","Shoals":"Shoals","Shore":"Shore","Shores":"Shores","Skies":"Skies","Skyway":"Skyway","Slip":"Slip","Spring":"Spring","Springs":"Springs","Spur":"Spur","Spurs":"Spurs","Square":"Square","Squares":"Squares","State Highway":"State Highway","State Park Road":"State Park Road","State Parkway":"State Parkway","State Road":"State Road","State Route":"State Route","State Secondary":"State Secondary","State Spur":"State Spur","Station":"Station","Strand":"Strand","Strasse":"Strasse","Stravenue":"Stravenue","Stream":"Stream","Street":"Street","Streets":"Streets","Street Circle":"Street Circle","Street Court":"Street Court","Street Loop":"Street Loop","Street Path":"Street Path","Street Place":"Street Place","Street Way":"Street Way","Strip":"Strip","Summit":"Summit","Taxiway":"Taxiway","Terminal":"Terminal","Tern":"Tern","Terrace":"Terrace","Throughway":"Throughway","Thruway":"Thruway","Timber Road":"Timber Road","Township Road":"Township Road","Trace":"Trace","Track":"Track","Trafficway":"Trafficway","Trail":"Trail","Trailer":"Trailer","Triangle":"Triangle","Truck Trail":"Truck Trail","Tunnel":"Tunnel","Turn":"Turn","Turnpike":"Turnpike","United States Forest Service Road":"United States Forest Service Road","United States Highway":"United States Highway","Underpass":"Underpass","Union":"Union","Unions":"Unions","Valley":"Valley","Valleys":"Valleys","Via":"Via","Viaduct":"Viaduct","View":"View","Views":"Views","Villa":"Villa","Village":"Village","Villages":"Villages","Ville":"Ville","Vista":"Vista","Waddy":"Waddy","Walk":"Walk","Walks":"Walks","Wall":"Wall","Way":"Way","Ways":"Ways","Weeg":"Weeg","Well":"Well","Wells":"Wells","Woods":"Woods","Wye":"Wye","Wynd":"Wynd"}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "StreetNameType", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "StreetNameType", "CODE", "ASCENDING")
domDict = {}
# This domain applies both for the primary street name types (pre/post) and the alias street name types.
# As NENA updates the StreetNamePreTypesAndStreetNamePostTypes registry the values in this domain will also need to be updated.

print ("Creating Domain StreetNamePreTypeSeparator...")
arcpy.CreateDomain_management(GeodatabaseName, "StreetNamePreTypeSeparator", "A preposition or prepositional phrase between the Street Name Pre Type and the Street Name.", "TEXT", "CODED")
domDict = {"of the":"of the", "at":"at", "de":"de", "de la":"de la", "del":"del", "de las":"de las", "des":"des", "in the":"in the", "to the":"to the", "of":"of", "on the":"on the", "to":"to"}
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
domDict = {"Primary":"Primary roads are generally divided, limited-access highways within the interstate highway system or under state management, and are distinguished by the presence of interchanges.", "Secondary":"Secondary roads are main arteries, usually in the US Highway, State Highway, or County Highway system.", "Local":"Local roads are generally a paved non-arterial street, road, or byway that usually has a single lane of traffic in each direction.", "Ramp":"Ramp designates a road that allows controlled access from adjacent roads onto a limited access highway, often in the form of a cloverleaf interchange.", "Service Drive":"Service Drive provides access to structures along the highway, usually parallel to a limited access highway.","Vehicular Trail":"Vehicular Trail (4WD, snowmobile) is an unpaved trail or path where a four-wheel-drive vehicle, snowmobile, or similar vehicle is required.", "Walkway/Pedestrian Trail":"Walkway/Pedestrian Trail is a path that is used for walking, being either too narrow for or legally restricted from vehicular traffic.", "Stairway":"Stairway is a pedestrian passageway from one level to another by a series of steps.", "Alley":"Alley is generally a service road that does not generally have associated addressed structures and is usually unnamed.", "Private":"Private (service vehicles, logging, oil fields, ranches, etc.) is a road within private property that is privately maintained for service, extractive, or other purposes.", "Parking Lot":"Parking Lot is the main travel route for vehicles through a paved parking area.", "Bike Path or Trail":"Bike Path or Trail is a path that is used for manual or small, motorized bicycles, being either too narrow for or legally restricted from vehicular traffic.", "Bridle Path":"Bridle Path is a path that is used for horses, being either too narrow for or legally restricted from vehicular traffic.", "Other":"Other is any road or path type that does not fit into the above categories."}
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GeodatabaseName, "RoadClass", code, domDict[code])
arcpy.SortCodedValueDomain_management(GeodatabaseName, "RoadClass", "CODE", "ASCENDING")
domDict = {}

print ("Creating Domain ServiceURI...")
arcpy.CreateDomain_management(GeodatabaseName, "ServiceURI", "URI for routing.  This attribute is contained in the Emergency Service Boundary layer and will define the Service URI of the service.", "TEXT", "CODED")

print ("Creating Domain ServiceURN...")
arcpy.CreateDomain_management(GeodatabaseName, "ServiceURN", "The URN used to select the service for which a route is desired.", "TEXT", "CODED")
domDict = {"urn:service:sos":"The generic 'sos' service reaches a public safety answering point (PSAP), which in turn dispatches aid appropriate to the emergency.","urn:service:sos.ambulance":"This service identifier reaches an ambulance service that provides emergency medical assistance and transportation.","urn:service:sos.animal-control":"Animal control typically enforces laws and ordinances pertaining to animal control and management, investigates cases of animal abuse, educates the community in responsible pet ownership and wildlife care, and provides for the housing and care of homeless animals, among other animal-related services.","urn:service:sos.fire":"The 'fire' service identifier summons the fire service, also known as the fire brigade or fire department.","urn:service:sos.gas":"The 'gas' service allows the reporting of natural gas (and other flammable gas) leaks or other natural gas emergencies.","urn:service:sos.marine":"The 'marine' service refers to maritime search and rescue services such as those offered by the coast guard, lifeboat, or surf lifesavers.","urn:service:sos.mountain":"The 'mountain' service refers to mountain rescue services (i.e., search and rescue activities that occur in a mountainous environment), although the term is sometimes also used to apply to search and rescue in other wilderness environments.","urn:service:sos.physician":"The 'physician' emergency service connects the caller to a physician referral service.","urn:service:sos.poison":"The 'poison' service refers to special information centers set up to inform citizens about how to respond to potential poisoning.","urn:service:sos.police":"The 'police' service refers to the police department or other law enforcement authorities.","urn:service:counseling.children":"The 'children' service refers to counseling and support services that are specifically tailored to the needs of children.  Such services may, for example, provide advice to run-aways or victims of child abuse.","urn:service:counseling.mental-health":"The 'mental-health' service refers to the \"diagnostic, treatment, and preventive care that helps improve how persons with mental illness feel both physically and emotionally as well as how they interact with other persons\". (U.S. Department of Health and Human Services)","urn:service:counseling.suicide":"The 'suicide' service refers to the suicide prevention hotline.","urn:emergency:service:sos.psap":"Route calls to primary PSAP.","urn:emergency:service:sos.level_2_esrp":"Route calls to a second level ESRP (for an example, a state ESRP routing towards a county ESRP).","urn:emergency:service:sos.level_3_esrp":"Route calls to a third level ESRP (for example, a regional ESRP that received a call from a state ESRP and in turn routes towards a county ESRP).","urn:emergency:service:sos.call_taker":"Route calls to a call taker within a PSAP.","urn:emergency:service:test.psap":"Route test calls to primary PSAP.","urn:emergency:service:test.level_2_esrp":"Route test calls to a second level ESRP (for an example, a state ESRP routing towards a county ESRP).","urn:emergency:service:test.level_3_esrp":"Route test calls to a third level ESRP (for example, a regional ESRP that received a call from a state ESRP and in turn routes towards a county ESRP).","urn:emergency:service:test.call_taker":"Normally not used, but some implementations may make use of this urn.","urn:emergency:service:responder.police":"Police Agency","urn:emergency:service:responder.fire":"Fire Department","urn:emergency:service:responder.ems":"Emergency Medical Service","urn:emergency:service:responder.poison_control":"Poison Control Center","urn:emergency:service:responder.mountain_rescue":"Mountain Rescue Service","urn:emergency:service:responder.coast_guard":"Coast Guard Station","urn:emergency:service:responder.psap":"Other purposes beyond use for dispatch via ECRF","urn:emergency:service:responder.police.federal":"An appropriate federal agency.","urn:emergency:service:responder.police.stateProvincial":"State or provincial police office","urn:emergency:service:responder.police.tribal":"Native American police (reservation)","urn:emergency:service:responder.police.countyParish":"County or Parish police (not Sheriff)","urn:emergency:service:responder.police.sheriff":"Sheriff's office, when both a police and Sheriff dispatch may be possible","urn:emergency:service:responder.police.local":"City, Town, Township, Borough or Village police","urn:emergency:service:responder.federal.fbi":"Federal Bureau of Investigation","urn:emergency:service:responder.federal.rcmp":"Royal Canadian Mounted Police","urn:emergency:service:responder.federal.usss":"U.S. Secret Service","urn:emergency:service:responder.federal.dea":"Drug Enforcement Agency","urn:emergency:service:responder.federal.marshal":"Marshals Service","urn:emergency:service:responder.federal.cbp":"Customs and Border Protection","urn:emergency:service:responder.federal.ice":"Immigration and Customs Enforcement","urn:emergency:service:responder.federal.atf":"Bureau of Alcohol, Tobacco, Fire Arms and Explosives","urn:emergency:service:responder.federal.pp":"U.S. Park Police","urn:emergency:service:responder.federal.dss":"Diplomatic Security Service","urn:emergency:service:responder.federal.fps":"Federal Protective Service","urn:emergency:service:responder.federal.military":"Used for military installations","urn:emergency:service:responder.fire.forest":"Forest Fire Service","urn:emergency:service:responder.fire.airport":"Airport Fire Service","urn:emergency:service:responder.fire.military":"Used for military installations","urn:emergency:service:responder.fire.private":"Private Fire Service","urn:emergency:service:responder.ems.tribal":"Native American EMS (reservation)","urn:emergency:service:responder.ems.countyParish":"County or Parish EMS","urn:emergency:service:responder.ems.local":"City, Town, Township, Borough or Village EMS","urn:emergency:service:responder.ems.private":"Contracted Ambulance Service","urn:emergency:service:responder.ems.military":"Used for military installations","urn:emergency:service:serviceAgencyLocator":"Return a URI to a Service or Agency","urn:emergency:service:serviceagencyLocator.ADR":"Additional Data Repository (if hosted on an ESInet)","urn:emergency:service:serviceagencyLocator.Bridge":"Bridge","urn:emergency:service:serviceagencyLocator.BCF":"Border Control Function","urn:emergency:service:serviceagencyLocator.ECRF":"Emergency Call Routing Function","urn:emergency:service:serviceagencyLocator.ESRP":"Emergency Service Routing Proxy","urn:emergency:service:serviceagencyLocator.GCS":"Geocode Conversion Service","urn:emergency:service:serviceagencyLocator.IMR":"Interactive Media Response Service","urn:emergency:service:serviceagencyLocator.Logging":"Logging Service","urn:emergency:service:serviceagencyLocator.LVF":"Location Validation Function","urn:emergency:service:serviceagencyLocator.MCS":"MSAG Conversion Service","urn:emergency:service:serviceagencyLocator.MDS":"Mapping Data Service","urn:emergency:service:serviceagencyLocator.PolicyStore":"Policy Store","urn:emergency:service:serviceagencyLocator.PSAP":"PSAP","urn:emergency:service:serviceagencyLocator.SAL":"Service/Agency Locator","urn:emergency:service:additionalData":"Return a URI to an Additional Data structure as defined in NENA-STA-012.2."}
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

FeatureClassLabel = "RoadCenterLine"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AdNumPre_L", "TEXT", "", "", "15", "Left Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AdNumPre_R", "TEXT", "", "", "15", "Right Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "FromAddr_L", "LONG", "", "", "", "Left FROM Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "ToAddr_L", "LONG", "", "", "", "Left TO Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "FromAddr_R", "LONG", "", "", "", "Right FROM Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "ToAddr_R", "LONG", "", "", "", "Right TO Address", "NON_NULLABLE", "REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "Parity_L", "TEXT", "", "", "1", "Parity Left", "NON_NULLABLE", "REQUIRED", "Parity")
arcpy.gp.AddField(FeatureClassName, "Parity_R", "TEXT", "", "", "1", "Parity Right", "NON_NULLABLE", "REQUIRED", "Parity")
arcpy.gp.AddField(FeatureClassName, "St_PreMod", "TEXT", "", "", "15", "Street Name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreDir", "TEXT", "", "", "10", "Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PreTyp", "TEXT", "", "", "50", "Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PreSep", "TEXT", "", "", "20", "Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "StreetNamePreTypeSeparator")
arcpy.gp.AddField(FeatureClassName, "St_Name", "TEXT", "", "", "254", "Street Name", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosTyp", "TEXT", "", "", "50", "Street Name Post Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PosDir", "TEXT", "", "", "10", "Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PosMod", "TEXT", "", "", "25", "Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_PreDir", "TEXT", "", "", "2", "Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "LSt_Name", "TEXT", "", "", "75", "Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Typ", "TEXT", "", "", "4", "Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameType")
arcpy.gp.AddField(FeatureClassName, "LSt_PosDir", "TEXT", "", "", "2", "Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ESN_L", "TEXT", "", "", "5", "ESN Left", "NULLABLE", "NON_REQUIRED", "ESN")
arcpy.gp.AddField(FeatureClassName, "ESN_R", "TEXT", "", "", "5", "ESN Right", "NULLABLE", "NON_REQUIRED", "ESN")
arcpy.gp.AddField(FeatureClassName, "MSAGComm_L", "TEXT", "", "", "30", "MSAG Community Name Left", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "MSAGComm_R", "TEXT", "", "", "30", "MSAG Community Name Right", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country_L", "TEXT", "", "", "2", "Country Left", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "Country_R", "TEXT", "", "", "2", "Country Right", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State_L", "TEXT", "", "", "2", "State or Equivalent Left (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "State_R", "TEXT", "", "", "2", "State or Equivalent Right (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County_L", "TEXT", "", "", "100", "County or Equivalent Left (A2)", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "County_R", "TEXT", "", "", "100", "County or Equivalent Right (A2)", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode_L", "TEXT", "", "", "6", "Additional Code Left", "NULLABLE", "NON_REQUIRED", "AdditionalCode")
arcpy.gp.AddField(FeatureClassName, "AddCode_R", "TEXT", "", "", "6", "Additional Code Right", "NULLABLE", "NON_REQUIRED", "AdditionalCode")
arcpy.gp.AddField(FeatureClassName, "IncMuni_L", "TEXT", "", "", "100", "Incorporated Municipality Left (A3)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "IncMuni_R", "TEXT", "", "", "100", "Incorporated Municipality Right (A3)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincCom_L", "TEXT", "", "", "100", "Unincorporated Community Left (A4)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "UnincCom_R", "TEXT", "", "", "100", "Unincorporated Community Right (A4)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdCom_L", "TEXT", "", "", "100", "Neighborhood Community Left (A5)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NbrhdCom_R", "TEXT", "", "", "100", "Neighborhood Community Right (A5)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "PostCode_L", "TEXT", "", "", "7", "Postal Code Left", "NULLABLE", "NON_REQUIRED", "PostalCode")
arcpy.gp.AddField(FeatureClassName, "PostCode_R", "TEXT", "", "", "7", "Postal Code Right", "NULLABLE", "NON_REQUIRED", "PostalCode")
arcpy.gp.AddField(FeatureClassName, "PostComm_L", "TEXT", "", "", "40", "Postal Community Name Left", "NULLABLE", "NON_REQUIRED", "PostalCommunityName")
arcpy.gp.AddField(FeatureClassName, "PostComm_R", "TEXT", "", "", "40", "Postal Community Name Right", "NULLABLE", "NON_REQUIRED", "PostalCommunityName")
arcpy.gp.AddField(FeatureClassName, "RoadClass", "TEXT", "", "", "24", "Road Class", "NULLABLE", "NON_REQUIRED", "RoadClass")
arcpy.gp.AddField(FeatureClassName, "OneWay", "TEXT", "", "", "2", "One-Way", "NULLABLE", "NON_REQUIRED", "OneWay")
arcpy.gp.AddField(FeatureClassName, "SpeedLimit", "SHORT", "", "", "", "Speed Limit", "NULLABLE", "NON_REQUIRED", "SpeedLimit")
arcpy.gp.AddField(FeatureClassName, "Valid_L", "TEXT", "", "", "1", "Validation Left", "NULLABLE", "NON_REQUIRED", "Validation")
arcpy.gp.AddField(FeatureClassName, "Valid_R", "TEXT", "", "", "1", "Validation Right", "NULLABLE", "NON_REQUIRED", "Validation")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "SiteStructureAddressPoint"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "100", "County or Equivalent (A2)", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "AdditionalCode")
arcpy.gp.AddField(FeatureClassName, "AddDataURI", "TEXT", "", "", "254", "Additional Data URI", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality (A3)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community (A4)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Nbrhd_Comm", "TEXT", "", "", "100", "Neighborhood Community (A5)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AddNum_Pre", "TEXT", "", "", "15", "Address Number Prefix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Add_Number", "LONG", "", "", "", "Address Number", "NULLABLE", "NON_REQUIRED", "AddressNumber")
arcpy.gp.AddField(FeatureClassName, "AddNum_Suf", "TEXT", "", "", "15", "Address Number Suffix", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreMod", "TEXT", "", "", "15", "Street Name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PreDir", "TEXT", "", "", "10", "Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PreTyp", "TEXT", "", "", "50", "Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PreSep", "TEXT", "", "", "20", "Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "StreetNamePreTypeSeparator")
arcpy.gp.AddField(FeatureClassName, "St_Name", "TEXT", "", "", "254", "Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "St_PosTyp", "TEXT", "", "", "50", "Street Name Post Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "St_PosDir", "TEXT", "", "", "10", "Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "St_PosMod", "TEXT", "", "", "25", "Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_PreDir", "TEXT", "", "", "2", "Legacy Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "LSt_Name", "TEXT", "", "", "75", "Legacy Street Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LSt_Typ", "TEXT", "", "", "4", "Legacy Street Name Type", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameType")
arcpy.gp.AddField(FeatureClassName, "LSt_PosDir", "TEXT", "", "", "2", "Legacy Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "LegacyStreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ESN", "TEXT", "", "", "5", "ESN", "NULLABLE", "NON_REQUIRED", "ESN")
arcpy.gp.AddField(FeatureClassName, "MSAGComm", "TEXT", "", "", "30", "MSAG Community Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Post_Comm", "TEXT", "", "", "40", "Postal Community Name", "NULLABLE", "NON_REQUIRED", "PostalCommunityName")
arcpy.gp.AddField(FeatureClassName, "Post_Code", "TEXT", "", "", "7", "Postal Code", "NULLABLE", "NON_REQUIRED", "PostalCode")
arcpy.gp.AddField(FeatureClassName, "PostCodeEx", "TEXT", "", "", "4", "Postal Code Extension", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Building", "TEXT", "", "", "75", "Building", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Floor", "TEXT", "", "", "75", "Floor", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Unit", "TEXT", "", "", "75", "Unit", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Room", "TEXT", "", "", "75", "Room", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Seat", "TEXT", "", "", "75", "Seat", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Addtl_Loc", "TEXT", "", "", "225", "Additional Location Information", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LandmkName", "TEXT", "", "", "150", "Complete Landmark Name", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Milepost", "TEXT", "", "", "150", "Milepost", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Place_Type", "TEXT", "", "", "50", "Place Type", "NULLABLE", "NON_REQUIRED", "PlaceType")
arcpy.gp.AddField(FeatureClassName, "Placement", "TEXT", "", "", "25", "Placement Method", "NULLABLE", "NON_REQUIRED", "PlacementMethod")
arcpy.gp.AddField(FeatureClassName, "Longitude", "DOUBLE", "", "", "", "Longitude", "NULLABLE", "NON_REQUIRED", "Longitude")
arcpy.gp.AddField(FeatureClassName, "Latitude", "DOUBLE", "", "", "", "Latitude", "NULLABLE", "NON_REQUIRED", "Latitude")
arcpy.gp.AddField(FeatureClassName, "Elevation", "SHORT", "", "", "", "Elevation", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PsapPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PolicePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "FirePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "FireForestPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "FireAirportPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "FireMilitaryPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "FirePrivatePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "EmsPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "EmsPrivatePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "EmsAirPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "EmsMilitaryPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoisonControlPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "MountainRescuePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "CoastGuardPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceCountyPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceStateProvincialPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalFbiPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalRcmpPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalSecretServicePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalDeaPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalMarshalPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalCustomsBorderProtectionPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalImmigrationCustomsPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalAtfPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalParkPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalDiplomaticSecurityPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceFederalProtectiveServicePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceSheriffPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceMilitaryPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceCampusPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PolicePrivatePolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceAirportPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceHousingPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "PoliceParkPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NULLABLE", "NON_REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NULLABLE", "NON_REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "Agency_ID", "TEXT", "", "", "100", "Agency Identifier", "NON_NULLABLE", "REQUIRED", "AgencyID")
arcpy.gp.AddField(FeatureClassName, "ServiceURI", "TEXT", "", "", "254", "Service URI", "NON_NULLABLE", "REQUIRED", "ServiceURI")
arcpy.gp.AddField(FeatureClassName, "ServiceURN", "TEXT", "", "", "50", "Service URN", "NON_NULLABLE", "REQUIRED", "ServiceURN")
arcpy.gp.AddField(FeatureClassName, "ServiceNum", "TEXT", "", "", "15", "Service Number", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "AVcard_URI", "TEXT", "", "", "254", "Agency vCard URI", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DsplayName", "TEXT", "", "", "60", "Display Name", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "ProvisioningPolygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "StreetNameAliasTable"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID (Primary Key)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "RCL_NGUID", "TEXT", "", "", "254", "Road Centerline NENA Globally Unique ID (Foreign Key)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PreMod", "TEXT", "", "", "15", "Alias Street Name Pre Modifier", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PreDir", "TEXT", "", "", "10", "Alias Street Name Pre Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ASt_PreTyp", "TEXT", "", "", "50", "Alias Street Name Pre Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "ASt_PreSep", "TEXT", "", "", "20", "Alias Street Name Pre Type Separator", "NULLABLE", "NON_REQUIRED", "StreetNamePreTypeSeparator")
arcpy.gp.AddField(FeatureClassName, "ASt_Name", "TEXT", "", "", "254", "Alias Street Name", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ASt_PosTyp", "TEXT", "", "", "50", "Alias Street Name Post Type", "NULLABLE", "NON_REQUIRED", "StreetNameType")
arcpy.gp.AddField(FeatureClassName, "ASt_PosDir", "TEXT", "", "", "10", "Alias Street Name Post Directional", "NULLABLE", "NON_REQUIRED", "StreetNameDirectional")
arcpy.gp.AddField(FeatureClassName, "ASt_PosMod", "TEXT", "", "", "25", "Alias Street Name Post Modifier", "NULLABLE", "NON_REQUIRED", "")
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
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID (Primary Key)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "SSAP_NGUID", "TEXT", "", "", "254", "Site NENA Globally Unique ID (Foreign Key)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CLNA_NGUID", "TEXT", "", "", "254", "Complete Landmark Name Alias NENA Globally Unique ID (Foreign Key)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNamePart", "TEXT", "", "", "150", "Landmark Name Part", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LMNP_Order", "SHORT", "", "", "", "Landmark Name Part Order", "NON_NULLABLE", "REQUIRED", "LandmarkNamePartOrder")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "LandmarkNameCompleteAliasTable"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateTable_management(GeodatabaseName, FeatureClassLabel, "", "")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID (Primary Key)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "SSAP_NGUID", "TEXT", "", "", "254", "Site NENA Globally Unique ID (Foreign Key)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CLNAlias", "TEXT", "", "", "150", "Complete Landmark Name Alias", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "A1Polygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel  #This should be provided by the state, not a local jurisdiction.
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NON_NULLABLE", "REQUIRED", "State")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "A2Polygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "100", "County or Equivalent (A2)", "NON_NULLABLE", "REQUIRED", "County")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "A3Polygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "100", "County or Equivalent (A2)", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality (A3)", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "A4Polygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "100", "County or Equivalent (A2)", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality (A3)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community (A4)", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "A5Polygon"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYGON", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Effective", "DATE", "", "", "", "Effective Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Expire", "DATE", "", "", "", "Expiration Date", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "100", "County or Equivalent (A2)", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "AddCode", "TEXT", "", "", "6", "Additional Code", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Inc_Muni", "TEXT", "", "", "100", "Incorporated Municipality (A3)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Uninc_Comm", "TEXT", "", "", "100", "Unincorporated Community (A4)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Nbrhd_Comm", "TEXT", "", "", "100", "Neighborhood Community (A5)", "NON_NULLABLE", "REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "RailroadCenterLine"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POLYLINE", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
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
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
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
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_Type", "TEXT", "", "", "100", "Hydrology Polygon Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "HP_Name", "TEXT", "", "", "100", "Hydrology Polygon Name", "NULLABLE", "NON_REQUIRED", "")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "CellSectorPoint"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Country", "TEXT", "", "", "2", "Country", "NON_NULLABLE", "REQUIRED", "Country")
arcpy.gp.AddField(FeatureClassName, "State", "TEXT", "", "", "2", "State or Equivalent (A1)", "NON_NULLABLE", "REQUIRED", "State")
arcpy.gp.AddField(FeatureClassName, "County", "TEXT", "", "", "75", "County or Equivalent (A2)", "NON_NULLABLE", "REQUIRED", "County")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID (Primary Key)", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Site_ID", "TEXT", "", "", "10", "Site ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Sector_ID", "TEXT", "", "", "4", "Sector ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Switch_ID", "TEXT", "", "", "10", "Switch ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CMarket_ID", "TEXT", "", "", "10", "Market ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CSite_Name", "TEXT", "", "", "10", "Cell Site ID", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESRD_ESRK", "LONG", "", "", "", "ESRD or First ESRK", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "ESRK_Last", "LONG", "", "", "", "Last ESRK", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "CSctr_Ornt", "TEXT", "", "", "4", "Sector Orientation", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Technology", "TEXT", "", "", "10", "Technology", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "SSAP_NGUID", "TEXT", "", "", "254", "Site NENA Globally Unique ID (Foreign Key)", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "Longitude", "DOUBLE", "", "", "", "Longitude", "NULLABLE", "NON_REQUIRED", "Longitude")
arcpy.gp.AddField(FeatureClassName, "Latitude", "DOUBLE", "", "", "", "Latitude", "NULLABLE", "NON_REQUIRED", "Latitude")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
#____________________________________________________________________________________________________________________________________________________
FeatureClassLabel = "LocationMarkerPoint"
FeatureClassName = GeodatabaseName + "\\" + FeatureClassLabel
arcpy.CreateFeatureclass_management(GeodatabaseName, FeatureClassLabel, "POINT", "", "DISABLED", "DISABLED", "GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119522E-09;0.001;0.001;IsHighPrecision", "", "0", "0", "0")
print
print ("Created Feature Class:          " + FeatureClassName)
print ("Adding Fields to Feature Class: " + FeatureClassName)
arcpy.gp.AddField(FeatureClassName, "DiscrpAgID", "TEXT", "", "", "100", "Discrepancy Agency ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "DateUpdate", "DATE", "", "", "", "Date Updated", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "NGUID", "TEXT", "", "", "254", "NENA Globally Unique ID", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LM_Unit", "TEXT", "", "", "15", "Location Marker Unit of Measurement", "NULLABLE", "NON_REQUIRED", "MilePostUnitOfMeasurement")
arcpy.gp.AddField(FeatureClassName, "LM_Value", "FLOAT", "", "", "", "Location Marker Measurement Value", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LM_Rte", "TEXT", "", "", "100", "Location Marker Route Name", "NON_NULLABLE", "REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LM_Label", "TEXT", "", "", "100", "Location Marker Label", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LM_Type", "TEXT", "", "", "15", "Location Marker Type", "NULLABLE", "NON_REQUIRED", "")
arcpy.gp.AddField(FeatureClassName, "LM_Ind", "TEXT", "", "", "1", "Location Marker Indicator", "NON_NULLABLE", "REQUIRED", "MilePostIndicator")
#arcpy.ImportMetadata_conversion(MetadataPath + FeatureClassLabel + ".xml", "FROM_ISO_19139", FeatureClassName, "ENABLED")
# Enable Editor Tracking in UTC.
arcpy.EnableEditorTracking_management(FeatureClassName, "", "", "", "DateUpdate", "NO_ADD_FIELDS", "UTC")
print
#____________________________________________________________________________________________________________________________________________________



#____________________________________________________________________________________________________________________________________________________
# Now that the feature classes and tables have been created, create relationship classes
#____________________________________________________________________________________________________________________________________________________
# First, the Alias Street Name relationship
rcs = GeodatabaseName + "/" + "RoadCenterLine"
sn_alias = GeodatabaseName + "/" + "StreetNameAliasTable"
print ("Creating Relationship Class between:          " + rcs)
print ("and...")
print (sn_alias)
print
relClass = GeodatabaseName + "/" + "RoadCenterline_Has_StreetNameAliases"
forLabel = "StreetNameAliasTable"
backLabel = "RoadCenterLine"
primaryKey = "NGUID"
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
# First the relationship between the SiteStructureAddressPoint
ssap = GeodatabaseName + "/" + "SiteStructureAddressPoint"
lmnp_table = GeodatabaseName + "/" + "LandmarkNamePartTable"
print ("Creating Relationship Class between:          " + ssap)
print ("and...")
print (lmnp_table)
print
relClass = GeodatabaseName + "/" + "SiteStructureAddressPoint_Has_LandmarkNameParts"
forLabel = "LandmarkNamePartTable"
backLabel = "SiteStructureAddressPoint"
primaryKey = "NGUID"
foreignKey = "SSAP_NGUID"
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

# Next the relationship between the SiteStructureAddressPoint and the LandmarkNameCompleteAliasTable
clmn_table = GeodatabaseName + "/" + "LandmarkNameCompleteAliasTable"
print ("Creating Relationship Class between:          " + ssap)
print ("and...")
print (clmn_table)
print
relClass = GeodatabaseName + "/" + "SiteStructureAddressPoint_Has_LandmarkNameCompleteAliases"
forLabel = "LandmarkNameCompleteAliasTable"
backLabel = "SiteStructureAddressPoint"
primaryKey = "NGUID"
foreignKey = "SSAP_NGUID"
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

# Lastly the relationship between LandmarkNameCompleteAliasTable and the LandmarkNamePartTable
print ("Creating Relationship Class between:          " + clmn_table)
print ("and...")
print (lmnp_table)
print
relClass = GeodatabaseName + "/" + "LandmarkNameCompleteAlias_Has_LandmarkNameParts"
forLabel = "LandmarkNamePartTable"
backLabel = "LandmarkNameCompleteAliasTable"
primaryKey = "NGUID"
foreignKey = "CLNA_NGUID"
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
