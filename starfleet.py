import mhn;

def __help__():
    return 'Starfleet Library 1.0';

def db_entry_decode(database, mhn):
    print('Name: '                                                + database[0]);
    print('Klasse: '                                              + database[1]);
    print('Registriernummer(n): '                                 + database[2]);
    print('Captain: '                                             + database[3]);
    print('Zeitraum: '                                            + database[4]);
    print('Medizinisches Holografisches Notfallprogramm (MHN): '  + mhn);

def library(name):
    print();

    spaceship_enterprise = [
        'USS Enterprise (NX-01)      NX Klasse            Captain Jonathan Archer,    2151 - 2161',
        'USS Enterprise (NCC-1701)   Constitution Klasse, Captain James Tiberus Kirk, 2245 - 2285',
        'USS Enterprise (NCC-1701-A) Constitution Klasse, Captain James Tiberus Kirk, 2286 - 2293',
        'USS Enterprise (NCC-1701-B) Excelsior Klasse,    Captain John Harriman,      2293 - Unbekannt',
        'USS Enterprise (NCC-1701-C) Ambassador Klasse,   Captain Rachel Garrett,     Unbekannt - 2344',
        'USS Enterprise (NCC-1701-D) Galaxy Klasse,       Captain Jean-Luc Picard,    2363 - 2371',
        'USS Enterprise (NCC-1701-E) Sovereign Klasse,    Captain Jean-Luc Picard,    2372 - Unbekannt',
        'USS Enterprise (NCC-1701-J) Universe Klasse,     Ubekannter Captain,         Unbekannt'];
    
    spaceship_prometheus = [
        'USS Prometheus (NX-59650/NX-74913) Prometheus Klasse, Unbekannter Captain,            2373 - 2385',
        'USS Prometheus (NCC-71201),        Nebula Klasse,     Lieutenant Commander Piersall, Unbekannt'  ];

    spaceship_voyager = [
        'USS Voyager (NCC-74656) Intrepid Klasse, Captain Kathryn Janeway, 2373 - 2385'];
    
    spaceship_prometheus_59650 = [
        'USS Prometheus',
        'Prometheus Klasse',
        'NX-59650 und NX-74913',
        'Unbekannt',
        '2373 - 2385',
        'Version 2']

    
    db = [
        spaceship_enterprise,
        spaceship_prometheus,
        spaceship_voyager,
        spaceship_prometheus_59650];
    if name == 'MHN' or name == 'Medizinisches Holografisches Notfallprogramm' or name == 'mhn':
        print(mhn.v1());
        print(mhn.v2());
        
    elif name == 'USS Enterprise':
        for listitem in spaceship_enterprise:
            print(listitem);
            
    elif name == 'USS Prometheus':
        for listitem in spaceship_prometheus:
            print(listitem);
            
    elif name == 'USS Voyager':
        for listitem in spaceship_voyager:
            print(listitem);
    
    elif name == 'NX-59650' or name == 'NX-74913':
        db_entry_decode(spaceship_prometheus_59650, mhn.v2());
    
    elif name == 'db_entry:nx59650':
        print(spaceship_prometheus_59650);

    elif name == 'exit' or name == 'quit' or name == 'stop':
        return 1;
        
    elif name == 'help' or name == 'info':
        print('Um eine Liste der Schiffe zu erhalten, die den selben namen tragen, geben sie bitte den Namen ein.');
        print('Um alle Informationen über ein bestimmtes Schiff zu erhalten, geben sie bitte die Registriernummer des Schiffes an.');
    
    elif name == 'db' or name == 'print_db' or name == 'print db' or name == 'database' or name == 'print_database' or name == 'print database':
        for listitem in db:
            for listitem_subitem in listitem:
                print('db_entry ' + listitem_subitem);
    else:
        print('Zugriff nicht möglich!');
        
    print();
    return 0;
