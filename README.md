# quiz_getter

Instructions for building and launching the service.

1. Clone the repository:
```
git clone https://github.com/sammyjankins/quiz_getter.git
```
2. Go to the project directory:

```
cd your-repo
```
3. Fill the .env file with actual data if necessary.

4. Build and start the containers:

```
docker-compose up -d
```
Console messages example:

![image](https://github.com/sammyjankins/quiz_getter/assets/26933434/b46f2f98-a647-4422-937b-0a30c9fdf4f5)

5. Check that the containers are running:

```
docker-compose ps
```
Console messages example:

![image](https://github.com/sammyjankins/quiz_getter/assets/26933434/b0a5903d-57f6-42a6-871d-cbbafc0bc38a)

6. Send a POST request to the address http://localhost:8000/quiz specifying the number of questions in the parameters.

Example request URL to the POST API service:
```
http://localhost:8000/quiz?questions_num=2
```
Curl:
```
curl -X 'POST' \
  'http://localhost:8000/quiz?questions_num=2' \
  -H 'accept: application/json' \
  -d ''
```
Example response body:
```
{
  "category": "where ya from?",
  "created_at": "2022-12-30T21:49:14.961000",
  "answer_text": "San Marino",
  "id": 202967,
  "recorded_to_db_at": "2023-05-28T19:30:07.571903",
  "question_text": "The Sammarinese are the people of this country"
}
```

To **connect to the database** type:
```
docker ps
```
then copy the name of the database container (for example "**quiz_getter-db-1**") and type:
```
docker exec -it <container_name> psql -U <your_db_user> -d <your_db_name>
```
