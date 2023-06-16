# IPL Match Win Predictor

## Table of Content
* [Overview](#overview)
* [Motivation](#motivation)
* [Problem Solving Steps](#problem-solving-steps)
* [Source of Dataset](#source-of-dataset)
* [Data Cleaning Techniques](#data-cleaning-techniques)
* [Exploratory Data Analysis](#exploratory-data-analysis)
* [Model Building](#model-building)
* [Model Performance](#model-performance)
* [Deployment](#deployment)
* [Future scope of project](#future-scope-of-project)

## Overview

Indian Premier League (IPL) is a Twenty20 cricket format league in India. It is usually played in April and May every year. As of 2019, the title sponsor of the game is Vivo. The league was founded by Board of Control for Cricket India (BCCI) in 2008

Based on the first innings performance of a team, this app takes in current data of second innings and predicts the win probability of the two teams. </br></br>

<img src="img/ipl_logo.png">

## Motivation

## Problem Solving Steps

1. Load the Dataset into a pandas Data frame
2. Perform Exploratory Data Analysis on the data
3. Feature Engineering: Extract new features
4. Fit a Machine Learning Pipeline on the extracted data
5. Integrate the Pipeline with the User Interface which is created using Streamlit
6. Deploy the model on a cloud service

## Source of Dataset

The dataset consist of data about IPL matches played from the year 2008 to 2019. The sources of the data sets are from;
* Data source from 2008-2017 - [CricSheet.org and Manas - Kaggle](https://cricsheet.org/)
* Data source for 2018-2019 - [IPL T20 - Official website](https://www.iplt20.com/)


## Data Cleaning Techniques

- For the teams, only the most frequent participating teams were uesed for the analysis, while old team names were replaced with theire respective curreent names.
- The to data sets were merged on th 1`match_id` column to enhace data analysis.
- New features like `current_score`, `runs_left`, `balls_left`, `players_dismmised` etc were created to improve the model performance.

## Exploratory Data Analysis

## Model Building

## Model Performance

## Deployment

## Future scope of project
