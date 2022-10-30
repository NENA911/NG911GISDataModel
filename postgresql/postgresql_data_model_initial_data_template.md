# NG9-1-1 Data Model PostGIS Initial Data Script

```sql
/* *****************************************************************************
   nena.States Initial Data
   ************************************************************************** */
INSERT INTO nena.States values 
	('AL','Alabama')
,	('AK','Alaska')
,	('AS','American Samoa')
,	('AZ','Arizona')
,	('AR','Arkansas')
,	('CA','California')
,	('CO','Colorado')
,	('CT','Connecticut')
,	('DE','Delaware')
,	('DC','District of Columbia')
,	('FM','Federated States of Micronesia')
,	('FL','Florida')
,	('GA','Georgia')
,	('GU','Guam')
,	('HI','Hawaii')
,	('ID','Idaho')
,	('IL','Illinois')
,	('IN','Indiana')
,	('IA','Iowa')
,	('KS','Kansas')
,	('KY','Kentucky')
,	('LA','Louisiana')
,	('ME','Maine')
,	('MH','Marshall Islands')
,	('MD','Maryland')
,	('MA','Massachusetts')
,	('MI','Michigan')
,	('MN','Minnesota')
,	('MS','Mississippi')
,	('MO','Missouri')
,	('MT','Montana')
,	('NE','Nebraska')
,	('NV','Nevada')
,	('NH','New Hampshire')
,	('NJ','New Jersey')
,	('NM','New Mexico')
,	('NY','New York')
,	('NC','North Carolina')
,	('ND','North Dakota')
,	('MP','Northern Mariana Islands')
,	('OH','Ohio')
,	('OK','Oklahoma')
,	('OR','Oregon')
,	('PW','Palau')
,	('PA','Pennsylvania')
,	('PR','Puerto Rico')
,	('RI','Rhode Island')
,	('SC','South Carolina')
,	('SD','South Dakota')
,	('TN','Tennessee')
,	('TX','Texas')
,	('UT','Utah')
,	('VT','Vermont')
,	('UM','United States Minor Outlying Islands')
,	('VI','Virgin Islands')
,	('VA','Virginia')
,	('WA','Washington')
,	('WV','West Virginia')
,	('WI','Wisconsin')
,	('WY','Wyoming')
; 

/* *****************************************************************************
   nena.ServiceBoundary_URNs Initial Data
   ************************************************************************** */
INSERT INTO nena.ServiceBoundary_URNs VALUES 
	('urn:service:sos','The generic ''sos'' service reaches a public safety answering point (PSAP), which in turn dispatches aid appropriate to the emergency.')
,	('urn:service:sos.ambulance','This service identifier reaches an ambulance service that provides emergency medical assistance and transportation.')
,	('urn:service:sos.animal-control','Animal control typically enforces laws and ordinances pertaining to animal control and management, investigates cases of animal abuse, educates the community in responsible pet ownership and wildlife care, and provides for the housing and care of homeless animals, among other animal-related services.')
,	('urn:service:sos.fire','The ''fire'' service identifier summons the fire service, also known as the fire brigade or fire department.')
,	('urn:service:sos.gas','The ''gas''service allows the reporting of natural gas (and other flammable gas) leaks or other natural gas emergencies.')
,	('urn:service:sos.marine','The ''marine ''service refers to maritime search and rescue services such as those offered by the coast guard, lifeboat, or surf lifesavers.')
,	('urn:service:sos.mountain','The ''mountain''service refers to mountain rescue services (i.e., search and rescue activities that occur in a mountainous environment), although the term is sometimes also used to apply to search and rescue in other wilderness environments.')
,	('urn:service:sos.physician','The ''physician''emergency service connects the caller to a physician referral service.')
,	('urn:service:sos.poison','The ''poison''service refers to special information centers set up to inform citizens about how to respond to potential poisoning.')
,	('urn:service:sos.police','The ''police''service refers to the police department or other law enforcement authorities.')
,	('urn:nena:service:sos.psap','Route calls to primary PSAP.')
,	('urn:nena:service:sos.level_2_esrp','Route calls to a second level ESRP (for an example, a state ESRP routing towards a county ESRP).')
,	('urn:nena:service:sos.level_3_esrp','Route calls to a third level ESRP (for example, a regional ESRP that received a call from a state ESRP and in turn routes towards a county ESRP).')
,	('urn:nena:service:sos.call_taker','Route calls to a call taker within a PSAP.')
,	('urn:nena:service:responder.police','Police Agency')
,	('urn:nena:service:responder.fire','Fire Department')
,	('urn:nena:service:responder.ems','Emergency Medical Service')
,	('urn:nena:service:responder.poison_control','Poison Control Center')
,	('urn:nena:service:responder.mountain_rescue','Mountain Rescue Service')
,	('urn:nena:service:responder.sheriff','Sheriff''s office, when both a police and Sheriff dispattch may be possible')
,	('urn:nena:service:responder.stateProvincial_police','State or provincial police office')
,	('urn:nena:service:responder.coast_guard','Coast Guard Station')
,	('urn:nena:service:responder.psap','Other purposes beyond use for dispatch via ECRF')
,	('urn:nena:service:responder.federal_police.fbi','Federal Bureau of Investigation')
,	('urn:nena:service:responder.federal_police.rcmp','Royal Canadian Mounted Police')
,	('urn:nena:service:responder.federal_police.usss','U.S. Secret Service')
,	('urn:nena:service:responder.federal_police.dea','Drug Enforcement Agency')
,	('urn:nena:service:responder.federal_police.marshal','Marshals Service')
,	('urn:nena:service:responder.federal_police.cbp','Customs and Border Protection')
,	('urn:nena:service:responder.federal_police.ice','Immigration and Customs Enforcement')
,	('urn:nena:service:responder.federal_police.atf','Bureau of Alcohol, Tobacco, Fire Arms and Explosives')
,	('urn:nena:service:responder.federal_police.pp','U.S. Park Police')
,	('urn:nena:service:responder.federal_police.dss','Diplomatic Security Service')
,	('urn:nena:service:responder.federal_police.fps','Federal Protective Service')
,	('urn:nena:service:additionalData','Return a URI to an Additional Data structure as defined in NENA-STA-012.2.')
,	('urn:nena:policy','Route Policy');

/* *****************************************************************************
   nena.LocationMarker_Indicators Initial Data
   ************************************************************************** */
INSERT INTO nena.MilePostIndicators VALUES (
  ('P', 'Posted')
, ('L', 'Logical/Calculated')
; 

/* *****************************************************************************
   nena.LocationMarker_Units Initial Data
   ************************************************************************** */
INSERT INTO nena.LocationMarker_Units VALUES 
	('miles')
,	('yards')
,	('feet')
,	('kilometers')
,	('meters')
; 
```
