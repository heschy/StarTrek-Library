def db_entry_ship_decode(database, mhn):
    output = '';
    output += 'Name: '                                                + database[0] + '\n';
    output += 'Klasse: '                                              + database[1] + '\n';
    output += 'Registriernummer(n): '                                 + database[2] + '\n';
    output += 'Captain: '                                             + database[3] + '\n';
    output += 'Zeitraum: '                                            + database[4] + '\n';
    output += 'Medizinisches Holografisches Notfallprogramm (MHN): '  + mhn + '\n';
    return output;

def db_entry_shipclass_UFP_decode(database):
    output = 'Library Build Uncomplete\n';
    return output;
    