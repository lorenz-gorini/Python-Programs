This program will do the following:

- Using a public API, it regularly gets the current position of the international space station (ISS).
- It draws a series of points (ISS coordinates) on a map and calculates the average speed.

An open service to get the ISS position is http://api.open-notify.org/iss-now.json

The resulting json looks like:

{
	timestamp: 1547626790,
	message: "success",
	iss_position: {
		latitude: "48.4406",
		longitude: "-87.2757"
	}
}

The generated map of ISS path can be found in HTML file inside the lib folder.
Instead "my_ISS_map_large" file is just an example created with a longer time.

The program is just a draft of a possible solution.