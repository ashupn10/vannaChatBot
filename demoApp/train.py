import vannaChatBot.demoApp.model as model
vnn=model.model_vanna()

def trainData(question,sql,documentation):
    response=vnn.train(question,sql,documentation)
    print(response)
sql="SELECT m.TITLE, g.NAME AS GENRE, SUM(s.VIEWS) AS TOTAL_VIEWS FROM MOVIESTREAM.movies m JOIN MOVIESTREAM.streams s ON m.MOVIE_ID = s.MOVIE_ID JOIN MOVIESTREAM.genre g ON s.GENRE_ID = g.GENRE_ID GROUP BY m.TITLE, g.NAME;"
trainData("List movies along with their genres and the total number of views for each movie",sql,"this is for getting views")
print(vnn.get_training_data().to_string())

trainData("give all movies data",sql,"NOt required" )

print(vnn.get_training_data())