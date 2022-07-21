Run `application.py` to run the entire web application.  `application.py` will import the getvr() function from `cellfunc.py`, which
imports the rest of the Phidget functions and libraries from `liblr.py`.  The load cell sample time (in seconds) defaults to 1 second,
but can be changed by passing a new integer (NUM) as `getvr(sampletime=NUM)`.  

See the `test_loadcells` directory for testing the load cells from the command line.
