## Summary

This tutorial will show you how to take the next step and store the Rick and Morty API results into a central repository, in this case, BigQuery.

Load data into Pandas to create a `row_hash` and an `ingestion_date`. Pandas makes the creation of these fields really easy across the whole dataset.

These are common best practices so that you have a UUID for a record in a dataset, as well as a date for when the data was loaded. In this case, we already have a unique ID that we're retrieving for a specific entity so it's sort of redundant, but in the real world, when you're extracting reporting data or some data that's combined, you aren't always given a record ID. Creating it yourself at this stage of the process can make downstream activities a lot more simple and you'll thank yourself later on. Just to reiterate, it's for demonstrative purposes here.

One thing we have in this dataset, as we will in a lot of data, is nested elements. We want to be able to handle this during our import to BigQuery since it can handle nested and repeated objects. There's a few additional steps that we need to go through to get the data into the correct format. These include, denormalizing the columns back into nested structure after we've done the transformations we need, converting the data to JSON (this is an easier way to load the data to BigQuery as we can handle nuances ourselves) and finally creating a schema of nested elements.

### Data Types

Generally, when we're loading data into a source table, we want to leave it unchanged so that we always have a raw version of the data to compare with if we ever need to do validation. In the case of dates (like `created`), if we know the string that's returned actually represents some sort of datetime object, it's better that we store it in the correct date format. In this example, we will parse the datetime as a datetime so that our script to generate the BigQuery schema works without having to check whether strings match a particular date format.

## Concepts to Cover

1. Setting up BigQuery Google Cloud Platform
2. DataFrame transformations
3. BigQuery schema creation
4. Load to BigQuery

## Prerequisites

- Be authenticated with `gcloud` and set your project to the one you want to load data to
- Create the dataset `rick_and_morty` within BigQuery and set the location to "EU"