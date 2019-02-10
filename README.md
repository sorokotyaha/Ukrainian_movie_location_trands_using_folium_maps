# Ukraininan_movie_trands_using_folium_maps
These modules work with location.csv database to generate the illustration of film trends in Ukraine, particularly in movie location choice. Here, as an example, will be showing the locations of movies of 2012-2018 years.

# Module film_data.py

This module proceeds the data from location.csv and separates the needed data about Ukraine rearanging it into
more convenient form and a separate cvs files.

# Module maps.py

This module proceeds the information from previously generated YEAR.csv files
 and creates a multiple layer map visiolizing the most popular locations for film making

# Main point of the research

We get the heat map of the film locations in Ukraine. The brighter the color is - the greater number of films was shut there.
Each layer is a heat map of a certain year. In this case, 2012-2018.
As we can see from different layears of the heat map, the most attractive locations for movie industry in Ukraine are:
  1. Carpathian mountains, Western Ukraine
  2. Kyiv and Kyiv region, Chernobyl
  3. Coastal Ukraine : Odessa, Crimea
  4. Donbass

And from the map we can see the factors influencing such results:
  1. Nature locatins
  2. Cultural heritages
  3. World War 2 main battle locations
  4. Modern military activities in the East, war with Russia

As well, the map illustrates the increase in film production for past 6 years.

# HTML page structure and tags

    <!DOCTYPE html> permanently set that type of the html file is html5
    <head> defines information about the document
    <meta> Defines metadata about an HTML document
      attributes:
          http-equiv provides an HTTP header for the information/value of the content attribute
          content gives the value associated with the http-equiv or name attribute
          name specifies a name for the metadata
    <script> defines a client-side script (JavaScript)
    attributes:
          src specifies the URL of an external script file
    <link> links to external style sheets
    attributes:
          rel specifies the relationship between the current document and the linked document
          href specifies the location of the linked document
    <style> defines style information for an HTML document
    <body> defines the document's body
    <div> defines a division or a section in an HTML document also used as a container for other HTML elements to style them with CSS or to perform certain tasks with JavaScript
