### Response
control the response we get back by using the `Accept` header to juggle between content formats
[`http://127.0.0.1:8000/snippets/ Accept:application/json` #Requestjson
`http://127.0.0.1:8000/snippets/ Accept:text/html` #Request HTML]

Or append a format suffix
[`http://127.0.0.1:8000/snippets.json` #json suffix
`http://127.0.0.1:8000/snippets.api` #html suffix]

Or using the `Content-Type` header
[`# POST using form data
http --form POST http://127.0.0.1:8000/snippets/ code="print(123)"`]

### Deleting a database
`rm -f db.sqlite3`

### Deleting migrations
`rm -r appname/migrations`
