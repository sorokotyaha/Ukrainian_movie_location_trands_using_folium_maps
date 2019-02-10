import pandas
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter


def csv_to_dict(path):
    """
    This function reads csv file and returns a dictionary of Ukrainian locations for movies
    :param path: str
    :return: dict -> {key=year : [(location, year, movie), (),()]}
    """
    data = pandas.read_csv(path, error_bad_lines=False)
    locations = data['location']
    year = data['year']
    movies = data['movie']
    movies_dict = {}
    for lc, yr, mv in zip(locations, year, movies):
        if 'Ukraine' in str(lc) and yr != 'NO DATA':
            yr = yr[:4]
            if yr not in movies_dict:
                movies_dict[yr] = [(lc, mv, yr)]
            else:
                movies_dict[yr] += [(lc, mv, yr)]

    return movies_dict


def find_coords(year, locations):
    """
    This function takes the year and
    the list of locations to find and writes them in a separate csv file
    with name YEAR.csv and returns the list of coordinates for each
    :param year: 1909 < int number < 2018
    :param locations: lst : [(location, year, movie), (),()]
    :return: lst: [(location, year, movie, latitude, longitude), (),()]
    """
    file = str(year) + '.csv'
    geolocator = Nominatim(user_agent="film_data.py")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    with open(file, "a", encoding='UTF-8') as f:
        f.write('location,movie,year,lat,lon')
        for mv in locations:
            loc = mv[0]
            location = geolocator.geocode(loc)
            try:
                mv += (location.latitude, location.longitude)
                line = mv[0] + ',' + mv[1] + ',' + mv[2] + ',' +\
                       str(location.latitude) + ',' + str(location.longitude) + "\n"
                f.write(line)
            except:
                continue
    return locations


if __name__ == "__main__":
    m_dict = csv_to_dict('locations.csv')
    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018]
    for i in range(len(years)):
        find_coords(year=years[i], locations=m_dict[years[i]])
