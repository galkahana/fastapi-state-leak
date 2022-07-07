Been getting this leak with fastapi server.
go `poetry install` for this to install.

`make run` will start a server 
`make test` will then run 50 parallel processes each making 50 sequential calls to the service.

im guessing the array saved in the request state is never released cause mem just grows and grows.
only workaround is to null the state var when done.


note the api endpoint is async. when sync (which guess uses threads) the leak shows much faster.