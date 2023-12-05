to register user:
curl -X POST -H "Content-Type: application/json" -d '{"username":"new_user_two", "password":"password1233", "email":"new_user_two@example.com"}' http:
//127.0.0.1:8000/register/

command for viewing files:
curl -u [username]:[password] http://127.0.0.1:8000/

curl command for uploading files:
curl -X POST -u [username]:[password] -F "file=@/[path to your file]" http://127.0.0.1:8000/upload/

for downloading files:(you should be logged in)
http://127.0.0.1:8000/download/[id of the file you want to download]
