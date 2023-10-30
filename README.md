# HTTP server by sockets
## Запуск:
`python main.py -r /home/soren/PycharmProjects/HTTP_Server -w 2`

Описание параметров:
- r - директория поиска файлов
- w - кол-во воркеров

## Результат запуска тестов
https://github.com/s-stupnikov/http-test-suite/blob/master/httptest.py

directory index file exists ... ok
document root escaping forbidden ... ok
Send bad http headers ... ok       
file located in nested folders ... ok
absent file returns 404 ... ok
urlencoded filename ... ok
file with two dots in name ... ok
query string after filename ... ok
slash after filename ... ok
filename with spaces ... ok
Content-Type for .css ... ok
Content-Type for .gif ... ok
Content-Type for .html ... ok
Content-Type for .jpeg ... ok
Content-Type for .jpg ... ok
Content-Type for .js ... ok
Content-Type for .png ... ok
Content-Type for .swf ... ok
head method support ... ok
directory index file absent ... ok
large file downloaded correctly ... ok
post method forbidden ... ok
Server header exists ... ok

----------------------------------------------------------------------
Ran 23 tests in 35.113s

## Нагрузочное тестирование.
ab -n 50000 -c 100 -r http://127.0.0.1:8091/
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:
Server Hostname:        127.0.0.1
Server Port:            8091

Document Path:          /
Document Length:        2170 bytes

Concurrency Level:      100
Time taken for tests:   5.326 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      117800000 bytes
HTML transferred:       108500000 bytes
Requests per second:    7022.34 [#/sec] (mean)
Time per request:       10.405 [ms] (mean)
Time per request:       0.120 [ms] (mean, across all concurrent requests)
Transfer rate:          16448.58 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.7      1      17
Processing:     1   12   7.5     11     135
Waiting:        1   11   7.4     10     140
Total:          1   12   7.5     11     141

Percentage of the requests served within a certain time (ms)
  50%     11
  66%     13
  75%     14
  80%     14
  90%     16
  95%     18
  98%     23
  99%     44
 100%    144 (longest request)