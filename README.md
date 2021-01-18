# Prefix & Infix Calculator and API

This repo contains my solutions to: https://github.com/Kheiron-Medical/swe_take_home_exercise

The solutions were completed using very few imported libraries. 
However, in case of any potential version issues the conda environment can be found in `environment.yaml`

# Part 1 and 2
- The prefix and infix calculator can be run using `./calculator.py`
- Description of code implementation is given in the comments of the respective functions
- The calculator runs all given tests cases before asking for new expressions
- The calculator will keep asking for new expressions until you press enter to finish (an empty expression)

# Bonus

- The calculator API can be be run locally by running `./calculator_api.py`
- Once the application is running the user can input calculations via the UI and receive the results
- The user could also send a post request to `http://127.0.0.1:5000/result_json` with inp as the calculation expression
For example:
```
import requests
r = requests.post("http://127.0.0.1:5000/result_json", data={'inp': '+ * 1 2 5'})
r.text 
r.status_code
```
Would return:
```
'{\n  "calc": "prefix", \n  "result": 7.0\n}\n'
200
```