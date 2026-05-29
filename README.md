# CS361-Sorting-Microservice
## Description
Sorts an input array of integers or a list of JSON objects by some value within each object, then returns the result.

## Calling the Microservice
Make an HTTP POST request to the microservice, specifying either the "sort_ints" or "sort_objects" endpoint. Include either the array of ints or array of objects as the POST payload.

```
test
```


Example subtraction:
`https://cs361-add-subtract-microservice.onrender.com/subtract?num1=4&num2=1`

Numbers may be decimals or integers. Negative numbers are accepted as well.

## Receiving Data
A JSON object will be returned.

Addition example:
`
{
  "num1": 4,
  "num2": 1,
  "sum": 5
}
`

Subtraction example:
`
{
  "num1": 4,
  "num2": 1,
  "difference": 3
}
`