
# --- Spaceships ---
spaceship_enterprise = [
    'USS Enterprise (NX-01)      NX Klasse            Captain Jonathan Archer,    2151 - 2161\n',
    'USS Enterprise (NCC-1701)   Constitution Klasse, Captain James Tiberus Kirk, 2245 - 2285\n',
    'USS Enterprise (NCC-1701-A) Constitution Klasse, Captain James Tiberus Kirk, 2286 - 2293\n',
    'USS Enterprise (NCC-1701-B) Excelsior Klasse,    Captain John Harriman,      2293 - Unbekannt\n',
    'USS Enterprise (NCC-1701-C) Ambassador Klasse,   Captain Rachel Garrett,     Unbekannt - 2344\n',
    'USS Enterprise (NCC-1701-D) Galaxy Klasse,       Captain Jean-Luc Picard,    2363 - 2371\n',
    'USS Enterprise (NCC-1701-E) Sovereign Klasse,    Captain Jean-Luc Picard,    2372 - Unbekannt\n',
    'USS Enterprise (NCC-1701-J) Universe Klasse,     Ubekannter Captain,         Unbekannt\n'];

spaceship_prometheus = [
    'USS Prometheus (NX-59650/NX-74913) Prometheus Klasse, Unbekannter Captain,            2373 - 2385\n',
    'USS Prometheus (NCC-71201),        Nebula Klasse,     Lieutenant Commander Piersall, Unbekannt\n'  ];

spaceship_voyager = [
    'USS Voyager (NCC-74656) Intrepid Klasse, Captain Kathryn Janeway, 2373 - 2385\n'];

# --- Individual Starships ---

spaceship_enterprise_1701 = [
    'USS Enterprise',
    'Constitution Klasse',
    'NCC-1701',
    'Captain James Tiberus Kirk',
    '2151 - 2161',
    'Zerstört (Selbstzerstörung)'];

spaceship_enterprise_1701a = [
    'USS Enterprise',
    'Constitution Klasse',
    'NCC-1701-A',
    'Captain James Tiberus Kirk',
    '2245 - 2285',
    'Außer Dienst gestellt.'];

spaceship_enterprise_1701b = [
    'USS Enterprise',
    'Excelsior Klasse',
    'NCC-1701-B',
    'Captain John Harriman',
    '2293 - Unbekannt',
    'Unbekannt'];

spaceship_enterprise_1701c = [
    'USS Enterprise',
    'Ambassador Klasse',
    'NCC-1701-C',
    'Captain Rachel Garrett',
    'Unbekannt - 2344',
    'Zerstört'];

spaceship_enterprise_1701d = [
    'USS Enterprise',
    'Galaxy Klasse',
    'NCC-1701-D',
    'Captain Jean-Luc Picard',
    '2363 - 2371',
    'Zerstört'];

spaceship_enterprise_1701e = [
    'USS Enterprise',
    'Sovereign Klasse',
    'NCC-1701-E',
    'Captain Jean-Luc Picard',
    '2372 - Unbekannt',
    'Unbekannt'];

spaceship_enterprise_1701j = [
    'USS Enterprise',
    'Universe Klasse',
    'NCC-1701-J',
    'Unbekannt',
    '26. Jahrhundert',
    'Unbekannt'];

spaceship_prometheus_59650 = [
    'USS Prometheus',
    'Prometheus Klasse',
    'NX-59650 und NX-74913',
    'Unbekannt',
    '2373 - 2385']

starships = [
    spaceship_enterprise,
    spaceship_prometheus,
    spaceship_voyager,
    spaceship_prometheus_59650];


# --- Starship Classes ---

starshipclass_ufp_galaxy = [
    'Library Build uncomplete...'
];


starshipclasses_ufp = [starshipclass_ufp_galaxy];
starshipclasses     = [starshipclasses_ufp];

# --- Database Merging ---

db = [
    starships,
    starshipclasses
    ];