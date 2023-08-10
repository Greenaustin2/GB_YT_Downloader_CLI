# GRAPHIC BALANCE CLI
[graphic-balance.com](https://graphic-balance-3bf05d57cb18.herokuapp.com/)

## About

The Graphic Balance CLI is a simple program used for discovering, cataloguing, and archiving randomly generated found footage. While a niche use-case, the program could easily be adapted or built upon to support a variety of needs. This was written specifically for use with experimental found-footage documentary. The main functionality is based upon in-camera file naming protocol (IMG 2383, GOPR3483, DSCF9247, 9247MP4 etc.), which when queried to the Youtube Database yields some interesting and unique results. The program has been slightly adapted for use by others, however it has not yet been built into a well-structured CLI program.

![screen shot one](../assets/gbd.png?raw=true)

## Tech Stack

![python logo](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![python logo](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white) 


## Process

Graphic Balance utilizes the MERN stack, which was an ideal set of frameworks for this concept. When initialized, the program generates a search query consiting of a string ("IMG") and a four digit number between 0000 and 9999 (eg. IMG 2157). IMG is a standard in camera file type, similar to MOV, AVI, DVI, MP4 etc. This query is then used to search Youtube via the Youtube Data API, and when a response is received, a video is chosed from that response at random and presented to the user.
This was a challenging project, and one that I started far too early in my developement career. However, the challenges it presented exposed me to a wide array of concepts, frameworks, and concepts that I may not have grasped had I followed common MERN stack tutorial projects.

## Key concepts learned:

### -State Management

Multiple React state management techniques (context, localized, custom hooks) were implemented before arriving at the end product. This conditioned me heavily with the React Lifecycle and how React behaves under the hood

### -API

For the program to function as I intended, multiple API calls were required due to the Youtube API's seperation of information into seperate API endpoints. The respective API call's response data was then filtered as per certain criteria, and then concatenated into one final object that is then used to communicate to the Youtube Iframe API, as well as send formatted data to the database. This gave me a healthy amount of practice with JSON, async await, and general API fetch, response protocol.

### -Database

All basic CRUD operations are utilized throughout this project. Once I was familiar with the structure of the Youtube API responses, the main task was destructuring those objects, extracting the necessary information, and assigning said infoirmation to the respective fields in the database Schema.

## Future Functionality

### -User Authentification

Save and archive videos to a personal account

Secondary database for video submission staging

When a video is submitted to the archive by a user, it will be sent to a staging database. Once approved by an admin, it will be transferred to the permanent public database

### -Styling

While all core functionality is enabled, the interface is clunky and buggy

Optimize for mobile (currently only desktop and large device viewing recommended)

### -Youtube Data API Quota

Awaiting Google Audited Developer Requests Form to be approved for unlimited API quota
