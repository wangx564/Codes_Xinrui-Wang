"""Graphical program to display information about flights"""

# The Graphical User Interface (GUI) module - so we can display info in a
# window
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from typing import Set

# The OS module - so we can determine whether or not a file is in a folder
import os
import sys

from typing import List

from flight_types_constants_and_test_data import AirportDict, RouteDict

# The student-created modules - so we can use student solutions
import flight_functions
import flight_reader

# Constants used in the window.
FONT = 'Courier'
FONT_SIZE = 14

DATA_DIR = '{}'

# The airport filename, countries filename, and routes filename.
AIRPORTS_FILENAME = DATA_DIR.format('airports.dat')
ROUTES_FILENAME = DATA_DIR.format('routes.dat')


def calculate_busiest(num_entries: str, info_text):
    """Display in info_text the busiest num_entries airports.
    """

    if not num_entries.isdigit():
        info_str = 'Please enter an integer for # busiest.'
    else:
        busiest_airports = flight_functions.find_busiest_airports(
            route_data, int(num_entries))

        rank = 1
        info_str = ''
        for airport in busiest_airports:
            info_str = f'{info_str}{rank}) {airport[0]}, {airport[1]}\n'
            rank += 1

    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def list_airports(airports: AirportDict, info_text):
    """Display in info_text the name, city, and country of the airports, one
    per line.
    """

    info = []
    for airport in airports:
        info.append(
            '{} {}, {}, {}\n'.format(
                airport,
                flight_functions.get_airport_info(airports, airport, 'Name'),
                flight_functions.get_airport_info(airports, airport, 'City'),
                flight_functions.get_airport_info(airports, airport, 'Country')
            ))

    info.sort()
    info_str = ''.join(info)

    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def show_airport_details(iata: str, airports: AirportDict, info_text):
    """Show in info_text detailed information about airport with IATA code iata.
    """

    if iata.strip() == '':
        info_str = f'Pelase enter an IATA Code.'
    elif iata.strip() != '' and iata in airports:
        info_str = f"""Airport details:
Airport ID: {flight_functions.get_airport_info(airports, iata, 'Airport ID')}
Name: {flight_functions.get_airport_info(airports, iata, 'Name')}
City: {flight_functions.get_airport_info(airports, iata, 'City')}
Country: {flight_functions.get_airport_info(airports, iata, 'Country')}
IATA: {flight_functions.get_airport_info(airports, iata, 'IATA')}
ICAO: {flight_functions.get_airport_info(airports, iata, 'ICAO')}
Latitude: {flight_functions.get_airport_info(airports, iata, 'Latitude')}
Longitude: {flight_functions.get_airport_info(airports, iata, 'Longitude')}
Altitude: {flight_functions.get_airport_info(airports, iata, 'Altitude')}
Timezone: {flight_functions.get_airport_info(airports, iata, 'Timezone')}
DST: {flight_functions.get_airport_info(airports, iata, 'DST')}
Tz: {flight_functions.get_airport_info(airports, iata, 'Tz')}
Type: {flight_functions.get_airport_info(airports, iata, 'Type')}
Source: {flight_functions.get_airport_info(airports, iata, 'Source')}"""

    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def check_direct_flight(routes: RouteDict, iata_src, iata_dest, info_text):
    """Check whether there is a direct flight from iata_src to iata_dest in
    routes and display the result in info_text.
    """

    if iata_src.strip() == '' or iata_dest.strip() == '':
        message_str = 'Please enter the Source and Destination IATA coddes.'
    else:
        if flight_functions.is_direct_flight(iata_src, iata_dest, routes):
            negative = ''
        else:
            negative = 'not '

        message_str = f'There is {negative}a direct flight from {iata_src} to {iata_dest}'

    info_str = message_str
    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def reachable(routes: RouteDict, iata_src: str, n_str: str, info_text):
    """Display in info_text the airports reachable from iata_src in
    int(n_str) legs.
    """

    if iata_src.strip() == '' or n_str.strip() == '' or not n_str.isdigit():
        info_str = "Please enter a Source IATA code and an integer Distance."
    else:
        reach_list = flight_functions.reachable_destinations(
            iata_src, int(n_str), routes)

        info_str = ''
        for i in range(len(reach_list)):
            info_str = f'{info_str}Distance {i}:\n'
            for iata in sorted(reach_list[i]):
                info_str = f'{info_str}  {iata}\n'

    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def get_airport_info_list(airports, iata_codes: List[str]) -> List[str]:
    """Return the airport information (Name, City, Country) for the IATA codes
    in iata_codes.
    """

    airport_info = []
    for airport in iata_codes:
        airport_info.append(
            '{} {}, {}, {}\n'.format(
                airport,
                flight_functions.get_airport_info(airports, airport, 'Name'),
                flight_functions.get_airport_info(airports, airport, 'City'),
                flight_functions.get_airport_info(airports, airport, 'Country')
            ))
    return airport_info


def check_flight_sequence(routes: RouteDict, path: str, info_text):
    """If path represents a valid series of direct flight IATA codes,
    display in info_text the airport information for the airports. Otherwise,
    display that the path is invalid.
    """

    if path.strip() == '':
        info_str = "Please enter a list of valid IATA codes."
    else:
        flight_sequence = path.split()
        is_valid = flight_functions.is_valid_flight_sequence(
            flight_sequence, routes)

        if not is_valid:
            info_str = 'Invalid flight sequence.'
        else:
            airport_info = get_airport_info_list(airport_data, flight_sequence)
            airports_strs = ['{}) {}'.format(
                str(i), airport_info[i]) for i in range(len(airport_info))]
            info_str = ''.join(airports_strs)
            info_str = f'{path} is a valid flight sequence:\n{info_str}'

    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def show_outgoing_flights(
        iata: str, airports: AirportDict, routes: RouteDict, info_text):
    """Show in info_text the outgoing flights for the airport with IATA
    code iata, based on the information in airports and routes.

    """

    if iata.strip() == '':
        destinations_str = f'Enter an IATA Code.'
    elif iata not in routes:
            destinations_str = f'IATA code {iata} not found in the routes information.'
    else:
        destinations = get_airport_info_list(airports, routes[iata])
        destinations.sort()
        destinations = ['{}) {}'.format(
            str(i + 1), destinations[i]) for i in range(len(destinations))]
        destinations_str = ''.join(destinations)

    info_str = f'Outgoing flights:\n{destinations_str}'

    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def get_incoming_flights(iata_dest: str, routes: RouteDict) -> Set[str]:
    """Return the set of IATA codes for airports that have a direct flight
    to the airport with IATA code iata_dest.
    """

    incoming = set()
    for (src, dsts) in routes.items():
        if iata_dest in dsts:
            incoming.add(src)

    return incoming


def show_incoming_flights(
        iata: str, airports: AirportDict, routes: RouteDict, info_text):
    """Show in info_text the incoming flights for the airport with IATA
    code iata, based on the information in airports and routes.
    """

    if iata.strip() == '':
        incoming_str = f'Enter an IATA Code.'
    else:
        incoming_flights = get_airport_info_list(
            airports, get_incoming_flights(iata, routes))
        incoming_flights.sort()
        incoming_flights = ['{}) {}'.format(
            str(i + 1), incoming_flights[i]) for i in range(len(incoming_flights))]
        incoming_str = ''.join(incoming_flights)

    info_str = f'Incoming flights:\n{incoming_str}'

    info_text.delete("1.0", tk.END)
    info_text.insert('insert', info_str)


def add_widgets(airports: AirportDict, routes: RouteDict, window_, frame_):
    """Create and display the flights window.

    This function does not return until the flights window is closed.
    """

    # Where all output will be displayed.
    info_text = ScrolledText(window_)
    info_text.pack()

    list_airports_btn = create_list_airports_button(frame_, airports, info_text)
    list_airports_btn.grid(row=1, column=1)

    create_row_2(airports, routes, frame_, info_text)
    create_row_3(frame_, info_text)
    create_row_4(frame_, info_text)
    create_row_5(frame_, info_text)
    create_row_6(frame_, info_text, routes)


def create_row_2(airports, routes, frame_, info_text):
    """Create the second row an IATA code text field,
    airport details, outgoing flights, and incoming flights."""

    iata_label = tk.Label(frame_, text='IATA Code:')
    iata_label.grid(row=2, column=1)
    iata_info_entry = tk.Entry(
        frame_, width=4, font=(FONT, FONT_SIZE, ''))
    iata_info_entry.grid(row=2, column=2)
    show_airport_details_btn = create_show_airport_details_button(
        frame_, show_airport_details, iata_info_entry, airports, info_text)
    show_airport_details_btn.grid(row=2, column=3)
    outgoing_flights_btn = create_outgoing_flights_button(
        frame_, iata_info_entry, airports, routes, info_text)
    outgoing_flights_btn.grid(row=2, column=4)
    incoming_flights_btn = create_incoming_flights_button(
        frame_, iata_info_entry, airports, routes, info_text)
    incoming_flights_btn.grid(row=2, column=5)


def create_row_3(frame_, info_text):
    """Create the third row: an int for the number of legs,
    and a reachable button."""

    busy_label = tk.Label(frame_, text='# busiest:')
    busy_label.grid(row=3, column=1)
    num_busiest_airports_entry = tk.Entry(
        frame_, width=3, font=(FONT, FONT_SIZE, ''))
    num_busiest_airports_entry.grid(row=3, column=2)
    busiest_btn = create_busiest_button(
        frame_, num_busiest_airports_entry, info_text)
    busiest_btn.grid(row=3, column=3)


def create_row_4(frame_, info_text):
    """Create the fourth row: source and destination airports and a button
    to check for a direct flight between them."""

    iata_src_label = tk.Label(frame_, text='Source IATA:')
    iata_src_label.grid(row=4, column=1)
    iata_src_entry = tk.Entry(
        frame_, width=4, font=(FONT, FONT_SIZE, ''))
    iata_src_entry.grid(row=4, column=2)
    iata_dest_label = tk.Label(frame, text='Destination IATA:')
    iata_dest_label.grid(row=4, column=3)
    iata_dest_entry = tk.Entry(
        frame_, width=4, font=(FONT, FONT_SIZE, ''))
    iata_dest_entry.grid(row=4, column=4)
    check_direct_flight_btn = create_direct_flight_button(
        frame_, iata_src_entry, iata_dest_entry, info_text)
    check_direct_flight_btn.grid(row=4, column=5)


def create_row_5(frame_, info_text):
    """Create the fifth row: a source airports, a distance, and a button
    to calculate the reachable cities at each distance in the range 0 to
    that distance."""

    iata_reach_label = tk.Label(frame_, text='Source IATA:')
    iata_reach_label.grid(row=5, column=1)
    iata_reach_entry = tk.Entry(
        frame_, width=4, font=(FONT, FONT_SIZE, ''))
    iata_reach_entry.grid(row=5, column=2)
    iata_reach_label = tk.Label(frame_, text='Distance:')
    iata_reach_label.grid(row=5, column=3)
    reach_distance_entry = tk.Entry(
        frame_, width=4, font=(FONT, FONT_SIZE, ''))
    reach_distance_entry.grid(row=5, column=4)
    reachable_btn = create_reachable_flight_button(
        frame_, iata_reach_entry, reach_distance_entry, info_text)
    reachable_btn.grid(row=5, column=5)


def create_row_6(frame_, info_text, routes):
    """Create the sixth row: a text field for a sequence of IATA codes
    and a button to check that it is valid."""

    path_entry = tk.Entry(
        frame_, width=16, font=(FONT, FONT_SIZE, ''))
    path_entry.grid(row=6, column=1, columnspan=2)
    valid_path_btn = create_valid_flight_sequence_button(
        frame_, routes, path_entry, info_text)
    valid_path_btn.grid(row=6, column=3)


def create_valid_flight_sequence_button(
        frame_, routes, path_entry, info_text):
    """Create the button for valid flight sequence.
    """
    path_btn = tk.Button(
        frame_,
        text="Check flight sequence",
        command=lambda: (
            check_flight_sequence(
                routes,
                path_entry.get(),
                info_text))
    )
    return path_btn


def create_reachable_flight_button(
        frame_, iata_src_entry, distance_entry, info_text):
    """Create the button for reachable flights
    """
    reachable_btn = tk.Button(
        frame_,
        text="Reachable destinations",
        command=lambda: (
            reachable(
                route_data,
                iata_src_entry.get(),
                distance_entry.get(),
                info_text))
    )
    return reachable_btn


def create_direct_flight_button(
        frame_, iata_src_entry, iata_dest_entry, info_text):
    """Create the button for direct flights
    """
    busiest_btn = tk.Button(
        frame_,
        text="Check for direct flight",
        command=lambda: (
            check_direct_flight(
                route_data,
                iata_src_entry.get(),
                iata_dest_entry.get(),
                info_text))
    )
    return busiest_btn


def create_list_airports_button(frame_, airports, info_text):
    """Create the button to list airports
    """
    list_airports_btn = tk.Button(
        frame_,
        text="List all airports",
        command=lambda: (
            list_airports(airports, info_text))
    )
    return list_airports_btn


def create_busiest_button(
        frame_, num_busiest_airports_entry, info_text):
    """Create the button to find busiest airports
    """
    busiest_btn = tk.Button(
        frame_,
        text="Calculate busiest",
        command=lambda: (
            calculate_busiest(
                num_busiest_airports_entry.get(), info_text))
    )
    return busiest_btn


def create_outgoing_flights_button(
        frame_, iata_info_entry, airports, routes, info_text):
    """Create the button to find outgoing flights
    """
    outgoing_flights_btn = tk.Button(
        frame_,
        text="Show outgoing flights",
        command=lambda: (
            show_outgoing_flights(
                iata_info_entry.get(), airports, routes, info_text))
    )
    return outgoing_flights_btn


def create_incoming_flights_button(
        frame_, iata_info_entry, airports, routes, info_text):
    """Create the button to find incoming flights
    """
    incoming_flights_btn = tk.Button(
        frame_,
        text="Show incoming flights",
        command=lambda: (
            show_incoming_flights(
                iata_info_entry.get(), airports, routes, info_text))
    )
    return incoming_flights_btn


def create_show_airport_details_button(
        frame_, show_airport_details_, iata_info_entry, airports, info_text):
    """Create the button to show airport details
    """
    show_airport_details_btn = tk.Button(
        frame_,
        text="Show airport details",
        command=lambda: (
            show_airport_details_(
                iata_info_entry.get(), airports, info_text))
    )
    return show_airport_details_btn


if __name__ == '__main__':
        
    if os.path.exists(AIRPORTS_FILENAME) and os.path.exists(ROUTES_FILENAME):

        with open(AIRPORTS_FILENAME, 'r', encoding='utf-8') as airports_file, \
             open(ROUTES_FILENAME, 'r', encoding='utf-8') as routes_file:

            airport_data = flight_reader.read_airports(airports_file)
            route_data = flight_reader.read_routes(routes_file, airport_data)

            # Create the window.  This has to be the first UI element created.
            window = tk.Tk()
            window.protocol("WM_DELETE_WINDOW", window.destroy)
            window.configure(background="#808000")
            window.title('CSC108 Flight Analysis '
                         '- close this window to return to python shell')
            frame = tk.Frame(
                window, width=130, height=110, bg='#ffffff', borderwidth=1,
                relief="sunken")
            frame.pack(fill='both', expand='yes')

            # Populate the window.
            add_widgets(airport_data, route_data, window, frame)

            window.lift()
            window.call('wm', 'attributes', '.', '-topmost', True)
            window.after_idle(window.call, 'wm', 'attributes', '.', '-topmost',
                              False)
            window.mainloop()
            print('\n\nCSC108: To quit the program, go to "Options" -> "Restart Shell" in the Wing101 Python Shell')
            
    else:
        print('The airport and route files were not found.')
        print('Copy files ' + AIRPORTS_FILENAME + ' and ' + ROUTES_FILENAME + \
              ' into the same folder as your A3 Python files and try again.')
