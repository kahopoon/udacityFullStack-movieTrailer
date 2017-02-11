# import 'media' for movie class, 'fresh_tomatoes' for creating web page
import media
import fresh_tomatoes

# movie instances
the_lego_batman_movie = media.Movie("The LEGO Batman Movie",
									"https://images-na.ssl-images-amazon.com/images/M/MV5BMTcyNTEyOTY0M15BMl5BanBnXkFtZTgwOTAyNzU3MDI@._V1_UY209_CR0,0,140,209_AL_.jpg",
									"https://www.youtube.com/watch?v=h6DOpfJzmo0")

fifty_shades_darker = media.Movie("Fifty Shades Darker",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5NTk0Njg2N15BMl5BanBnXkFtZTgwNzk5Nzk3MDI@._V1_UX140_CR0,0,140,209_AL_.jpg",
								"https://www.youtube.com/watch?v=n6BVyk7hty8")

john_wick_chapter_2 = media.Movie("John Wick: Chapter 2",
								"https://images-na.ssl-images-amazon.com/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@._V1_UX140_CR0,0,140,209_AL_.jpg",
								"https://www.youtube.com/watch?v=ChpLV9AMqm4")

a_united_kindom = media.Movie("A United Kingdom",
							"https://images-na.ssl-images-amazon.com/images/M/MV5BNDUyNzE1MTAxNF5BMl5BanBnXkFtZTgwODU1Mzk5OTE@._V1_UY209_CR0,0,140,209_AL_.jpg",
							"https://www.youtube.com/watch?v=pX5vI4osR50")
	
hidden_figures = media.Movie("Hidden Figures",
							"https://images-na.ssl-images-amazon.com/images/M/MV5BMjQxOTkxODUyN15BMl5BanBnXkFtZTgwNTU3NTM3OTE@._V1_UY209_CR0,0,140,209_AL_.jpg",
							"https://www.youtube.com/watch?v=5wfrDhgUMGI")

la_la_land = media.Movie("La La Land",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_UY209_CR0,0,140,209_AL_.jpg",
						"https://www.youtube.com/watch?v=0pdqf4P9MB8")

# combine all movie instances into list
movie_list = [the_lego_batman_movie, fifty_shades_darker,john_wick_chapter_2,
			a_united_kindom, hidden_figures, la_la_land]

# call fresh tomatoes to create and open webpage
fresh_tomatoes.open_movies_page(movie_list)

