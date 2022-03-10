# CSGO.SUPPLY
# Introduction

This project is a website that displays and aggregates information on items from the video game CS:GO. Within the game, players can unlock, trade, and buy “skins” for real-life money. Skins are cosmetic textures for weapons that provide no real gameplay advantage. They are able to be obtained by spending $2.50 to unlock a “case”, which generates one completely random skin. Over nearly a decade since CS:GO’s launch, players have created a virtual economy based around skins, resulting in hundreds of millions of US Dollars worth of skins being in circulation.

  

Skins are so highly valued in the game due to their float value. Float is a unique mechanic in which each skin has a float (0.00… - 0.99…) value assigned to it, and no two skins in existence will have the same float. The float also determines the degradation of the skin, values closer to 0.99… will be more “damaged” and dull looking, while floats closer to 0.00… will be pristine, bright, and brand new looking. This system creates a hierarchy in skins and allows the most pristine ones to be valued for thousands of dollars.

  

![](https://lh3.googleusercontent.com/mwh_A29lcjOAy45DBVQTsaDtvLKHjY7CjWenuZbl6xY7LzySC_isTdjY7oL6YvCd0xLr9SGJZ2zwPsP4U4a1XoQ0DHlMIh5rsIx23d5IhzWMTgUwCCot2B4ddjtUKdnrz8CLnU6C)
*A picture depicting a low float (closer to 0.00…) on the left, and a high float (closer to 0.99…) on the right. Note that the one on the right is more damaged and less vibrant in color.*

# Rationale

We are interested in creating a website for users to generate and calculate the price of a complete CS:GO loadout (multiple weapons/skins). The users will be able to browse market prices for their desired skins and view all the available skins for a certain weapon. They can also view price trend graphs to determine if it is a good time to invest.

  

Out interest in this project started from our love of playing CS:GO and collecting skins. We have played CS:GO for years and have watched the economy shift over time. We are majors from different backgrounds including Information Sciences, Computer Science, and Business. Between us, we are experienced with UI/UX design, Python, APIs, and overall game knowledge.

  

![](https://lh5.googleusercontent.com/E_oaYr3XVRIF_1p6h7T76ZwCTK0HP4e1mCCg7hcboDRuYoVpFtT2oclql_Y3ym58dXH-dgSZkrKIa-i1CGPBMta3ShJpYe_8UpQ5iK77hhtdtQ0jHvSccEYsQhKhw01d07JZLBhv)
*People can spend a lot of money on CS:GO.*

  

There are many sites that allow players to buy and sell skins online (buy/sell/trade sites), but there are very few resources that allow you to customize a full loadout. These sites allow users to create listings similar to Craigslist, where other players can view their skins and choose to buy them with real money.

  

Here are some popular buy/sell websites that function similarly, but are not exactly the same as ours:

-   [cs.money](https://cs.money/)
    
-   [cs.deals](https://cs.deals/)
    
-   [skinport.com](https://skinport.com/)
    
-   [csgostash.com](https://csgostash.com/)
    
-   [tradeit.gg](https://tradeit.gg/)
    
-   [csgobackpack.net](https://csgobackpack.net/items-db/index.php)
    

# Methodology

We intend to create a website using Django, which is a web framework based on Python. The benefits of using Django include modularity and ease of deployment. Our user interface will be created using Figma and then converted to HTML and CSS. Users can also connect their CS:GO account to view their inventory on the site. The website will also require a database to store data like prices, skins, saved configurations of skin loadouts, and user data, most of which is handled by Django.

  

Commits to the website and Django are viewable on the GitHub page, and the Figma wireframe is viewable [here](https://www.figma.com/file/vv0T6Y8B3S8Yz7EPsWnlfz/Website?node-id=0%3A1). The website’s URL is [www.csgo.supply](http://www.csgo.supply)

## API’s

We will be using various public APIs to gather data like market prices, the types of skins, and user info. Most buy/sell websites offer their own APIs to track the price of a certain skin on their site. By aggregating multiple sites, prices can be compared for the same skin so the user can compare and buy the cheapest one. We will have to collect very little data on the skins/prices themselves, instead, we will primarily collect the “saved loadouts” that users configure so they can share and access them after visiting the site.

  

## Displaying the Data

Prices will be shown along with their specific listings across multiple buy/sell websites. We also may implement a currency feature where users can change their native currency to get accurate prices. Trend graphs will also be shown for each skin where users can view the increase/decrease in market value over time.

# Work Plan

Our work will be divided as follows:

-   Arnav (UIUC)

	-   Front-end/User Interface Design
    
	-   API calls
    
	-   Price-trend graphs
    
	-   Analytics / Domain management
    

-   Devan (CMU)
    

	-   Back-end coding with Python
    
	-   Django setup
    
	- Database management
    

-   Abhi (IU Kelley)
    

	- Feature Implementation Testing
    
	-   Back-end Python
    
	-   Filters
    
	-   Game knowledge and guidance
