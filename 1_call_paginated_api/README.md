## Summary

This tutorial will show you how to paginate through API results with Python, using the Rick and Morty open API as an example.

Most API's that return data have a concept of pagination, if there's too many records to display (e.g. number of pages on a website or individual records in a report), the API will most likely default to returning a fixed number of records and break down how many pages of records there are. Sometimes, you are also given an option to specify how many records to return with each call, but in this case, we're restricted to 20.

In the example of the Rick and Morty `Character` endpoint, there are 826 total records and a total of 42 pages (42 x 20 = 840 meaning the last page will only show 6 records).

API's, and pagination in particulate, can be a confusing concept if you're new to working with them, or have never considered a "clean" way of dealing with them, so there's a few things I want to demonstrate in this example that will hopefully save you time, and make your lives easier in a real-world scenario.

Note - obviously Rick and Morty data isn't a real world use case, but the API demonstrates some very common features (excluding authentication) of an API which can be altered to fit most other situations.

In this API, we're actually given an additional piece of information with each API call, a record called `next` which gives us the exact URL we need to call to get the next bit of information. There's a reason I've chosen not to use this approach, which will make more sense if you continue following this series as I expand on the use case and bring it to life with more real-world approaches.

## Concepts to Cover

1. Dataclasses
	1. Creating a dataclass to handle input parameters
	2. Creating a dataclass to handle the API results
2. Paginating through all of the results for the API entity

## Logic of the Script
- Get the total number of pages
- Loop through a range of 1 to number of pages calling the endpoint with a page parameter.