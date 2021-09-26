import mhn;




def db_entry_decode(database, mhn):
    output = '';
    output += 'Name: '                                                + database[0] + '\n';
    output += 'Klasse: '                                              + database[1] + '\n';
    output += 'Registriernummer(n): '                                 + database[2] + '\n';
    output += 'Captain: '                                             + database[3] + '\n';
    output += 'Zeitraum: '                                            + database[4] + '\n';
    output += 'Medizinisches Holografisches Notfallprogramm (MHN): '  + mhn + '\n';
    output += 'Status: '                                              + database[5] + '\n';
    return output;

def library(name):
    output='\n';

    spaceship_enterprise = [
        'USS Enterprise (NX-01)      NX Klasse            Captain Jonathan Archer,    2151 - 2161\n',
        'USS Enterprise (NCC-1701)   Constitution Klasse, Captain James Tiberus Kirk, 2245 - 2285\n',
        'USS Enterprise (NCC-1701-A) Constitution Klasse, Captain James Tiberus Kirk, 2286 - 2293\n',
        'USS Enterprise (NCC-1701-B) Excelsior Klasse,    Captain John Harriman,      2293 - Unbekannt\n',
        'USS Enterprise (NCC-1701-C) Ambassador Klasse,   Captain Rachel Garrett,     Unbekannt - 2344\n',
        'USS Enterprise (NCC-1701-D) Galaxy Klasse,       Captain Jean-Luc Picard,    2363 - 2371\n',
        'USS Enterprise (NCC-1701-E) Sovereign Klasse,    Captain Jean-Luc Picard,    2372 - Unbekannt\n',
        'USS Enterprise (NCC-1701-J) Universe Klasse,     Unbekannter Captain,        Unbekannt\n'];
    
    spaceship_prometheus = [
        'USS Prometheus (NX-59650/NX-74913) Prometheus Klasse, Unbekannter Captain,            2373 - 2385\n',
        'USS Prometheus (NCC-71201),        Nebula Klasse,     Lieutenant Commander Piersall, Unbekannt\n'  ];

    spaceship_voyager = [
        'USS Voyager (NCC-74656) Intrepid Klasse, Captain Kathryn Janeway, 2373 - 2385\n'];
    
    spaceship_prometheus_59650 = [
        'USS Prometheus',
        'Prometheus Klasse',
        'NX-59650 und NX-74913',
        'Unbekannt',
        '2373 - 2385',
        'Unbekannt']
        
    spaceship_enterprise_1701 = [
        'USS Enterprise',
        'Constitution Klasse',
        'NCC-1701',
        'Captain James Tiberus Kirk',
        '2151 - 2161',
        'Zerstört (Selbstzerstörung)']
        
    spaceship_enterprise_1701a = [
        'USS Enterprise',
        'Constitution Klasse',
        'NCC-1701-A',
        'Captain James Tiberus Kirk',
        '2245 - 2285',
        'Außer Dienst gestellt.']
        
    spaceship_enterprise_1701b = [
        'USS Enterprise',
        'Excelsior Klasse',
        'NCC-1701-B',
        'Captain John Harriman',
        '2293 - Unbekannt',
        'Unbekannt']
        
    spaceship_enterprise_1701c = [
        'USS Enterprise',
        'Ambassador Klasse',
        'NCC-1701-C',
        'Captain Rachel Garrett',
        'Unbekannt - 2344',
        'Zerstört']
             
    spaceship_enterprise_1701d = [
        'USS Enterprise',
        'Galaxy Klasse',
        'NCC-1701-D',
        'Captain Jean-Luc Picard',
        '2363 - 2371',
        'Zerstört']
        
    spaceship_enterprise_1701e = [
        'USS Enterprise',
        'Sovereign Klasse',
        'NCC-1701-E',
        'Captain Jean-Luc Picard',
        '2372 - Unbekannt',
        'Unbekannt']

    spaceship_voyager74656 = [
        'USS Voyager',
        'Intrepid Klasse',
        'NCC-74656',
        'Captain Kathryn Janeway',
        '2373 - 2385',
        'Wird Ermittelt']
    
    db = [
        spaceship_enterprise,
        spaceship_enterprise_1701,
        spaceship_enterprise_1701a,
        spaceship_enterprise_1701b,
        spaceship_enterprise_1701c,
        spaceship_enterprise_1701d,
        spaceship_enterprise_1701e,
        spaceship_prometheus,
        spaceship_voyager,
        spaceship_voyager74656,
        spaceship_prometheus_59650];
        
    if name == 'MHN' or name == 'Medizinisches Holografisches Notfallprogramm' or name == 'mhn'or name == 'Medizinisch Holografisches Notfallprogramm':
        output = mhn.v1()+'\n';
        output += mhn.v2();
        
    elif name == 'USS Enterprise':
        for listitem in spaceship_enterprise:
            output += listitem;
            
    elif name == 'USS Prometheus':
        for listitem in spaceship_prometheus:
            output += listitem;
            
    elif name == 'USS Voyager':
        for listitem in spaceship_voyager:
            output += listitem;
    
    elif name == 'NX-59650' or name == 'NX-74913':
        output += db_entry_decode(spaceship_prometheus_59650, mhn.v2());
        
    elif name == 'NCC-1701':
        output += db_entry_decode(spaceship_enterprise_1701, 'Auf diesem Shiff war kein MHN installiert.');
    
    elif name == 'NCC-1701-A':
        output += db_entry_decode(spaceship_enterprise_1701a, 'Auf diesem Shiff war kein MHN installiert.');
    
    elif name == 'NCC-1701-B':
        output += db_entry_decode(spaceship_enterprise_1701b, 'Auf diesem Shiff war kein MHN installiert.');
    
    elif name == 'NCC-1701-C':
        output += db_entry_decode(spaceship_enterprise_1701c, 'Auf diesem Shiff war kein MHN installiert.');
    
    elif name == 'NCC-1701-D':
        output += db_entry_decode(spaceship_enterprise_1701d, 'Auf diesem Shiff war kein MHN installiert.');
    
    elif name == 'NCC-1701-E':
        output += db_entry_decode(spaceship_enterprise_1701e, mhn.v1());
       
    elif name == 'NCC-74656':
        output += db_entry_decode(spaceship_voyager74656, mhn.v1());
        
    elif name == 'db_entry:nx59650' or name == 'db_entry:nx74913':
        output += str(spaceship_prometheus_59650);

    elif name == 'exit' or name == 'quit' or name == 'stop':
        return 1;
        
    elif name == 'help' or name == 'info':
        output += 'Um eine Liste der Schiffe zu erhalten, die den selben namen tragen, geben sie bitte den Namen ein.' + '\n';
        output += 'Um alle Informationen über ein bestimmtes Schiff zu erhalten, geben sie bitte die Registriernummer des Schiffes an.' + '\n';
    
    elif name == 'db' or name == 'print_db' or name == 'print db' or name == 'database' or name == 'print_database' or name == 'print database':
        print('db' + str(db));
        output = 'Output to Large, wrote into Console';
    else:
        output += 'Zugriff nicht möglich!'+'\n';
        
    return output;
