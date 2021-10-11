import mhn;
from starfleet_functions import *;
from starfleet_maindb import *;

def library(name):
    output='\n';
    
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
        output += db_entry_ship_decode(spaceship_prometheus_59650, mhn.v2());

    elif name == 'NCC-1701' or name == 'NCC 1701':
        output += db_entry_ship_decode(spaceship_enterprise_1701, 'Nicht Installiert');

    elif name == 'NCC-1701-A' or name == 'NCC 1701 A' or name == 'NCC-1701 A':
        output += db_entry_ship_decode(spaceship_enterprise_1701a, 'Nicht Installiert');

    elif name == 'NCC-1701-B' or name == 'NCC 1701 B' or name == 'NCC-1701 B':
        output += db_entry_ship_decode(spaceship_enterprise_1701b, 'Nicht Installiert');

    elif name == 'NCC-1701-C' or name == 'NCC 1701 C' or name == 'NCC-1701 C':
        output += db_entry_ship_decode(spaceship_enterprise_1701c, 'Nicht Installiert');

    elif name == 'NCC-1701-D' or name == 'NCC 1701 D' or name == 'NCC-1701 D':
        output += db_entry_ship_decode(spaceship_enterprise_1701d, 'Nicht Installiert');

    elif name == 'NCC-1701-E' or name == 'NCC 1701 E' or name == 'NCC-1701 E':
        output += db_entry_ship_decode(spaceship_enterprise_1701e, mhn.v1());

    elif name == 'NCC-1701-J' or name == 'NCC 1701 J' or name == 'NCC-1701 J':
        output += db_entry_ship_decode(spaceship_enterprise_1701j, 'Unbekannt');
    
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

